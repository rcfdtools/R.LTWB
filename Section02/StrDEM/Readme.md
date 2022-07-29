##  Demarcación de drenajes – Stream Definition - STR y localización de nodos característicos
Keywords: `STR DEM` `Stream definition` `FAC DEM` `Flow accumulation` `Arc Hydro Tools` `Extract Multi Values to Points` `Raster to Polyline` `Add Field` `Geometry Calculator`

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/StrDEM.png)

A partir de grillas de acumulación de flujo, se puede identificar cuáles celdas confluyen hacia cada drenaje; para ello, se especifica el área de aportación p. ej. de 1 o 4 km² o el número equivalente de celdas en función de su resolución y considerando que a menor área de aportación, mayor será el número de corrientes obtenidas. El procedimiento general para la definición de drenajes incluye la creación de una grilla binarizada con celdas a las que se les asigna 1 como valor de pixel.

Es importante tener en cuenta que algunos de los tramos obtenidos, corresponderán a áreas de aportación inferiores al valor de aportación definido, específicamente en cuencas intermedias o cuencas de tránsito entre dos puntos de unión próximos.


### Objetivos

* Marcar las celdas o pixeles correspondientes a cada cuenca de drenaje para un área determinada.
* Convertir el mapa binarizado en un red de drenaje vectorizada.
* Obtener los puntos de inicio y confluencia de la red obtenida.
* Para cada punto obtenido obtener el total de celdas acumuladas y calcular las áreas de aportación. 


### Requerimientos

* [ArcGIS for Desktop 10+](https://desktop.arcgis.com/es/desktop/)
* [ArcGIS Pro 2+](https://pro.arcgis.com/en/pro-app/latest/get-started/download-arcgis-pro.htm) (opcional)
* [QGIS 3+](https://qgis.org/) (opcional)
* [Grillas de acumulaciones de Flujo – Flow Accumulation – FAC. ](https://github.com/rcfdtools/R.LTWB/tree/main/HECGeoHMS/Layers)[:blue_book:Aprender.](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/FacDEM)


### Procedimiento general

<div align="center">
<br><img alt="R.LTWB" src="https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Graph/StrDEMFlowchart.png" width="65%"><br>
<sub>Convenciones generales en diagramas: clases de entidad en azul, dataset en gris oscuro, grillas en color verde, geo-procesos en rojo y procesos manuales en amarillo. Líneas con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>

La demarcación de drenajes a partir de un área de aportación definida puede ser realizada con HEC-GeoHMS sobre ArcGIS 10.2.2 a través de Arc Hydro Tools, Arc Hydro Tools sobre ArcGIS Pro, XXXXXXXXQGIS y HEC-HMS a través del menú GIS.


#### Demarcación de drenajes con HEC-GeoHMS sobre ArcGIS for Desktop

1. En ArcGIS for Desktop, abra el mapa _D:\R.LTWB\HECGeoHMS\HECGeoHMS.mxd_ creado en la actividad de [reacondicionamiento de modelos digitales de elevación](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/AgreeDEM) y modificado en la clase de [acumulaciones de flujo](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/FacDEM) que contiene las grillas FAC. En caso de que este generando un mapa nuevo, cargue directamente las grillas FAC contenidas en el directorio  _[D:\R.LTWB\HECGeoHMS\Layers](https://github.com/rcfdtools/R.LTWB/tree/main/HECGeoHMS/Layers)_.

2. En la barra de herramientas _HEC-GeoHMS_, vaya al menú _Preprocessing_, seleccione la opción _Stream Definition_ y cree la grilla de marcación de drenajes en formato GeoTIFF para los 3 modelos digitales de acumulación y asigne los nombres ASTERStr.tif, SRTMStr.tif y ALOSStr.tif en la ruta D:\R.LTWB\HECGeoHMS\Layers\. Como criterio de área de aportación utilice p. ej. 1 km², que para modelos ASTER y SRTM corresponderá a 1062 celdas de aportación debido a que su resolución es de 30.68464585 metros y para el modelo ALOS PALSAR corresponderá a 6400 celdas de aportación ya que su resolución es de 12.5 metros. Para la representación en pantalla, use la red de drenaje vectorial como fondo.

Parámetros de entrada para demarcación de drenajes ASTER
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSStrDEMASTERParameters.png)

Resultados ventana de ejecución grilla ASTER (dt: 00'05.82")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSStrDEMASTERLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSStrDEMASTER.png)

Resultados ventana de ejecución grilla SRTM (dt: 00'05.72")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSStrDEMSRTMLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSStrDEMSRTM.png)

Resultados ventana de ejecución grilla ALOS (dt: 42'24.63")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSStrDEMALOSParameters.png)  
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSStrDEMALOSLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2HECGeoHMSStrDEMALOS.png)

> Como puede observar en las ilustraciones, para las áreas de aportación definidas se han marcado múltiples celdas de drenaje en localizaciones similares a las de los vectores utilizados para el reacondicionamiento del terreno. 

|    Grilla    |                            Descargar :open_file_folder:                             |
|:------------:|:-----------------------------------------------------------------------------------:|
| ASTERStr.tif | [.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ASTERStr.rar) |
| SRTMStr.tif  | [.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/SRTMStr.rar)  |
| ALOSStr.tif  | [.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ALOSStr.rar)  |

3. Convierta las grillas de demarcación de drenajes a vectores con la herramienta _ArcToolBox / Conversion Tools / From Raster / Raster to Polyline_, nombre como _ASTERStr.shp_, _SRTMStr.shp_ y _ALOSStr.shp_ en la carpeta _D:\R.LTWB\\.shp_. Desactive la casilla _Simplify polylines_ para obtener líneas detalladas sobre cada celda horizontal, vertical y diagonal. Automáticamente, esta herramienta genera tramos de drenaje independientes manteniendo la correspondencia en los puntos de unión de afluentes.

Parámetros de entrada para la conversión a polilínea en grilla ASTER
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2RasterToPolylineStrDEMASTERParameters.png)

Resultados ventana de ejecución grilla ASTER (dt: 03'20")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2RasterToPolylineStrDEMASTERLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2RasterToPolylineStrDEMASTER.png)

Resultados ventana de ejecución grilla SRTM (dt: 04'39")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2RasterToPolylineStrDEMSRTMLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2RasterToPolylineStrDEMSRTM.png)

Resultados ventana de ejecución grilla ALOS (dt: 06'52")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2RasterToPolylineStrDEMALOSLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2RasterToPolylineStrDEMALOS.png)

> A diferencia de las líneas de drenaje utilizadas para el reacondicionamiento del modelo de terreno a partir de la red de drenaje del IGAC, las líneas de drenaje obtenidas a partir de la marcación de celdas de terrreno, son localizadas a lo largo y en la diagonal de los pixeles, lo que permite obtener la localización exacta de los puntos de inicio, entrega y confluencia de toda la red pero sobre las celdas específicas donde se realiza la acumulación principal del flujo.

4. Utilizando la herramienta _ArcToolBox / Data Management Tools / Features / Feature Vertices To Points_, obtenga los nodos inicio / fin de cada tramo de drenaje identificado, nombre como _ASTERStrNode.shp_, _SRTMStrNode.shp_ y _ALOSStrNode.shp_ en la carpeta _D:\R.LTWB\\.shp_. En `Point Type` seleccione `BOTH_ENDS` para obtener el punto inicial y final de cada línea de drenaje.

Parámetros de entrada para la obtención de nodos característicos en grilla ASTER
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2FeatureVerticesToPointsStrDEMASTERParameters.png)

Resultados ventana de ejecución grilla ASTER con 65554 nodos (dt: 00'29.82")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2FeatureVerticesToPointsStrDEMASTERLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2FeatureVerticesToPointsStrDEMASTER.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISPro3.0.0FeatureVerticesToPointsStrDEMASTER.png)

Resultados ventana de ejecución grilla SRTM con 65688 nodos (dt: 00'18.80")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2FeatureVerticesToPointsStrDEMSRTMLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2FeatureVerticesToPointsStrDEMSRTM.png)

Resultados ventana de ejecución grilla ALOS con 72210 nodos (dt: 00'35.67")
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2FeatureVerticesToPointsStrDEMALOSLog.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2FeatureVerticesToPointsStrDEMALOS.png)

> Debido a la alta densidad de la red de nodos, es posible que en escalas reducidas no se visualicen completamente los puntos en pantalla en ArcGIS for Desktop. Visualizar con ArcGIS Pro o con QGIS.
>
> Los nodos obtenidos en los puntos finales de los tramos de drenaje que confluyen en una misma localización estarán duplicados y en la misma localización obtendremos también un nodo adicional correspondiente al punto inicial del tramo aguas abajo de la unión. En las confluencias solo se requiere de 1 nodo para la lectura de los valores de celdas acumuladas y los posteriores procesos de lectura de caudal medio de largo plazo que desarrollaremos en este curso.

5. Para cada red de puntos característicos, elimine los nodos duplicados utilizando el siguiente procedimiento:

Abra la tabla de atributos de ASTERStrNode.shp y agregue 2 campos de atributos numéricos dobles y nómbrelos como CX, CY.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2AddField.png)

Desde las cabeceras de los campos de atributos CX y CY, calcule la geometría de los puntos y obtenga las propiedades `X Coordinate of Point` y `Y Coordinate of Point` a partir del _CRS MAGNA Colombia CMT12_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2CalculateGeometry.png)

Repita el procedimiento anterior para las redes de puntos SRTMStrNode.shp y ALOSStrNode.shp

> En QGIS 3, el procedimiento de eliminación de elementos duplicados que puede ser realizado con la herramienta _Processing Toolbox / Vector general / Delete duplicate geometries_, es más simple debido a que todos aquellos elementos que espacialmente sean coincidentes en su geometría, son eliminados automáticamente. Este procedimiento crea una nueva capa geográfica. El proceso de eliminación homologable a Delete Identical de ArcGIS se realiza en QGIS con la herramienta _Processing Toolbox / Vector general / Delete duplicates by attribute_.

Resultados obtenidos

| Nodos característicos | Nodos con duplicados | Nodos finales | Descargar :open_file_folder:  |
|:---------------------:|:--------------------:|:-------------:|:-----------------------------:|
|   ASTERStrNode.shp    |        65554         |               |             .rar              | 
|    SRTMStrNode.shp    |        65688         |               |             .rar              | 
|    ALOSStrNode.shp    |        72210         |               |             .rar              | 











Utilizando la herramienta _ArcToolBox / Spatial Analyst Tools / Extraction / Extract Multi Values to Points_, obtenga los el total de celdas acumuladas a partir del mapa _ASTERFac.tif_. En la tabla de atributos de la capa de puntos _[FacDEMTablaMuestra.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/FacDEMTablaMuestra.zip)_ encontrará una nueva columna de atributos con el total de celdas acumuladas.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2ExtractMultiValuestoPoints.png)

> La herramienta _Extract Multi Values to Points_ permite obtener simultáneamente los valores de acumulación para diferentes grillas, sin embargo, este proceso no puede ser realizado debido a que los puntos de muestreo solo son válidos para las posiciones de las celdas del modelo ASTER. Se recomienda verificar cada posición definida y su correspondencia con las demás grillas, podrá observar que no en todos los casos corresponden a las mismas localizaciones específicas sobre la red de drenaje principal.

En la tabla de atributos de la capa _[FacDEMTablaMuestra.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/FacDEMTablaMuestra.zip)_, verifique los valores registrados en la columna _ASTERFac_ y ordene ascendentemente. Para las localizaciones de muestra, el cauce con menor acumulación corresponde al _Arroyo Garrapata_ con 27562 celdas y el cauce con la mayor acumulación al _Río Calenturitas_ con 1328240 celdas.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2ExtractMultiValuestoPointsASTERFac.png)

5. A partir de la tabla de puntos de muestreo y los valores de celdas acumuladas, calcule el área de aportación en km² y rotule cada punto indicando el número de punto, nombre de la corriente, total de celdas acumuladas y área de aportación.

Desde las propiedades de la tabla de atributos de _FacDEMTablaMuestra.shp_, cree un campo de atributos numérico doble y nombre como _Akm2_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2AddField.png)

Desde la cabecera de la columna de atributos _Akm2_ y seleccionado la opción _Field Calculator_, calcule el área de aportación utilizando la expresión VB Script `[ASTERFac] * 30.68464585 * 30.68464585 / 1000000` donde 30.68464585 corresponde al tamaño de cada celda y 1000000 corresponde al valor de conversión de m² a km².

> Este cálculo puede también ser realizado con la expresión Python `!ASTERFac! * 30.68464585 * 30.68464585 / 1000000`

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2FieldCalculator.png)

Rotule con la expresión VB Script `[Punto] &" - "& [Cauce] &VBNewline& "FAC: " & [ASTERFac] &VBNewline& "A, km²: "  & Round( [Akm2] ,2)`

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2Label.png)

> **Actividad complementaria**: realice el procedimiento de lectura de celdas en puntos de muestreo y calcule las áreas acumuladas utilizando las grillas de acumulación SRTM y ALOS. Para esta actividad es necesario crear 2 hojas adicionales en el libro de Microsoft Excel y modificar las coordenadas específicas para cada grilla de acumulación.


#### Acumulaciones de flujo - FDR con otras herramientas

| Herramienta                                                                                                                                | Procedimiento                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ArcGIS for Desktop / Spatial Analyst Tools](https://desktop.arcgis.com/en/arcmap/latest/tools/spatial-analyst-toolbox/flow-direction.htm) | En el ArcToolBox, busque la caja de herramientas _Spatial Analyst Tools / Hydrology_ y seleccione la herramienta _Flow Accumulation_. Seleccione la grilla de entrada y asigne un nombre a la grilla de salida. Esta herramienta además permite mediante la opción _Imput weight raster_, incluir una grilla de pesos a ser acumulados y definir el tipo de datos de salida Float o Integer para la grilla resultante.                                                                                                                                              |
| [ArcGIS 10.2.2 / Arc Hydro Tools](http://downloads.esri.com/archydro/archydro/Setup/)                                                      | El procedimiento es el mismo presentado en esta actividad a través de HEC-GeoHMS debido a que esta herramienta utiliza Arc Hydro Tools.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [ArcGIS Pro / Spatial Analyst](https://pro.arcgis.com/en/pro-app/latest/help/analysis/raster-functions/flow-direction-raster-function.htm) | En el panel _Geoprocessing_, busque la caja de herramientas _Spatial Analyst Tools / Hydrology_ y seleccione la herramienta _Flow Accumulation_.  Seleccione la grilla de entrada y asigne un nombre a la grilla de salida. Esta herramienta además permite mediante la opción _Imput weight raster_, incluir una grilla de pesos a ser acumulados y definir el tipo de datos de salida Float o Integer para la grilla resultante. Al igual que la herramienta FIL, se puede seleccionar el algoritmo que define el tipo de direcciones a procesar (D8, MFD, DINF). |
| [ArcGIS Pro / Arc Hydro Tools Pro](http://downloads.esri.com/archydro/archydro/setup/Pro/)                                                 | En el panel _Geoprocessing_, busque la caja de herramientas _Arc Hydro Tools Pro / Terrain Preprocessing_ y seleccione la herramienta _Flow Accumulation_. Seleccione la grilla de entrada y asigne un nombre a la grilla de salida.                                                                                                                                                                                                                                                                                                                                |
| [HEC-HMS](https://www.hec.usace.army.mil/confluence/hmsdocs/hmsum/4.9/geographic-information/gis-menu)                                     | En el panel lateral seleccione en _Basin Models_ el modelo de cuenca creado, luego en el menú _GIS_ seleccione la opción _Preprocessing Drainage_. Este procedimiento crea automáticamente las grillas de direcciones y acumulaciones de flujo.                                                                                                                                                                                                                                                                                                                     |
| [QGIS 3](https://acolita.com/direccion-del-drenaje-en-qgis-3/)                                                                             | En el _Processing Toolbox_ busque el grupo de herramientas _SAGA / Terrain Analysis_ y ejecute _Fill Sinks (Wang & Lui)_ que además de rellenas las depresiones permite generar el mapa de direcciones de flujo y el mapa de acumulación.                                                                                                                                                                                                                                                                                                                           |
En este momento dispone de grillas de acumulación de flujo para obtener las celdas de los drenajes sobre los diferentes modelos digitales de elevación.


### Referencias

* https://docs.qgis.org/3.22/en/docs/user_manual/processing_algs/qgis/vectorgeneral.html


### Compatibilidad

* Se recomienda desarrollar la demarcación de celdas de drenaje con el mismo grupo de herramientas donde desarrollo el reacondicionamiento, p. ej. si la grilla de acumulación fué generada directamente con Arc Hydro Tools Pro de ArcGIS Pro, obtenga las celdas marcadas STR con las mismas herramientas.  
 

### Control de versiones

| Versión    | Descripción                                                                                                                                                     | Autor                                      | Horas |
|------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|:-----:|
| 2022.07.28 | Versión inicial con acumulaciones de flujo para DEM ASTER, SRTM y ALOS. Puntos de muestreo para lectura de valores acumulados y cálculo de áreas de aportación. | [rcfdtools](https://github.com/rcfdtools)  |   7   |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Anterior](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/FdrDEM)  | [:house: Inicio](https://github.com/rcfdtools/R.LTWB/wiki) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/11) | [Siguiente]() |
|-----------------------------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------------------|---------------|
