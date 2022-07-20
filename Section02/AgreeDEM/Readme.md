## Reacondicionamiento de terreno - DEM Reconditioning – AgreeDEM
Keywords: `DEM` `AgreeDEM` `Buffer` `Feature Envelope To Polygon` `Raster Clip`

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/AgreeDEM.png)

Para garantizar que la acumulación del flujo se realice sobre las celdas del modelo de terreno y por los cauces o drenajes obtenidos o digitalizados, es necesario reacondicionar el terreno incrustando los drenajes. Este procedimiento es especialmente requerido en zonas predominantemente planas o en zonas donde no puedan ser identificadas las celdas correspondientes a los drenajes.


### Objetivos

* Crear un polígono aferente a la envolvente de la zona de estudio.
* Recortar los modelos digitales de elevación DEM apartir del polígono buffer de la zona de estudio.
* Crear el proyecto HEC-HMS para el procesamiento del modelo de terreno.
* Reacondicionar el modelo de terreno incrustando la red de drenaje. 


### Requerimientos

* [ArcGIS Pro 2+](https://pro.arcgis.com/en/pro-app/latest/get-started/download-arcgis-pro.htm)
* [ArcGIS for Desktop 10+](https://desktop.arcgis.com/es/desktop/) (opcional)
* [QGIS 3+](https://qgis.org/) (opcional)
* [HEC-HMS 4.9+](https://www.hec.usace.army.mil/software/hec-hms/)
* Polígono envolvente que delimita la [zona de estudio](https://github.com/rcfdtools/R.LTWB/tree/main/Section01/CaseStudy), [(shp)](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudioEnvelope.shp)
* [Red de drenaje](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/GDB100k) de la zona de estudio, [(shp)](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/DrenajeSencilloIGAC100kZEMerge.zip).
* [Modelo digital de elevación ASTER GDEM 30m](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/DEMAster)
* [Modelo digital de elevación SRTM 30m](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/DEMSrtm)
* [Modelo digital de elevación ALOS PALSAR 12.5m](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/DEMAlos)


### Procedimiento general

<div align="center">
<br><img alt="R.LTWB" src="https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Graph/AgreeDEMFlowchart.png" width="80%"><br>
<sub>Convenciones del diagrama: Base de datos geográfica GDB en azul, Clases de entidad en gris, Geo-procesos en verde y Procesos manuales en amarillo.<br>Líneas con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>

#### Recorte de grillas de elevación con ArcGIS Pro

1. En ArcGIS Pro y utilizando la herramienta _Geoprocessing / Analysis Tools / Proximity / Buffer_, cree un polígono aferente al rededor del polígono envolvente de la zona de estudio. Como criterio de aferencia, aplicar 2 veces el mayor tamaño de pixel o celda de los DEM, para el caso de estudio utilizaremos una distancia de 30m x 2 = 60m debido a que los modelos ASTER GDEM y SRTM han sido descargados en resoluciones de 30m. Nombre el polígono resultante en la carpeta _.shp_ como _ZonaEstudioBufferDEM.shp_. Como puede observar, el buffer es creado con esquinas redondeadas debido a que la aferencia se mantiene en todas las aristas.

> La aferencia garantiza que el posterior recorte de los DEM incluya todas las celdas perimetrales dentro de la zona de estudio.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISPro3.0.0ZonaEstudioBufferDEM.png)

Utilizando la herramienta _Geoprocessing / Data Management Tools / Features / Feature Envelope To Polygon_, obtenga el polígono regular sin esquinas redondeadas que será utilizado para recortar los modelos digitales de elevación. Nombre el polígono resultante en la carpeta _.shp_ como _ZonaEstudioEnvelopeBufferDEM.shp_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISPro3.0.0ZonaEstudioEnvelopeBufferDEM.png)

2. Utilizando la herramienta _Geoprocessing / Raster / Raster Processing / Clip Raster_, recorte las grillas de terreno hasta el buffer del polígono envolvente de la zona de estudio _ZonaEstudioEnvelopeBufferDEM.shp_ asignando los nombres indicados en la siguiente tabla:

| MDE         | Grilla mosaico descargada     | Grilla mosaico recortada        | Carpeta              |
|-------------|-------------------------------|---------------------------------|----------------------|
| ASTER GDEM  | ASTGTMV003MosaicArcGISPro.tif | ASTGTMV003MosaicArcGISProZE.tif | D:\R.LTWB\.dem\ASTER | 
| SRTM        | SRTMV003MosaicArcGISPro.tif   | SRTMV003MosaicArcGISProZE.tif   | D:\R.LTWB\.dem\SRTM  |
| ALOS PALSAR | APFBSRT1MosaicArcGISPro.tif   | APFBSRT1MosaicArcGISProZE.tif   | D:\R.LTWB\.dem\ALOS  |

ASTER GDEM de la zona de estudio (59 MB aprox.)

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISPro3.0.0ASTGTMV003MosaicArcGISProZE.png)

SRTM de la zona de estudio (58 MB aprox.)

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISPro3.0.SRTMV003MosaicArcGISProZE.png)

ALOS PALSAR de la zona de estudio (288 MB aprox.)

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISPro3.0.APFBSRT1MosaicArcGISProZE.png)


#### Reacondicionamiento de grillas de elevación con HEC-HMS

> Antes de iniciar este procedimiento, se recomienda cerrar las herramientas GIS y demás aplicaciones que consuman masivamente recursos de su sistema operativo y equipo.

1. En HEC-HMS, cree un proyecto nuevo en blanco definiendo _Metric_ en el sistema de unidades por defecto, guardar como _HECHMS_ en la carpeta _D:\R.LTWB\_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9CreateNewProject.png)

Automáticamente, obtendrá una carpeta con la estructura de directorios y archivos requeridos por este modelo que para la versión 4.9 contendrá:

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9CreateNewProjectStructure.png)

2. En el menú _Components – Create Component – Basin Model_, cree 3 modelos de cuencas y nombrelos como como _BasinASTER_, _BasinSRTM_, y _BasinALOS_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9CreateBasinModel.png)

3. En la tabla de contenido localizada a la izquierda, seleccione _HECHMS – Basin Models – BasinASTER_, luego en el menú _GIS – Coordinate System_ seleccione el sistema de proyección de coordenadas _MAGNA_OrigenNacional.prj_ localizado en el directorio _D:\R.LTWB\\.ProjectionFile_. Repita este procedimiento para los demás modelos de cuenca.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9CoordinateSystem.png)

4. En el menú _Components – Create Component – Terrain Data_, cree los terrenos a partir de los modelos digitales de elevación - DEM recortados anteriormente hasta el límite de la zona de estudio localizados en las carpetas _D:\R.LTWB\\.dem\ASTER_, _D:\R.LTWB\\.dem\SRTM_ y _D:\R.LTWB\\.dem\ALOS_, seleccionando unidades verticales en metros, nombrar como _TerrainASTER_, _TerrainSRTM_ y _TerrainALOS_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9TerrainData1.png)

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9TerrainData2.png)

Automáticamente los archivos _ASTGTMV003MosaicArcGISProZE.tif_, _SRTMV003MosaicArcGISProZE.tif_ y _APFBSRT1MosaicArcGISProZE.tif_ serán copiados con los nombres _TerrainASTER.elevation.tif_, _TerrainSRTM.elevation.tif_ y _TerrainALOS.elevation.tif_ en la carpeta _D:\R.LTWB\HECHMS\terrain_ y también en la carpeta _D:\R.LTWB\HECHMS\gis_ dentro de subcarpetas independientes.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9TerrainData3.png)

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9TerrainData3a.png)

5. En la tabla de contenido, seleccione _HECHMS – Basin Models – BasinASTER_ y en la parte inferior asocie el terreno creado al modelo de cuencas. Repita este procedimiento para los modelos de elevación SRTM y ALOS.

> Este proceso puede tardar algunos segundos debido a la extensión del DEM y a su resolución.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9TerrainData4.png)

6. En la tabla de contenido, seleccione _HECHMS – Basin Models – BasinASTER_ y en el menú _GIS_, seleccione la opción _Terrain Reconditioning_. El primer paso (Step 1) permite crear paredes perimetrales de confinamiento utilizando el borde de una cuenca previamente digitalizada, dar clic en _Next >_. 

> Para el caso de estudio no ejecutaremos la generación de paredes perimetrales a partir de la zona de estudio correspondiente a la zona hidrográfica 28 - Cesar, debido a que realizaremos el cálculo de los caudales medios de largo plazo sobre todo el modelo digital de elevación. 

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9TerrainReconditioningStep1.png)

El segundo paso (Step 2) permite modificar el terreno incrustando los drenajes, para ello seleccione la red de drenaje en formato Shapefile denominada _DrenajeSencilloIGAC100kZEMerge.shp_ localizada en _D:\R.LTWB\\.shp_, defina el número de celdas aferentes o _Smooth drop cell buffer_ (p. ej. 5), la profundidad de suavizado lateral o _Smooth drop height_ (p. ej. 10) y la profundidad de incrustación en el cauce o _Sharp drop height_ (p. ej. 1000 para garantizar que en el relleno de sumideros se mantenga la localización de las celdas correspondientes a los drenajes marcados), de clic en _Next >_. 

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9TerrainReconditioningStep2.png)

Espere hasta que el proceso se complete.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9TerrainReconditioningStep2a.png)

> Al igual que en la asociación y visualización en pantalla, este proceso puede tardar varios minutos debido a la extensión del DEM y a su resolución.

Repita el procedimiento anterior para los modelos de cuenca _BasinSRTM_ y _BasinALOS_. Los modelos de terreno serán almacenados en los directorios _\HECHMS\gis\BasinASTER_, _\HECHMS\gis\BasinSRTM_ y _\HECHMS\gis\BasinALOS_. 

A través del monitor de procesos o _Processes_ del administrador de tareas o _Task Manager_ de su sistema operativo, verifique que se esté ejecutando el proceso _OpenJDK Platform binary_ de HEC-HMS. Este proceso requiere de mínimo 8GB de memoria RAM para modelos de terrenos como los utilizados en el caso de estudio.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9TerrainReconditioningStep2b.png)

7. En ArcGIS Pro, ArcGIS for Desktop o QGIS, cargue y visualice la grilla reacondicionada, cree perfiles de visualización alrededor de algunos drenajes para comprender el proceso de incrustación de la red de drenaje en el DEM.


Realice este mismo procedimiento para los modelos digitales de elevación ASTER GDEM y SRTM. 

En este momento ya dispone de la grilla de terreno reacondicionada requerida para el relleno de sumideros.


### Referencias

* https://www.hec.usace.army.mil/confluence/hmsdocs/hmsum/4.9/geographic-information/gis-menu


### Compatibilidad

* Esta actividad puede ser desarrollada en versiones standalone de HEC-HMS 4.9 o superior o en HEC-GeoHMS sobre ArcGIS 10.2.2. Se recomienda su creación utilizando la versión standalone debido a que contiene controles de excepción de errores y volcado en celdas nulas.


### Control de versiones

| Versión    | Descripción                                                                                                                                                                                                                                | Autor                                      | Horas |
|------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|:-----:|
| 2022.07.20 | Versión inicial con creación de polígono buffer a envolvente zona de estudio, recorte de grillas de terreno, creación de modelo HEC-HMS, creación de modelos de cuencas, asociación de modelos de terreno, reacondicionamiento ASTER GDEM. | [rcfdtools](https://github.com/rcfdtools)  |  6.5  |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Actividad anterior](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/GDB100k) | [Inicio](https://github.com/rcfdtools/R.LTWB/wiki) | [Actividad siguiente]() |
|---------------------------------------------------------------------------------------|----------------------------------------------------|-------------------------|
 