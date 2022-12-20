## Balance hidrológico a partir de cuencas delimitadas
Keywords: `LTWB` `Flow` `Zonal-statistics-as-table`

![R.LTWB](Graph/LTWBBasin.png)

Cuando existen zonas delimitadas como cuencas hidrográficas, es posible mediante estadísticos zonales, estimar manualmente el balance hidrológico a partir de los mapas de precipitación media y evapotranspiración real.

### Objetivos

* A partir de los mapas de precipitación total y evapotranspiración real compuesta y por fenómeno climatológico, obtener los valores medios zonales y realizar el balance hidrológico de largo plazo para la zona 28 y subzonas hidrográfica IDEAM en estudio.
* Analizar los resultados obtenidos para series compuestas y por fenómeno climatológico.


### Requerimientos

* [ArcGIS Pro 2+](https://pro.arcgis.com/en/pro-app/latest/get-started/download-arcgis-pro.htm)
* [ArcGIS for Desktop 10+](https://desktop.arcgis.com/es/desktop/) (opcional)
* [QGIS 3+](https://qgis.org/) (opcional)
* Subzonas hidrográficas IDEAM - Colombia. [:mortar_board:Aprender.](../../Section01/CaseStudy) 
* Mapas de precipitación total. [:mortar_board:Aprender.](../../Section04/Rain)
* Mapa de evapotranspiración real. [:mortar_board:Aprender.](../../Section04/ETR)


### Procedimiento general

<div align="center">
<br><img alt="R.LTWB" src="Graph/LTWBBasin.svg" width="65%"><br>
<sub>Convenciones generales en diagramas: clases de entidad en azul, dataset en gris oscuro, grillas en color verde, geo-procesos en rojo, procesos automáticos o semiautomáticos en guiones rojos y procesos manuales en amarillo. Líneas conectoras con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>

1. En ArcGIS Pro, abra el proyecto _ArcGISProSection05.aprx_ creado en la primera actividad de esta sección y almacenado en la ruta _D:\R.LTWB\\.map_.

![R.LTWB](Screenshot/ArcGISPro3.0.3OpenMapProject.png)

> Tenga en cuenta que automáticamente fué asignado al proyecto, el sistema de coordenadas geográficas 9377 de Colombia, correspondiente a MAGNA-SIRGAS Origen-Nacional.

2. Desde la carpeta _D:\R.LTWB\HECGeoHMS\.shp_ disponible en el catálogo, agregue al proyecto los archivos de formas [ZonaEstudio.shp](../../.shp/ZonaEstudio.zip) y [Zonificacion_hidrografica_2013.shp](../../.shp/Zonificacion_Hidrografica_2013.zip). Modifique la simbología de representación para la zona de estudio a borde rojo, grosor 3 sin relleno y para las subzonas en borde negro, grosor 1 sin relleno. Utilizando la expresión `COD_ZH = 28`, filtre la capa de zonificación hidrográfica para solo los polígonos asociados a la subzona hidrográfica 28 y rotule a partir del campo `COD_SZH`.

![R.LTWB](Screenshot/ArcGISPro3.0.3ZESZHFilter.png)

3. Utilizando la herramienta _Geoprocessing / Spatial Analyst Tools / Zonal / Zonal Statistics as Table_, obtenga los estadísticos zonales para la zona de estudio a partir de los mapas de precipitación total y evapotranspiración real.

![R.LTWB](Screenshot/ArcGISPro3.0.3ZonalStatisticsAsTable.png)

Nombre los archivos de estadísticas zonales de acuerdo a las indicaciones de la siguiente tabla y almacene dentro de la Geodatabase del proyecto _ArcGISProSection05.aprx_ en `D:\R.LTWB\\.map`. Registre los valores medios obtenidos.

| Fenómeno / Zona                              | Tabla zonal           | Promedio, mm/año |
|----------------------------------------------|-----------------------|------------------|
| **Precipitación zona de estudio**            |                       |                  |
| Compuesto / Zona estudio - ZE                | RainTotalCompositeZE  |                  |
| Niña / Zona estudio - ZE                     | RainTotalNinaZE       |                  |
| Niño / Zona estudio - ZE                     | RainTotalNinoZE       |                  |
| neutro / Zona estudio - ZE                   | RainTotalNeutralZE    |                  |
| **Precipitación subzona hidrográfica**       |                       |                  |
| Compuesto / Subzona hidrográfica - SZH       | RainTotalCompositeSZH |                  |
| Niña / Subzona hidrográfica - SZH            | RainTotalNinaSZH      |                  |
| Niño / Subzona hidrográfica - SZH            | RainTotalNinoSZH      |                  |
| neutro / Subzona hidrográfica - SZH          | RainTotalNeutralSZH   |                  |
| **Evapotranspiración zona de estudio**       |                       |                  |
| **Budyko**                                   |                       |                  |
| Compuesto / Zona estudio - ZE                | ETRBudykoCompositeZE  |                  |
| Niña / Zona estudio - ZE                     | ETRBudykoNinaZE       |                  |
| Niño / Zona estudio - ZE                     | ETRBudykoNinoZE       |                  |
| neutro / Zona estudio - ZE                   | ETRBudykoNeutralZE    |                  |
| **Dekop**                                    |                       |                  |
| Compuesto / Zona estudio - ZE                | ETRDekopCompositeZE   |                  |
| Niña / Zona estudio - ZE                     | ETRDekopNinaZE        |                  |
| Niño / Zona estudio - ZE                     | ETRDekopNinoZE        |                  |
| neutro / Zona estudio - ZE                   | ETRDekopNeutralZE     |                  |
| **Turc**                                     |                       |                  |
| Compuesto / Zona estudio - ZE                | ETRTurcCompositeZE    |                  |
| Niña / Zona estudio - ZE                     | ETRTurcNinaZE         |                  |
| Niño / Zona estudio - ZE                     | ETRTurcNinoZE         |                  |
| neutro / Zona estudio - ZE                   | ETRTurcNeutralZE      |                  |
| **Evapotranspiración  subzona hidrográfica** |                       |                  |
| **Budyko**                                   |                       |                  |
| Compuesto / Subzona hidrográfica - SZH       | ETRBudykoCompositeSZH |                  |
| Niña / Subzona hidrográfica - SZH            | ETRBudykoNinaSZH      |                  |
| Niño / Subzona hidrográfica - SZH            | ETRBudykoNinoSZH      |                  |
| neutro / Subzona hidrográfica - SZH          | ETRBudykoNeutralSZH   |                  |
| **Dekop**                                    |                       |                  |
| Compuesto / Subzona hidrográfica - SZH       | ETRDekopCompositeSZH  |                  |
| Niña / Subzona hidrográfica - SZH            | ETRDekopNinaSZH       |                  |
| Niño / Subzona hidrográfica - SZH            | ETRDekopNinoSZH       |                  |
| neutro / Subzona hidrográfica - SZH          | ETRDekopNeutralSZH    |                  |
| **Turc**                                     |                       |                  |
| Compuesto / Subzona hidrográfica - SZH       | ETRTurcCompositeSZH   |                  |
| Niña / Subzona hidrográfica - SZH            | ETRTurcNinaSZH        |                  |
| Niño / Subzona hidrográfica - SZH            | ETRTurcNinoSZH        |                  |
| neutro / Subzona hidrográfica - SZH          | ETRTurcNeutralSZH     |                  |







> Para este ejemplo, generaremos el mapa de isorendimiento a partir de los caudales medios obtenidos con el mapa de evapotranspiración real compuesta de Budyko utilizando la siguiente expresión:

<div align="center">

Im = Qm / A

</div>

Donde,

* Im: isorendimiento medio, lps/km²
* Qm: caudal medio, lps
* A: área de aportación,km²

Expresión algebra de mapas: `FlowPerfBudykoComposite.tif = "LTWBBudykoComposite.tif"*1000/("ALOSFac.tif"*12.5*12.5/1000000)`

Una vez obtenido elmapa, modifique la simbología de representación a _Classify_ utilizando la paleta de color _Spectrum by Wavelength - Fullbright_ y _Method: Quantile_ en 12 clases

Matriz de isorendimiento Budyko Compuesto
![R.LTWB](Screenshot/ArcGISPro3.0.3LTWBBudykoComposite.png)

Como observa en la ilustración, se han obtenido valores de hasta 109.113 lps/km² y los rendimientos cercanos a este valor se encuentran localizados en la zona norte sobre la Sierra Nevada de Santa Marta y al sur-este en la zona de la cordillera oriental.

4. Abra la tabla de atributos de la clase de entidad _ALOSStrNodeGDB_ contenida en la Geodatabase del proyecto, creado en ArcGIS Pro para la sección 5, podrá observar que contiene el número de celdas acumuladas, los valores de área de aportación calculados a partir de la resolución de la grilla y los valores leídos de las diferentes grillas de caudal.

![R.LTWB](Screenshot/ArcGISPro3.0.3ALOSStrNodeGDB.png)

5. En la tabla de atributos de la clase de entidad _ALOSStrNodeGDB_, cree un campo de atributos numérico doble con el nombre `FlowPerfBudykoComposite`

![R.LTWB](Screenshot/ArcGISPro3.0.3ALOSStrNodeGDBAddField.png)

6. Utilizando el calculador de campo, calcule en el campo `FlowPerfBudykoComposite`, el isorendimiento medio de cada nodo característicos de la red de drenaje, utilice la expresión `(!LTWBBudykoComposite!*1000)/!Akm2!`

![R.LTWB](Screenshot/ArcGISPro3.0.3ALOSStrNodeGDBFieldCalculator.png)

7. A partir de los valores obtenidos en el campo `FlowPerfBudykoComposite`, cree un histograma con 12 bandas y analice los resultados obtenidos. Podrá observar que de 31879 nodos, 9697 presentan valores cercanos a la media en la banda comprendida entre 2.2 y 29 lps/km².

![R.LTWB](Screenshot/ArcGISPro3.0.3ALOSStrNodeGDBHistogram.png)

8. Utilizando los valores contenidos en la tabla, cree un gráfico de dispersión relacionando el área de aportación `Akm2` con los valores de isorendimiento medio obtenidos. Obtenga los parámetros de la tendencia lineal y el valor del coeficiente de determinación R². Filtre los valores de área inferiores o iguales a 1000 km² e isorendimientos medios mayores a cero, utilice la expresión SQL `Akm2 <= 1000 And FlowPerfBudykoComposite > 0`

![R.LTWB](Screenshot/ArcGISPro3.0.3ALOSStrNodeGDBScatterPlot.png)

Como puede observar en la gráfica, no existe una correlación general que permita establecer que la ecuación `y = 24.7 + 0.00085 x` con coeficiente de determinación `R² = 0.000017`, describe el cambio en el isorendimiento en función del área de aportación. Lo anterior debido a que esta relación depende de múltiples factores, tales como el régimen hidrológico de la zona y su distribución espacial, el tipo de geomorfometría de la red de drenaje, la inclinación del terreno y el tipo de regionalización empleada para la estimación de los mapas de temperatura, evapotranspiración potencial y real.

En este momento dispone para la zona de estudio, de un mapa de isorendimientos que permite entender la relación entre las acumulaciones de flujo y los valores obtenidos de caudal medio.


### Actividades complementarias:pencil2:

En la siguiente tabla se listan las actividades complementarias que deben ser desarrolladas y documentadas por el estudiante en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (mostrar nombre completo, código y enlace a su cuenta de GitHub), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.


| Actividad | Alcance                                                                                                                                                                                                                         |
|:---------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1     | Utilizando los valores obtenidos de caudal medio por fenómeno climatológico a partir de la ecuación de Budyko, cree mapas de isorendimientos y analice las diferencias obtenidas respecto al mapa de isorendimientos compuesto. |
|     2     | Investigue y documente la utilidad y aplicabilidad de los mapas de isorendimientos medios.                                                                                                                                      |


### Referencias

* https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/raster-calculator.htm


### Compatibilidad

* Esta actividad puede ser desarrollada con cualquier software SIG que disponga de herramientas de algebra de mapas.


### Control de versiones

| Versión    | Descripción                                                                                                                                                                                                     | Autor                                     | Horas |
|------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|:-----:|
| 2022.12.19 | Documentación. Generación mapa isorendimiento. Cálculo isorendimientos en puntos característicos. Histograma. Matriz de dispersión, ecuación de tendencia lineal.  Ilustración cabecera y diagrama de procesos. | [rcfdtools](https://github.com/rcfdtools) |   3   |

_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Actividad anterior](../FlowPoint) | [Inicio](../../Readme.md) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/35) | [Actividad siguiente](../../xxx) |
|------------------------------------|---------------------------|------------------------------------------------------------------------|----------------------------------|

