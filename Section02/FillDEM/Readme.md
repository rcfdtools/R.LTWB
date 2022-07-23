##  Relleno de sumideros o depresiones de modelos digitales de elevación – Fill Sinks – FIL
Keywords: `Fill DEM`

![GDB25k.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FillDEM/Screenshot/FillDEM.png)

Cuando una celda se encuentra rodeada por celdas de mayor elevación la escorrentía es retenida y no fluye. El relleno de sumideros eleva estas celdas utilizando como referencia los valores en altura de las celdas circundantes, garantizando que las celdas de la superficie del terreno drenen hacia una localización más baja.

Los modelos digitales de elevación obtenidos a partir de información satelital contienen información relacionada a la superficie terrestre (Digital Surface model – DSM, cubiertas de construcciones, línea superior del canopy en vegetación) y no a las elevaciones más bajas en el terreno. Es por ello por lo que al ejecutar el procedimiento de relleno de sumideros se pueden identificar múltiples localizaciones y áreas que pueden producir encharcamiento interrumpiendo el drenaje continuo a largo plazo.


### Objetivos

* Rellenar los sumideros del modelo digital de elevación reacondicionado para garantizar que la escorrentía de todo el modelo hidrológico fluya hacia los puntos de control más aguas abajo.
* Identificar y cuantificar sumideros a través de la diferencia de elevaciones del DEM original y DEM rellenado.
* Utilizar diferentes herramientas de relleno de sumideros.
* Visualizar y comparar perfiles de modelos digitales de elevación con y sin relleno de sumideros.


### Requerimientos

* [ArcGIS Pro 2+](https://pro.arcgis.com/en/pro-app/latest/get-started/download-arcgis-pro.htm)
* [ArcGIS for Desktop 10+](https://desktop.arcgis.com/es/desktop/) (opcional)
* [QGIS 3+](https://qgis.org/) (opcional)
* DEM ASTER GDEM 30m recortado hasta el límite de la zona de estudio
* DEM SRTM 30m recortado hasta el límite de la zona de estudio
* DEM ALOS PALSAR 12.5m recortado hasta el límite de la zona de estudio
* DEM ASTER GDEM 30m reacondicionado
* DEM SRTM 30m reacondicionado
* DEM ALOS PALSAR 12.5m reacondicionado

:page_facing_up: [Aprender a recortar y reacondicionar grillas DEM](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/AgreeDEM).  
:open_file_folder: [Descargar grillas DEM recortadas](https://github.com/rcfdtools/R.LTWB/tree/main/.dem).  
:open_file_folder: [Descargar grillas DEM reacondicionadas](https://github.com/rcfdtools/R.LTWB/tree/main/HECGeoHMS/Layers).    


### Procedimiento general

<div align="center">
<br><img alt="R.LTWB" src="https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FillDEM/Graph/FillDEMFlowchart.png" width="80%"><br>
<sub>Convenciones del diagrama: Base de datos geográfica GDB en azul, Clases de entidad en gris, Geo-procesos en verde y Procesos manuales en amarillo.<br>Líneas con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>

El relleno de sumideros puede ser realizado con Spatial Analyst Tools de ArcGIS for Desktop, HEC-GeoHMS sobre ArcGIS 10.2.2 a través de Arc Hydro Tools, Spatial Analyst de ArcGIS Pro, Arc Hydro Tools sobre ArcGIS Pro, QGIS, HEC-HMS a través del menú GIS y otras herramientas y librerías.

#### Reacondicionamiento de modelos digitales de elevación DEM con HEC-GeoHMS sobre ArcGIS for Desktop

1. En ArcGIS for Desktop, abra el mapa _D:\R.LTWB\HECGeoHMS\HECGeoHMS.mxd_ creado en la actividad de [reacondicionamiento de modelos digitales de elevación](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/AgreeDEM) que contiene las grillas DEM reacondicionadas. En caso de que este generando un mapa nuevo, cargue directamente las grillas contenidas en el directorio  _D:\R.LTWB\HECGeoHMS\Layers_.

2. En la barra de herramientas _HEC-GeoHMS_, vaya al menú _Preprocessing_ y seleccione la opción _Fill Sinks_ y realice el procedimiento de relleno de sumideros en formato GeoTIFF para los 3 modelos digitales de elevación reacondicionados y asigne los nombres ASTERFil.tif, SRTMFil.tif y ALOSFil.tif en la ruta _D:\R.LTWB\HECGeoHMS\Layers\_

En esta herramienta puede establecer el límite de relleno con la opción _Fill Threshold_ y delimitar la zona a ser rellenada con la selección de un polígono mediante _Input Deranged Polygon Feature Class_.

Parámetros de entrada para relleno de sumideros para grillas reacondicionada ASTER
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FillDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFillDEMASTERParameters.png)

Resultados ventana de ejecución grillas ASTER (dt: 03'34")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FillDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFillDEMASTERLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FillDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFillDEMASTER.png)

Resultados ventana de ejecución grillas SRTM (dt: 03'33")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FillDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFillDEMSRTMLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FillDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFillDEMSRTM.png)

Resultados ventana de ejecución grillas SRTM (XX'XX")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FillDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFillDEMALOSLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FillDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFillDEMALOS.png)

| MDE reacondicionado | Cota mínima, m | Cota máxima, m | Relleno de sumideros | Cota mínima, m | Cota máxima, m | :open_file_folder: Descargar                                        |
|---------------------|----------------|----------------|----------------------|----------------|----------------|---------------------------------------------------------------------|
| ASTERAgreeDEM.tif   | -1006          | 5687           | ASTERFil.tif         | 0              | 5687           | [ASTERFil.rar]()                                                    |
| SRTMAgreeDEM.tif    | -1044          | 5696           | SRTMFil.tif          | -4             | 5696           | [SRTMFil.rar]()                                                     |
| ALOSAgreeDEM.tif    | -1046          | 5709           | ALOSFil.tif          | 0              | 5687           | [ALOSFil.part1.rar](), [ALOSFil.part2.rar](), [ALOSFil.part3.rar]() |

| Los valores de cota mínima pueden variar dependiendo de la versión de ArcGIS, la versión de HEC-GeoHMS o la herramienta utilizada para el relleno.


#### Reacondicionamiento de modelos digitales de elevación DEM con otras herramientas

| Herramienta                                                                                                                      | Procedimiento                                                                                                                                                                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ArcGIS for Desktop / Spatial Analyst Tools](https://desktop.arcgis.com/en/arcmap/latest/tools/spatial-analyst-toolbox/fill.htm) |                                                                                                                                                                                                                                                                                                                                                                   |
| ArcGIS 10.2.2 / Arc Hydro Tools                                                                                                  | El procedimiento es el mismo presentado en esta actividad a través de HEC-GeoHMS debido a que esta herramienta utiliza Arc Hydro Tools.                                                                                                                                                                                                                           |
| [ArcGIS Pro / Spatial Analyst](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/fill.htm)                 | En el panel _Geoprocessing_, busque la caja de herramientas _Spatial Analyst Tools / Hydrology_ y seleccione la herramienta _Fill_. Seleccione la grilla de entrada, asigne un nombre de la grilla de salida y opcionalmente ingrese el valor _Z limit_ correspondiente a la máxima diferencia de elevación entre la celda de terreno y la celda rellenada.       |
| ArcGIS Pro / Arc Hydro Tools Pro                                                                                                 | En el panel _Geoprocessing_, busque la caja de herramientas _Arc Hydro Tools Pro / Terrain Preprocessing_ y seleccione la herramienta _Fill Sinks_. En esta herramienta puede establecer el límite de relleno con la opción _Fill Threshold_ y delimitar la zona a ser rellenada con la selección de un polígono mediante _Input Deranged Polygon Feature Class_. |
| HEC-HMS                                                                                                                          | En el panel lateral seleccione en _Basin Models_ el modelo de cuenca creado, luego en el menú _GIS_ seleccione la opción _Preprocessing Sinks_.                                                                                                                                                                                                                   |
| QGIS                                                                                                                             | En el _Processing Toolbox_ busque el grupo de herramientas _SAGA / Terrain Analysis_ y ejecute cualquiera de los 3 métodos disponibles: _Fill Sinks (Planchon/Darboux, 2001), Fill Sinks (Wang & Lui) o Fill Sinks XXL (Wang & Lui)_                                                                                                                              |

En este momento dispone de grillas de relleno de sumideros requeridas para la marcación de direcciones de flujo.


### Referencias

* https://desktop.arcgis.com/en/arcmap/latest/tools/spatial-analyst-toolbox/fill.htm
* https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/fill.htm


### Compatibilidad

* Se recomienda desarrollar el relleno de sumideros - Fil con el mismo grupo de herramientas donde se desarrollo el reacondicionamiento, p. ej. si el AgreeDEM fué generado directamente con Arc Hydro Tools Pro de ArcGIS Pro, ejecute el relleno con las mismas herramientas _Terrain Processing_.  
 

### Control de versiones

| Versión     | Descripción                                                          | Autor                                      | Horas |
|-------------|:---------------------------------------------------------------------|--------------------------------------------|:-----:|
| 2022.07.23  | Versión inicial con relleno de sumideros para DEM ASTER, SRTM y ALOS | [rcfdtools](https://github.com/rcfdtools)  |   4   |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Actividad anterior](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/AgreeDEM) | [Inicio](https://github.com/rcfdtools/R.LTWB/wiki) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/9999) | [Actividad siguiente]()  |
|----------------------------------------------------------------------------------------|----------------------------------------------------|--------------------------------------------------------------------------|--------------------------|
