# Home_Credit_Default_Risk_Microservice_ML
Este repositorio tiene como propósito almacenar cada una de las etapas de realización de una Maquina Predictiva a través de microservicios, siguiendo el orden estipulado por CRISP-DM. Todo esto se realizará en base al dataset de Home Credit Default Risk, el cual posee información variada sobre sus clientes influyente en sus capacidades para solicitar créditos.

# Home Credit
Home Credit es un proveedor de financiamiento al consumo con variadas sedes entre Europa y Asia, enfocada en la entrega de préstamos a personas que poseen poco o nulo historial crediticio, busca acercar el mundo del financiamiento a las personas cuyas solicitudes serían rechazadas por otras entidades. Con un conjunto de datos variado y de grandes dimensiones, Home Credit planteó el desafío de utilizar estos datos para crear diferentes modelos de Machine Learning que apoyen sus decisiones en base a la aceptación o no de las solicitudes de préstamo de sus clientes.

# Descripción de técnicas
Inicialmente, este proyecto fue realizado a través de la plataforma de Google Drive "Colaboratory", la cual nos permitió un desarrollo conciso del código a través de Python, apoyado por la metodología de CRISP-DM que nos permitió tener un desarrollo ordenado en diferentes etapas, evitando confusiones sobre el orden de las acciones realizadas sobre los datos. Finalmente, para la creación de un modelo capaz de realizar clasificaciones de clientes se utilizó K-Means, basado en la facilidad que plantea su uso para trabajar con grandes cantidades de datos y que, a diferencia de DBSCAN, tiene la capacidad de trabajar con los datos luego de ser limpiados y reducidos.

Todo esto fue transformado de tal forma en la que se dividieron los elementos en 6 etapas diferentes basadas en las de la metodología de CRISP-DM, siguiendo un estílo arquitectónico de microservicios para la creación de una API capaz de utilizar el modelo generado con simplicidad a través de streamlit.

# Instrucciones de instalación


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
