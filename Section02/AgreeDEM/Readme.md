## Reacondicionamiento de terreno - DEM Reconditioning – AgreeDEM
Keywords: `DEM` `AgreeDEM`

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/AgreeDEM.png)

Para garantizar que la acumulación del flujo se realice sobre las celdas del modelo de terreno y por los cauces o drenajes obtenidos o digitalizados, es necesario reacondicionar el terreno incrustando los drenajes. Este procedimiento es especialmente requerido en zonas predominantemente planas o en zonas donde no puedan ser identificadas las celdas correspondientes a los drenajes.


### Objetivos

* Crear el proyecto HEC-HMS para el procesamiento del modelo de terreno.
* Reacondicionar el modelo de terreno incrustando la red de drenaje. 


### Requerimientos

* [ArcGIS Pro 2+](https://pro.arcgis.com/en/pro-app/latest/get-started/download-arcgis-pro.htm)
* [ArcGIS for Desktop 10+](https://desktop.arcgis.com/es/desktop/) (opcional)
* [QGIS 3+](https://qgis.org/) (opcional)
* [HEC-HMS 4.9+](https://www.hec.usace.army.mil/software/hec-hms/)
* [Red de drenaje](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/GDB100k) de la [zona de estudio](https://github.com/rcfdtools/R.LTWB/tree/main/Section01/CaseStudy), [(shp)](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/DrenajeSencilloIGAC100kZEMerge.zip).


### Procedimiento general con HEC-HMS

<div align="center">
<br><img alt="R.LTWB" src="https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Graph/AgreeDEMFlowchart.png" width="80%"><br>
<sub>Convenciones del diagrama: Base de datos geográfica GDB en azul, Clases de entidad en gris, Geo-procesos en verde y Procesos manuales en amarillo.<br>Líneas con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>

1. En HEC-HMS, cree un proyecto nuevo en blanco definiendo _Metric_ en el sistema de unidades por defecto, guardar como _HECHMS_ en la carpeta _D:\R.LTWB\_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9CreateNewProject.png)

Automáticamente, obtendrá una carpeta con la estructura de directorios y archivos requeridos por este modelo que para la versión 4.9 contendrá:

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9CreateNewProjectStructure.png)

2. En el menú _Components – Create Component – Basin Model_, cree el modelo de cuencas, nombrar como _Basin 1_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9CreateBasinModel.png)

3. En la tabla de contenido localizada a la izquierda, seleccione _HECHMS – Basin Models – Basin 1_, luego en el menú _GIS – Coordinate System_ seleccione el sistema de proyección de coordenadas _MAGNA_OrigenNacional.prj_ localizado en el directorio _D:\R.LTWB\\.ProjectionFile_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9CoordinateSystem.png)

4. En el menú _Components – Create Component – Terrain Data_, cree el terreno a partir del modelo digital de elevación - DEM a partir del DEM ALOS PALSAR denominado _APFBSRT1MosaicArcGISPro.tif_ localizado en la carpeta _D:\R.LTWB\.dem\ALOS_ seleccionando unidades verticales en metros, nombrar como Terrain 1.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9TerrainData1.png)

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9TerrainData2.png)

Automáticamente el archivo _APFBSRT1MosaicArcGISPro.tif_ sera copiado con el nombre _Terrain_1.elevation.tif_ en la carpeta _D:\R.LTWB\HECHMS\terrain_

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9TerrainData3.png)

> Para reducir la extensión del DEM, este puede ser recortado utilizando la herramienta _Clip_ de ArcGIS hasta el límite de la envolvente de la zona de estudio denominada '\\.shp\ZonaEstudioEnvelope.shp' 

5. En la tabla de contenido, seleccione _HECHMS – Basin Models – Basin 1_ y en la parte inferior asocie el terreno creado al modelo de cuencas. 

> Este proceso puede tardar algunos segundos debido a la extensión del DEM y a su resolución.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9TerrainData4.png)

6. En el menú _GIS_, seleccione la opción _Terrain Reconditioning_. El primer paso (Step 1) permite crear paredes perimetrales de confinamiento utilizando el borde de una cuenca previamente digitalizada, dar clic en _Next >_. 

> Para el caso de estudio no ejecutaremos la generación de paredes perimetrales a partir de la zona de estudio correspondiente a la zona hidrográfica 28 - Cesar, debido a que realizaremos el cálculo de los caudales medios de largo plazo sobre todo el modelo. 

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9TerrainReconditioningStep1.png)

El segundo paso (Step 2) permite modificar el terreno incrustando los drenajes, para ello seleccione la red de drenaje en formato Shapefile denominada _DrenajeSencilloIGAC100kZEMerge.shp_ localizada en _D:\R.LTWB\\.shp_, defina el número de celdas aferentes o _Smooth drop cell buffer_ (p.ej, 5), la profundidad de suavizado lateral o _Smooth drop height_ (p.ej, 10) y la profundidad de incrustación en el cauce o _Sharp drop height_ (p.ej, 1000 para garantizar que en el relleno de sumideros se mantenga la localización de las celdas correspondientes a los drenajes marcados), de clic en _Next >_. El modelo de terreno será almacenado en el directorio …\HECHMS_v0\gis\Basin_1

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9TerrainReconditioningStep2.png)

Espere hasta que el proceso se complete.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9TerrainReconditioningStep2a.png)

> Al igual que en la asociación y visualización en pantalla, este proceso puede tardar algunos minutos debido a la extensión del DEM y a su resolución.

A través del monitor de procesos _Processes_ del administrador de tareas o _Task Maneger_ de su sistema operativo, verifique que se esté ejecutando el proceso _OpenJDK Platform binary_ de HEC-HMS. Este proceso requiere de mínimo 8GB de memoria RAM para modelos de terrenos como el utilizado en el caso de estudio.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9TerrainReconditioningStep2b.png)

7. En ArcGIS Pro, ArcGIS for Desktop o QGIS, cargue y visualice la grilla reacondicionada, cree perfiles de visualización alrededor de algunos drenajes para comprender el proceso de incrustación de la red de drenaje en DEM.


Realice este mismo procedimiento para los modelos digitales de elevación ASTER GDEM y SRTM. 

En este momento ya dispone de la grilla de terreno reacondicionada requerida para el relleno de sumideros.


### Referencias

* https://www.hec.usace.army.mil/confluence/hmsdocs/hmsum/4.9/geographic-information/gis-menu


### Compatibilidad

* Esta actividad puede ser desarrollada en versiones standalone de HEC-HMS 4.9 o superior o en HEC-GeoHMS sobre ArcGIS 10.2.2. Se recomienda su creación utilizando la versión standalone.


### Control de versiones

| Versión    | Descripción     | Autor                                      | Horas |
|------------|:----------------|--------------------------------------------|:-----:|
| 2022.07.20 | Versión inicial | [rcfdtools](https://github.com/rcfdtools)  |   2   |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Actividad anterior](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/GDB100k) | [Inicio](https://github.com/rcfdtools/R.LTWB/wiki) | [Actividad siguiente]() |
|---------------------------------------------------------------------------------------|----------------------------------------------------|-------------------------|

[^1]: 