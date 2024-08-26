---------------------S&P 500 analsis Completo Project---------------------
---------------------Descripción del Proyecto---------------------
Este proyecto tiene como objetivo el análisis de las empresas del S&P 500 a través de la extracción de sus datos mediante Python a dos archivos CSV para su posterior análisis. Se limpiaron los datos extraídos usando OpenRefine y Power Query para dar formato a los distintos datos. Después de esto, se realizó el montaje de los archivos CSV a una base de datos en SQL Management Studio. Estos datos se montaron a dos tablas que se crearon mediante el query de SQL. Al terminar su montaje, se enlazó esta base de datos con Power BI para la visualización de estos datos. También se visualizaron estos datos en Python y se desarrollaron procesos de clusterización para un análisis financiero con fines de identificación del riesgo. Esto último se realizó en Google Colab, usando librerías de automatización y visualización en Python.
---------------------Requisitos---------------------
*Python 3.x
*Librerías: requests, beautifulsoup4, pandas, yfinance, logging, prophet, sqlalchemy, pyodbc, numpy, matplotlib, seaborn, scikit-learn.
*Excel
*OpenRefine
*Power BI Desktop
*SQL Server
*Google Colab
---------------------Estructura del Proyecto---------------------
*data/: Contiene los archivos CSV con los datos de las empresas y perfiles.
*Index/: Contiene los scripts Python para las diferentes fases del proyecto.
*SP500 análisis visual/: Contiene el archivo .pbix de Power BI.
*README.md: Documento explicativo del proyecto.
---------------------Instrucciones de Instalación y Uso---------------------
*Clona este repositorio: git clone https://github.com/tuusuario/Sp500-analisis-Completo.git
                         cd Sp500-analisis-Completo

---------------------Instala las dependencias necesarias:---------------------
*pip install -r requirements.txt (verificar mayúsculas para evitar errores)
*Configura la conexión a SQL Server en los scripts de las fases correspondientes.
*Ejecuta los scripts en orden para realizar el análisis completo.
---------------------Fases del Proyecto---------------------
**Fase 1: Extracción de Datos
*Obtención de datos de empresas del S&P 500 desde Wikipedia.
*Descarga de los precios de cotización del último año.
*Limpieza de los datos usando Power Query y OpenRefine, se eliminaron columnas innecesarias.
**Fase 3: Almacenamiento en SQL Server
*Carga de los datos limpios en una base de datos SQL Server. La carga se realizó con Python después de que se hizo la conexión a la base de datos.
**Fase 4: Dashboard en Power BI
*Creación de un dashboard interactivo con KPIs, tooltips y bookmarks.
**Fase 5: Clusterización de las Acciones
*Agrupamiento de las acciones en clusters según indicadores de volatilidad.
**Fase 6: Publicación en GitHub
*Subida del proyecto al repositorio de GitHub mediante la consola y documentación en este archivo README.md.
