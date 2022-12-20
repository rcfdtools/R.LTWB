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

Ejemplo para precipitación total compuesta en zona de estudio 
![R.LTWB](Screenshot/ArcGISPro3.0.3ZonalStatisticsAsTableZE.png)

Ejemplo para evapotranspiración real en subzona hidrográfica 
![R.LTWB](Screenshot/ArcGISPro3.0.3ZonalStatisticsAsTableSZH.png)

Nombre los archivos de estadísticas zonales de acuerdo a las indicaciones de la siguiente tabla y almacene dentro de la Geodatabase del proyecto _ArcGISProSection05.aprx_ en `D:\R.LTWB\\.map`. Registre los valores medios obtenidos.

| Fenómeno / Zona                              | Tabla zonal           | Promedio general, mm/año | SZH 2801, mm/año | SZH 2802, mm/año | SZH 2804, mm/año | SZH 2805, mm/año |
|----------------------------------------------|-----------------------|--------------------------|------------------|------------------|------------------|------------------|
| **Precipitación zona de estudio**            |                       |                          |                  |                  |                  |                  |
| Compuesto / Zona estudio - ZE                | RainTotalCompositeZE  | 1545.077                 |                  |                  |                  |                  |
| Niña / Zona estudio - ZE                     | RainTotalNinaZE       | 1760.878                 |                  |                  |                  |                  |
| Niño / Zona estudio - ZE                     | RainTotalNinoZE       | 1280.771                 |                  |                  |                  |                  |
| neutro / Zona estudio - ZE                   | RainTotalNeutralZE    | 1550.741                 |                  |                  |                  |                  |
| **Precipitación subzona hidrográfica**       |                       |                          |                  |                  |                  |                  |
| Compuesto / Subzona hidrográfica - SZH       | RainTotalCompositeSZH |                          |                  |                  |                  |                  |
| Niña / Subzona hidrográfica - SZH            | RainTotalNinaSZH      |                          |                  |                  |                  |                  |
| Niño / Subzona hidrográfica - SZH            | RainTotalNinoSZH      |                          |                  |                  |                  |                  |
| neutro / Subzona hidrográfica - SZH          | RainTotalNeutralSZH   |                          |                  |                  |                  |                  |
| **Evapotranspiración zona de estudio**       |                       |                          |                  |                  |                  |                  |
| **Budyko**                                   |                       |                          |                  |                  |                  |                  |
| Compuesto / Zona estudio - ZE                | ETRBudykoCompositeZE  |                          |                  |                  |                  |                  |
| Niña / Zona estudio - ZE                     | ETRBudykoNinaZE       |                          |                  |                  |                  |                  |
| Niño / Zona estudio - ZE                     | ETRBudykoNinoZE       |                          |                  |                  |                  |                  |
| neutro / Zona estudio - ZE                   | ETRBudykoNeutralZE    |                          |                  |                  |                  |                  |
| **Dekop**                                    |                       |                          |                  |                  |                  |                  |
| Compuesto / Zona estudio - ZE                | ETRDekopCompositeZE   |                          |                  |                  |                  |                  |
| Niña / Zona estudio - ZE                     | ETRDekopNinaZE        |                          |                  |                  |                  |                  |
| Niño / Zona estudio - ZE                     | ETRDekopNinoZE        |                          |                  |                  |                  |                  |
| neutro / Zona estudio - ZE                   | ETRDekopNeutralZE     |                          |                  |                  |                  |                  |
| **Turc**                                     |                       |                          |                  |                  |                  |                  |
| Compuesto / Zona estudio - ZE                | ETRTurcCompositeZE    |                          |                  |                  |                  |                  |
| Niña / Zona estudio - ZE                     | ETRTurcNinaZE         |                          |                  |                  |                  |                  |
| Niño / Zona estudio - ZE                     | ETRTurcNinoZE         |                          |                  |                  |                  |                  |
| neutro / Zona estudio - ZE                   | ETRTurcNeutralZE      |                          |                  |                  |                  |                  |
| **Evapotranspiración  subzona hidrográfica** |                       |                          |                  |                  |                  |                  |
| **Budyko**                                   |                       |                          |                  |                  |                  |                  |
| Compuesto / Subzona hidrográfica - SZH       | ETRBudykoCompositeSZH |                          |                  |                  |                  |                  |
| Niña / Subzona hidrográfica - SZH            | ETRBudykoNinaSZH      |                          |                  |                  |                  |                  |
| Niño / Subzona hidrográfica - SZH            | ETRBudykoNinoSZH      |                          |                  |                  |                  |                  |
| neutro / Subzona hidrográfica - SZH          | ETRBudykoNeutralSZH   |                          |                  |                  |                  |                  |
| **Dekop**                                    |                       |                          |                  |                  |                  |                  |
| Compuesto / Subzona hidrográfica - SZH       | ETRDekopCompositeSZH  |                          |                  |                  |                  |                  |
| Niña / Subzona hidrográfica - SZH            | ETRDekopNinaSZH       |                          |                  |                  |                  |                  |
| Niño / Subzona hidrográfica - SZH            | ETRDekopNinoSZH       |                          |                  |                  |                  |                  |
| neutro / Subzona hidrográfica - SZH          | ETRDekopNeutralSZH    |                          |                  |                  |                  |                  |
| **Turc**                                     |                       |                          |                  |                  |                  |                  |
| Compuesto / Subzona hidrográfica - SZH       | ETRTurcCompositeSZH   |                          |                  |                  |                  |                  |
| Niña / Subzona hidrográfica - SZH            | ETRTurcNinaSZH        |                          |                  |                  |                  |                  |
| Niño / Subzona hidrográfica - SZH            | ETRTurcNinoSZH        |                          |                  |                  |                  |                  |
| neutro / Subzona hidrográfica - SZH          | ETRTurcNeutralSZH     |                          |                  |                  |                  |                  |





En este momento dispone para la zona de estudio, de un mapa de isorendimientos que permite entender la relación entre las acumulaciones de flujo y los valores obtenidos de caudal medio.


### Actividades complementarias:pencil2:

En la siguiente tabla se listan las actividades complementarias que deben ser desarrolladas y documentadas por el estudiante en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (mostrar nombre completo, código y enlace a su cuenta de GitHub), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.


| Actividad | Alcance |
|:---------:|:--------|
|     1     | xxx     |
|     2     | xxx     |


### Referencias

* 


### Compatibilidad

* Esta actividad puede ser desarrollada con cualquier software SIG que disponga de herramientas de estadística zonal.


### Control de versiones

| Versión    | Descripción | Autor                                     | Horas |
|------------|:------------|-------------------------------------------|:-----:|
| 2022.12.20 | xxx         | [rcfdtools](https://github.com/rcfdtools) |   x   |

_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Actividad anterior](../FlowPerformance) | [Inicio](../../Readme.md) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/9999) | [Actividad siguiente](../../xxx) |
|------------------------------------------|---------------------------|--------------------------------------------------------------------------|----------------------------------|

