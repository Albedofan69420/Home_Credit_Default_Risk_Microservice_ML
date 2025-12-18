# Home_Credit_Default_Risk_Microservice_ML
Este repositorio tiene como propósito almacenar cada una de las etapas de realización de una Maquina Predictiva a través de microservicios, siguiendo el orden estipulado por CRISP-DM. Todo esto se realizará en base al dataset de Home Credit Default Risk, el cual posee información variada sobre sus clientes influyente en sus capacidades para solicitar créditos.

# Home Credit
Home Credit es un proveedor de financiamiento al consumo con variadas sedes entre Europa y Asia, enfocada en la entrega de préstamos a personas que poseen poco o nulo historial crediticio, busca acercar el mundo del financiamiento a las personas cuyas solicitudes serían rechazadas por otras entidades. Con un conjunto de datos variado y de grandes dimensiones, Home Credit planteó el desafío de utilizar estos datos para crear diferentes modelos de Machine Learning que apoyen sus decisiones en base a la aceptación o no de las solicitudes de préstamo de sus clientes.

# Descripción de técnicas
Inicialmente, este proyecto fue realizado a través de la plataforma de Google Drive "Colaboratory", la cual nos permitió un desarrollo conciso del código a través de Python, apoyado por la metodología de CRISP-DM que nos permitió tener un desarrollo ordenado en diferentes etapas, evitando confusiones sobre el orden de las acciones realizadas sobre los datos. Finalmente, para la creación de un modelo capaz de realizar clasificaciones de clientes se utilizó K-Means, basado en la facilidad que plantea su uso para trabajar con grandes cantidades de datos y que, a diferencia de DBSCAN, tiene la capacidad de trabajar con los datos luego de ser limpiados y reducidos.

Todo esto fue transformado de tal forma en la que se dividieron los elementos en 6 etapas diferentes basadas en las de la metodología de CRISP-DM, siguiendo un estílo arquitectónico de microservicios para la creación de una API capaz de utilizar el modelo generado con simplicidad a través de streamlit.

# Instrucciones de instalación y ejecución
El proyecto debe ser descargado en formato .ZIP, por lo que se requieren de herramientas de extracción tales como WinRAR, 7-Zip o similares para poder trabajarlo y ejecutarlo. Al descargarse, este puede descomprimirse en cualquier carpeta deseada, obteniendose como resultado una carpeta llamada ```project_root```. Al abrirse se visualizarán variadas carpetas en las que se divide el proyecto en formato .py, basada en la estructura de microservicios y un archivo txt llamado.

Para la instalación de las dependencias necesarias para ejecutar el código, se debe abrir la carpeta ```project_root``` dentro del terminal CMD y ejecutar el siguiente código dentro de la ventana del terminal:

  ```python -m pip install -r requirements.txt```

Puede que la instalación de dependencias requiera de mayor tiempo de espera en equipos de bajo rendimiento. En caso de que la instalación tome demasiado tiempo se recomienda reabrir una ventana de CMD en la carpeta de ```project_root``` y ejecutar nuevamente el código indicado arriba. Se verificarán las intalaciones anteriores y realizará aquellas que no fueron ejecutadas antes.

Tras finalizar la instalación de dependencias, se procederá con la visualización del modelo realizado a través de Streamlit. Para ello, se debe ejecutar el siguiente código en la ventana de CMD abierta con anterioridad:

  ```python -m streamlit run 05_deployment/app.py```

# Instrucciones de uso
Luego de ejecutar el código, se abrirá una ventana en el navegador con el modelo visualizado a través de Streamlit. A partir de esta etapa se podrá seleccionar clientes incluidos dentro del set de solicitantes y consultar sobre sus capacidades de pagar los préstamos solicitados.

<img width="1914" height="838" alt="image" src="https://github.com/user-attachments/assets/64aee2c8-8892-4fde-aaaa-2091d36a72bf" />

En casos en los que no se posea información suficiente sobre los solicitantes o en los que ocurran errores con la información, se mostrará un mensaje en pantalla indicando el error.

<img width="1916" height="833" alt="image" src="https://github.com/user-attachments/assets/4a627a5b-9474-4286-80d2-c5d5c5928da1" />

## Análisis e interpretación de resultados
A la hora de consultar sobre los solicitantes y su información, estos pueden ser divididos en 4 secciones diferentes:

- Clientes con alta capacidad financiera y buen historial: Solicitantes con bajo riesgo de incumplimiento, con alta capacidad financiera y un historial crediticio favorable.

- Clientes con alto uso de crédito y mayor exposición al riesgo: Solicitantes con mayor nivel de riesgo crediticio, asociados a un uso intensivo del crédito y mayor probabilidad de incumplimiento.

- Clientes con ingresos medios y comportamiento crediticio estable: Solicitantes con riesgo crediticio moderado, con ingresos estables y un historial de pago generalmente confiable.

- Clientes con perfil financiero conservador y bajo endeudamiento: Solicitantes con bajo nivel de riesgo crediticio, caracterizados por un bajo nivel de endeudamiento y comportamiento financiero conservador.

Cabe destacar que la aceptación de las solicitudes de préstamos se está sujeto a criterio humano, por lo que este puede diferir basado en diferentes experiencias y personas, no definiendose como una herramienta objetiva capaz de determinar con certeza las capacidades de cada cliente del ente financiero de Home Credit.

# Datos utilizados

### Las variables seleccionadas fueron las siguientes:

- AMT_INCOME_TOTAL
- AMT_CREDIT
- AMT_ANNUITY
- AGE
- YEARS_EMPLOYED
- BUREAU_CREDIT_MEAN
- BUREAU_CREDIT_SUM
- BUREAU_DAYS_CREDIT_MEAN
- BUREAU_MAX_OVERDUE
- BB_MONTHS_COUNT_MEAN
- BB_STATUS_MEAN
- BB_MAX_STATUS
- BB_HAS_OVERDUE
- PREV_APP_COUNT
- PREV_APP_AMT_CREDIT_MEAN
- PREV_APP_REFUSED_RATIO
- PREV_APP_DAYS_DECISION_MEAN
- POS_MONTHS_COUNT
- POS_DPD_MEAN
- POS_DPD_MAX
- INST_PAYMENT_RATIO_MEAN
- INST_DPD_MEAN
- INST_DPD_MAX
- CC_BALANCE_MEAN
- CC_LIMIT_MEAN
- CC_UTILIZATION_MEAN
- CC_DPD_MEAN

Se priorizó el uso de estas variables debido a su gran capacidad descriptiva sobre los usuarios de Home Credit y sus capacidades financieras. Basandose en edad, estabilidad laboral, ingresos e historial crediticio (en conjunto con sus capacidades para pagar los prestamos en los tiempos designados) se logra obtener información necesaria para comprender los comportamientos de los clientes y segmentarlos basandose en caracteristicas similares encontradas entre todas las personas identificadas dentro de los datasets.

# Aplicación de CRISP-DM y flujo de trabajo
Para el correcto desarrollo del proyecto, se siguieron las 6 etapas necesarias de la metodología de CRISP-DM.

- Comprensión del negocio: Se analiza el negocio de Home Credit, una entidad financiera que se enfoca en la entrega de préstamos a aquellas personas que poseen poco o nulo historial crediticio. Se comprende el riesgo de entregar préstamos a personas que no pueden cumplir con los plazos especificados y se plantea la necesidad de segmentar a los clientes analizando sus características.

- Comprensión de los datos: Se trabaja con todos los parquet prestados por Home Credit, los cuales contienen información sobre sus solicitantes de préstamos, solicitudes hechas en diferentes entidades e información crediticia. Tras realizar un análisis de la información se comprende la presencia de nulos y una gran cantidad de columnas que no necesariamente deban incluirse al proyecto final, queriendo evitar problemas dimensionales y seleccionando las mejores variables para trabajar.

- Preparación de datos: Se transforman datos contenidos dentro de diferentes columnas para un mayor entendimiento. Se imputan valores y escalan. Es reducida la dimensionalidad para trabajar con variables consideradas importantes a la hora de definir si se acepta o no un préstamo. Finalmente, se tratan outliers para evitar el desplazo de categorías por clientes inusuales.

- Modelamiento: A partir de los datos seleccionados, se dividen los datos en train y test para evitar el data leakage. Se realiza el modelo con K-Means, donde se determinó la cantidad final de clusters gracias a la utilización del método del codo para su elección.

- Evaluación: Análisis de clusters a partir de la visualización con PCA, se realiza análisis de la variable TARGET y se identifican las caracteristicas principales de cada uno de los segmentos de clientes generados.

- Despliegue: Realización de una aplicación interactiva a partir de Streamlit. Se aplican correcciones en el código para evitar errores en la presentación visual de los resultados del modelo.

Proyecto desarrollado con fines académicos.
