## Obtención de series de datos discretos climatológicos satelitales y correlación con datos terrestres
Keywords: `Remote sensing` `Chirps` `Correlation` `Pearson` `Kendall` `Spearman` `Scatter plot` `pandas` `rasterio` `requests` `tabulate`

![R.LTWB](Screenshot/RemoteSensing.png)

Para la validación o el contraste de información terrestre, se pueden obtener datos satelitales de precipitación diaria total, temperatura y evapotranspiración sobre las localizaciones específicas de la red climatológica utilizada. A partir de la información recopilada y validada para la red estaciones a usar en la zona de estudio y la conformación de series a partir de datos satelitales en las localizaciones específicas de la red, se correlacionan estos datos para evaluar si existe correspondencia y homogeneidad entre ellos.                                                                                                                                                                                                 


### Objetivos

* Descargar grillas de precipitación mensual total usando el servicio [CHIRPS](https://www.chc.ucsb.edu/data/chirps) - Climate hazards group infrared precipitation.
* Realizar la lectura de los valores de precipitación Chirps, en las localizaciones de la red de estaciones terrestres utilizadas para la obtención de datos del [IDEAM - Colombia](http://www.ideam.gov.co/).
* Realizar análisis de correlación entre datos terrestres y datos obtenidos a partir de observaciones satelitales.


### Requerimientos

* [Python 3+](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/docs/index.html) para Python
* [Rasterio](https://pypi.org/project/rasterio/) para Python
* [Requests](https://requests.readthedocs.io/) para Python
* [Tabulate](https://pypi.org/project/tabulate/) para Python, requerido para impresión de tablas en formato Markdown desde pandas.
* Series de datos discretos climatológicos de estaciones terrestres del IDEAM. [:mortar_board:Aprender.](../CNEStationDatasetDownload)


### Procedimiento general - Precipitación CHIRPS [^1] 

<div align="center">
<br><img alt="R.LTWB" src="Graph/RemoteSensing.svg" width="80%"><br>
<sub>Convenciones del diagrama: Base de datos geográfica GDB en azul, Clases de entidad en gris, Geo-procesos en verde y Procesos manuales en amarillo.<br>Líneas con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>

CHIRPS permite descargar datos de precipitación diaria con resoluciones espaciales de 0.05 y 0.25 grados (5.5 y 27.8 km aprox.) en formatos BIL, TIDD o NetCDF y con series de 30 o más años. La banda de descarga se ubica entre las latitudes 50°S a -50°N en todas las longitudes de la superficie terrestre, iniciando su captura desde 1981 y hasta la actualidad. CHIRPS combina imágenes satelitales (NASA y NOAA) con datos registrados en estaciones terrestres y es frecuentemente utilizado para análisis de tendencias y monitoreo de sequías debidas a cambios estacionales. Esta fusión de datos permite estimar valores en zonas en las que no existen estaciones terrestres, complementando valores obtenidos por otros métodos que tienen en cuenta la relación espacial entre estaciones próximas.

Desde el año 1999, el Servicio Geológico de los Estados Unidos de América – USGS y los científicos del Grupo de Amenazas Climáticas - CHG, con el apoyo de la Agencia Internacional para el Desarrollo de los Estados Unidos – USAID, la NASA y la NOAA, han desarrollado técnicas para producir mapas de precipitación especialmente en zonas donde existen pocos datos. Estimar espacial y temporalmente las variaciones de la precipitación, es un aspecto importante para el monitoreo del medio ambiente y para mitigar las sequías.

1. Para la descarga, lectura y análisis de correlación, descargue el script [ChirpsGetValue.py](../../.src/ChirpsGetValue.py) y muévalo a la carpeta local `D:\R.LTWB\.src` de su equipo. Este script ha sido desarrollado por [rcfdtools](https://github.com/rcfdtools). 

Funcionalidades del script [ChirpsGetValue.py](../../.src/ChirpsGetValue.py)

* Descarga directa de archivos comprimidos de grillas Chirps de precipitación mensual total a partir de la definición de un rango de año, p.ej., entre 1981 y 2021.
* Descompresión de grillas .tif.
* Segmentación mensual por año del archivo integrado de registros discretos obtenidos del IDEAM para la Etiqueta = "PTPM_TT_M" correspondiente a datos de precipitación mensual total.
* Lectura de valores Chirps por mes en cada año sobre las localizaciones específicas de la red de estaciones terrestres del IDEAM. Para cada mes en cada año, se crea un archivo .csv que contiene los valores leídos de Chirps, p.ej., [chirps-v2.0.1981.01.csv](../../.datasets/CHIRPS/chirps-v2.0.1981.01.csv).
* Integración de archivos .csv en un único archivo, nombrado como [IDEAMJoinedChirps.csv](../../.datasets/CHIRPS/IDEAMJoinedChirps.csv).
* Para cada mes de cada año, se calculan las correlaciones utilizando los métodos de Pearson, Kendal y Spearman y se genera el archivo [IDEAMJoinedChirpsCorrelationDate.csv](../../.datasets/CHIRPS/IDEAMJoinedChirpsCorrelationDate.csv).
* A partir de los valores de correlación estimados en cada mes para cada año, se calculan los valores promedio de las correlaciones y se genera el archivo [IDEAMJoinedChirpsCorrelationDateMean.csv](../../.datasets/CHIRPS/IDEAMJoinedChirpsCorrelationDateMean.csv) que contiene 3 valores.
* A partir de los valores de correlación estimados en cada mes para cada año, se calculan los valores promedio de las correlaciones por año y se genera el archivo [IDEAMJoinedChirpsCorrelationYear.csv](../../.datasets/CHIRPS/IDEAMJoinedChirpsCorrelationYear.csv) que contiene 3 valores por cada año. 
* A partir de los valores de correlación estimados en cada mes para cada año, se calculan los valores promedio de las correlaciones por mes y se genera el archivo [IDEAMJoinedChirpsCorrelationMonth.csv](../../.datasets/CHIRPS/IDEAMJoinedChirpsCorrelationMonth.csv) que contiene 3 valores para los 12 meses del año.
* Generación de 6 gráficas de análisis con análisis de series de correlación y cajas de bigotes.
* Generación de reporte integrado en formato Markdown, nombrado como [RemoteSensingRainChirps.md](../../.datasets/CHIRPS/RemoteSensingRainChirps.md)
 

Contenido del script [ChirpsGetValue.py](../../.src/ChirpsGetValue.py)

'''



'''

2. Cree una nueva carpeta en blanco con el nombre CHIRPS en su directorio de proyecto local `D:\R.LTWB\.datasets`



![R.LTWB](Screenshot/xxxx.png)


En este momento, dispone de registros IDEAM de precipitación con el registro de valores Chirps y diferentes análisis de correlación.


### Actividades complementarias:pencil2:

En la siguiente tabla se listan las actividades complementarias que deben ser desarrolladas y documentadas por el estudiante en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (mostrar nombre completo, código y enlace a su cuenta de GitHub), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.

| Actividad | Alcance                                                                                                                                                                                                                                                                                                                                                                                              |
|:---------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1     | Para las estaciones identificadas en la actividad complementaria [CNEStation](../CNEStation) relacionadas con brillo solar, radiación solar, humedad del aire cerca al suelo y parámetros relacionados con viento y nubosidad, descargue los registros disponibles en DHIME del IDEAM e integre las series a las presentadas en esta actividad. | 




### Referencias

* https://www.earthdata.nasa.gov/learn/backgrounders/remote-sensing
* https://www.chc.ucsb.edu/data/chirps
* https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_monthly/tifs/
* https://hatarilabs.com/ih-en/extract-point-value-from-a-raster-file-with-python-geopandas-and-rasterio-tutorial
* [Python Scripting for Exporting Multiple Rasters into Time Series](https://www.youtube.com/watch?v=6zzneGT4mkg)
* https://sparkbyexamples.com/pandas/pandas-dataframe-filter/
* https://towardsdatascience.com/8-ways-to-filter-pandas-dataframes-d34ba585c1b8
* https://towardsdatascience.com/4-tricks-you-should-know-to-parse-date-columns-with-pandas-read-csv-27355bb2ad0e
* https://www.codegrepper.com/code-examples/python/how+to+extract+gz+file+python
* https://www.geeksforgeeks.org/python-pandas-dataframe-corr/
* https://stackoverflow.com/questions/42579908/use-corr-to-get-the-correlation-between-two-columns
* https://stackoverflow.com/questions/36454494
* https://www.geeksforgeeks.org/python-pandas-dataframe-set_index/
* https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html
* https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html
* https://pandas.pydata.org/docs/reference/api/pandas.concat.html
* https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html
* https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.GroupBy.mean.html
* https://www.w3schools.com/python/ref_func_range.asp
* https://matplotlib.org/stable/tutorials/colors/colormaps.html
* [Pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)
* [Kendall rank correlation coefficient](https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient)
* [Spearman’s rank correlation coefficient](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient)


### Compatibilidad

* Esta actividad puede ser desarrollada con cualquier software SIG que disponga de herramientas para de digitalización con opciones de encajado o snapping.
* 


### Control de versiones

| Versión    | Descripción     | Autor                                      | Horas |
|------------|:----------------|--------------------------------------------|:-----:|
| 2022.10.07 | Versión inicial | [rcfdtools](https://github.com/rcfdtools)  |   0   |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Actividad anterior](../CNEStationDatasetDownload) | [Inicio](../../Readme.md) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/99999) | [Actividad siguiente]()  |
|----------------------------------------------------|---------------------------|---------------------------------------------------------------------------|--------------------------|

[^1]: https://www.chc.ucsb.edu/data/chirps