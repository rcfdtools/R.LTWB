##  Acumulación de Flujo - FAC
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
* [Grillas de direcciones de Flujo – Flow Direction – FDR. ](https://github.com/rcfdtools/R.LTWB/tree/main/HECGeoHMS/Layers)[(Aprender.)](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/FdrDEM)


### Procedimiento general

<div align="center">
<br><img alt="R.LTWB" src="https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FacDEM/Graph/FacDEMFlowchart.png" width="65%"><br>
<sub>Convenciones del diagrama: Clases de entidad y grillas en gris, Geo-procesos en verde y Procesos manuales en amarillo.<br>Líneas con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>

La acumulación de flujo o de celdas  puede ser realizada con Spatial Analyst Tools de ArcGIS for Desktop, HEC-GeoHMS sobre ArcGIS 10.2.2 a través de Arc Hydro Tools, Spatial Analyst de ArcGIS Pro, Arc Hydro Tools sobre ArcGIS Pro, QGIS, HEC-HMS a través del menú GIS y otras herramientas y librerías.

#### Acumulación de flujo con HEC-GeoHMS sobre ArcGIS for Desktop

1. En ArcGIS for Desktop, abra el mapa _D:\R.LTWB\HECGeoHMS\HECGeoHMS.mxd_ creado en la actividad de [reacondicionamiento de modelos digitales de elevación](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/AgreeDEM) y modificado en la clase de [direcciones de flujo](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/FdrDEM) que contiene las grillas FDR. En caso de que este generando un mapa nuevo, cargue directamente las grillas FDR contenidas en el directorio  _[D:\R.LTWB\HECGeoHMS\Layers](https://github.com/rcfdtools/R.LTWB/tree/main/HECGeoHMS/Layers)_.

2. En la barra de herramientas _HEC-GeoHMS_, vaya al menú _Preprocessing_ y seleccione la opción _Flow Accumulation_ y realice el procedimiento de direcciones de flujo en formato GeoTIFF para los 3 modelos digitales de elevación con relleno de sumideros y asigne los nombres ASTERFac.tif, SRTMFac.tif y ALOSFac.tif en la ruta D:\R.LTWB\HECGeoHMS\Layers\.

Parámetros de entrada para acumulaciones de flujo ASTER
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FacDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFacDEMASTERParameters.png)

Resultados ventana de ejecución grilla ASTER (dt: 01'11")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FacDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFacDEMASTERLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FacDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFacDEMASTER.png)

Resultados ventana de ejecución grilla SRTM (dt: 01'12")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FacDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFacDEMSRTMLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FacDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFacDEMSRTM.png)

Resultados ventana de ejecución grilla ALOS (dt: 09'08")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FacDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFacDEMALOSLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FacDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFacDEMALOS.png)

> Para saber si las grillas FAC han sido creadas correctamente, en la simbología de representación verifique que el máximo número de celdas de los modelos digitales de elevación ASTER y SRTM sean similares debido a que su resolución es aproximadamente la misma y corresponde a celdas de 30 x 30 metros.  

|    Grilla    |                          Descargar :open_file_folder:                               |
|:------------:|:-----------------------------------------------------------------------------------:|
| ASTERFdr.tif | [.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ASTERFdr.rar) |
| SRTMFdr.tif  | [.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/SRTMFdr.rar)  |
| ALOSFdr.tif  | [.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ALOSFdr.rar)  |

3. Visualice la tabla de atributos de la grilla [ASTERFdr.tif](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ASTERFdr.rar) que contiene valores discretos contables de las 9 direcciones de flujo (incluida la 255 o no dirección) y cree una gráfica de barras desde el menú _View / Graphs / Create Graph_. 

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FdrDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFdrDEMASTERGraph.png)

Como puede observar en la gráfica y en la tabla de atributos, la dirección dominante en la grilla ASTER es 16 - Oeste con 7571807 celdas, similar a lo que ocurre en las grillas SRTM y ALOS en las que la dirección predominante también es 16.  

> Opcional: repita este procedimiento para los modelos digitales de elevación SRTM y ALOS.


#### Direcciones de flujo - FDR con otras herramientas

| Herramienta                                                                                                                                | Procedimiento                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ArcGIS for Desktop / Spatial Analyst Tools](https://desktop.arcgis.com/en/arcmap/latest/tools/spatial-analyst-toolbox/flow-direction.htm) | En el ArcToolBox, busque la caja de herramientas _Spatial Analyst Tools / Hydrology_ y seleccione la herramienta _Flow Direction_. Seleccione la grilla de entrada, asigne un nombre de la grilla de salida y opcionalmente ingrese el valor _Output drop raster_ correspondiente a la máxima diferencia en % de elevación entre la celda de terreno para definir la dirección de drenaje.                                                                                                  |
| [ArcGIS 10.2.2 / Arc Hydro Tools](http://downloads.esri.com/archydro/archydro/Setup/)                                                      | El procedimiento es el mismo presentado en esta actividad a través de HEC-GeoHMS debido a que esta herramienta utiliza Arc Hydro Tools.                                                                                                                                                                                                                                                                                                                                                     |
| [ArcGIS Pro / Spatial Analyst](https://pro.arcgis.com/en/pro-app/latest/help/analysis/raster-functions/flow-direction-raster-function.htm) | En el panel _Geoprocessing_, busque la caja de herramientas _Spatial Analyst Tools / Hydrology_ y seleccione la herramienta _Flow Direction_. Seleccione la grilla de entrada, asigne un nombre de la grilla de salida y opcionalmente ingrese el valor _Output drop raster_ correspondiente a la máxima diferencia en % de elevación entre la celda de terreno para definir la dirección de drenaje y seleccione el algoritmo que define el tipo de direcciones a obtener (D8, MFD, DINF). |
| [ArcGIS Pro / Arc Hydro Tools Pro](http://downloads.esri.com/archydro/archydro/setup/Pro/)                                                 | En el panel _Geoprocessing_, busque la caja de herramientas _Arc Hydro Tools Pro / Terrain Preprocessing_ y seleccione la herramienta _Flow Direction_. En esta herramienta puede delimitar la zona a ser evaluada con la selección de un polígono mediante _Input External Wall Polygon Class_.                                                                                                                                                                                            |
| [HEC-HMS](https://www.hec.usace.army.mil/confluence/hmsdocs/hmsum/4.9/geographic-information/gis-menu)                                     | En el panel lateral seleccione en _Basin Models_ el modelo de cuenca creado, luego en el menú _GIS_ seleccione la opción _Preprocessing Drainage_. Este procedimiento crea automáticamente las grillas de direcciones y acumulaciones de flujo.                                                                                                                                                                                                                                             |
| [QGIS 3](https://acolita.com/direccion-del-drenaje-en-qgis-3/)                                                                             | En el _Processing Toolbox_ busque el grupo de herramientas _SAGA / Terrain Analysis_ y ejecute _Fill Sinks (Wang & Lui)_ que además de rellenas las depresiones permite generar el mapa de direcciones de flujo.                                                                                                                                                                                                                                                                            |

Los métodos para estimar el tipo de dirección de flujo en ArcGIS Pro son:

| Método | Descripción                                                                                                                                                                                                                                                                                                                                                                             |
|--------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D8     | The D8 flow option models flow direction from each pixel to its steepest downslope neighbor. All of the flow is directed to this steepest neighbor. The output of the D8 direction type is an integer raster whose values range from 1 to 255.                                                                                                                                          |
| MFD    | The Multiple Flow Direction (MFD) algorithm, described by Qin (2007), partitions flow from a pixel to all downslope neighbors. A flow-partition exponent is created from an adaptive approach based on local terrain conditions and is used to determine the fraction of flow draining to each downslope neighbor.                                                                      |
| DINF   | The D-Infinity (DINF) flow method, described by Tarboton (1997), determines flow direction as the steepest downward slope on eight triangular facets formed in a 3x3 pixel window centered on the pixel of interest. Flow direction output is a floating point raster represented as a single angle in degrees, progressing counterclockwise from 0 (due east) to 360 (again due east). |


### Recodificación de direcciones de flujo con algebra de mapas de ArcGIS

Para recodificar el mapa FDR en formato ArcGIS a QGIS 3, primero convierta a formato rcfdtools con la siguiente expresión:

Conversión de ArcGIS a rcfdtools (dt: 00'06.33") [ASTERFdrrcfdtools.tif](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ASTERFdrrcfdtools.rar)

```
Con("ASTERFdr.tif"==1,20,Con("ASTERFdr.tif"==2,21,Con("ASTERFdr.tif"==4,22,Con("ASTERFdr.tif"==8,23,Con("ASTERFdr.tif"==16,24,Con("ASTERFdr.tif"==32,25,Con("ASTERFdr.tif"==64,26,Con("ASTERFdr.tif"==128,27,255))))))))
```

> Para otros modelos digitales de elevación, en la expresión, reemplace el nombre "ASTERFdr.tif" por el nombre de la grilla FDR requerida.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FdrDEM/Screenshot/ArcGISDesktop10.2.2ConvertFdrArcGIS2rcdftools.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FdrDEM/Screenshot/ArcGISDesktop10.2.2ConvertFdrArcGIS2rcdftoolsLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FdrDEM/Screenshot/ArcGISDesktop10.2.2ConvertFdrArcGIS2rcdftoolsMap.png)

Conversión de rcfdtools a QGIS3 (dt: 00'06.70") [ASTERFdrQGIS.tif](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ASTERFdrQGIS.rar)

```
Con("ASTERFdrrcfdtools.tif"==20,2,Con("ASTERFdrrcfdtools.tif"==21,3,Con("ASTERFdrrcfdtools.tif"==22,4,Con("ASTERFdrrcfdtools.tif"==23,5,Con("ASTERFdrrcfdtools.tif"==24,6,Con("ASTERFdrrcfdtools.tif"==25,7,Con("ASTERFdrrcfdtools.tif"==26,0,Con("ASTERFdrrcfdtools.tif"==27,1,255))))))))
```

> Para otros modelos digitales de elevación, en la expresión, reemplace el nombre "ASTERFdrrcfdtools.tif" por el nombre de la grilla FDR requerida.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FdrDEM/Screenshot/ArcGISDesktop10.2.2ConvertFdrrcdftools2QGIS3.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FdrDEM/Screenshot/ArcGISDesktop10.2.2ConvertFdrrcdftools2QGIS3Log.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FdrDEM/Screenshot/ArcGISDesktop10.2.2ConvertFdrrcdftools2QGIS3Map.png)

En este momento dispone de grillas de direcciones para acumulación de flujo sobre todo el modelo digital de elevación.


### Referencias

* https://pro.arcgis.com/en/pro-app/latest/help/analysis/raster-functions/flow-direction-raster-function.htm
* https://desktop.arcgis.com/en/arcmap/latest/tools/spatial-analyst-toolbox/flow-direction.htm
* https://acolita.com/direccion-del-drenaje-en-qgis-3/
* https://docs.qgis.org/2.6/en/docs/user_manual/processing_algs/taudem/basic_grid_analysis_tools/d8flowdirections.html
* https://desktop.arcgis.com/en/arcmap/latest/extensions/spatial-analyst/map-algebra/what-is-map-algebra.htm
* https://desktop.arcgis.com/en/arcmap/latest/tools/spatial-analyst-toolbox/conditional-evaluation-with-con.htm


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
