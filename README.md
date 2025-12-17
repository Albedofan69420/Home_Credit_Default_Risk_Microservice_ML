# Home_Credit_Default_Risk_Microservice_ML
Este repositorio tiene como propósito almacenar cada una de las etapas de realización de una Maquina Predictiva a través de microservicios, siguiendo el orden estipulado por CRISP-DM. Todo esto se realizará en base al dataset de Home Credit Default Risk, el cual posee información variada sobre sus clientes influyente en sus capacidades para solicitar créditos.

El proyecto fue desarrollado como parte de un examen academico, siguiendo la metodologia CRISP-DM e incorpora buenas practicas de preparacion de datos, prevencion de data leakage, evaluacion y despliegue del modelo.

# Metodologia (CRISP-DM)

Este proyecto sigue las siguientes etapas:

### Comprensión del negocio 
Análisis del problema de riesgo crediticio y la necesidad de segmentar clientes.

### Comprensión de los datos
Uso del dataset principal application_train.csv del proyecto Home Credit.

### Preparación de los datos
Ingeniería de variables (edad, años trabajados)

- Imputación de valores faltantes

- Tratamiento de outliers

- Escalado de variables

- División en conjuntos de entrenamiento y prueba

### Modelamiento
Entrenamiento de un modelo K-Means, determinando el número óptimo de clusters mediante el método del codo.

### Evaluación
Análisis de clusters en training y test, incluyendo visualización con PCA y análisis de la variable TARGET.

### Despliegue
Implementación de una aplicación interactiva utilizando Streamlit.

# Datos utilizados

Dataset principal: application_train.csv

### Variables seleccionadas fueron:

- AMT_INCOME_TOTAL
- AMT_CREDIT
- AMT_ANNUITY
- AGE
- YEARS_EMPLOYED
- 
Nota: Se priorizó el uso de la tabla principal para mantener un flujo controlado y evitar data leakage. El proyecto fue diseñado de forma modular para permitir la incorporación futura de tablas secundarias.

# Despliegue

El modelo fue desplegado usando streamlit, los pasos para poder instalar todo correctamente son:

- Ejecutar el siguiente codigo en cmd dentro de la carpeta "project_root":
  
  ```python -m pip install -r requirements.txt```

- Esto nos servira para instalar las dependencias del proyecto. Una vez se instalen las dependencias, deberemos instalar StreamLit para poder ver de forma visual como se maneja este proyecto, se instala ocupando el siguiente comando: 

  ```python -m pythonpip install streamlit```

- Finalmente cuando se instale StreamLit, ejecutaremos el proyecto con el siguiente codigo

  ```python -m streamlit run 05_deployment/app.py```



Proyecto desarrollado para fines académicos como parte de un examen de Machine Learning.
