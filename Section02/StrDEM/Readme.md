## Demarcación de drenajes – Stream Definition - STR y localización de nodos característicos
Keywords: `STR DEM` `Stream definition` `FAC DEM` `Flow accumulation` `Arc Hydro Tools` `Extract Multi Values to Points` `Raster to Polyline` `Add Field` `Geometry Calculator` `Delete Identical` `Raster Calculator`

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/StrDEM.png)

A partir de las grillas de acumulación de flujo, se pueden identificar las celdas que hacen parte de la red de drenaje principal. Para ello se especifica el área de aportación p. ej. de 1 o 4 km² o el número equivalente de celdas en función de su resolución, considerando que a menor área de aportación, mayor será el número de corrientes obtenidas. El procedimiento general para la definición de drenajes incluye la creación de una grilla binarizada con celdas a las que se les asigna 1 como valor de pixel. Es importante tener en cuenta que algunos de los tramos obtenidos, corresponderán a áreas de aportación inferiores al valor de aportación definido, específicamente en cuencas intermedias o cuencas de tránsito entre dos puntos de unión próximos.


### Objetivos

* Marcar las celdas o pixeles correspondientes a cada cuenca de drenaje para un área de aportación determinada.
* Convertir el mapa binarizado en un red de drenaje vectorizada.
* Obtener los puntos de inicio y confluencia característicos de toda la red obtenida.
* Eliminar nodos duplicados.
* Para cada punto característico obtener el total de celdas acumuladas y calcular las áreas de aportación. 


### Requerimientos

* [ArcGIS for Desktop 10+](https://desktop.arcgis.com/es/desktop/)
* [ArcGIS Pro 2+](https://pro.arcgis.com/en/pro-app/latest/get-started/download-arcgis-pro.htm) (opcional)
* [QGIS 3+](https://qgis.org/) (opcional)
* [Grillas de acumulaciones de Flujo – Flow Accumulation – FAC. ](https://github.com/rcfdtools/R.LTWB/tree/main/HECGeoHMS/Layers)[:mortar_board:Aprender.](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/FacDEM)

> El libro de cálculo [StrDEM.xlsx](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/StrDEM.xlsx) de Microsoft Excel disponible en esta actividad, contiene un ejemplo del número de celdas requeridas y subcuencas obtenidas para diferentes áreas de aportación en función del área de una cuenca principal y la resolución específica de una grilla DEM. 

<div align="center">
<br><img alt="R.LTWB" src="https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/MicrosoftExcel365StrDEM.png" width="65%">
<br><img alt="R.LTWB" src="https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/MicrosoftExcel365StrDEMGraph.png" width="65%"><br>
</div>


### Procedimiento general

<div align="center">
<br><img alt="R.LTWB" src="https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Graph/StrDEMFlowchart.png" width="65%"><br>
<sub>Convenciones generales en diagramas: clases de entidad en azul, dataset en gris oscuro, grillas en color verde, geo-procesos en rojo, procesos automáticos o semiautomáticos en guiones rojos y procesos manuales en amarillo. Líneas conectoras con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>

La demarcación de drenajes a partir de un área de aportación definida puede ser realizada con ArcGIS for Desktop y ArcGIS Pro a través de la calculadora ráster, HEC-GeoHMS sobre ArcGIS 10.2.2 a través de Arc Hydro Tools, Arc Hydro Tools sobre ArcGIS Pro, QGIS Raster Calculator y HEC-HMS a través del menú GIS.


#### Demarcación de drenajes con HEC-GeoHMS sobre ArcGIS for Desktop

1. En ArcGIS for Desktop, abra el mapa _D:\R.LTWB\HECGeoHMS\HECGeoHMS.mxd_ creado en la actividad de [reacondicionamiento de modelos digitales de elevación](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/AgreeDEM) y modificado en la clase de [acumulaciones de flujo](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/FacDEM) que contiene las grillas FAC. En caso de que este generando un mapa nuevo, cargue directamente las grillas FAC contenidas en el directorio  _[D:\R.LTWB\HECGeoHMS\Layers](https://github.com/rcfdtools/R.LTWB/tree/main/HECGeoHMS/Layers)_.

2. En la barra de herramientas _HEC-GeoHMS_, vaya al menú _Preprocessing_, seleccione la opción _Stream Definition_ y cree la grilla de marcación de drenajes en formato GeoTIFF para los 3 modelos digitales de acumulación y asigne los nombres [ASTERStr.tif](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ASTERStr.rar), [SRTMStr.tif](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/SRTMStr.rar) y [ALOSStr.tif](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ALOSStr.rar) en la ruta _D:\R.LTWB\HECGeoHMS\Layers\_. Como criterio de área de aportación utilice p. ej. 1 km², que para los modelos ASTER y SRTM corresponderá a 1062 celdas de aportación debido a que su resolución es de 30.68464585 metros y para el modelo ALOS PALSAR, 6400 celdas de aportación ya que su resolución es de 12.5 metros. Para la representación en pantalla, use como fondo la red de drenaje vectorial.

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

> Como puede observar en las ilustraciones, para las áreas de aportación definidas se han marcado múltiples celdas de drenaje en localizaciones similares a las de los vectores utilizados para el reacondicionamiento del terreno, excepto en algunas zonas donde existen bucles en la red de drenaje original con la que se realizó el reacondicionamiento del modelo digital de elevación. 

<div align="center">

|    Grilla    |                            Descargar :open_file_folder:                             |
|:------------:|:-----------------------------------------------------------------------------------:|
| ASTERStr.tif | [.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ASTERStr.rar) |
| SRTMStr.tif  | [.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/SRTMStr.rar)  |
| ALOSStr.tif  | [.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ALOSStr.rar)  |

</div>

> El procedimiento de identificación y marcación de las celdas que igualan o exceden el valor del área de aportación definido, puede ser realizado manualmente en cualquier herramienta GIS a través de la calculadora ráster, utilizando como entrada la grilla de acumulación y definiendo un condicional. Por ejemplo, para la grilla ASTER la expresión a usar es `Con("ASTERFac.tif">=1062,1)` donde 1062 corresponde al número de celdas necesarias para obtener un área de aportación de 1 km² para una grilla con resolución de 30.68464585 metros (1062 = 1000000 m² / (30.68464585m * 30.68464585m)).

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2RasterCalculatorStrDEMASTER.png)

3. Convierta las grillas de demarcación de drenajes a vectores con la herramienta _ArcToolBox / Conversion Tools / From Raster / Raster to Polyline_, nombre como _[ASTERStr.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/asterstr.zip)_, _[SRTMStr.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/srtmstr.zip)_ y _[ALOSStr.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/alosstr.zip)_ en la carpeta _D:\R.LTWB\\.shp_. Desactive la casilla `Simplify polylines` para obtener líneas detalladas sobre cada celda horizontal, vertical y diagonal. Automáticamente, esta herramienta genera tramos de drenaje independientes manteniendo la correspondencia entre los puntos de unión de afluentes.

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

4. Utilizando la herramienta _ArcToolBox / Data Management Tools / Features / Feature Vertices To Points_, obtenga los nodos inicio / fin de cada tramo de drenaje identificado, nombre como _[ASTERStrNode.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ASTERStrNode.zip)_, _[SRTMStrNode.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/SRTMStrNode.zip)_ y _[ALOSStrNode.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ALOSStrNode.zip)_ en la carpeta _D:\R.LTWB\\.shp_. En `Point Type` seleccione `BOTH_ENDS` para obtener el punto inicial y final de cada línea de drenaje.

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

> Los nodos iniciales de cada tramo de drenaje son requeridos debido a que aguas arriba de estos nodos existen múltiples celdas que son acumuladas hasta el pixel o celda identificado a partir del cual se conforma la escorrentía para el área característica de aportación establecida. 
> 
> Debido a la alta densidad de la red de nodos, es posible que en escalas reducidas no se visualicen completamente los puntos en pantalla en ArcGIS for Desktop. Visualizar con ArcGIS Pro o con QGIS.
>
> Los nodos obtenidos en los puntos finales de los tramos de drenaje que confluyen en una misma localización estarán duplicados y en la misma localización obtendremos también un nodo adicional correspondiente al punto inicial del tramo aguas abajo de la unión. En las confluencias solo se requiere de 1 nodo para la lectura de los valores de celdas acumuladas y los posteriores procesos de lectura de caudal medio de largo plazo que desarrollaremos en este curso.

5. Para cada red de puntos característicos, elimine los nodos duplicados utilizando el siguiente procedimiento:

Abra la tabla de atributos de _ASTERStrNode.shp_ y agregue 2 campos de atributos numéricos dobles y nómbrelos como `CX`, `CY`.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2AddField.png)

Desde las cabeceras de los campos de atributos `CX` y `CY`, calcule la geometría de los puntos y obtenga las propiedades `X Coordinate of Point` y `Y Coordinate of Point` a partir del _CRS MAGNA Colombia CMT12_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2CalculateGeometry.png)

Utilizando la herramienta _ArcToolBox / Data Management Tools / General / Delete Identical_, elimine los nodos repetidos en cada una de las capas vectoriales generadas previamente. Este procedimiento realiza la eliminación sobre la misma capa a partir de los valores duplicados en los campos `CX` y `CY`.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2DeleteIdenticalParameters.png)  
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2DeleteIdenticalStrDEMASTER.png)

> En QGIS 3, el procedimiento de eliminación de elementos duplicados puede ser realizado con la herramienta _Processing Toolbox / Vector general / Delete duplicate geometries_, es más simple que en ArcGIS debido a que todos aquellos elementos que espacialmente sean coincidentes en su geometría, son eliminados automáticamente, sin embargo, es necesario crear una nueva capa geográfica. El proceso de eliminación homologable a _Delete Identical_ de ArcGIS puede ser realizado en QGIS con la herramienta _Processing Toolbox / Vector general / Delete duplicates by attribute_.

Repita el procedimiento anterior para los puntos contenidos en SRTMStrNode.shp y ALOSStrNode.shp. Resultados obtenidos:  

<div align="center">

|                        Polilíneas Str :open_file_folder:                        |                              Nodos Str :open_file_folder:                               | Total nodos | Total duplicados | Nodos finales |
|:-------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|:-----------:|:----------------:|:-------------:|
| [ASTERStr.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/asterstr.zip) | [ASTERStrNode.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ASTERStrNode.zip) |    65554    |      36429       |     30125     | 
|  [SRTMStr.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/srtmstr.zip)  |  [SRTMStrNode.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/SRTMStrNode.zip)  |    65688    |      36046       |     29622     | 
|  [ALOSStr.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/alosstr.zip)  |  [ALOSStrNode.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ALOSStrNode.zip)  |    72210    |      40132       |     32078     | 

</div>

6. Utilizando la herramienta _ArcToolBox / Spatial Analyst Tools / Extraction / Extract Multi Values to Points_, obtenga el total de celdas acumuladas en capa de nodos _ASTERStrNode.shp_ a partir del mapa _ASTERFac.tif_. Luego de finalizada su ejecución, en la tabla de atributos de la capa de puntos _ASTERStrNode.shp_ encontrará una nueva columna de atributos con el total de celdas acumuladas denominada `ASTERFac`. Ordene descendentemente el campo `ASTERFac` y seleccione y visualice los 10 nodos con mayores acumulaciones, 

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2ExtractMultiValuestoPointsASTERFac.png)

> La herramienta _Extract Multi Values to Points_ permite obtener simultáneamente los valores de acumulación para diferentes grillas sobre una misma capa de puntos, sin embargo, este proceso no puede ser realizado debido a que los puntos de muestreo solo son válidos para las posiciones de las celdas de cada capa de puntos. 

Repita el procedimiento anterior para los puntos contenidos en _SRTMStrNode.shp_ utilizando la grilla de acumulación _SRTMFac.tif_.
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2ExtractMultiValuestoPointsSRTMFac.png)

Repita el procedimiento anterior para los puntos contenidos en _ALOSStrNode.shp_ utilizando la grilla de acumulación _ALOSFac.tif_.
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2ExtractMultiValuestoPointsALOSFac.png)

> Como observa en las 3 ilustraciones anteriores, la localización de los nodos con el mayor número de celdas acumuladas no corresponde a la misma zona geográfica debido a que las elevaciones en los 3 modelos DEM iniciales no son idénticas y también debido a los bucles presentes en la red de drenaje.

7. A partir de las tablas de puntos característicos de la red de drenaje y los valores de celdas acumuladas, calcule el área de aportación para cada nodo en km² y rotule cada punto indicando el total de celdas acumuladas y área de aportación.

Desde las propiedades de la tabla de atributos de _ASTERStrNode.shp, SRTMStrNode.shp y ALOSStrNode.shp_, cree un campo de atributos numérico doble y nombre como `Akm2`.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2AddFieldArea.png)

Desde la cabecera de la columna de atributos _Akm2_ y seleccionado la opción _Field Calculator_, calcule el área de aportación utilizando las expresiones VB Script:

* `[ASTERFac] * 30.68464585 * 30.68464585 / 1000000` donde 30.68464585 corresponde al tamaño de cada celda y 1000000 corresponde al valor de conversión de m² a km².
* `[SRTMFac] * 30.68464585 * 30.68464585 / 1000000` donde 30.68464585 corresponde al tamaño de cada celda y 1000000 corresponde al valor de conversión de m² a km².
* `[ALOSFac] * 12.5 * 12.5 / 1000000` donde 12.5 corresponde al tamaño de cada celda y 1000000 corresponde al valor de conversión de m² a km².
 
> Este cálculo puede también ser realizado con la expresión Python `!ASTERFac! * 30.68464585 * 30.68464585 / 1000000`

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2FieldCalculator.png)

Rotule con las expresiones VB Script:

* `"FAC: " & [ASTERFac] &VBNewline& "A, km²: "  & Round( [Akm2] ,2)`
* `"FAC: " & [SRTMFac] &VBNewline& "A, km²: "  & Round( [Akm2] ,2)`
* `"FAC: " & [ALOSFac] &VBNewline& "A, km²: "  & Round( [Akm2] ,2)`

Áreas de aportación por nodo para acumulaciones ASTER
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2LabelASTERStrNode.png)

Áreas de aportación por nodo para acumulaciones SRTM
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2LabelSRTMStrNode.png)

Áreas de aportación por nodo para acumulaciones ALOS
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/ArcGISDesktop10.2.2LabelALOSStrNode.png)


#### Demarcación de drenajes - SRT con otras herramientas

| Herramienta                                                                                                                                | Procedimiento                                                                                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ArcGIS for Desktop / Spatial Analyst Tools](https://desktop.arcgis.com/en/arcmap/latest/tools/spatial-analyst-toolbox/flow-direction.htm) | En ArcToolBox, busque la caja de herramientas _Spatial Analyst Tools / Map Algebra_ y seleccione la herramienta _Raster Calculator_. Ingrese la expresión, p. ej. `Con("ASTERFac.tif">=1062,1)` para grillas ASTER con resolución de 30.68464585 metros y defina el nombre del archivo vectorizado de salida.               |
| [ArcGIS 10.2.2 / Arc Hydro Tools](http://downloads.esri.com/archydro/archydro/Setup/)                                                      | El procedimiento es el mismo presentado en esta actividad a través de HEC-GeoHMS debido a que esta herramienta utiliza Arc Hydro Tools.                                                                                                                                                                                     |
| [ArcGIS Pro / Spatial Analyst](https://pro.arcgis.com/en/pro-app/latest/help/analysis/raster-functions/flow-direction-raster-function.htm) | En el panel _Geoprocessing_, busque la caja de herramientas _Spatial Analyst Tools / Map Algebra_ y seleccione la herramienta _Raster Calculator_. Ingrese la expresión, p. ej. `Con("ASTERFac.tif">=1062,1)` para grillas ASTER con resolución de 30.68464585 metros y defina el nombre del archivo vectorizado de salida. |
| [ArcGIS Pro / Arc Hydro Tools Pro](http://downloads.esri.com/archydro/archydro/setup/Pro/)                                                 | En el panel _Geoprocessing_, busque la caja de herramientas _Arc Hydro Tools Pro / Terrain Preprocessing_ y seleccione la herramienta _Stream Definition_. Seleccione la grilla FAC de entrada, establezca el área de aportación o el número de celdas equivalentes y asigne un nombre a la grilla de salida.               |
| [HEC-HMS](https://www.hec.usace.army.mil/confluence/hmsdocs/hmsum/4.9/geographic-information/gis-menu)                                     | En el panel lateral seleccione en _Basin Models_ el modelo de cuenca creado, luego en el menú _GIS_ seleccione la opción _Identify Streams_ y defina el área de aportación.                                                                                                                                                 |
| [QGIS 3](https://acolita.com/direccion-del-drenaje-en-qgis-3/)                                                                             | En el _Processing Toolbox_ busque el grupo de herramientas _Raster Analysis _ y ejecute _Raster Calculator_ ingresando, p. ej. `if("ASTERFac@1" >= 1062, 1, 0)`.                                                                                                                                                                                            |

Ejemplo de raster calculator sobre QGIS  
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/QGIS3.26.0RasterCalculatorStrDEMASTER.png)

En este momento dispone de grillas de demarcación de drenajes, líneas de drenajes y puntos característicos de la red con el total de celdas convergentes y las áreas de aportación para la posterior lectura de los valores de caudal medio y cálculo de isorendimientos. 


### Referencias

* https://docs.qgis.org/3.22/en/docs/user_manual/processing_algs/qgis/vectorgeneral.html
* https://desktop.arcgis.com/en/arcmap/10.4/tools/spatial-analyst-toolbox/identifying-stream-networks.htm
* https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/identifying-stream-networks.htm
* https://docs.qgis.org/2.8/en/docs/user_manual/working_with_raster/raster_calculator.html


### Compatibilidad

* Se recomienda desarrollar la demarcación de celdas de drenaje con el mismo grupo de herramientas donde desarrollo el reacondicionamiento, p. ej. si la grilla de acumulación fué generada directamente con Arc Hydro Tools Pro de ArcGIS Pro, obtenga las celdas marcadas STR con las mismas herramientas.  
 

### Control de versiones

| Versión    | Descripción                                                                                                                                                                                                                                                                       | Autor                                      | Horas |
|------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|:-----:|
| 2022.07.30 | Finalización documentación versión inicial. Procedimiento demarcación de drenajes - SRT con otras herramientas. Diagrama de procesos.                                                                                                                                             | [rcfdtools](https://github.com/rcfdtools)  |   2   |
| 2022.07.29 | Versión inicial demarcación de drenajes para áreas de aportación de 1km² para acumulaciones de flujo DEM ASTER, SRTM y ALOS. Conversión de celdas a vectores de drenaje y obtención de puntos característicos con lectura de valores acumulados y cálculo de áreas de aportación. | [rcfdtools](https://github.com/rcfdtools)  |   8   |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Anterior](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/FacDEM)  | [:house: Inicio](https://github.com/rcfdtools/R.LTWB/wiki) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/12)  | [Siguiente](https://github.com/rcfdtools/R.LTWB/tree/main/Section03/CNEStation) |
|-----------------------------------------------------------------------------|------------------------------------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------------|
