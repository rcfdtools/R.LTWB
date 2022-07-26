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

> Las direcciones de flujo en ArcGIS for Desktop y ArcGIS Pro son idénticas y no requieren de homologación.
>
> Cuando se crea el mapa de direcciones de flujo, p. ej. en QGIS, y el proceso posterior de acumulación se va a realizar en ArcGIS, es necesario realizar la conversión y homologación de las direcciones de flujo a la herramienta requerida utilizando un proceso intermedio de cambio de variable, lo anterior debido a que no se puede homologar por directamente, p. ej. la dirección 1 - nordeste de QGIS a la dirección 1 - este de ArcGIS. Igual sucede con las direcciones 2, 4 y 8.


### Procedimiento general

<div align="center">
<br><img alt="R.LTWB" src="https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FdrDEM/Graph/FdrDEMFlowchart.png" width="65%"><br>
<sub>Convenciones del diagrama: Clases de entidad y grillas en gris, Geo-procesos en verde y Procesos manuales en amarillo.<br>Líneas con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>

La marcación de direcciones de flujo puede ser realizado con Spatial Analyst Tools de ArcGIS for Desktop, HEC-GeoHMS sobre ArcGIS 10.2.2 a través de Arc Hydro Tools, Spatial Analyst de ArcGIS Pro, Arc Hydro Tools sobre ArcGIS Pro, QGIS, HEC-HMS a través del menú GIS y otras herramientas y librerías.

#### Direcciones de flujo con HEC-GeoHMS sobre ArcGIS for Desktop

1. En ArcGIS for Desktop, abra el mapa _D:\R.LTWB\HECGeoHMS\HECGeoHMS.mxd_ creado en la actividad de [reacondicionamiento de modelos digitales de elevación](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/AgreeDEM) y modificado en la clase de [relleno de sumideros](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/FillDEM) en que contiene las grillas FIL. En caso de que este generando un mapa nuevo, cargue directamente las grillas FIL contenidas en el directorio  _[D:\R.LTWB\HECGeoHMS\Layers](https://github.com/rcfdtools/R.LTWB/tree/main/HECGeoHMS/Layers)_.

2. En la barra de herramientas _HEC-GeoHMS_, vaya al menú _Preprocessing_ y seleccione la opción _Flow Direction_ y realice el procedimiento de direcciones de flujo en formato GeoTIFF para los 3 modelos digitales de elevación con relleno de sumideros y asigne los nombres ASTERFdr.tif, SRTMFdr.tif y ALOSFdr.tif en la ruta _D:\R.LTWB\HECGeoHMS\Layers\_

> En esta herramienta puede establecer el límite del mapa de direcciones con la opción _Input Outer Wall Polygon_.

Parámetros de entrada para direcciones de flujo ASTER
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FdrDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFdrDEMASTERParameters.png)

Resultados ventana de ejecución grilla ASTER (dt: 01'11")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FdrDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFdrDEMASTERLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FdrDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFdrDEMASTER.png)

Resultados ventana de ejecución grilla SRTM (dt: 01'12")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FdrDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFdrDEMSRTMLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FdrDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFdrDEMSRTM.png)

Resultados ventana de ejecución grilla ALOS (dt: 09'08")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FdrDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFdrDEMALOSLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FdrDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFdrDEMALOS.png)

> Para saber si las grillas FDR han sido creadas correctamente, en la simbología de representación desplegada en la tabla de atributos, únicamente deben ser visibles las direcciones 1, 2, 4, 8, 16, 32, 64, 128 y 255 que corresponde a celdas sin dirección. En caso de que aparezcan números consecutivos 1, 2, 3, 4... hasta 255, deberá revisar y volver a generar el mapa de relleno de sumideros debido a que existen múltiples zonas con depresiones o sifones que no drenan sobre la superficie del modelo de elevación a una localización más baja.

| Direcciones de flujo | Descargar FDR :open_file_folder:                                                    |
|:--------------------:|:------------------------------------------------------------------------------------|
|     ASTERFdr.tif     | [.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ASTERFdr.rar) |
|     SRTMFdr.tif      | [.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/SRTMFdr.rar)  |
|     ALOSFdr.tif      | [.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ALOSFdr.rar)  |

3. Visualice la tabla de atributos de la grilla [ASTERFdr.tif](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ASTERFdr.rar) que contiene valores discretos contables de las 9 direcciones de flujo (incluida la 255 o no dirección) y cree una gráfica de barras desde el menú _View / Graphs / Create Graph_. 

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/FillDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSFillDEMASTERSinkLocationsGraph.png)

Como puede observar en la gráfica y en la tabla de atributos, la dirección dominante es 16 - Oeste con 7571807 celdas.

> Opcional: repita este procedimiento para los modelos digitales de elevación SRTM y ALOS.



#### Direcciones de flujo - FDR con otras herramientas

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
