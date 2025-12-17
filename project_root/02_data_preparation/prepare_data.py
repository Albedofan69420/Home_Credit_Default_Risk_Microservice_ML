import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib
from sklearn.model_selection import train_test_split

DATA_PATH = "data/application_train.csv"
BUREAU_PATH = "data/bureau.csv"
BUREAU_BALANCE_PATH = "data/bureau_balance.csv"




ARTIFACTS_PATH = "artifacts/"

def clip_outliers_train_test(train, test, cols, lower=0.01, upper=0.99):
    train = train.copy()
    test = test.copy()


    for col in cols:
        q_low = train[col].quantile(lower)
        q_high = train[col].quantile(upper)
        train[col] = train[col].clip(q_low, q_high)
        test[col] = test[col].clip(q_low, q_high)


    return train, test



def main():

    df_bb = pd.read_csv(BUREAU_BALANCE_PATH)
    df = pd.read_csv(DATA_PATH)
    bureau = pd.read_csv(BUREAU_PATH)
    df_prev = pd.read_csv("data/previous_application.csv")

    prev_agg = (
    df_prev
    .groupby("SK_ID_CURR")
    .agg(
        PREV_APP_COUNT=("SK_ID_PREV", "count"),
        PREV_APP_AMT_CREDIT_MEAN=("AMT_CREDIT", "mean"),
        PREV_APP_REFUSED_RATIO=("NAME_CONTRACT_STATUS",
                                lambda x: (x == "Refused").mean()),
        PREV_APP_DAYS_DECISION_MEAN=("DAYS_DECISION", "mean")
    )
    .reset_index()
)

    df = df.merge(prev_agg, on="SK_ID_CURR", how="left")

    df_pos = pd.read_csv("data/POS_CASH_balance.csv")

    pos_agg = (
        df_pos
        .groupby("SK_ID_CURR")
        .agg(
            POS_MONTHS_COUNT=("MONTHS_BALANCE", "count"),
            POS_DPD_MEAN=("SK_DPD", "mean"),
            POS_DPD_MAX=("SK_DPD", "max")
        )
        .reset_index()
    )

    df = df.merge(pos_agg, on="SK_ID_CURR", how="left")


    df_inst = pd.read_csv("data/installments_payments.csv")

    df_inst["PAYMENT_RATIO"] = (
    df_inst["AMT_PAYMENT"] / df_inst["AMT_INSTALMENT"].replace(0, np.nan)   
    )

    df_inst["DPD"] = (
        df_inst["DAYS_ENTRY_PAYMENT"] - df_inst["DAYS_INSTALMENT"]
    )

    inst_agg = (
        df_inst
        .groupby("SK_ID_CURR")
        .agg(
            INST_PAYMENT_RATIO_MEAN=("PAYMENT_RATIO", "mean"),
            INST_DPD_MEAN=("DPD", "mean"),
            INST_DPD_MAX=("DPD", "max")
        )
        .reset_index()
    )

    df = df.merge(inst_agg, on="SK_ID_CURR", how="left")

    df_cc = pd.read_csv("data/credit_card_balance.csv")

    df_cc["CC_UTILIZATION"] = (
    df_cc["AMT_BALANCE"] / df_cc["AMT_CREDIT_LIMIT_ACTUAL"].replace(0, np.nan)
)

    cc_agg = (
        df_cc
        .groupby("SK_ID_CURR")
        .agg(
            CC_BALANCE_MEAN=("AMT_BALANCE", "mean"),
            CC_LIMIT_MEAN=("AMT_CREDIT_LIMIT_ACTUAL", "mean"),
            CC_UTILIZATION_MEAN=("CC_UTILIZATION", "mean"),
            CC_DPD_MEAN=("SK_DPD", "mean")
        )
        .reset_index()
    )

    df = df.merge(cc_agg, on="SK_ID_CURR", how="left")




    STATUS_MAP = {"C": 0, "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
    df_bb["STATUS_NUM"] = df_bb["STATUS"].map(STATUS_MAP)

    bb_agg = (
        df_bb
        .groupby("SK_ID_BUREAU")
        .agg(
            BB_MONTHS_COUNT=("MONTHS_BALANCE", "count"),
            BB_STATUS_MEAN=("STATUS_NUM", "mean"),
            BB_MAX_STATUS=("STATUS_NUM", "max"),
            BB_HAS_OVERDUE=("STATUS_NUM", lambda x: int(x.max() > 0))
        )
        .reset_index()
    )

    #unir tablas
    df_bureau = pd.read_csv("data/bureau.csv")
    df_bureau = df_bureau.merge(
        bb_agg,
        on="SK_ID_BUREAU",
        how="left"
    )

    bureau_final = (
    df_bureau
    .groupby("SK_ID_CURR")
    .agg(
        BB_MONTHS_COUNT_MEAN=("BB_MONTHS_COUNT", "mean"),
        BB_STATUS_MEAN=("BB_STATUS_MEAN", "mean"),
        BB_MAX_STATUS=("BB_MAX_STATUS", "max"),
        BB_HAS_OVERDUE=("BB_HAS_OVERDUE", "max")
    )
    .reset_index()
    )

    df = df.merge(
        bureau_final,
        on="SK_ID_CURR",
        how="left"
    )
    bureau_balance_cols = [
    "BB_MONTHS_COUNT_MEAN",
    "BB_STATUS_MEAN",
    "BB_MAX_STATUS",
    "BB_HAS_OVERDUE"
    ]

    df[bureau_balance_cols] = df[bureau_balance_cols].fillna(0)

    df["AGE"] = df["DAYS_BIRTH"] / -365
    df["YEARS_EMPLOYED"] = df["DAYS_EMPLOYED"] / 365

    df.loc[df["DAYS_EMPLOYED"] == 365243, "YEARS_EMPLOYED"] = np.nan
    df.loc[df["YEARS_EMPLOYED"] > 60, "YEARS_EMPLOYED"] = np.nan

    df['YEARS_EMPLOYED'] = df['YEARS_EMPLOYED'].fillna(df['YEARS_EMPLOYED'].median())

    bureau_agg = bureau.groupby("SK_ID_CURR").agg({
    "AMT_CREDIT_SUM": ["mean", "sum"],
    "CREDIT_DAY_OVERDUE": "max",
    "DAYS_CREDIT": "mean"
    })


    bureau_agg.columns = [
    "BUREAU_CREDIT_MEAN",
    "BUREAU_CREDIT_SUM",
    "BUREAU_MAX_DAYS_OVERDUE",
    "BUREAU_DAYS_CREDIT_MEAN"
    ]
        
    VARIABLES = [
    # Base
    "AMT_INCOME_TOTAL", "AMT_CREDIT", "AMT_ANNUITY",
    "AGE", "YEARS_EMPLOYED",

    # Bureau
    "BUREAU_CREDIT_MEAN", "BUREAU_CREDIT_SUM",
    "BUREAU_DAYS_CREDIT_MEAN", "BUREAU_MAX_DAYS_OVERDUE",

    # Bureau balance
    "BB_MONTHS_COUNT_MEAN", "BB_STATUS_MEAN",
    "BB_MAX_STATUS", "BB_HAS_OVERDUE",

    # Previous
    "PREV_APP_COUNT", "PREV_APP_AMT_CREDIT_MEAN",
    "PREV_APP_REFUSED_RATIO", "PREV_APP_DAYS_DECISION_MEAN",

    # POS
    "POS_MONTHS_COUNT", "POS_DPD_MEAN", "POS_DPD_MAX",

    # Installments
    "INST_PAYMENT_RATIO_MEAN", "INST_DPD_MEAN", "INST_DPD_MAX",

    # Credit card
    "CC_BALANCE_MEAN", "CC_LIMIT_MEAN",
    "CC_UTILIZATION_MEAN", "CC_DPD_MEAN"
] 
    

    df = df.merge(
    bureau_agg,
    how="left",
    left_on="SK_ID_CURR",
    right_index=True
    )

    new_cols = [
    "PREV_APP_COUNT", "PREV_APP_AMT_CREDIT_MEAN", "PREV_APP_REFUSED_RATIO",
    "PREV_APP_DAYS_DECISION_MEAN",
    "POS_MONTHS_COUNT", "POS_DPD_MEAN", "POS_DPD_MAX",
    "INST_PAYMENT_RATIO_MEAN", "INST_DPD_MEAN", "INST_DPD_MAX",
    "CC_BALANCE_MEAN", "CC_LIMIT_MEAN", "CC_UTILIZATION_MEAN", "CC_DPD_MEAN"
]

    df[new_cols] = df[new_cols].fillna(0)
    df_model = df[VARIABLES].copy()

    min_non_null = int(len(VARIABLES) * 0.7)
    df_model = df_model.dropna(thresh=min_non_null)
    df_model = df_model.fillna(0)
    df_model.replace([np.inf, -np.inf], 0, inplace=True)


    df_variables = df[["SK_ID_CURR"] + VARIABLES].loc[df_model.index].copy()
    df_variables.head()

    df_train, df_test = train_test_split(
    df_model,
    test_size=0.2,
    random_state=42
)
        
    df['YEARS_EMPLOYED'] = df['YEARS_EMPLOYED'].fillna(df['YEARS_EMPLOYED'].median())

    for col in VARIABLES:
        median_val = df_train[col].median()
        df_train[col] = df_train[col].fillna(median_val)
        df_test[col] = df_test[col].fillna(median_val)

    df_train, df_test = clip_outliers_train_test(df_train, df_test, VARIABLES)
    
    df_variables.to_csv(ARTIFACTS_PATH + "df_variables.csv", index=False)


    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(df_train)
    X_test_scaled = scaler.transform(df_test)
    X_scaled = scaler.transform(df_model)


    medians = df_train.median()
    joblib.dump(medians, ARTIFACTS_PATH + "medians.pkl")
    
    joblib.dump(scaler, ARTIFACTS_PATH + "scaler.pkl")

    df_scaled = pd.DataFrame(
    X_scaled,
    columns=VARIABLES,
    index=df_model.index
)
    df_scaled.to_csv(ARTIFACTS_PATH + "df_scaled.csv", index=False)
    df_variables.to_csv(ARTIFACTS_PATH + "df_variables.csv", index=False)
    df_scaled.head()

    
    pd.DataFrame(X_train_scaled, columns=VARIABLES).to_csv(ARTIFACTS_PATH + "X_train_scaled.csv", index=False)

    pd.DataFrame(X_test_scaled,columns=VARIABLES).to_csv(ARTIFACTS_PATH + "X_test_scaled.csv", index=False)

    df_train.to_csv(ARTIFACTS_PATH + "df_train_variables.csv", index=False)
    df_test.to_csv(ARTIFACTS_PATH + "df_test_variables.csv", index=False)

    print("Preparación de datos completada sin data leakage.")    

    

if __name__ == "__main__":
    main()
