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

Nombre los archivos de estadísticas zonales de acuerdo a las indicaciones de las siguientes tablas y almacene dentro de la Geodatabase del proyecto _ArcGISProSection05.aprx_ en `D:\R.LTWB\\.map`. Registre los valores medios obtenidos.

<div align="center">

**Zona de estudio - ZE**
| Fenómeno / Zona                                  | Tabla zonal           | General, mm/año |
|--------------------------------------------------|-----------------------|:----------------:|
| **Precipitación zona de estudio**                |                       |                  |
| Compuesto / Zona estudio - ZE                    | RainTotalCompositeZE  |     1545.077     |
| Niña / Zona estudio - ZE                         | RainTotalNinaZE       |     1760.878     |
| Niño / Zona estudio - ZE                         | RainTotalNinoZE       |     1280.771     |
| neutro / Zona estudio - ZE                       | RainTotalNeutralZE    |     1550.741     |
| **Evapotranspiración real zona de estudio**      |                       |                  |
| **Budyko**                                       |                       |                  |
| Compuesto / Zona estudio - ZE                    | ETRBudykoCompositeZE  |     1053.944     |
| Niña / Zona estudio - ZE                         | ETRBudykoNinaZE       |     1118.535     |
| Niño / Zona estudio - ZE                         | ETRBudykoNinoZE       |     956.504      |
| neutro / Zona estudio - ZE                       | ETRBudykoNeutralZE    |     1054.165     |
| **Dekop**                                        |                       |                  |
| Compuesto / Zona estudio - ZE                    | ETRDekopCompositeZE   |     1152.198     |
| Niña / Zona estudio - ZE                         | ETRDekopNinaZE        |     1231.288     |
| Niño / Zona estudio - ZE                         | ETRDekopNinoZE        |     1032.202     |
| neutro / Zona estudio - ZE                       | ETRDekopNeutralZE     |     1152.373     |
| **Turc**                                         |                       |                  |
| Compuesto / Zona estudio - ZE                    | ETRTurcCompositeZE    |     1197.412     |
| Niña / Zona estudio - ZE                         | ETRTurcNinaZE         |     1276.271     |
| Niño / Zona estudio - ZE                         | ETRTurcNinoZE         |     1072.555     |
| neutro / Zona estudio - ZE                       | ETRTurcNeutralZE      |     1192.169     |

</div>

Ejemplo para evapotranspiración real por subzona hidrográfica 
![R.LTWB](Screenshot/ArcGISPro3.0.3ZonalStatisticsAsTableSZH.png)

<div align="center">

**Subzona hidrográfica - SZH**
| Fenómeno / Zona                                  | Tabla zonal           | SZH 2801, mm/año | SZH 2802, mm/año | SZH 2804, mm/año | SZH 2805, mm/año |
|--------------------------------------------------|-----------------------|:----------------:|:----------------:|:----------------:|:----------------:|
| **Precipitación subzona hidrográfica**           |                       |                  |                  |                  |                  |
| Compuesto / Subzona hidrográfica - SZH           | RainTotalCompositeSZH | 1465.465         | 1453.047         | 1405.987         | 1847.385         |
| Niña / Subzona hidrográfica - SZH                | RainTotalNinaSZH      | 1634.776         | 1656.346         | 1583.920         | 2142.350         |
| Niño / Subzona hidrográfica - SZH                | RainTotalNinoSZH      | 1226.379         | 1216.649         | 1224.506         | 1453.897         |
| neutro / Subzona hidrográfica - SZH              | RainTotalNeutralSZH   | 1489.294         | 1450.687         | 1388.385         | 1874.819         |
| **Evapotranspiración real subzona hidrográfica** |                       |                  |                  |                  |                  |
| **Budyko**                                       |                       |                  |                  |                  |                  |
| Compuesto / Subzona hidrográfica - SZH           | ETRBudykoCompositeSZH | 927.518          | 1018.556         | 1035.483         | 1194.497         |
| Niña / Subzona hidrográfica - SZH                | ETRBudykoNinaSZH      | 975.774          | 1083.929         | 1101.484         | 1266.270         |
| Niño / Subzona hidrográfica - SZH                | ETRBudykoNinoSZH      | 846.433          | 925.474          | 956.467          | 1064.636         |
| neutro / Subzona hidrográfica - SZH              | ETRBudykoNeutralSZH   | 933.802          | 1017.041         | 1027.893         | 1200.701         |
| **Dekop**                                        |                       |                  |                  |                  |                  |
| Compuesto / Subzona hidrográfica - SZH           | ETRDekopCompositeSZH  | 1009.092         | 1111.204         | 1123.905         | 1319.326         |
| Niña / Subzona hidrográfica - SZH                | ETRDekopNinaSZH       |  1066.989        | 1191.660         | 1205.908         | 1406.253         |
| Niño / Subzona hidrográfica - SZH                | ETRDekopNinoSZH       | 911.979          | 996.538          | 1026.379         | 1158.047         |
| neutro / Subzona hidrográfica - SZH              | ETRDekopNeutralSZH    | 1016.598         | 1109.342         | 1114.481         | 1326.785         |
| **Turc**                                         |                       |                  |                  |                  |                  |
| Compuesto / Subzona hidrográfica - SZH           | ETRTurcCompositeSZH   | 988.219          | 1142.803         | 1181.816         | 1410.862         |
| Niña / Subzona hidrográfica - SZH                | ETRTurcNinaSZH        | 1035.541         | 1219.644         | 1264.568         | 1507.486         |
| Niño / Subzona hidrográfica - SZH                | ETRTurcNinoSZH        | 896.375          | 1027.607         | 1080.938         | 1231.332         |
| neutro / Subzona hidrográfica - SZH              | ETRTurcNeutralSZH     | 988.173          | 1135.232         | 1167.591         | 1414.003         |



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

