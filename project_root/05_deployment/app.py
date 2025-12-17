import streamlit as st
import pandas as pd
import joblib

ARTIFACTS_PATH = "artifacts/"

@st.cache_resource
def load_artifacts():
    scaler = joblib.load(ARTIFACTS_PATH + "scaler.pkl")
    kmeans = joblib.load(ARTIFACTS_PATH + "kmeans_model.pkl")
    df_variables = pd.read_csv(ARTIFACTS_PATH + "df_variables.csv")
    df_scaled = pd.read_csv(ARTIFACTS_PATH + "df_scaled.csv")
    return scaler, kmeans, df_variables, df_scaled

scaler, kmeans, df_variables, df_scaled = load_artifacts()

st.set_page_config(
    page_title="Home Credit Clustering",
    layout="centered"
)

@st.cache_resource
def load_models():
    scaler = joblib.load(ARTIFACTS_PATH + "scaler.pkl")
    kmeans = joblib.load(ARTIFACTS_PATH + "kmeans_model.pkl")
    medians = joblib.load(ARTIFACTS_PATH + "medians.pkl")
    return scaler, kmeans, medians

scaler, kmeans, medians = load_models()

st.title("Segmentación de Clientes – Home Credit")

st.write(
    """
    Esta aplicación permite **explorar clientes reales** del dataset Home Credit
    y visualizar el **cluster asignado** según su perfil financiero e histórico crediticio.
    """
)

# ===============================
# Selección de cliente
# ===============================
st.sidebar.header("Búsqueda de cliente")

client_id = st.sidebar.number_input(
    "Ingrese SK_ID_CURR",
    min_value=int(df_variables["SK_ID_CURR"].min()),
    max_value=int(df_variables["SK_ID_CURR"].max()),
    step=1
)

buscar = st.sidebar.button("Buscar cliente")


if buscar:

    # ===============================
    # Obtener cliente
    # ===============================
    client_row = df_variables[df_variables["SK_ID_CURR"] == client_id]

    # Cliente no existe o fue eliminado en preparación
    if client_row.empty:
        st.warning(
            "Este cliente no cuenta con información suficiente para ser segmentado."
        )
        st.stop()

    # ===============================
    # Verificar nivel de datos
    # ===============================
    missing_ratio = client_row.isna().mean(axis=1).iloc[0]

    if missing_ratio > 0.3:
        st.warning(
            "⚠️ Este cliente no tiene suficiente información histórica "
            "para asignar un cluster confiable."
        )
        st.stop()

    # ===============================
    # Preparar features
    # ===============================
    client_features = client_row.drop(columns=["SK_ID_CURR"])

    # Rellenar NaN con medianas del entrenamiento
    for col in client_features.columns:
        if col in medians:
            client_features[col] = client_features[col].fillna(medians[col])
        else:
            client_features[col] = client_features[col].fillna(0)

    # Asegurar mismo orden que el scaler
    client_features = client_features[scaler.feature_names_in_]

    # ===============================
    # Escalar y predecir
    # ===============================
    client_scaled = scaler.transform(client_features)
    cluster = int(kmeans.predict(client_scaled)[0])

    # ===============================
    # Mostrar resultados
    # ===============================
    st.subheader("Resultado del Clustering")
    st.success(f"El cliente **{client_id}** pertenece al **Cluster {cluster}**")

    cluster_desc = {
        0: "Clientes con perfil financiero conservador y bajo endeudamiento.",
        1: "Clientes con ingresos medios y comportamiento crediticio estable.",
        2: "Clientes con alto uso de crédito y mayor exposición al riesgo.",
        3: "Clientes con alta capacidad financiera y buen historial."
    }

    st.info(cluster_desc.get(cluster, "Descripción no disponible"))

    # ===============================
    # Mostrar datos completos
    # ===============================
    st.subheader("Perfil completo del cliente")

    st.dataframe(
        client_row.drop(columns=["SK_ID_CURR"]).T,
        use_container_width=True
    )