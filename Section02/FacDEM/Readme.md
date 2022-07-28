##  Acumulación de Flujo - FAC :colombia:
Keywords: `FAC DEM` `Flow accumulation` `Spatial Analyst Tools` `Arc Hydro Tools`

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FacDEM/Screenshot/FacDEM.png)

Esta grilla calcula para una celda dada, el número de celdas de drenaje aguas arriba de dicha celda. El área de drenaje aguas arriba en una celda dada puede calcularse multiplicando el valor de acumulación contenido por el área de una celda.


### Objetivos

* Crear y validar el mapa de acumulación de flujo o celdas.
* Calcular el área de aportación en diferentes localizaciones y para diferentes modelos digitales de elevación DEM.


### Requerimientos

* [ArcGIS for Desktop 10+](https://desktop.arcgis.com/es/desktop/)
* [ArcGIS Pro 2+](https://pro.arcgis.com/en/pro-app/latest/get-started/download-arcgis-pro.htm) (opcional)
* [QGIS 3+](https://qgis.org/) (opcional)
* [Grillas de direcciones de Flujo – Flow Direction – FDR. ](https://github.com/rcfdtools/R.LTWB/tree/main/HECGeoHMS/Layers)[:blue_book:Aprender.](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/FdrDEM)


### Procedimiento general

<div align="center">
<br><img alt="R.LTWB" src="https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FacDEM/Graph/FacDEMFlowchart.png" width="65%"><br>
<sub>Convenciones del diagrama: Clases de entidad y grillas en gris, Geo-procesos en verde y Procesos manuales en amarillo.<br>Líneas con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>

La acumulación de flujo o de celdas  puede ser realizada con Spatial Analyst Tools de ArcGIS for Desktop, HEC-GeoHMS sobre ArcGIS 10.2.2 a través de Arc Hydro Tools, Spatial Analyst de ArcGIS Pro, Arc Hydro Tools sobre ArcGIS Pro, QGIS, HEC-HMS a través del menú GIS y otras herramientas y librerías.

#### Acumulación de flujo con HEC-GeoHMS sobre ArcGIS for Desktop

1. En ArcGIS for Desktop, abra el mapa _D:\R.LTWB\HECGeoHMS\HECGeoHMS.mxd_ creado en la actividad de [reacondicionamiento de modelos digitales de elevación](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/AgreeDEM) y modificado en la clase de [direcciones de flujo](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/FdrDEM) que contiene las grillas FDR. En caso de que este generando un mapa nuevo, cargue directamente las grillas FDR contenidas en el directorio  _[D:\R.LTWB\HECGeoHMS\Layers](https://github.com/rcfdtools/R.LTWB/tree/main/HECGeoHMS/Layers)_.

2. En la barra de herramientas _HEC-GeoHMS_, vaya al menú _Preprocessing_ y seleccione la opción _Flow Accumulation_ y realice el procedimiento de direcciones de flujo en formato GeoTIFF para los 3 modelos digitales de elevación con relleno de sumideros y asigne los nombres ASTERFac.tif, SRTMFac.tif y ALOSFac.tif en la ruta D:\R.LTWB\HECGeoHMS\Layers\. Simbolice por visualización ajustada o _Stretched_ con una rampa de colores múltiple que contenga un color blanco o claro al inicio y el tipo _Histogram Equalize_.

Parámetros de entrada para acumulaciones de flujo ASTER
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FacDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFacDEMASTERParameters.png)

Parámetros para representación  
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FacDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFacDEMASTERSymbology.png)

Resultados ventana de ejecución grilla ASTER (dt: 05'5")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FacDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFacDEMASTERLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FacDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFacDEMASTER.png)

Resultados ventana de ejecución grilla SRTM (dt: 06'03")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FacDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFacDEMSRTMLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FacDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFacDEMSRTM.png)

Resultados ventana de ejecución grilla ALOS (dt: 09'08")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FacDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFacDEMALOSLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FacDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFacDEMALOS.png)

> Para saber si las grillas FAC han sido creadas correctamente, en la simbología de representación verifique que el máximo número de celdas acumuladas de los modelos digitales de elevación ASTER (2.73951e+007 celdas) y SRTM (xxxxxxx) sea similar debido a que su resolución es aproximadamente la misma y corresponde a celdas de 30.68464585 x  30.68464585 metros. Para los modelos ALOS, el número máximo de celdas acumuladas es mayor debido a que su resolución es de 12.5 x 12.5 metros.   

|    Grilla    |                            Descargar :open_file_folder:                             |
|:------------:|:-----------------------------------------------------------------------------------:|
| ASTERFac.tif | [.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ASTERFac.rar) |
| SRTMFac.tif  | [.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/SRTMFac.rar)  |
| ALOSFac.tif  | [.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ALOSFac.rar)  |

3. Busque e identifique la localización de la celda con el máximo número de celdas acumuladas, active la red de drenaje e identifique visualmente la cuenca hidrográfica a la cual pertenece. En la simbología de representación de la grilla _ASTERFac.tif_, simbolice en 2 rangos asignando como valor de corte el 95% del máximo valor acumulado, de esta forma podrá visualizar e identificar fácilmente varios de los pixeles o celdas que se encuentran próximos a la zona de máxima acululación.




#### Direcciones de flujo - FDR con otras herramientas

| Herramienta                                                                                                                                | Procedimiento                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ArcGIS for Desktop / Spatial Analyst Tools](https://desktop.arcgis.com/en/arcmap/latest/tools/spatial-analyst-toolbox/flow-direction.htm) | En el ArcToolBox, busque la caja de herramientas _Spatial Analyst Tools / Hydrology_ y seleccione la herramienta _Flow Direction_. Seleccione la grilla de entrada, asigne un nombre de la grilla de salida y opcionalmente ingrese el valor _Output drop raster_ correspondiente a la máxima diferencia en % de elevación entre la celda de terreno para definir la dirección de drenaje.                                                                                                  |
| [ArcGIS 10.2.2 / Arc Hydro Tools](http://downloads.esri.com/archydro/archydro/Setup/)                                                      | El procedimiento es el mismo presentado en esta actividad a través de HEC-GeoHMS debido a que esta herramienta utiliza Arc Hydro Tools.                                                                                                                                                                                                                                                                                                                                                     |
| [ArcGIS Pro / Spatial Analyst](https://pro.arcgis.com/en/pro-app/latest/help/analysis/raster-functions/flow-direction-raster-function.htm) | En el panel _Geoprocessing_, busque la caja de herramientas _Spatial Analyst Tools / Hydrology_ y seleccione la herramienta _Flow Direction_. Seleccione la grilla de entrada, asigne un nombre de la grilla de salida y opcionalmente ingrese el valor _Output drop raster_ correspondiente a la máxima diferencia en % de elevación entre la celda de terreno para definir la dirección de drenaje y seleccione el algoritmo que define el tipo de direcciones a obtener (D8, MFD, DINF). |
| [ArcGIS Pro / Arc Hydro Tools Pro](http://downloads.esri.com/archydro/archydro/setup/Pro/)                                                 | En el panel _Geoprocessing_, busque la caja de herramientas _Arc Hydro Tools Pro / Terrain Preprocessing_ y seleccione la herramienta _Flow Direction_. En esta herramienta puede delimitar la zona a ser evaluada con la selección de un polígono mediante _Input External Wall Polygon Class_.                                                                                                                                                                                            |
| [HEC-HMS](https://www.hec.usace.army.mil/confluence/hmsdocs/hmsum/4.9/geographic-information/gis-menu)                                     | En el panel lateral seleccione en _Basin Models_ el modelo de cuenca creado, luego en el menú _GIS_ seleccione la opción _Preprocessing Drainage_. Este procedimiento crea automáticamente las grillas de direcciones y acumulaciones de flujo.                                                                                                                                                                                                                                             |
| [QGIS 3](https://acolita.com/direccion-del-drenaje-en-qgis-3/)                                                                             | En el _Processing Toolbox_ busque el grupo de herramientas _SAGA / Terrain Analysis_ y ejecute _Fill Sinks (Wang & Lui)_ que además de rellenas las depresiones permite generar el mapa de direcciones de flujo.                                                                                                                                                                                                                                                                            |

En este momento dispone de grillas de acumulación de flujo para obtener las celdas de los drenajes sobre todo el modelo digital de elevación.


### Referencias

* https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/flow-accumulation.htm
* https://desktop.arcgis.com/en/arcmap/latest/tools/spatial-analyst-toolbox/flow-accumulation.htm
* https://saga-gis.sourceforge.io/saga_tool_doc/2.2.1/ta_preprocessor_4.html


### Compatibilidad

* Se recomienda desarrollar la marcación de direcciones de drenaje con el mismo grupo de herramientas donde desarrollo el reacondicionamiento, p. ej. si el AgreeDEM fué generado directamente con Arc Hydro Tools Pro de ArcGIS Pro, ejecute el relleno con las mismas herramientas _Terrain Processing_.  
 

### Control de versiones

| Versión     | Descripción                                                                                                                           | Autor                                      | Horas |
|-------------|:--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|:-----:|
| 2022.07.26  | Versión inicial con direcciones de flujo para DEM ASTER, SRTM y ALOS. Algebra de mapas para recodificación FDR. Diagrama de procesos. | [rcfdtools](https://github.com/rcfdtools)  |  6   |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Anterior](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/FillDEM) | [:house: Inicio](https://github.com/rcfdtools/R.LTWB/wiki) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/10) | [Siguiente]() |
|-----------------------------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------------------|---------------|
