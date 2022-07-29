##  Demarcación de drenajes – Stream Definition - STR
Keywords: `STR DEM` `Stream definition` `FAC DEM` `Flow accumulation` `Spatial Analyst Tools` `Arc Hydro Tools` `Display XY Data` `Extract Multi Values to Points`

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/StrDEM/Screenshot/StrDEM.png)

A partir de las grillas de acumulación de flujo, se puede identificar cuáles celdas confluyen hacia cada drenaje; para ello, se especifica el área de aportación p. ej. de 1 o 4 km² o el número equivalente de celdas en función de su resolución y considerando que a menor área de aportación, mayor será el número de corrientes obtenidas. El procedimiento general para la definición de drenajes incluye la creación de una grilla binarizada con celdas a las que se les asigna 1 como valor de pixel.

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
* [Grillas de acumulaciones de Flujo – Flow Direction – FDR. ](https://github.com/rcfdtools/R.LTWB/tree/main/HECGeoHMS/Layers)[:blue_book:Aprender.](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/FacDEM)


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

|    Grilla    | Descargar :open_file_folder:                                                          |
|:------------:|:--------------------------------------------------------------------------------------|
| ASTERStr.tif | [.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ASTERStr.rar)   |
| SRTMStr.tif  | [.rar](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/SRTMStr.rar)    |
| ALOSStr.tif  | [.rar, ](https://github.com/rcfdtools/R.LTWB/blob/main/HECGeoHMS/Layers/ALOSStr.rar)  |

3. Convierta las grillas de demarcación de drenajes a vectores.

> A diferencia de las líneas de drenaje utilizadas para el reacondicionamiento del modelo de terreno a partir de la red de drenaje del IGAC, las líneas de drenaje obtenidas a partir de la marcación de celdas de terrreno, 




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

Los métodos para estimar el tipo de dirección de flujo en ArcGIS Pro son:

| Método | Descripción                                                                                                                                                                                                                                                                                                                                                                             |
|--------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D8     | The D8 flow option models flow direction from each pixel to its steepest downslope neighbor. All of the flow is directed to this steepest neighbor. The output of the D8 direction type is an integer raster whose values range from 1 to 255.                                                                                                                                          |
| MFD    | The Multiple Flow Direction (MFD) algorithm, described by Qin (2007), partitions flow from a pixel to all downslope neighbors. A flow-partition exponent is created from an adaptive approach based on local terrain conditions and is used to determine the fraction of flow draining to each downslope neighbor.                                                                      |
| DINF   | The D-Infinity (DINF) flow method, described by Tarboton (1997), determines flow direction as the steepest downward slope on eight triangular facets formed in a 3x3 pixel window centered on the pixel of interest. Flow direction output is a floating point raster represented as a single angle in degrees, progressing counterclockwise from 0 (due east) to 360 (again due east). |

> La herramienta _Spatial Analyst Tools / Hydrology / Flow Accumulation_ será utilizada en la sección 5 de este curso para la realización del balance hidrológico de largo plazo distribuido debido a que permite incluir una grilla de pesos que corresponderá al potencial de escurrimiento obtenido de la diferencia entre la precipitación y la evaporación.

En este momento dispone de grillas de acumulación de flujo para obtener las celdas de los drenajes sobre los diferentes modelos digitales de elevación.


### Referencias

* https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/flow-accumulation.htm
* https://desktop.arcgis.com/en/arcmap/latest/tools/spatial-analyst-toolbox/flow-accumulation.htm
* https://saga-gis.sourceforge.io/saga_tool_doc/2.2.1/ta_preprocessor_4.html


### Compatibilidad

* Se recomienda desarrollar la acumulación de celdas con el mismo grupo de herramientas donde desarrollo el reacondicionamiento, p. ej. si el AgreeDEM fué generado directamente con Arc Hydro Tools Pro de ArcGIS Pro, obtenga las acumulaciones con las mismas herramientas _Terrain Processing_.  
 

### Control de versiones

| Versión    | Descripción                                                                                                                                                     | Autor                                      | Horas |
|------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|:-----:|
| 2022.07.28 | Versión inicial con acumulaciones de flujo para DEM ASTER, SRTM y ALOS. Puntos de muestreo para lectura de valores acumulados y cálculo de áreas de aportación. | [rcfdtools](https://github.com/rcfdtools)  |   7   |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Anterior](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/FdrDEM)  | [:house: Inicio](https://github.com/rcfdtools/R.LTWB/wiki) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/11) | [Siguiente]() |
|-----------------------------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------------------|---------------|
