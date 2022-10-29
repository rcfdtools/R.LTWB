## Exploración y análisis de series - EDA - Representación gráfica
Keywords: `EDA` `matplotlib` `pandas` `tabulate`

<div align="center"><img alt="R.LTWB" src="Screenshot/EDA.png" width="75%"></div> 

Durante el proceso de revisión, validación y comprensión de los datos, es necesario utilizar diferentes técnicas que permitan identificar discontinuidades, cambios en el comportamiento temporal y en general revisar los paramétricos de cada serie por parámetro.

¿Qué y para que sirve EDA?



### Objetivos

* Aplicar técnicas de exploración y análisis de datos a series temporales.
* Identificar los tipos de datos contenidos en el conjunto de datos IDEAM.
* Identificar valores nulos en las colecciones de datos para cada objeto o variable.
* Obtener estadísticas generales para las variables numéricas del conjunto de datos.
* Identificar las estaciones contenidas en el conjunto de datos.
* Contar el número de registros por estación para cada parámetro.
* Crear tablas dinámicas (pivot table) por parámetro.
* Crear tablas de correlación por parámetro.
* Realizar análisis segmentados generales de cada parámetro (visualización conjunta de series temporales y densidades KDE, estadísticos generales, matriz de correlación, estadísticos de correlación) y análisis individuales por estación (metadatos por estación, análisis estadístico para los valores registrados, gráficos de serie de tiempo, caja de vigotes, histograma y densidad).


### Requerimientos

* [Python 3+](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/docs/index.html) para Python
* [Tabulate](https://pypi.org/project/tabulate/) para Python, requerido para impresión de tablas en formato Markdown desde pandas.
* Series de datos discretos climatológicos de estaciones terrestres del IDEAM. [:mortar_board:Aprender.](../CNEStationDatasetDownload)


### Procedimiento general

<div align="center">
<br><img alt="R.LTWB" src="Graph/EDA.svg" width="60%"><br>
<sub>Convenciones generales en diagramas: clases de entidad en azul, dataset en gris oscuro, grillas en color verde, geo-procesos en rojo, procesos automáticos o semiautomáticos en guiones rojos y procesos manuales en amarillo. Líneas conectoras con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>

1. Para realizar el análisis exploratorio de datos, descargue el script [EDA.py](../../.src/EDA.py) y guárdelo en la carpeta local `D:\R.LTWB\.src` de su equipo.

Funcionalidades del script

* Permite definir la ventana de tiempo para el análisis a partir de un año inicial y final.
* Generación de reporte detallado Markdown [EDA.md](../../.datasets/IDEAM_EDA/EDA.md).
* Análisis masivo de registros por parámetro generando tablas dinámicas y gráficas generales de análisis.
* Análisis masivo de estaciones por parámetro generando estadísticos y gráficas detalladas de análisis.

> Para el ejemplo, se ha establecido como ventana de tiempo 1980 a 2021.

Contenido del script

```

```

2. Cree una nueva carpeta en blanco con el nombre `IDEAM_EDA` en su directorio de proyecto local `D:\R.LTWB\.datasets`. Verifique que la carpeta `D:\R.LTWB\.datasets\IDEAM`, contenga el archivo [IDEAMJoined.csv](../../.datasets/IDEAM/IDEAMJoined.csv) que fue procesado en la actividad denominada [CNEStationDatasetDownload](../CNEStationDatasetDownload). 

3. En Microsoft Windows, ejecute el _Command Prompt_ o _CMD_, ingrese `D:` y de <kbd>Enter</kbd> para cambiar a la unidad D:\ donde se encuentra el repositorio R.LTWB. Utilizando el comando  `CD D:\R.LTWB\.datasets\IDEAM_EDA` ubíquese dentro de la carpeta IDEAM_EDA.

![R.LTWB](Screenshot/Windows11CMDCD.png)

4. En él `CMD`, ejecute la instrucción `C:\Python3.10.5\python.exe "D:\R.LTWB\.src\EDA.py"` que realizará el procesamiento y análisis de los datos. Durante la ejecución, podrá observar que en la consola se presenta el detalle de los procesos ejecutados para cada parámetro y sus estaciones, además de la previsualización de diferentes tablas en formato Markdown.

![R.LTWB](Screenshot/Windows11CMDEDA1.png)
![R.LTWB](Screenshot/Windows11CMDEDA2.png)
![R.LTWB](Screenshot/Windows11CMDEDA3.png)
![R.LTWB](Screenshot/Windows11CMDEDA4.png)
![R.LTWB](Screenshot/Windows11CMDEDA5.png)
![R.LTWB](Screenshot/Windows11CMDEDA6.png)

Luego de la ejecución, podrá observar que en la carpeta local `D:\R.LTWB\.datasets\IDEAM_EDA` se han generado diferentes archivos de resultados.

![R.LTWB](Screenshot/Windows11CMDEDA7.png)

Dentro de la carpeta `D:\R.LTWB\.datasets\IDEAM_EDA\Graph`, han sido exportadas las diferentes gráficas generales y detalladas de análisis.

![R.LTWB](Screenshot/Windows11CMDEDA8.png)
![R.LTWB](Screenshot/Windows11CMDEDA9.png)
![R.LTWB](Screenshot/Windows11CMDEDA10.png)

Una vez finalizado el proceso de ejecución, podrá sincronizar en la nube los resultados en su repositorio de proyectos de GitHub y podrá observar el reporte detallado en formato Markdown [EDA.md](../../.datasets/IDEAM_EDA/EDA.md).

![R.LTWB](Screenshot/Windows11CMDEDA11.png)
![R.LTWB](Screenshot/Windows11CMDEDA12.png)
![R.LTWB](Screenshot/Windows11CMDEDA13.png)
![R.LTWB](Screenshot/Windows11CMDEDA14.png)
![R.LTWB](Screenshot/Windows11CMDEDA15.png)
![R.LTWB](Screenshot/Windows11CMDEDA16.png)
![R.LTWB](Screenshot/Windows11CMDEDA17.png)

Durante el proceso de ejecución del script, se genera automáticamente las gráficas de análisis que son almacenadas en la carpeta [IDEAM_EDA/Graph](../../.datasets/IDEAM_EDA/Graph), un reporte integrado de resultados en formato Markdown con el nombre [D:\R.LTWB\.datasets\IDEAM_EDA\EDA.md](../../.datasets/IDEAM_EDA/EDA.md) y las siguientes tablas en formato .csv:

| Tabla                                                                                        | Descripción                                                      | Estaciones |
|----------------------------------------------------------------------------------------------|------------------------------------------------------------------|:----------:|
| [Pivot_EV_TT_D.csv](../../.datasets/IDEAM_EDA/Pivot_EV_TT_D.csv)                             | Tabla dinámica con series de evaporación diaria.                 |     1      |
| [Pivot_EV_TT_D_Correlation.csv](../../.datasets/IDEAM_EDA/Pivot_EV_TT_D_Correlation.csv)     | Tabla de correlaciones para series de evaporación diaria.        |     1      |
| [Pivot_PTPM_TT_M.csv](../../.datasets/IDEAM_EDA/Pivot_PTPM_TT_M.csv)                         | Tabla dinámica con series de precipitación mensual.              |    130     |
| [Pivot_PTPM_TT_M_Correlation.csv](../../.datasets/IDEAM_EDA/Pivot_PTPM_TT_M_Correlation.csv) | Tabla de correlaciones para series de precipitación mensual.     |    130     |
| [Pivot_Q_MEDIA_M.csv](../../.datasets/IDEAM_EDA/Pivot_Q_MEDIA_M.csv)                         | Tabla dinámica con series de caudal mensual.                     |     57     |
| [Pivot_Q_MEDIA_M_Correlation.csv](../../.datasets/IDEAM_EDA/Pivot_Q_MEDIA_M_Correlation.csv) | Tabla de correlaciones para series de caudal mensual.            |     57     |
| [Pivot_TMN_CON.csv](../../.datasets/IDEAM_EDA/Pivot_TMN_CON.csv)                             | Tabla dinámica con series de temperatura mínima diaria.          |     25     |
| [Pivot_TMN_CON_Correlation.csv](../../.datasets/IDEAM_EDA/Pivot_TMN_CON_Correlation.csv)     | Tabla de correlaciones para series de temperatura mínima diaria. |     25     |
| [Pivot_TMX_CON.csv](../../.datasets/IDEAM_EDA/Pivot_TMX_CON.csv)                             | Tabla dinámica con series de temperatura máxima diaria.          |     25     |
| [Pivot_TMX_CON_Correlation.csv](../../.datasets/IDEAM_EDA/Pivot_TMX_CON_Correlation.csv)     | Tabla de correlaciones para series de temperatura máxima diaria. |     25     |

En este momento, dispone de un reporte detallado de análisis, tablas dinámicas (pivot tables) y tablas de correlaciones por parámetro.


### Actividades complementarias:pencil2:

En la siguiente tabla se listan las actividades complementarias que deben ser desarrolladas y documentadas por el estudiante en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (mostrar nombre completo, código y enlace a su cuenta de GitHub), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.

| Actividad | Alcance                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:---------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1     | A partir del conteo de registros por estación obtenido para cada grupo de parámetros dentro de la ventana de tiempo establecida, calcule la longitud del registro obtenido y compare con la longitud de registro hipotética de la estación. En la actividad https://github.com/rcfdtools/R.LTWB/tree/main/Section03/CNEStation se realizó el análisis de longitud hipotética.                                            | 
|     2     | Utilizando el script [EDA.py](../../.src/EDA.py), realice el análisis de las variables definidas como actividad complementaria en la actividad https://github.com/rcfdtools/R.LTWB/tree/main/Section03/CNEStationDatasetDownload correspondientes a brillo solar, radiación solar, humedad del aire cerca al suelo y parámetros relacionados con viento y nubosidad.                                                     |
|     3     | Para todas las variables y a partir de las gráficas y tablas de análisis generadas mediante el script [EDA.py](../../.src/EDA.py), presente un análisis cualitativo identificando y explicando posibles datos atípicos, datos fuera de rango y estaciones que deberían ser excluidas del arreglo geográfico de estaciones definido para la zona de estudio por no tener correspondencia espacial o estacional similares. | 


### Referencias

* https://kanoki.org/2020/01/21/pandas-dataframe-filter-with-multiple-conditions/
* https://stackoverflow.com/questions/49684951/pandas-read-csv-dtype-read-all-columns-but-few-as-string
* https://sparkbyexamples.com/pandas/pandas-find-unique-values-from-columns
* https://www.w3schools.com/python/pandas/ref_df_describe.asp
* https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
* https://stackoverflow.com/questions/29370057/select-dataframe-rows-between-two-dates
* https://www.dataquest.io/blog/tutorial-time-series-analysis-with-pandas/
* https://www.statology.org/pandas-plot-distribution-of-column/
* https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.kde.html
* https://towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0
* https://www.digitalocean.com/community/tutorials/exploratory-data-analysis-python
* https://datatofish.com/numpy-array-to-pandas-dataframe/
* https://stackoverflow.com/questions/12286607/making-heatmap-from-pandas-dataframe
* https://stackoverflow.com/questions/17679089/pandas-dataframe-groupby-two-columns-and-get-counts
* https://www.easytweaks.com/pandas-group-one-multiple-columns/
* https://www.geeksforgeeks.org/display-the-pandas-dataframe-in-heatmap-style/


### Control de versiones

| Versión    | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                          | Autor                                      | Horas |
|------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|:-----:|
| 2022.10.29 | Documentación y procedimiento general. Diagrama de procesos.                                                                                                                                                                                                                                                                                                                                                                                         | [rcfdtools](https://github.com/rcfdtools)  |  7.5  |
| 2022.10.28 | Estadísticos generales para cada tabla pivot creada por parámetros. Generación de tablas de correlaciones por cada tabla pivot. Estadísticos generales de las tablas de correlación. Graficación de mapa de calor para correlaciones por parámetro.                                                                                                                                                                                                  | [rcfdtools](https://github.com/rcfdtools)  |   4   |
| 2022.10.27 | Gráfica de análisis de densidad KDE por cada parámetro. Gráficas de análisis por parámetro para cada estación: serie tiempo, boxplot, histograma, densidad KDE. Generación de archivo Markdown EDA.md con análisis general por parámetro y detallado por estación.                                                                                                                                                                                   | [rcfdtools](https://github.com/rcfdtools)  |   8   |
| 2022.10.24 | Inicio creación script EDA.py. Creación de tablas pivot .csv para cada parámetro contenido en el archivo IDEAMJoined.csv: Pivot_EV_TT_D.csv, Pivot_PTPM_TT_M.csv, Pivot_Q_MEDIA_M.csv, Pivot_TMN_CON.csv, Pivot_TMX_CON.csv. Creación de gráficas de series temporales agrupadas para cada parámetro: Plot_EV_TT_D_TimeSerie.png, Plot_PTPM_TT_M_TimeSerie.png, Plot_Q_MEDIA_M_TimeSerie.png, Plot_TMN_CON_TimeSerie.png, Plot_TMX_CON_TimeSerie.png | [rcfdtools](https://github.com/rcfdtools)  |   8   |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Actividad anterior](../RemoteSensing) | [Inicio](../../Readme.md) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/9999) | [Actividad siguiente]()  |
|----------------------------------------|---------------------------|--------------------------------------------------------------------------|--------------------------|

