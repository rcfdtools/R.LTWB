## Análisis y mapa de temperatura media
Keywords: `Elevation` `Temperature` `Scatter-plot` `Trend-line`

![R.LTWB](Graph/Temperature.png)

A partir de las series agregadas de temperatura máxima y mínima a nivel anual, se estima la temperatura media anual en cada estación, requerida para la estimación de la evapotranspiración potencial.


### Objetivos

* Calcular la temperatura media multianual en cada estación a partir del promedio de la temperatura máxima y mínima.
* Evaluar el rango de elevaciones y la localización de las estaciones con datos de temperatura disponible. 
* A partir de relación entre los datos de temperatura y elevación, obtener y evaluar ecuaciones características.
* A partir de ecuaciones regionales, crear el mapa de temperatura de la zona de estudio a partir del modelo digital de elevación.


### Requerimientos

* [ArcGIS Pro 2+](https://pro.arcgis.com/en/pro-app/latest/get-started/download-arcgis-pro.htm)
* [ArcGIS for Desktop 10+](https://desktop.arcgis.com/es/desktop/) (opcional)
* [QGIS 3+](https://qgis.org/) (opcional)
* Estaciones hidroclimatológicas de la zona de estudio con validación de altitud a partir de información satelital. [:mortar_board:Aprender.](../../Section03/CNEStationElevation)
* Tablas de valores agregados promedio multianual por parámetro hidroclimatológico. [:mortar_board:Aprender.](../../Section03/Agg)


### Procedimiento general para interpolación de precipitación total

<div align="center">
<br><img alt="R.LTWB" src="Graph/Temperature.svg" width="65%"><br>
<sub>Convenciones generales en diagramas: clases de entidad en azul, dataset en gris oscuro, grillas en color verde, geo-procesos en rojo, procesos automáticos o semiautomáticos en guiones rojos y procesos manuales en amarillo. Líneas conectoras con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>


1. En ArcGIS Pro, abra el proyecto _ArcGISProSection04.aprx_ que se encuentra en la ruta _D:\R.LTWB\\.map_ y que fué creado en la actividad anterior.

![R.LTWB](Screenshot/ArcGISPro3.0.3OpenProject.png)

> Tenga en cuenta que previamente asignamos al mapa el sistema de coordenadas 9377 de Colombia, correspondiente a MAGNA-SIRGAS Origen-Nacional.

2. Desde la tabla de contenido del mapa, renombre la clase de entidad _CNE_IDEAM_OE_ZE_ como _CNE_IDEAM_OE_ZE_Rain_ para conservar la unión y los filtros previamente realizados con los datos de precipitación.

3. Desde la tabla de contenido del mapa y dando clic derecho en _CNE_IDEAM_OE_ZE_Rain_, cree una copia de esta capa y nómbrela como _CNE_IDEAM_OE_ZE_TempMinMax_, luego elimine las uniones, gráficas y filtros existentes asociados a la capa copiada.

![R.LTWB](Screenshot/ArcGISPro3.0.3TempMinMax.png)

4. Desde la carpeta _.datasets/IDEAM_Agg_ disponible en el catálogo, agregue al mapa actual (botón derecho sobre el archivo / Add To Current Map) los archivos [Agg_Impute_MICE_Outlier_IQR_Cap_Pivot_TMN_CON.csv](../../.datasets/IDEAM_Agg/Agg_Impute_MICE_Outlier_IQR_Cap_Pivot_TMN_CON.csv) y [Agg_Impute_MICE_Outlier_IQR_Cap_Pivot_TMX_CON.csv](../../.datasets/IDEAM_Agg/Agg_Impute_MICE_Outlier_IQR_Cap_Pivot_TMX_CON.csv) correspondientes a las tablas de agregaciones multianuales de temperatura mínima y máxima por estación. Luego desde la tabla de contenido o Contents, abra los archivos; podrá observar que se componen de 25 registros o estaciones y que contienen datos compuestos y por fenómeno climatológico.

![R.LTWB](Screenshot/ArcGISPro3.0.3AddTemperatureCsv.png)

5. Desde la tabla de contenido y dando clic derecho sobre cada tabla y mediante la opción _Data / Export Table_, exporte los archivos .csv a archivos dBase .dbf en la misma ruta original y con los nombres [Agg_Impute_MICE_Outlier_IQR_Cap_Pivot_TMN_CON.dbf](../../.datasets/IDEAM_Agg/Agg_Impute_MICE_Outlier_IQR_Cap_Pivot_TMN_CON.dbf) y [Agg_Impute_MICE_Outlier_IQR_Cap_Pivot_TMX_CON.dbf](../../.datasets/IDEAM_Agg/Agg_Impute_MICE_Outlier_IQR_Cap_Pivot_TMX_CON.dbf)

![R.LTWB](Screenshot/ArcGISPro3.0.3TemperatureCsvToDbf.png)

> El proceso de conversión es requerido debido a que es necesario modificar la estructura de la tabla agregando un campo de atributos tipo texto que contendrá el código de la estación, lo anterior debido a que el campo Station es interpretado como un campo numérico entero y el código de las estaciones del catálogo del IDEAM ha sido definido como cadena de texto.

Luego del proceso de exportación, serán cargadas la tabla .dbf al mapa. Remover los archivo .csv de la tabla de contenido y abrir los archivos .dbf.

6. Modifique la estructura de las tablas agregando un nuevo campo de atributos tipo texto de 255 caracteres con el nombre `CODIGO`.

![R.LTWB](Screenshot/ArcGISPro3.0.3AddFieldCODIGO.png)

7. Desde la cabecera del campo `CODIGO` y utilizando la herramienta _Calculate Field_, asigne a este campo los valores contenidos en el campo Station.

![R.LTWB](Screenshot/ArcGISPro3.0.3CalculateFieldCODIGO.png)

8. En la capa de estaciones _CNE_IDEAM_OE_ZE_TempMinMax_, realice dos uniones (clic derecho sobre la capa geográfica / Join) con los datos de las tablas de agregación Agg_Impute_MICE_Outlier_IQR_Cap_Pivot_TMN_CON.dbf y Agg_Impute_MICE_Outlier_IQR_Cap_Pivot_TMX_CON.dbf, utilice como llave de unión el campo `CODIGO`.

![R.LTWB](Screenshot/ArcGISPro3.0.3TempJoinCODIGO.png)

> Tenga en cuenta que los nombres de los campos de atributos AggComposi, AggNina, AggNino y AggNeutral son idénticos en las tablas de agregaciones de datos de temperatura máxima y mínima. Las uniones mantendrán el nombre de las tablas originales antes del nombre del campo, para que pueda identificar su correspondencia, para lo cual, las primeras columnas corresponderán a los datos de temperatura mínima y las columnas finales a temperatura máxima.

9. Abra la tabla de atributos de la capa _CNE_IDEAM_OE_ZE_TempMinMax_ y verifique los datos asociados mediante la unión, podrá observar que existen datos de temperatura  en 25 de las 440 estaciones seleccionadas para la zona de estudio.

![R.LTWB](Screenshot/ArcGISPro3.0.3TempJoinCODIGOTable.png)

10. Desde las propiedades de la capa _CNE_IDEAM_OE_ZE_TempMinMax_, realice un filtro (Definition Query con `Agg_Impute_MICE_Outlier_IQR_Cap_Pivot_TMN_CON.OID >= 0`) para códigos OID mayores o iguales a cero correspondientes a los identificadores de ordenamiento de la tabla .dbf de agregaciones. Luego de dar clic en _Ok_ podrá observar en pantalla la localización de las estaciones con datos de temperatura y los registros correspondientes en la tabla de atributos.

![R.LTWB](Screenshot/ArcGISPro3.0.3TempJoinDefinitionQuery.png)

11. Desde la tabla de contenido, exporte la capa geográfica _CNE_IDEAM_OE_ZE_TempMinMax_ que contiene las uniones y el filtro como _CNE_IDEAM_OE_ZE_TempMinMax.shp_ en el directorio `D:\R.LTWB\.shp`. Automáticamente, será agregada la capa al mapa con la misma simbología de la capa original.

![R.LTWB](Screenshot/ArcGISPro3.0.3CNE_IDEAM_OE_ZE_TempMinMaxExport.png)

12. Modifique la estructura de la capa _CNE_IDEAM_OE_ZE_TempMinMax.shp_ agregando 4 campos de atributos numéricos dobles con los nombres `TMedComp`, `TMedNina`, `TMedNino` y `TMedNeutra`.

![R.LTWB](Screenshot/ArcGISPro3.0.3AddFieldTMed.png)

13. Desde la cabecera de cada uno de los campos creados y utilizando la herramienta _Calculate Field_, calcule la temperatura media por estación utilizando las siguientes expresiones:

* `(!AggCompo_1! + !AggComposi!)/2`
* `(!AggNina_1! + !AggNina!)/2`
* `(!AggNino_1! + !AggNino!)/2`
* `(!AggNeutr_1! + !AggNeutral!)/2`

> Los campos cuyo nombre contienen el sufijo `_1` corresponden a los valores de temperatura máxima.

![R.LTWB](Screenshot/ArcGISPro3.0.3CalculateFieldTMed.png)

![R.LTWB](Screenshot/ArcGISPro3.0.3TMedTable.png)

14. En la tabla de contenido, de clic derecho en la capa _CNE_IDEAM_OE_ZE_TempMinMax_ y seleccione la opción _Create Chart / Scatter Plot_. En el eje X seleccione el campo de atributos `DEMALOS` correspondiente a las elevaciones de las estaciones a partir del modelo digital de elevación ALOS PALSAR, en el eje Y seleccione el campo `TMedComp` correspondiente a valores de temperatura compuesta.

![R.LTWB](Screenshot/ArcGISPro3.0.3TMedDEMALOSTMedCompCorrelation.png)

Como puede observar en la regresion, dos de las estaciones se encuentran dispersas dentro del conjunto de datos incluidos en el análisis. La estación derecha presenta una temperatura de 29.19 °C con altitud 1285 msnm, y la estación en la parte inferior de a gráfica 24.29 °C con altitud 1285 msnm. 

15. Utilizando la tecla <kbd>Ctrl</kbd>, seleccione estas dos estaciones e identifique sus códigos en la tabla de atributos, observará que corresponden a las estaciones 28025040 y 28035070. Utilizando el _Definition Query_ de la capa, exclúyalas utilizando la expresión `CODIGO NOT IN ('28025040', '28035070')`

![R.LTWB](Screenshot/ArcGISPro3.0.3TMedDefinitionQuery1.png)

Para la exclusión realizada, la tendencia presenta la ecuación lineal `y = 28.6 + -0.00238 x` con R² = 0.083, donde `x` representa el valor de la altura y `y` corresponde a la temperatura.

![R.LTWB](Screenshot/ArcGISPro3.0.3TMedDEMALOSTMedCompCorrelationQuery.png)

16. Utilizando el mismo filtro de exclusión de las estaciones 28025040 y 28035070, obtenga las ecuaciones características lineales para los datos de temperatura correspondientes a fenómenos climatológicos, para todas lasseries obtendrá las siguientes expresiones:

| Fenómeno  | Expresión            | R²    |
|-----------|----------------------|-------|
| Compuesto | y = 28.6 - 0.00238 x | 0.083 |
| Niña      | y = 28.5 - 0.0025 x  | 0.093 |
| Niño      | y = 28.8 - 0.00203 x | 0.054 |
| Neutro    | y = 28.6 - 0.0025 x  | 0.095 |

> Como puede observar, los valores obtenidos de los coeficientes de determinación R² son bajos debido a la alta dispersión que existe entre los datos.
> 
> De acuerdo a las elevaciones DEMALOS de la tabla de atributos, los valores presentados en las expresiones únicamente son válidos para estaciones dentro del rango de elevaciones de 

## 



Tabla de grillas obtenidas y de comparación de resultados
| Fenómeno  | Mínimo en estación | Máximo en estación | Mínimo en grilla | Máximo en grilla | Grilla                                                                                                 | Tamaño sin compresión |
|-----------|:---------------:|:---------------:|:------------------:|:------------------:|:--------------------------------------------------------------------------------------------------------:|:-----------------------:|
| Compuesto | 363.2           | 4933.6             | 363.234          | 4933.619         | [Part1](../../.grid/RainTotalComposite.part01.rar), [Part2](../../.grid/RainTotalComposite.part02.rar) | 1.2 GB                |
| Niño      | 252.7              | 4590.4             | 252.749          | 4590.447         | [Part1](../../.grid/RainTotalNino.part01.rar), [Part2](../../.grid/RainTotalNino.part02.rar)           | 1.2 GB                |
| Niña      | 536.3              | 5420.7             | 536.31           | 5420.688         | [Part1](../../.grid/RainTotalNina.part01.rar), [Part2](../../.grid/RainTotalNina.part02.rar)           | 1.2 GB                |
| Neutro    | 305.8              | 4891.5             | 305.754          | 4891.527         | [Part1](../../.grid/RainTotalNeutral.part01.rar), [Part2](../../.grid/RainTotalNeutral.part02.rar)     | 1.2 GB                |

> Debido al tamaño de los archivos generados, cada grilla ha sido comprimida en archivos .rar en partes de 95 MB.
>
> Si bien el método IDW no permite generar isoyetas con apariencia suavizada como el método de líneas espirales, permite obtener valores interpolados próximos al rango de valores de las estaciones utilizadas.

En este momento dispone de grillas interpoladas de precipitación total, requeridas para el balance hidrológico de largo plazo.


### Actividades complementarias:pencil2:

En la siguiente tabla se listan las actividades complementarias que deben ser desarrolladas y documentadas por el estudiante en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (mostrar nombre completo, código y enlace a su cuenta de GitHub), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.


| Actividad | Alcance                                                                                                                                                                                    |
|:---------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1     | Realice la interpolación de la precipitación total en ArcGIS for Desktop y en QGIS, compare con los valores obtenidos en ArcGIS Pro.                                                     |
|     2     | Investigue e interpole la precipitación total compuesta por 3 métodos diferentes (p.ej., Spline, Natural Neghbor, Kriging, Tred) y compare los resultados con los obtenidos en ArcGIS Pro. |


### Referencias

* 


### Compatibilidad

* Esta actividad puede ser desarrollada con cualquier software SIG que disponga de herramientas de interpolación espacial.


### Control de versiones

| Versión    | Descripción | Autor                                      | Horas |
|------------|:------------|--------------------------------------------|:-----:|
| 2022.12.03 | xxxx        | [rcfdtools](https://github.com/rcfdtools)  |  2.5  |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Actividad anterior](../) | [Inicio](../../Readme.md) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/99999) | [Actividad siguiente]()  |
|---------------------------|---------------------------|---------------------------------------------------------------------------|--------------------------|
