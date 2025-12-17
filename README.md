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
Luego de ejecutar el código, se abrirá una ventana en el navegador con el modelo visualizado a través de Streamlit. A partir de esta etapa se podrá agregar información sobre el cliente como lo son sus ingresos o edad. Para que funcione correctamente deben rellenarse todas los cuadros con la información necesaria. Finalmente, podrá hacer click en el botón ```Calcular cluster``` para realizar el calculo final y demostrar las capacidades financieras del cliente ingresado.

# Datos utilizados

### Las variables seleccionadas fueron:

- AMT_INCOME_TOTAL
- AMT_CREDIT
- AMT_ANNUITY
- AGE
- YEARS_EMPLOYED

Se priorizó el uso de estas variables debido a 

Proyecto desarrollado con fines académicos.
