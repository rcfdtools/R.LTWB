##  Direcciones de Flujo – Flow Direction – FDR
Keywords: `FDR DEM` `Flow direction` `Map Algebra` `Raster Calculator` `Spatial Analyst Tools` `Arc Hydro Tools`

![GDB25k.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FdrDEM/Screenshot/FdrDEM.png)

Esta grilla define la dirección de la máxima pendiente del terreno para cada celda utilizando el modelo de relleno de sumideros FIL. Esta capa es usada para a través del algoritmo de acumulación, crear el mapa discreto de acumulación de celdas que convergen hacia celdas más bajas y da como resultado ocho posibles direcciones en cada celda.


### Objetivos

* Crear y validar el mapa de direcciones de flujo.
* A partir de la tabla de atributos de direcciones, crear un gráfico de conteo para evaluar la dirección predominante del flujo.
* Homologar mapas de direcciones de flujo a través de la calculadora ráster.


### Requerimientos

* [ArcGIS for Desktop 10+](https://desktop.arcgis.com/es/desktop/)
* [ArcGIS Pro 2+](https://pro.arcgis.com/en/pro-app/latest/get-started/download-arcgis-pro.htm) (opcional)
* [QGIS 3+](https://qgis.org/) (opcional)
* [Grillas DEM ASTER GDEM 30m, SRTM 30m y ALOS PALSAR 12.5m reacondicionadas](https://github.com/rcfdtools/R.LTWB/tree/main/HECGeoHMS/Layers)


### Direcciones de flujo FDR en diferentes herramientas

Existen diferentes codificaciones para la marcación de direcciones de flujo que dependen principalmente de la herramienta utilizada.

<div align="center">
| Orientación | ArcGIS | HidroSIG 4.0 | MapWindow 4.5 | QGIS | HEC-HMS  | Homologador  |
|:-----------:|:------:|:------------:|:-------------:|:----:|:--------:|:------------:|
|    Este     |   1    |      6       |       1       |  2   |          |      20      |
|   Sureste   |   2    |      3       |       8       |  3   |          |      21      |
|     Sur     |   4    |      2       |       7       |  4   |          |      22      |
|  Suroeste   |   8    |      1       |       6       |  5   |          |      23      |
|    Oeste    |   16   |      4       |       5       |  6   |          |      24      |
|  Noroeste   |   32   |      7       |       4       |  7   |          |      25      |
|    Norte    |   64   |      8       |       3       |  0   |          |      26      |
|  Nordeste   |  128   |      9       |       2       |  1   |          |      27      |
</div>

> Las direcciones de flujo en ArcGIS for Desktop y ArcGIS Pro son idénticas y no requieren de homologación.
>
> Cuando se crea el mapa de direcciones de flujo, p. ej. en QGIS, y el proceso posterior de acumulación se va a realizar en ArcGIS, es necesario realizar la conversión y homologación de las direcciones de flujo a la herramienta requerida utilizando un proceso intermedio de cambio de variable, lo anterior debido a que no se puede homologar por directamente, p. ej. la dirección 1 - nordeste de QGIS a la dirección 1 - este de ArcGIS. Igual sucede con las direcciones 2, 4 y 8.


### Procedimiento general

<div align="center">
<br><img alt="R.LTWB" src="https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FdrDEM/Graph/FdrDEMFlowchart.png" width="65%"><br>
<sub>Convenciones del diagrama: Clases de entidad y grillas en gris, Geo-procesos en verde y Procesos manuales en amarillo.<br>Líneas con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>

La marcación de direcciones de flujo puede ser realizado con Spatial Analyst Tools de ArcGIS for Desktop, HEC-GeoHMS sobre ArcGIS 10.2.2 a través de Arc Hydro Tools, Spatial Analyst de ArcGIS Pro, Arc Hydro Tools sobre ArcGIS Pro, QGIS, HEC-HMS a través del menú GIS y otras herramientas y librerías.

#### Direcciones de flujo en modelos digitales de elevación DEM con HEC-GeoHMS sobre ArcGIS for Desktop

1. En ArcGIS for Desktop, abra el mapa _D:\R.LTWB\HECGeoHMS\HECGeoHMS.mxd_ creado en la actividad de [reacondicionamiento de modelos digitales de elevación](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/AgreeDEM) que contiene las grillas DEM reacondicionadas. En caso de que este generando un mapa nuevo, cargue directamente las grillas contenidas en el directorio  _[D:\R.LTWB\HECGeoHMS\Layers](https://github.com/rcfdtools/R.LTWB/tree/main/HECGeoHMS/Layers)_.

2. En la barra de herramientas _HEC-GeoHMS_, vaya al menú _Preprocessing_ y seleccione la opción _Fill Sinks_ y realice el procedimiento de relleno de sumideros en formato GeoTIFF para los 3 modelos digitales de elevación reacondicionados y asigne los nombres ASTERFil.tif, SRTMFil.tif y ALOSFil.tif en la ruta _D:\R.LTWB\HECGeoHMS\Layers\_

> En esta herramienta puede establecer el límite de relleno con la opción _Fill Threshold_ y delimitar la zona a ser rellenada con la selección de un polígono mediante _Input Deranged Polygon Feature Class_.

Parámetros de entrada para relleno de sumideros para grillas reacondicionada ASTER
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FillDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFillDEMASTERParameters.png)

Resultados ventana de ejecución grilla ASTER (dt: 03'34")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FillDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFillDEMASTERLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FillDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFillDEMASTER.png)

Resultados ventana de ejecución grilla SRTM (dt: 03'33")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FillDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFillDEMSRTMLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FillDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFillDEMSRTM.png)

Resultados ventana de ejecución grilla ALOS (dt: 01h06'35")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FillDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFillDEMALOSLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FillDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFillDEMALOS.png)

| MDE reacondicionado | Cota mínima, m | Cota máxima, m | Relleno de sumideros | Cota mínima, m | Cota máxima, m | Descargar Fil :open_file_folder:                                                                                                                                                                                                                                                            |
|:-------------------:|:--------------:|:--------------:|:--------------------:|:--------------:|:--------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  ASTERAgreeDEM.tif  |     -1006      |     5687       |     ASTERFil.tif     |       0        |      5687      | [.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ASTERFil.rar)                                                                                                                                                                                                         |
|  SRTMAgreeDEM.tif   |     -1044      |      5696      |     SRTMFil.tif      |       -4       |      5696      | [.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/SRTMFil.rar)                                                                                                                                                                                                          |
|  ALOSAgreeDEM.tif   |     -1046      |      5709      |     ALOSFil.tif      |       0        |      5687      | [part1.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ALOSFil.part1.rar), [part2.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ALOSFil.part2.rar), [part3.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ALOSFil.part3.rar) |

| Los valores de cotas mínimas pueden variar dependiendo de la versión de ArcGIS, la versión de HEC-GeoHMS o la herramienta utilizada para el relleno.

3. Utilizando algebra de mapas, calcule la diferencia entre el mapa de relleno de sumideros y el mapa reacondicionado para conocer la localización específica de las zonas rellenadas entre 1 y 50 metros. Ejecute _ArcToolBox / Spatial Analyst Tools / Map Algebra / Raster Calculator_ e ingrese la expresión `Con(("ASTERFil.tif"-"ASTERAgreeDEM.tif">0)  & ("ASTERFil.tif"-"ASTERAgreeDEM.tif"<=50) ,"ASTERFil.tif" - "ASTERAgreeDEM.tif")`, guarde la grilla resultante como _D:\R.LTWB\HECGeoHMS\Layers\ASTERSinkLocations.tif_ 

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FillDEM/Screenshot/ArcGISDesktop10.2.2RasterCalculator.png)

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FillDEM/Screenshot/ArcGISDesktop10.2.2RasterCalculatorLog.png)

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FillDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFillDEMASTERSinkLocations.png)

4. Visualice la tabla de atributos de la grilla [ASTERSinkLocations.tif](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ASTERSinkLocations.rar) que contiene valores discretos contables de 1 a 50 metros de diferencia de elevación y cree una gráfica de barras desde el menú _View / Graphs / Create Graph_. 

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FillDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFillDEMASTERSinkLocationsGraph.png)

Como puede observar en la gráfica y en la tabla de atributos, se han rellenado p. ej. 1.265.842 celdas 1 metro por encima de su elevación original, 823.059 celdas 2 metros por encima su elevación original y al sumar el total de celdas rellenadas hasta una diferencia de 50 metros se cuentan 4.020.911 celdas.

> Opcional: repita este procedimiento para los modelos digitales de elevación SRTM y ALOS.

5. Utilizando la barra de herramienta 3D Analyst, cree y visualice perfiles de terreno con y sin relleno de sumideros.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FillDEM/Screenshot/ArcGISDesktop10.2.2ProfileView.png)


#### Reacondicionamiento de modelos digitales de elevación DEM con otras herramientas

| Herramienta                                                                                                                     | Procedimiento                                                                                                                                                                                                                                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ArcGIS for Desktop / Spatial Analyst Tools](https://desktop.arcgis.com/en/arcmap/latest/tools/spatial-analyst-toolbox/fill.htm) | En el ArcToolBox, busque la caja de herramientas _Spatial Analyst Tools / Hydrology_ y seleccione la herramienta _Fill_. Seleccione la grilla de entrada, asigne un nombre de la grilla de salida y opcionalmente ingrese el valor _Z limit_ correspondiente a la máxima diferencia de elevación entre la celda de terreno y la celda rellenada.                  |
| [ArcGIS 10.2.2 / Arc Hydro Tools](http://downloads.esri.com/archydro/archydro/Setup/)                                           | El procedimiento es el mismo presentado en esta actividad a través de HEC-GeoHMS debido a que esta herramienta utiliza Arc Hydro Tools.                                                                                                                                                                                                                           |
| [ArcGIS Pro / Spatial Analyst](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/fill.htm)                | En el panel _Geoprocessing_, busque la caja de herramientas _Spatial Analyst Tools / Hydrology_ y seleccione la herramienta _Fill_. Seleccione la grilla de entrada, asigne un nombre de la grilla de salida y opcionalmente ingrese el valor _Z limit_ correspondiente a la máxima diferencia de elevación entre la celda de terreno y la celda rellenada.       |
| [ArcGIS Pro / Arc Hydro Tools Pro](http://downloads.esri.com/archydro/archydro/setup/Pro/)                                      | En el panel _Geoprocessing_, busque la caja de herramientas _Arc Hydro Tools Pro / Terrain Preprocessing_ y seleccione la herramienta _Fill Sinks_. En esta herramienta puede establecer el límite de relleno con la opción _Fill Threshold_ y delimitar la zona a ser rellenada con la selección de un polígono mediante _Input Deranged Polygon Feature Class_. |
| [HEC-HMS](https://www.hec.usace.army.mil/confluence/hmsdocs/hmsum/4.9/geographic-information/gis-menu)                          | En el panel lateral seleccione en _Basin Models_ el modelo de cuenca creado, luego en el menú _GIS_ seleccione la opción _Preprocessing Sinks_. Luego de la ejecución, HEC-HMS genera automáticamente dos grillas de resultados, la primera con el DEM rellenado y la segunda con las localizaciones y profundidades específicas de las zonas rellenadas.         |
| [QGIS](https://saga-gis.sourceforge.io/saga_tool_doc/2.1.4/ta_preprocessor_3.html)                                              | En el _Processing Toolbox_ busque el grupo de herramientas _SAGA / Terrain Analysis_ y ejecute cualquiera de los 3 métodos disponibles: _Fill Sinks (Planchon/Darboux, 2001), Fill Sinks (Wang & Lui) o Fill Sinks XXL (Wang & Lui)_                                                                                                                              |

HEC-HMS grilla de resultados con localización de sumideros
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FillDEM/Screenshot/HECHMS4.9PreprocessingSinksLocations.png)

En este momento dispone de la grilla de relleno de sumideros requerida para la marcación de direcciones de flujo.

> **Actividad complementaria**: utilizando diferentes herramientas, cree mapas de relleno de sumideros a partir de la grilla reacondicionada ASTER GDEM y a través de un análisis de diferencias de elevación obtenido con la calculadora ráster, compare, analice y explique las diferencias encontradas.


### Referencias

* https://desktop.arcgis.com/en/arcmap/latest/tools/spatial-analyst-toolbox/fill.htm
* https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/fill.htm
* https://desktop.arcgis.com/en/arcmap/latest/tools/spatial-analyst-toolbox/conditional-evaluation-with-con.htm


### Compatibilidad

* Se recomienda desarrollar el relleno de sumideros - Fil con el mismo grupo de herramientas donde se desarrollo el reacondicionamiento, p. ej. si el AgreeDEM fué generado directamente con Arc Hydro Tools Pro de ArcGIS Pro, ejecute el relleno con las mismas herramientas _Terrain Processing_.  
 

### Control de versiones

| Versión     | Descripción                                                                                                                                                                   | Autor                                      | Horas |
|-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|:-----:|
| 2022.07.23  | Versión inicial con relleno de sumideros para DEM ASTER, SRTM y ALOS. Cálculo de diferencias de elevación para identificación de zonas rellenadas, visualización de perfiles. | [rcfdtools](https://github.com/rcfdtools)  |   5   |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Actividad anterior](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/AgreeDEM) | [:house: Inicio](https://github.com/rcfdtools/R.LTWB/wiki) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/9) | [Actividad siguiente]()  |
|----------------------------------------------------------------------------------------|----------------------------------------------------|--------------------------------------------------------------------------|--------------------------|
