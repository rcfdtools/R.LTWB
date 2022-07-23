##  Relleno de sumideros – Fill Sinks – FIL
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

1. En ArcGIS for Desktop, abra el mapa _D:\R.LTWB\HECGeoHMS\HECGeoHMS.mxd_ creado en la actividad de [reacondicionamiento de modelos digitales de elevación](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/AgreeDEM), este mapa contiene las grillas DEM reacondicionadas. En caso de que este creando un mapa nuevo, cargue directamente las grillas contenidas en el directorio  _D:\R.LTWB\HECGeoHMS\Layers_. En la barra de herramientas _HEC-GeoHMS_, vaya al menú _Preprocessing_ y seleccione la opción _Fill Sinks_. 

Realice el procedimiento de relleno de sumideros en formato GeoTIFF para los 3 modelos digitales de elevación reacondicionados y asigne los siguientes nombres en la ruta _D:\R.LTWB\HECGeoHMS\Layers\_:

| MDE reacondicionado | Relleno de sumideros | 
|---------------------|----------------------|
| ASTERAgreeDEM.tif   | ASTERFil.tif        | 
| SRTMAgreeDEM.tif    | SRTMFil.tif         |
| ALOSAgreeDEM.tif    | ALOSFil.tif         |

Parámetros de entrada para relleno de sumideros para grillas reacondicionada ASTER
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFillDEMASTER.png)

Resultados ventana de ejecución grillas ASTER (03'34")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFillDEMASTER.png)



En este momento ya dispone de la grilla de relleno de sumideros requerida para la marcación de direcciones de flujo.


### Referencias

* 


### Compatibilidad

* Esta actividad puede ser desarrollada en ArcGIS for Desktop, HEC-GeoHMS sobre ArcGIS 10.2.2, Arc Hydro Tools sobre ArcGIS 10.2.2, ArcGIS Pro, Arc Hydro Tools sobre ArcGIS Pro y en QGIS.
 

### Control de versiones

| Versión    | Descripción     | Autor                                      | Horas |
|------------|:----------------|--------------------------------------------|:-----:|
| 2022.07.22 | Versión inicial | [rcfdtools](https://github.com/rcfdtools)  |   0   |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Actividad anterior](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/AgreeDEM) | [Inicio](https://github.com/rcfdtools/R.LTWB/wiki) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/9999) | [Actividad siguiente]()  |
|---------------------------------------------------------------------------------------|----------------------------------------------------|--------------------------------------------------------------------------|--------------------------|
[^1]: 