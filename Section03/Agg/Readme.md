## Agregación estadística para obtención de promedios multianuales compuestos y por fenómeno climatológico
Keywords: `Compuesto` `El Niño` `La Niña` `Neutro` `matplotlib` `pandas` `Agregación-estadística`

<div align="center"><img alt="R.LTWB" src="Graph/Agg.png" width="95%"></div> 

Luego de validadas y completadas las series, y de realizada la marcación de años por fenómeno climatológico, se efectúa el proceso de agregación estadística para obtener los valores promedio multianuales requeridos en cada estación para su interpolación espacial.


### Objetivos

* Agregar estadísticamente los registros de cada estación para obtener los valores promedio multianuales requeridos para la creación de mapas continuos interpolados.
* Segmentar las series de datos por parámetro por fenómeno climatológico (El Niño, La Niña y Neutro) y realizar su agregación a valores promedio multianual.
* Graficar los registros agregados mensuales y anuales de cada parámetro para todas las estaciones del arreglo de datos.
* Graficar los valores agregados de promedio multianual para datos compuestos y por fenómeno.
* Obtener y graficar valores zonales para cada parámetro estudiado. 


### Requerimientos

* [Python 3+](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/docs/index.html) para Python
* [Tabulate](https://pypi.org/project/tabulate/) para Python, requerido para impresión de tablas en formato Markdown desde pandas.
* [Notepad++](https://notepad-plus-plus.org/), editor de texto y código.
* Tablas con series de datos discretos completados y extendidos (por imputación) de estaciones terrestres del IDEAM por parámetro hidroclimatológico. [:mortar_board:Aprender.](../Impute)
* Tablas de marcación de años por fenómeno climatológico (Niño, Nina y Neutro). [:mortar_board:Aprender.](../ENSOONI)

> Para el desarrollo de esta actividad, no realizaremos la agregación de datos de evaporación potencial debido a que solo existe información diaria en una estación de la zona de estudio. Es posible que actualmente estos registros ya estén disponibles en el servicio [DHIME](https://dhime.ideam.gov.co/) del [IDEAM - Colombia](http://www.ideam.gov.co/) para su descarga.
> 
> Para la segmentación de series utilizaremos la tabla de marcación de años por fenómeno a partir de 5 eventos sucesivos.

### Procedimiento general

<div align="center">
<br><img alt="R.LTWB" src="Graph/Agg.svg" width="75%"><br>
<sub>Convenciones generales en diagramas: clases de entidad en azul, dataset en gris oscuro, grillas en color verde, geo-procesos en rojo, procesos automáticos o semiautomáticos en guiones rojos y procesos manuales en amarillo. Líneas conectoras con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>

Para el desarrollo de esta actividad, realizaremos diferentes tipos de agregaciones utilizando los siguientes parámetros:

| Parámetro / Datos                                                                                                                                              | daily_serie | agg_func | unit label                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|----------|---------------------------|
| Precipitación total mensual<br>[Impute_MICE_Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv](../../.datasets/IDEAM_Impute/Impute_MICE_Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv) | False       | Sum      | Rain, mm                  |
| Temperatura mínima diaria<br>[Impute_MICE_Outlier_IQR_Cap_Pivot_TMN_CON.csv](../../.datasets/IDEAM_Impute/Impute_MICE_Outlier_IQR_Cap_Pivot_TMN_CON.csv)       | True        | Mean     | Min temperature, °C       |
| Temperatura máxima diaria<br>[Impute_MICE_Outlier_IQR_Cap_Pivot_TMX_CON.csv](../../.datasets/IDEAM_Impute/Impute_MICE_Outlier_IQR_Cap_Pivot_TMX_CON.csv)       | True        | Mean     | Max temperature, °C       |
| Caudal medio mensual<>br[Impute_MICE_Outlier_IQR_Cap_Pivot_Q_MEDIA_M.csv](../../.datasets/IDEAM_Impute/Impute_MICE_Outlier_IQR_Cap_Pivot_Q_MEDIA_M.csv)        | False       | Mean     | Flow, m³/s                |
| Evaporación total diaria<br>[Outlier_IQR_Cap_Pivot_EV_TT_D.csv](../../.datasets/IDEAM_Outlier/Outlier_IQR_Cap_Pivot_EV_TT_D.csv)                               | False       | Sum      | Potential evaporation, mm |

> Las variables `daily_serie`, `agg_func` y `unit` deben ser definidas dentro del script de análisis en Python, para la agregación correcta de cada parámetro hidro-climatológico.
> 
> Por defecto, el directorio de archivos con registros por parámetro completados y extendidos por estación se encuentra en el directorio `D:/R.LTWB/.datasets/IDEAM_Impute/`. En caso de que requiera realizar este análisis sin datos completados o extendidos e incluso con las series de datos originales, modifique la variable `station_path` del script.

1. Para realizar las agregaciones estadísticas, descargue el script [Agg.py](../../.src/Agg.py) y guárdelo en la carpeta local `D:\R.LTWB\.src` de su equipo.

**Funcionalidades del script**

* Agregación estadística de datos diarios a mensuales y anuales.
* Agregación estadística de datos mensuales a anuales.
* Segmentación de series por fenómenos climatológicos.
* Agregación mensual.
* Generación de gráficas de análisis.
* Generación de reporte detallado Markdown y tablas de valores agregados y desviaciones estándar en formato de texto separado por comas .csv.

Contenido del script

```
```

2. Cree una nueva carpeta en blanco con el nombre `ENSOONI` en su directorio de proyecto local `D:\R.LTWB\.datasets`.

3. Desde el editor de texto [Notepad++](https://notepad-plus-plus.org/), abra el archivo [D:\R.LTWB\.src\ENSOONI.py](../../.src/ENSOONI.py), y verifique y defina las variables `consecutive_event = 5` y `threshold = 0.5`:

![R.LTWB](Screenshot/NotepadPlusENSOONIpy.png)

4. En Microsoft Windows, ejecute el _Command Prompt_ o _CMD_, ingrese `D:` y de <kbd>Enter</kbd> para cambiar a la unidad D:\ donde se encuentra el repositorio R.LTWB. Utilizando el comando  `CD D:\R.LTWB\.datasets\ENSOONI` ubíquese dentro de la carpeta IDEAM_Impute.

![R.LTWB](Screenshot/Windows11CMDCD.png)

5. En él `CMD`, ejecute la instrucción `C:\Python3.10.5\python.exe "D:\R.LTWB\.src\ENSOONI.py"` que realizará el procesamiento y marcado de años por evento. Durante la ejecución, podrá observar que en la consola se presenta el detalle de los procesos ejecutados, además de la previsualización de diferentes tablas en formato Markdown.

> Para visualizar durante la ejecución las gráficas generales de análisis, establezca la variable `show_plot = True`.

El archivo oni.ascii.txt de la NOAA utiliza la siguiente estructura:

| Atributo | Tipo   | Descripción                                                                                                                                                                              |
|----------|--------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SEAS     | object | Periodo correspondiente a la media móvil de 3 meses, p.ej. DJF corresponde a diciembre, enero y febrero                                                                                  |
| YR       | int64  | Año asociado al periodo                                                                                                                                                                  |
| TOTAL    | int64  | Temperatura en °C                                                                                                                                                                        |
| ANOM     | int64  | Anomalía de temperatura en °C correspondiente a la diferencia entre la temperatura registrada y la media de temperatura centrada de 30 años basada en periodos actualizados cada 5 años. |

![R.LTWB](Screenshot/Windows11CMDENSOONI1.png)
![R.LTWB](Screenshot/Windows11CMDENSOONI2.png)
![R.LTWB](Screenshot/Windows11CMDENSOONI3.png)
![R.LTWB](Screenshot/Windows11CMDENSOONI4.png)
![R.LTWB](Screenshot/Windows11CMDENSOONI5.png)
![R.LTWB](Screenshot/Windows11CMDENSOONI6.png)
![R.LTWB](Screenshot/Windows11CMDENSOONI7.png)

Luego de la ejecución, podrá observar que en la carpeta local `D:\R.LTWB\.datasets\ENSOONI` se encuentra el archivo de texto ONI_Ascii_20221120.txt (cuyo contenido corresponde al archivo oni.ascii.txt obtenido directamente de la NOAA, renombrado incluyendo la fecha de descarga), dos archivos de resultados en formato .csv, diferentes gráficas de análisis y el reporte Markdown.

![R.LTWB](Screenshot/Windows11CMDENSOONI8.png)

Una vez finalizado el proceso de ejecución, podrá sincronizar en la nube los resultados en su repositorio de proyectos de GitHub y podrá observar el reporte detallado en formato Markdown [ONI_Eval.md](../../.datasets/ENSOONI/ONI_Eval.md).

![R.LTWB](Screenshot/Windows11CMDENSOONI9.png)
![R.LTWB](Screenshot/Windows11CMDENSOONI10.png)
![R.LTWB](Screenshot/Windows11CMDENSOONI11.png)
![R.LTWB](Screenshot/Windows11CMDENSOONI12.png)
![R.LTWB](Screenshot/Windows11CMDENSOONI13.png)


### Tablas de resultados y análisis generales

Durante el proceso de ejecución del script, se generan automáticamente dos tablas en formato .csv con el marcado de años por evento para periodos no consecutivos y consecutivos.

| Tabla .csv                                                                         | Descripción                                                                                                   |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [ONI_Eval_NonConsecutive.csv](../../.datasets/ENSOONI/ONI_Eval_NonConsecutive.csv) | Tabla de resultados con marcado de evento por año a partir de 5 o más periodos no consecutivos identificados. |
| [ONI_Eval_Consecutive.csv](../../.datasets/ENSOONI/ONI_Eval_Consecutive.csv)       | Tabla de resultados con marcado de evento por año a partir de 5 o más periodos consecutivos identificados.    |

Los archivos de resultados .csv generados por el script utilizan la siguiente estructura:

| Atributo     | Tipo   | Descripción                                                               |
|--------------|--------|---------------------------------------------------------------------------|
| YR           | int64  | Año                                                                       |
| NinaCount    | int64  | Conteo de eventos Niño (años calientes y secos)                           |
| NinoCount    | int64  | Conteo de eventos Niña (años fríos y húmedos)                             |
| NeutralCount | int64  | Conteo de eventos Neutro                                                  |
| Event        | object | Nombre del evento                                                         |
| EventMark    | int64  | Marcación para gráfica: -1 para Niñas, 0 para Neutros, 1 para Niño        |
| EventLabel   | int64  | Conteo de eventos del fenómeno asociado a utilizar como rótulo en gráfica |

> En la tabla anterior, el campo `Tipo` es asociado a los tipos obtenidos en el dataframe procesado por Pandas en Python.  

En este momento, dispone del reporte detallado de marcación de años por evento climatológico [ONI_Eval.md](../../.datasets/ENSOONI/ONI_Eval.md) y dos tablas en formato de texto separado por comas `.csv` para la posterior segmentación de las series de parámetros hidroclimatológicos.


### Actividades complementarias:pencil2:

En la siguiente tabla se listan las actividades complementarias que deben ser desarrolladas y documentadas por el estudiante en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (mostrar nombre completo, código y enlace a su cuenta de GitHub), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.

| Actividad | Alcance         |
|:---------:|:----------------|
|     1     |                 |
|     2     |                 | 


### Referencias

* https://library.wmo.int/doc_num.php?explnum_id=4167
* https://library.wmo.int/index.php?lvl=notice_display&id=20130
* https://library.wmo.int/doc_num.php?explnum_id=9521
* https://library.wmo.int/doc_num.php?explnum_id=4549
* https://stackoverflow.com/questions/11391969/how-to-group-pandas-dataframe-entries-by-date-in-a-non-unique-column
* https://stackoverflow.com/questions/5283649/plot-smooth-line-with-pyplot
* https://www.geeksforgeeks.org/indexing-and-selecting-data-with-pandas/
* https://www.geeksforgeeks.org/pandas-find-unique-values-from-multiple-columns/
* https://www.geeksforgeeks.org/ways-to-filter-pandas-dataframe-by-column-values/
* https://www.geeksforgeeks.org/how-to-concatenate-two-or-more-pandas-dataframes/
* https://stackoverflow.com/questions/29550414/how-can-i-split-a-column-of-tuples-in-a-pandas-dataframe
* https://www.geeksforgeeks.org/convert-the-column-type-from-string-to-datetime-format-in-pandas-dataframe/
* https://www.geeksforgeeks.org/how-to-drop-one-or-multiple-columns-in-pandas-dataframe/
* https://www.geeksforgeeks.org/how-to-move-a-column-to-first-position-in-pandas-dataframe/


### Control de versiones

| Versión    | Descripción | Autor                                       | Horas |
|------------|:------------|---------------------------------------------|:-----:|
| 2022.11.20 | XXX         | [rcfdtools](https://github.com/rcfdtools)   |   4   |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Actividad anterior](../ENSOONI) | [Inicio](../../Readme.md) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/9999) | [Actividad siguiente]() |
|----------------------------------|---------------------------|--------------------------------------------------------------------------|-------------------------|

[^1]: https://es.wikipedia.org/