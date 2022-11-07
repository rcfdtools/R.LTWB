## Identificación y procesamiento de datos atípicos - Outliers
Keywords: `Outlier` `matplotlib` `pandas` `tabulate` `dtypes` `isnull` `describe` `Drop` `Capped` `Impute` `Interquartile-range` `Empirical-rule` `Z-score`

<div align="center"><img alt="R.LTWB" src="Graph/Outlier.png" width="85%"></div> 

En esta actividad se obtienen los parámetros estadísticos de cada parámetro hidroclimatológico en cada estación y se identifican, excluyen y completan los datos atípicos a través de métodos estadísticos.

Para el desarrollo de esta actividad se utilizarán los siguientes métodos:

* Método 1 - Rango intercuartílico - IQR[^1]: aplica para datos que no siguen una distribución normal y permite identificar valores atípicos a partir de valores que se encuentran por fuera del rango intercuartílico Q1 a Q3. El valor del primer cuartil puede corresponder al percentil 25 y el valor del tercer cuartil puede corresponder al percentil 75 del conjunto de datos, por lo que el rango intercuartílico se calcula como Q3-Q1.  
* Método 2 - Regla empírica - ER[^2]: este método, también denominado regla 3-sigma o regla 68-5-99.7 correspondientes a una distribución normal, permiten identificar valores atípicos cuyas observaciones se encuentran fuera de la banda $\mu$ +- K * $\sigma$. 
* Método 3 - núcleo estándar Z-score[^3]: este método, similar o idéntico al método 2, permite calificar cada observación a partir del valor Z = ( x - $\mu$ ) / $\sigma$. Valores fuera de un valor establecido, p.ej. Z-score=3, son identificados como atípicos.


### Objetivos

* Obtener estadísticas generales de cada estación para cada parámetro hidroclimatológico.
* Identificar valores atípicos a través de diferentes métodos estadísticos (Rango intercuartílico - IQR, regla empírica - ER y núcleo estándar Z-score).
* Representar gráficamente las series de cada parámetro visualizando también los datos atípicos identificados.
* Excluir valores atípicos de la matriz de estaciones para cada parámetro.
* Reemplazar valores atípicos por valores límite definidos a partir de un rango de confianza ( $\mu$ +- K * $\sigma$ ).
* Imputar valores atípicos con el valor de la media de cada estación.


### Requerimientos

* [Python 3+](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/docs/index.html) para Python
* [Tabulate](https://pypi.org/project/tabulate/) para Python, requerido para impresión de tablas en formato Markdown desde pandas.
* [numpy](https://numpy.org/) para python.
* [Notepad++](https://notepad-plus-plus.org/), editor de texto y código.
* Tablas dinámicas (pivot tables) con series de datos discretos de estaciones terrestres del IDEAM por parámetro hidroclimatológico. [:mortar_board:Aprender.](../EDA)


### Procedimiento general

<div align="center">
<br><img alt="R.LTWB" src="Graph/Outlier.svg" width="60%"><br>
<sub>Convenciones generales en diagramas: clases de entidad en azul, dataset en gris oscuro, grillas en color verde, geo-procesos en rojo, procesos automáticos o semiautomáticos en guiones rojos y procesos manuales en amarillo. Líneas conectoras con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>

1. Para realizar la identificación y procesamiento de datos atípicos, descargue el script [Outlier.py](../../.src/Outlier.py) y guárdelo en la carpeta local `D:\R.LTWB\.src` de su equipo.

Funcionalidades del script

* Identificación de atípicos por 3 métodos estadísticos (Método 1 - Rango intercuartílico - IQR, Método 2 - Regla empírica - ER y Método 3 - núcleo estándar Z-score).
* Permite definir la tabla dinámica (pivot table) del parámetro hidroclimatológico a evaluar.
* El usuario puede excluir estaciones del análisis a través de la variable `station_exclude`.
* Definición del cuartil inferior `q1_val` y superior `q3_val` que define el rango de exclusión en el método de rango intercuartílico - IQR.
* Definición manual del multiplicador `cap_multiplier` o K-sigma que permite definir los valores de reemplazo ( $\mu$ +- %s * $\sigma$ ).  
* Definición manual del límite de exclusión `zscore_threshold` en el método de exclusión por núcleo estándar.
* Análisis masivo de estaciones por parámetro hidroclimatológico con estadísticos, parámetros de evaluación y gráficas con marcado de atípicos.
* Generación de reportes detallados Markdown por cada parámetro hidroclimatológico evaluado. [IDEAM_Outlier](../../.datasets/IDEAM_Outlier).
* Para cada método y cada parámetro hidroclimatológico analizado, crea las siguientes tablas: datos atípicos identificados, datos de entrada sin datos atípicos (drop), datos de entrada con datos atípicos reemplazados (cap) y datos de entrada con datos atípicos imputados (impute). 

> En el Método 3 o núcleo estándar Z-score, se genera una tabla adicional para cada parámetro hidroclimatológico que contiene los puntajes a partir de los cuales se realiza la identificación de valores atípicos.   
> 
> Para el ejemplo, se han excluido diferentes estaciones con registros de caudal sobre el Río Magdalena y otros ríos con caudales altos.

Contenido del script

```

```

2. Cree una nueva carpeta en blanco con el nombre `IDEAM_Outlier` en su directorio de proyecto local `D:\R.LTWB\.datasets`. Verifique que la carpeta `D:\R.LTWB\.datasets\IDEAM_EDA`, contenga los archivos de las tablas dinámicas de cada parámetro hicroclimatológico [IDEAM_EDA](../../.datasets/IDEAM_EDA) que fueron obtenidas en la actividad denominada [EDA](../EDA).

> Para la identificación de valores atípicos no son requeridas las tablas de datos de correlaciones identificadas con nombre terminado en _correlation.csv.

3. Desde el editor de texto [Notepad++](https://notepad-plus-plus.org/), abra el archivo [D:\R.LTWB\.src\Outlier.py](../../.src/Outlier.py), y defina las siguientes variables:

* pivot_table_name = 'Pivot_PTPM_TT_M.csv': corresponde a la tabla dinámica (pivot table) a procesar, p.ej., Pivot_PTPM_TT_M.csv corresponde a datos de precipitación mensual total, Pivot_EV_TT_D.csv corresponde a datos de evaporación diaria total, Pivot_Q_MEDIA_M.csv corresponde a datos de caudal medio mensual, Pivot_TMN_CON.csv corresponde a datos de temperatura mínima diaria y Pivot_TMX_CON.csv corresponde a datos de temperatura máxima diaria.

* q1_val = 0.1: cuartil inferior, el valor por defecto es 0.25 en el Método 1 de rango intercuartílico. Para este ejemplo utilizaremos 0.1 para excluir precipitaciones totales altas atípicas.

* q3_val = 0.9: cuartil inferior, el valor por defecto es 0.75 en el Método 1 de rango intercuartílico. Para este ejemplo utilizaremos 0.9 para excluir precipitaciones totales bajas atípicas.

* cap_multiplier = 4.5: multiplicado K-sigma, el valor por defecto es 3. En el método 1 este valor es usado para definir el límite de reemplazo de valores y en el método 2 para identificación de valores atípicos.

* zscore_threshold = 4.5: límite de exclusión en Z-score del método 3, el valor por defecto es 3.  

> Para los datos ejemplo de precipitación mensual total, la identificación de valores atípicos en el rango intercuartílico 0.1 a 0.9 es similar a la obtenida en los métodos 2 y 3 definiendo K-sigma y el Z-score en 4.5.
> 
> Los métodos 2 y 3 permiten identificar los mismos valores atípicos cuando el valor de K-sigma y Z-score es idéntico. Utilice estos métodos para comparar gráficamente exclusión de valores atípicos con diferentes posiciones en la distribución normal.

![R.LTWB](Screenshot/NotepadPlusOutlierpy.png)

4. En Microsoft Windows, ejecute el _Command Prompt_ o _CMD_, ingrese `D:` y de <kbd>Enter</kbd> para cambiar a la unidad D:\ donde se encuentra el repositorio R.LTWB. Utilizando el comando  `CD D:\R.LTWB\.datasets\IDEAM_Outlier` ubíquese dentro de la carpeta IDEAM_Outlier.

![R.LTWB](Screenshot/Windows11CMDCD.png)

5. En él `CMD`, ejecute la instrucción `C:\Python3.10.5\python.exe "D:\R.LTWB\.src\Outlier.py"` que realizará el procesamiento y análisis de los datos. Durante la ejecución, podrá observar que en la consola se presenta el detalle de los procesos ejecutados para cada método, además de la previsualización de diferentes tablas en formato Markdown y gráficas.

![R.LTWB](Screenshot/Windows11CMDOutlier1.png)
![R.LTWB](Screenshot/Windows11CMDOutlier2.png)
![R.LTWB](Screenshot/Windows11CMDOutlier3.png)
![R.LTWB](Screenshot/Windows11CMDOutlier4.png)
![R.LTWB](Screenshot/Windows11CMDOutlier5.png)
![R.LTWB](Screenshot/Windows11CMDOutlier6.png)
![R.LTWB](Screenshot/Windows11CMDOutlier7.png)
![R.LTWB](Screenshot/Windows11CMDOutlier8.png)

Luego de la ejecución, podrá observar que en la carpeta local `D:\R.LTWB\.datasets\IDEAM_Outlier` se han generado diferentes archivos de resultados por cada método para la tabla de datos de precipitación mensual total Pivot_PTPM_TT_M.csv.

![R.LTWB](Screenshot/Windows11CMDOutlier9.png)

Una vez finalizado el proceso de ejecución, podrá sincronizar en la nube los resultados en su repositorio de proyectos de GitHub y podrá observar el reporte detallado en formato Markdown [Outlier_IQR_Pivot_PTPM_TT_M.csv.md](../../.datasets/IDEAM_Outlier/Outlier_IQR_Pivot_PTPM_TT_M.csv.md).

![R.LTWB](Screenshot/Windows11CMDOutlier10.png)
![R.LTWB](Screenshot/Windows11CMDOutlier11.png)
![R.LTWB](Screenshot/Windows11CMDOutlier12.png)
![R.LTWB](Screenshot/Windows11CMDOutlier13.png)
![R.LTWB](Screenshot/Windows11CMDOutlier14.png)
![R.LTWB](Screenshot/Windows11CMDOutlier15.png)
![R.LTWB](Screenshot/Windows11CMDOutlier16.png)
![R.LTWB](Screenshot/Windows11CMDOutlier17.png)
![R.LTWB](Screenshot/Windows11CMDOutlier18.png)
![R.LTWB](Screenshot/Windows11CMDOutlier19.png)

6. Repita el procedimiento anterior para los datos de evaporación, caudal, temperatura mínima y máxima.

Durante el proceso de ejecución del script, se generan automáticamente para cada parámetro hidroclimatológico, un reporte integrado de resultados en formato Markdown (.md), gráficas de análisis y diferentes tablas en formato .csv.

| Reporte                                                                                                | Descripción                                                                 | Estaciones | Registros | 1.IQR | 1.ER | 3.Z-Score | 
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|:----------:|:---------:|:-----:|:----:|:---------:|
| [Outlier_IQR_Pivot_PTPM_TT_M.csv.md](../../.datasets/IDEAM_Outlier/Outlier_IQR_Pivot_PTPM_TT_M.csv.md) | Precipitación mensual total, mm. q1=0.1, q3=0.9, k-sigma=4.5, Z-score=4.5   |    130     |    504    |  94   |  92  |    92     |
| [Outlier_IQR_Pivot_EV_TT_D.csv.md](../../.datasets/IDEAM_Outlier/Outlier_IQR_Pivot_EV_TT_D.csv.md)     | Evaporación diaria total, mm. q1=0.25, q3=0.75, k-sigma=0.45, Z-score=0.45  |     1      |   4821    |  781  | 706  |    706    |
| [Outlier_IQR_Pivot_Q_MEDIA_M.csv.md](../../.datasets/IDEAM_Outlier/Outlier_IQR_Pivot_Q_MEDIA_M.csv.md) | Caudal medio mensual, m³/s. q1=0.1, q3=0.9, k-sigma=3.85, Z-score=3.85      |     46     |    504    |  126  | 123  |    123    |
| [Outlier_IQR_Pivot_TMN_CON.csv.md](../../.datasets/IDEAM_Outlier/Outlier_IQR_Pivot_TMN_CON.csv.md)     | Temperatura diaria mínima, °C. q1=0.175, q3=0.825, k-sigma=3.5, Z-score=3.5 |     25     |   15341   |  403  | 410  |    410    |
| [Outlier_IQR_Pivot_TMX_CON.csv.md](../../.datasets/IDEAM_Outlier/Outlier_IQR_Pivot_TMX_CON.csv.md)     | Temperatura diaria máxima, °C. q1=0.175, q3=0.825, k-sigma=3.6, Z-score=3.6 |     25     |   15341   |  225  | 216  |    216    |

> En la tabla: 1.IQR: número de valores atípicos identificados en Método 1 - Rango intercuartílico, 2.ER: número de valores atípicos identificados en Método 2 - Regla empírica y 3.Z-score: número de valores atípicos identificados en Método 3 - Z-score. La columna _registros_ corresponde al número de registros de cada estación, incluidos los valores faltantes y/o nulos.
>
> Nótese que para datos de temperatura mínima, se han identificado por los 3 métodos, valores atípicos en la zona inferior de las gráficas. En el caso de la temperatura máxima se han identificado valores atípicos en la zona superior e inferior de las gráficas.

Al revisar los estadísticos característicos, p. ej. de la estación 15015020, correspondiente a datos de precipitación total mensual, se pueden observar los siguientes valores similares de media y desviación estándar:

<div align='center'>

| Método                                                             | $\mu$, media | $\sigma$, std |
|:-------------------------------------------------------------------|:-------------|:--------------|
| Serie original                                                     | 59.7829      | 74.2829       |
| 1. Rango intercuartílico - IQR. Reemplazo con $\mu$ - K * $\sigma$ | 59.718       | 73.9846       |
| 1. Rango intercuartílico - IQR. Imputación con $\mu$               | 57.7459      | 69.3425       |
| 2. Regla empírica - ER. Reemplazo con $\mu$ - K * $\sigma$         | 59.718       | 73.9846       |
| 2. Regla empírica - ER. Imputación con $\mu$                       | 57.7459      | 69.3425       |
| 3. Z-score o núcleo estándar. Reemplazo con $\mu$ - K * $\sigma$   | 59.718       | 73.9846       |
| 3. Z-score o núcleo estándar. Imputación con $\mu$                 | 57.7459      | 69.3425       |

</div>

**Conclusión general**

De acuerdo a los valores atípicos identificados para cada variable hidroclimatológica y evaluando las gráficas compuestas donde se representan todas las series de las estaciones objeto de estudio, se puede evidenciar y concluir que no existen en los conjuntos de datos, valores que deban ser necesariamente excluidos, reemplazados o imputados por métodos estadísticos. Para el desarrollo de las actividades posteriores, podrá trabajar con los datos originales o con las tablas de datos con valores atípicos limpiados y/o ajustados, toda vez que se mantienen similares los estadísticos característicos.  

En este momento, dispone de reportes detallados de análisis por cada parámetro hidroclimatológico y diferentes tablas con el procesamiento de datos atípicos.


### Actividades complementarias:pencil2:

En la siguiente tabla se listan las actividades complementarias que deben ser desarrolladas y documentadas por el estudiante en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (mostrar nombre completo, código y enlace a su cuenta de GitHub), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.

| Actividad | Alcance                                                                                                                                                                                                                                                                                                                                                                                                |
|:---------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1     | A partir el script [Outlier.py](../../.src/Outlier.py), realice el análisis de valores atípicos de los parámetros climatológicos definidos como actividad complementaria en la actividad de [descarga de datos hidroclimatológicos](../CNEStationDatasetDownload); correspondientes a brillo solar, radiación solar, humedad del aire cerca al suelo y parámetros relacionados con viento y nubosidad. |
|     2     | Para todas los parámetros climatológicos y a partir de las gráficas y tablas de análisis generadas mediante el script [Outlier.py](../../.src/Outlier.py), presente un análisis cuantitativo definiendo diferentes cuartiles q1 y q3, obtenga el valor K-sigma y Z-score que permita identificar un número similar de valores atípicos.                                                                | 


### Referencias

* https://careerfoundry.com/en/blog/data-analytics/how-to-find-outliers/
* https://datasciencesphere.com/analytics/5-easy-ways-to-detect-outliers-in-python/
* https://realpython.com/pandas-merge-join-and-concat/
* https://www.geeksforgeeks.org/pandas-plot-multiple-time-series-dataframe-into-a-single-plot/
* https://www.tutorialspoint.com/plotting-multiple-dataframes-using-pandas-functionality
* https://sparkbyexamples.com/pandas/pandas-get-column-names
* https://www.statology.org/pandas-index-to-list/
* https://www.statology.org/pandas-exclude-column/
* https://www.investopedia.com/terms/e/empirical-rule.asp
* https://latex-tutorial.com/symbols/greek-alphabet/


### Control de versiones

| Versión    | Descripción                                                                                                                                                                                                                                                                                                    | Autor                                      | Horas |
|------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|:-----:|
| 2022.11.07 | Documentación general. Ejecución para precipitación, evaporación, caudal, temperatura mínima y temperatura máxima. Ajuste de valores de exclusión en método 3 a partir del valor absoluto Z-score obtenido para cada dato. Ilustración cabecera y diagrama de procesos.                                        | [rcfdtools](https://github.com/rcfdtools)  |  7.5  |
| 2022.11.05 | Método 2: funciones para identificación, eliminación, reemplazo e imputación. Generador documento detallado análisis Markdown. Método 3: Z-Score. Idéntico al método 2 con la diferencia que se crea la tabla de puntajes. Al utilizar el k-sigma igual al Z-score threshold, se obtienen los mismos outliers. | [rcfdtools](https://github.com/rcfdtools)  |   5   |
| 2022.11.04 | Método 1: inclusión de reemplazo de outliers usando rango definido  (mean() +- cap_multiplier * std()).                                                                                                                                                                                                        | [rcfdtools](https://github.com/rcfdtools)  |   4   |
| 2022.11.03 | Método 1: inclusión de límites de reemplazo en tabla de parámetros IQR. Ajuste de datos descartando outliers identificados (drop). Método 2, borrador:  identificación de outliers y reemplaza con valores cap con  (mean() +- cap_multiplier * std())                                                         | [rcfdtools](https://github.com/rcfdtools)  |  4.5  |
| 2022.11.03 | Método 1: Rango intercuartílico definido por usuario. Tabla de marcación. Tabla de análisis. Gráfico de análisis.                                                                                                                                                                                              | [rcfdtools](https://github.com/rcfdtools)  |   8   |

_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Actividad anterior](../RemoteSensing) | [Inicio](../../Readme.md) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/9999) | [Actividad siguiente]() |
|----------------------------------------|---------------------------|--------------------------------------------------------------------------|-------------------------|

[^1]: Adapted from: https://careerfoundry.com/en/blog/data-analytics/how-to-find-outliers/
[^2]: https://www.investopedia.com/terms/e/empirical-rule.asp
[^3]: Adapted from: https://www.geeksforgeeks.org/z-score-for-outlier-detection-python/
