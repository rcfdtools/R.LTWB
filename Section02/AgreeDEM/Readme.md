## Reacondicionamiento de terreno - DEM Reconditioning – AgreeDEM
Keywords: `AgreeDEM` `DEM Reconditioning` `DEM burning` `Buffer` `Feature Envelope To Polygon` `Raster Clip` `HEC-HMS` `HEC-GeoHMS` `Arc Hydro Tools Pro` `Feature to Raster`

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/AgreeDEM.png)

Para garantizar que la acumulación del flujo se realice sobre las celdas del modelo de terreno y por los cauces o drenajes obtenidos o digitalizados, es necesario reacondicionar los modelos digitales de elevación DEM incrustando los drenajes. Este procedimiento es especialmente requerido en zonas predominantemente planas o en zonas donde no puedan ser identificadas las celdas correspondientes a los drenajes.


### Objetivos

* Crear un polígono aferente a la envolvente de la zona de estudio.
* Recortar los modelos digitales de elevación DEM a partir del polígono buffer de la zona de estudio.
* Crear un proyecto HEC-HMS para el procesamiento de modelos digitales de elevación DEM.
* Reacondicionar los modelos digitales de elevación DEM incrustando la red de drenaje.
* Utilizar diferentes herramientas de reacondicionamiento.
* Visualizar perfiles de terreno reacondicionados.


### Requerimientos

* [ArcGIS Pro 2+](https://pro.arcgis.com/en/pro-app/latest/get-started/download-arcgis-pro.htm)
* [ArcGIS for Desktop 10+](https://desktop.arcgis.com/es/desktop/) (opcional)
* [QGIS 3+](https://qgis.org/) (opcional)
* [HEC-HMS 4.9+](https://www.hec.usace.army.mil/software/hec-hms/)
* [HEC-GeoHMS 10.2](https://www.hec.usace.army.mil/software/hec-geohms/downloads.aspx) for ArcGIS for Desktop 10.2.2
* [Arc Hydro Tools Pro](http://downloads.esri.com/archydro/archydro/setup/Pro/)
* Polígono envolvente que delimita la [zona de estudio](https://github.com/rcfdtools/R.LTWB/tree/main/Section01/CaseStudy), [(shp)](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudioEnvelope.shp)
* [Red de drenaje](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/GDB100k) de la zona de estudio, [(shp)](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/DrenajeSencilloIGAC100kZEMerge.zip).
* [Modelo digital de elevación ASTER GDEM 30m](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/DEMAster)
* [Modelo digital de elevación SRTM 30m](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/DEMSrtm)
* [Modelo digital de elevación ALOS PALSAR 12.5m](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/DEMAlos)

:open_file_folder: [Descargar mosaicos grillas DEM](https://github.com/rcfdtools/R.LTWB/tree/main/.dem).

### Procedimiento general

<div align="center">
<br><img alt="R.LTWB" src="https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Graph/AgreeDEMFlowchart1.png" width="75%"><br>
<sub>Convenciones generales en diagramas: clases de entidad en azul, dataset en gris oscuro, grillas en color verde, geo-procesos en rojo y procesos manuales en amarillo. Líneas con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>


#### Recorte de modelos digitales de elevación DEM con ArcGIS Pro

1. Utilizando la herramienta _Geoprocessing / Analysis Tools / Proximity / Buffer_, cree un polígono aferente al rededor del polígono envolvente de la zona de estudio _ZonaEstudioEnvelope.shp_. Como criterio de aferencia, aplicar 2 veces el mayor tamaño de pixel o celda de los DEM, para el caso de estudio utilizaremos una distancia de 30m x 2 = 60m debido a que los modelos ASTER GDEM y SRTM han sido descargados en resoluciones de 30m. Nombre el polígono resultante en la carpeta _.shp_ como _ZonaEstudioBufferDEM.shp_. Como puede observar, el buffer contiene esquinas redondeadas debido a que la aferencia se mantiene en todas las aristas.

> La aferencia garantiza que el posterior recorte de los DEM incluya todas las celdas perimetrales dentro de la zona de estudio.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISPro3.0.0ZonaEstudioBufferDEM.png)

Utilizando la herramienta _Geoprocessing / Data Management Tools / Features / Feature Envelope To Polygon_, obtenga el polígono regular sin esquinas redondeadas que será utilizado para recortar los modelos digitales de elevación. Nombre el polígono resultante en la carpeta _.shp_ como _ZonaEstudioEnvelopeBufferDEM.shp_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISPro3.0.0ZonaEstudioEnvelopeBufferDEM.png)

2. Utilizando la herramienta _Geoprocessing / Raster / Raster Processing / Clip Raster_, recorte las grillas de terreno hasta el buffer del polígono envolvente de la zona de estudio _ZonaEstudioEnvelopeBufferDEM.shp_ asignando los nombres indicados en la siguiente tabla:

<div align="center">

| MDE         | Grilla mosaico                | Grilla mosaico recortada        | Carpeta              |
|:------------|:------------------------------|:--------------------------------|:---------------------|
| ASTER GDEM  | ASTGTMV003MosaicArcGISPro.tif | ASTGTMV003MosaicArcGISProZE.tif | D:\R.LTWB\.dem\ASTER | 
| SRTM        | SRTMV003MosaicArcGISPro.tif   | SRTMV003MosaicArcGISProZE.tif   | D:\R.LTWB\.dem\SRTM  |
| ALOS PALSAR | APFBSRT1MosaicArcGISPro.tif   | APFBSRT1MosaicArcGISProZE.tif   | D:\R.LTWB\.dem\ALOS  |

</div>

ASTER GDEM de la zona de estudio (59 MB aprox.)

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISPro3.0.0ASTGTMV003MosaicArcGISProZE.png)

SRTM de la zona de estudio (58 MB aprox.)

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISPro3.0.0SRTMV003MosaicArcGISProZE.png)

ALOS PALSAR de la zona de estudio (288 MB aprox.)

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISPro3.0.0APFBSRT1MosaicArcGISProZE.png)

Especificaciones de las grillas recortadas de la zona de estudio, referencia espacial MAGNA_SIRGAS_CMT12:

|                                  MDE                                   | Grilla mosaico recortada         |  Resolución, m  | Cols  | Filas  | Area, km² | Cota mín, m | Cota máx, m | Descargar :open_file_folder:                                                                                                                                                                                                                                                                                                 |
|:----------------------------------------------------------------------:|:---------------------------------|:---------------:|:-----:|:------:|:---------:|:--------------:|:--------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ASTER GDEM](https://github.com/rcfdtools/R.LTWB/tree/main/.dem/ASTER) | ASTGTMV003MosaicArcGISProZE.tif  |      30.68      | 5408  |  8221  | 41860.42  |       0        |      5687      | [.rar](ASTGTMV003MosaicArcGISProZE.rar)                                                                                                                                                                                                                                                                                      |
|    [SRTM](https://github.com/rcfdtools/R.LTWB/tree/main/.dem/SRTM)     | SRTMV003MosaicArcGISProZE.tif    |      30.68      | 5408  |  8221  | 41860.42  |      -46       |      5696      | [.rar](https://github.com/rcfdtools/R.LTWB/blob/main/.dem/SRTM/SRTMV003MosaicArcGISProZE.rar)                                                                                                                                                                                                                                |
| [ALOS PALSAR](https://github.com/rcfdtools/R.LTWB/tree/main/.dem/ALOS) | APFBSRT1MosaicArcGISProZE.tif    |      12.5       | 13274 | 20179  | 41852.51  |      -48       |      5709      | [part1.rar](https://github.com/rcfdtools/R.LTWB/blob/main/.dem/ALOS/APFBSRT1MosaicArcGISProZE.part1.rar), [part2.rar](https://github.com/rcfdtools/R.LTWB/blob/main/.dem/ALOS/APFBSRT1MosaicArcGISProZE.part2.rar), [part3.rar](https://github.com/rcfdtools/R.LTWB/blob/main/.dem/ALOS/APFBSRT1MosaicArcGISProZE.part3.rar) |

> El procedimiento anterior puede ser ejecutado en ArcGIS for Desktop utilizando las herramientas _ArcToolBox / Analysis Tools / Buffer_ y _ArcToolBox / Analysis Tools / Feature Envelope To Polygon_
> 
> También puede ser ejecutado en QGIS con las herramientas _Processing Toolbox / Vector geometry / Buffer_ y _Processing Toolbox / Vector geometry / Bounding boxes_.  


#### Reacondicionamiento de modelos digitales de elevación DEM con HEC-HMS

> Antes de iniciar este procedimiento, se recomienda cerrar las herramientas GIS y demás aplicaciones que consuman masivamente recursos de su sistema operativo y equipo.

1. En HEC-HMS, cree un proyecto nuevo en blanco definiendo _Metric_ en el sistema de unidades por defecto, guardar como _HECHMS_ en la carpeta D:\R.LTWB\.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9CreateNewProject.png)

Automáticamente, obtendrá una carpeta con la estructura de directorios y archivos requeridos por este modelo, que para la versión 4.9 contendrá:

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9CreateNewProjectStructure.png)

2. En el menú _Components – Create Component – Basin Model_, cree 3 modelos de cuencas y nómbrelos como como _BasinASTER_, _BasinSRTM_, y _BasinALOS_.

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

> Espere hasta que el proceso se complete, para la grilla de terreno _ASTGTMV003MosaicArcGISProZE.tif_ y la red _DrenajeSencilloIGAC100kZEMerge.shp_ este proceso en HEC-HMS requiere de aproximadamente 10 horas.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9TerrainReconditioningStep3.png)

> Al igual que en la asociación y visualización en pantalla, este proceso puede tardar varios minutos debido a la extensión del DEM y a su resolución.

A través del monitor de procesos o _Processes_ del administrador de tareas o _Task Manager_ de su sistema operativo, verifique que se esté ejecutando el proceso _OpenJDK Platform binary_ de HEC-HMS. Este proceso requiere de mínimo 8GB de memoria RAM para modelos de terrenos como los utilizados en el caso de estudio.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/Windows11TaskManagerProcesses.png)

Reacondicionamiento completado.
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9TerrainReconditioningStep4.png)

Grilla obtenida localizada en _D:\R.LTWB\HECHMS\gis\BasinASTER_
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9TerrainReconditioningStep5.png)

Opcional: repita el procedimiento anterior en HEC-HMS para los modelos de cuenca _BasinSRTM_ y _BasinALOS_. Los modelos de terreno serán almacenados en los directorios _\HECHMS\gis\BasinASTER_, _\HECHMS\gis\BasinSRTM_ y _\HECHMS\gis\BasinALOS_. 

> Debido a que los algoritmos y motor de cálculo del componente GIS de HEC-HMS requieren de varias horas para completar los procesos de reacondicionamiento en modelos digitales de elevación de gran tamaño, se recomienda realizar este procedimiento en _ArcGIS for Desktop_ a través de la herramienta _HEC-GeoHMS_ o desde _Arc Hydro Tools_ para ArcGIS.


#### Reacondicionamiento de modelos digitales de elevación DEM con HEC-GeoHMS sobre ArcGIS for Desktop

1. En Microsoft Windows, cree una carpeta nueva y nombre como _HECGeoHMS_ en la ruta _D:\R.LTWB_.

> Para garantizar el correcto procesamiento del modelo reacondicionado en indispensable establecer permisos de lectura y escritura sobre la carpeta _HECGeoHMS_ a su usuario local. Desde el explorador de archivos de clic derecho sobre la carpeta _HECGeoHMS_, seleccione propiedades u oprima <kbd>Alt</kbd>+<kbd>Enter</kbd>. En la ventana de propiedades, seleccione la pestaña _Security_, de clic en el botón _Edit_

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/Windows11FolderProperties.png)

En la ventana de edición de permisos, de clic en el botón _Add..._, busque su cuenta de usuario y establezca permisos completos sobre el directorio.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/Windows11FolderPropertiesSecurity.png)

2. En ArcGIS for Desktop 10.2.2, cree un mapa nuevo en blanco, guarde como _HECGeoHMS.mxd_ en la carpeta _D:\R.LTWB\HECGeoHMS_ y asigne el sistema de proyección de coordenadas _MAGNA_Colombia_CTM12_ disponible en la carpeta _D:\R.LTWB\\.ProjectionFile_ como _MAGNA_OrigenNacional.prj_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISDesktop10.2.2NewMap.png)

3. Agregue al mapa la red de drenaje _D:\R.LTWB\\.shp\DrenajeSencilloIGAC100kZEMerge.shp_, dando clic derecho en la capa exporte la red de drenaje en la carpeta _.shp_ como _DrenajeSencilloIGAC100kZEMergeNoAttrib.shp_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISDesktop10.2.2ExportData.png)

> Opcional, para simplificar el procesamiento del modelo reacondicionado puede eliminar los atributos de la capa vectorial de drenajes conservando y recalculando únicamente la longitud en el campo SHAPE_Leng.

Abra la tabla de atributos de DrenajeSencilloIGAC100kZEMergeNoAttrib.shp y dando clic derecho en la cabecera de cada campo de atributos, elimine los atributos a excepción de _SHAPE_Leng_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISDesktop10.2.2DeleteField.png)

En el campo _SHAPE_Leng_, dando clic en la cabecera y seleccionando la opción _Calculate Geometry_ recalcule la longitud geométrica en metros de cada entidad.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISDesktop10.2.2CalculateGeometry.png)

Obtenga las estadísticas de campo para los 17069 tramos de drenaje de la red utilizada en la zona de estudio. Clic derecho en la cabecera del campo _SHAPE_Leng_ y seleccione _Statistics_. Podrá observar que la red de drenaje a incrustar en el terreno tiene una longitud de 42968 km.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISDesktop10.2.2FieldStatistics.png)

4. Desde las subcarpetas contenidas en _D:\R.LTWB\\.dem_, cargue al mapa las grillas recortadas hasta el límite de la zona de estudio ASTGTMV003MosaicArcGISProZE.tif, SRTMV003MosaicArcGISProZE.tif y APFBSRT1MosaicArcGISProZE.tif. 

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISDesktop10.2.2LoadDEMGrids.png)

5. Desde el menú _Customize / Toolbars_ active la barra denominada _HEC-GeoHMS_

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSToolbar.png)

6. En la barra de herramientas _HEC-GeoHMS_ de clic en el menú _Preprocessing_ y seleccione la opción _DEM Reconditioning_. Reacondicione las grillas DEM utilizando los parámetros definidos en la siguiente ilustración y nombre cada grilla resultante como ASTERAgreeDEM.tif, SRTMAgreeDEM.tif y ALOSAgreeDEM.tif. Guarde las grillas en la carpeta _D:\R.LTWB\HECGeoHMS\Layers\_

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSDEMReconditioningParameters.png)

Resultados en ventana de ejecución para ASTERAgreeDEM.tif (dt: 01'21")

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSDEMReconditioningASTERLog1.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSDEMReconditioningASTERLog2.png)

Resultados en ventana de ejecución para SRTMAgreeDEM.tif (dt: 01'12")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSDEMReconditioningSRTMLog1.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSDEMReconditioningSRTMLog2.png)

Resultados en ventana de ejecución para ALOSAgreeDEM.tif (dt: 07'21")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSDEMReconditioningALOSLog1.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSDEMReconditioningALOSLog2.png)

<div align="center">

| MDE reacondicionado | Cota mínima, m | Cota máxima, m | Descargar :open_file_folder:                                                                                                                                                                                                                                                                                |
|---------------------|----------------|----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ASTERAgreeDEM.tif   | -1006          | 5687           | [.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ASTERAgreeDEM.rar)                                                                                                                                                                                                                    |
| SRTMAgreeDEM.tif    | -1044          | 5696           | [.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/SRTMAgreeDEM.rar)                                                                                                                                                                                                                     |
| ALOSAgreeDEM.tif    | -1046          | 5709           | [part1.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ALOSAgreeDEM.part1.rar), [part2.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ALOSAgreeDEM.part2.rar), [part3.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ALOSAgreeDEM.part3.rar)  |

</div>

> En caso de que el proceso de ejecución devuelva error de escritura en memoria y no permita generar las grillas, cree en la raíz del disco una copia de la carpeta _D:\R.LTWB\HECGeoHMS_, reinicie su equipo y ejecute el readoncicionamiento desde esta localización.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSDEMReconditioningError.png)

> Si el error persiste, cree un nuevo usuario local tipo Administrador en su sistema operativo, cierre la sesión actual e inicie sesión con el nuevo usuario, luego ejecute el reacondicionamiento de terreno. Generalmente, el error se presenta por inconsistencia en los permisos de escritura de usuario en los directorios de la unidad local y estos permisos son generados nuevamente cuando se crea un nuevo usuario Administrador.  

7. En ArcGIS for Desktop, cargue y visualice las grillas reacondicionadas y con la barra de herramientas 3D Analyst, cree perfiles de visualización alrededor de algunos drenajes para comprender el proceso de incrustación de la red de drenaje en los DEM.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISDesktop10.2.2DEMReconditioning3DAnalystProfile.png)

> Para conocer como realizar la visualización de perfiles en ArcGIS Pro y QGIS, [clic aquí](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/DEMAster).


#### Reacondicionamiento de modelos digitales de elevación DEM con ArcGIS Pro

El reacondicionamiento de terreno ArcGIS Pro puede ser realizado con la herramienta _Geoprocessing / Arc Hydro Tools Pro / Terrain Processing / DEM Reconditioning_ a través del complemento _Arc Hydro Tools for Pro_ que puede ser obtenido desde http://downloads.esri.com/archydro/archydro/setup/Pro/. 

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISPro3.0.0ArcHydroToolsPro.png)

Para el reacondicionamiento, primero deberá convertir la red de drenaje en una grilla ráster con la herramienta _Geoprocessing / Conversion Tools / To Raster / Feature to Raster_ definiendo la menor resolución de las grillas de terreno que corresponde a 12.5 metros.[^1]

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISPro3.0.0FeatureToRaster.png)

Reacondicionamiento.
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISPro3.0.0DEMReconditioning.png)


#### Reacondicionamiento de modelos digitales de elevación DEM con QGIS

El reacondicionamiento de terreno con QGIS puede ser realizado con la herramienta _Processing Toolbox / GRASS / Raster / r.carve_ que convierte los vectores que conforman la red de drenaje de un archivo Shapefile a una grilla raster extrayendo para cada celda o pixel el valor de la elevación del DEM y luego a partir de la definición del ancho de los drenajes y la definición de la profundidad adicional por debajo del terreno, se obtiene la grilla ajustada.[^2]

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/QGIS3.26.0DEMBurning.png)

En este momento dispone de grillas de terreno reacondicionadas para relleno de sumideros.


### Referencias

* https://www.hec.usace.army.mil/confluence/hmsdocs/hmsum/4.9/geographic-information/gis-menu
* https://www.hec.usace.army.mil/software/hec-geohms/downloads.aspx


### Compatibilidad

* Esta actividad puede ser desarrollada en versiones standalone de HEC-HMS 4.9 o superior, en HEC-GeoHMS sobre ArcGIS 10.2.2 y en QGIS. 


### Control de versiones

| Versión     | Descripción                                                                                                                                                                                                                                | Autor                                      | Horas |
|-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|:-----:|
| 2022.07.21  | Reacondicionamiento de grillas ASTER, SRTM y ALOS con HEC-GeoHMS. Visualización de perfiles con 3D Analyst sobre ArcGIS for Desktop. Documentación general de la actividad.                                                                | [rcfdtools](https://github.com/rcfdtools)  | 5.5  |
| 2022.07.20  | Versión inicial con creación de polígono buffer a envolvente zona de estudio, recorte de grillas de terreno, creación de modelo HEC-HMS, creación de modelos de cuencas, asociación de modelos de terreno, reacondicionamiento ASTER GDEM. | [rcfdtools](https://github.com/rcfdtools)  |  6.5  |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Anterior](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/GDB100k) | [:house: Inicio](https://github.com/rcfdtools/R.LTWB/wiki) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/8) | [Siguiente](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/FillDEM) |
|-----------------------------------------------------------------------------|------------------------------------------------------------|-----------------------------------------------------------------------|------------------------------------------------------------------------------|
 
[^1]: Burning stream network into DEM layer in QGIS https://www.youtube.com/watch?v=ZyM1jnxFamU
[^2]: Arc Hydro Tools for ArcGIS Pro http://downloads.esri.com/archydro/archydro/setup/Pro/