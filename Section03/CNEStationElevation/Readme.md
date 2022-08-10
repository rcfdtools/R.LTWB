## Análisis, representación de elevaciones y densidad de estaciones terrestres
Keywords: `IDEAM` `Weather Station` `Bar graph` `Select By Location` `Chart` `Scatter Plot Matrix` `Definition Query` `Normal distribution` `Statistics` `Extract Multi Values to Points` `Calculate Geometry Attributes` `Calculate Fields`

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Graph/CNEStationElevation.svg)

Los catálogos de estaciones terrestres contienen el atributo de elevación asociada a cada estación que debe ser validado a partir de los modelos digitales de elevación DEM para su uso posterior en la implementación de métodos de imputación de datos faltantes por relaciones espaciales.                       


### Objetivos

* Obtener las cotas de las estaciones a partir de los modelos satelitales digitales de elevación ASTER, SRTM y ALOS.
* Analizar la correspondencia entre las elevaciones presentadas en el campo `altitud` del IDEAM y las elevaciones obtenidas a partir de modelos satelitales.
* Utilizando Python, clasificar las estaciones terrestres por piso térmico a partir de cortes convencionales cada 1000 m.s.n.m y los cortes definidos por Caldas en 1802.
* Estimar la densidad promedio de estaciones por km² y el cubrimiento promedio en km² por estación dentro del área aferente de la zona de estudio y dentro del polígono de la zona hidrográfica 28 correspondientes al Cesar.
* Definir las elevaciones de las estaciones que posteriormente se utilizarán como referencia en los algoritmos de imputación o completado de datos faltantes a partir de relaciones geográficas. 


### Requerimientos

* [ArcGIS Pro 2+](https://pro.arcgis.com/en/pro-app/latest/get-started/download-arcgis-pro.htm)
* [ArcGIS for Desktop 10+](https://desktop.arcgis.com/es/desktop/) (opcional)
* [QGIS 3+](https://qgis.org/) (opcional)
* [Polígono que delimita la zona de estudio. ](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudio.zip)[:mortar_board:Aprender.](https://github.com/rcfdtools/R.LTWB/tree/main/Section01/CaseStudy)
* [Polígono envolvente aferente que delimita la zona de estudio. ](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudioBufferStation.zip)[:mortar_board:Aprender.](https://github.com/rcfdtools/R.LTWB/tree/main/Section03/CNEStation)
* [Capa integrada de estaciones terrestres del IDEAM y otras entidades de la zona de estudio. ](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/CNE_IDEAM_OE_ZE.zip)[:mortar_board:Aprender.](https://github.com/rcfdtools/R.LTWB/tree/main/Section03/CNEStation)
* Modelo digital de elevación ASTER GDEM 30m. [:mortar_board:Aprender.](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/DEMAster)
* Modelo digital de elevación SRTM 30m. [:mortar_board:Aprender.](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/DEMSrtm)
* Modelo digital de elevación ALOS PALSAR 12.5m. [:mortar_board:Aprender.](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/DEMAlos)
* :open_file_folder: [Descargar mosaicos grillas DEM](https://github.com/rcfdtools/R.LTWB/tree/main/.dem).


### Diagrama general de procesos

El siguiente diagrama representa los procedimientos generales requeridos para el desarrollo de esta actividad.

<div align="center">
<br><img alt="R.LTWB" src="https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Graph/CNEStationFlowchart.svg" width="65%"><br>
<sub>Convenciones generales en diagramas: clases de entidad en azul, dataset en gris oscuro, grillas en color verde, geo-procesos en rojo y procesos manuales en amarillo. Líneas con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>


### Arreglos de datos para clasificación de estaciones por pisos térmicos


#### Cortes convencionales

| Valor de corte | Etiqueta                        |
|:---------------|:--------------------------------|
| 1000           | Cálido, 24°C+, <= 1000 meters   |
| 2000           | Templado, 18°C+, <= 2000 meters |
| 3000           | Frío, 12°C+, <= 3000 meters     |
| 4000           | Páramo, 0°C, <= 4000 meters     |
| 99999          | Glacial, 0°C-, > 4000 meters    |


#### Cortes Francisco José de Caldas, año 1802

| Valor de corte | Etiqueta                                    |
|:---------------|:--------------------------------------------|
| 800            | Cálido, T>=24°C, <=800meter                 |
| 1800           | Templado, 24°C>T>18°C, <=1800meter          |
| 2800           | Frío, 18°C>T>12°C, <=2800meter              |
| 3700           | Muy Frío, 12°C>T>6°C, <=3700meter           |
| 4700           | Extremadamente Frio, 6°C>T>0°C, <=4700meter |
| 99999          | Nival, T<0°C, >4700meter                    |


### Procedimiento general

1. En ArcGIS Pro, abra el mapa _D:\R.LTWB\.map\ArcGISProSection03.aprx_ creado en la actividad de [selección de estaciones para la zona de estudio](https://github.com/rcfdtools/R.LTWB/tree/main/Section03/CNEStation) que contiene las estaciones integradas y los polígonos de la zona de estudio y su zona aferente. En caso de que este generando un proyecto nuevo, cargue directamente los archivos de formas geométricas [CNE_IDEAM_OE_ZE.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/CNE_IDEAM_OE_ZE.zip), [ZonaEstudio.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudio.zip) y [ZonaEstudioBufferStation.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudioBufferStation.zip). 

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0MapProject.png)

2. Simbolice las estaciones por colores graduados a partir del campo `altitud` del IDEAM por el método de representación `Intervalo Definido` en 3 clases utilizando tamaños de intervalo cada 1000 m.s.n.m y utilice el esquema de color continuo `Yellow to Red`. Desde el menú desplegable de más opciones `More`, active la visualización de estadísticos, podrá observar que para las 440 estaciones utilizadas en la zona de estudio, el rango de las elevaciones se encuentra entre 1 y 2700 m.s.n.m con elevaciones medias de 204.98 m.s.n.m y desviación estándar de 328.84 m.s.n.m, lo que indica que mayoritariamente las estaciones utilizadas se encuentran en la zona de llanura para la zona hidrográfica en estudio.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0SimboogyElevationConventional.png)

En el panel de simbología, de clic en la pestaña Histogram, podrá observar las barras o bandas que representan las estacionen en cada clase y la localización del valor promedio.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0SimboogyElevationConventionalHistogram.png)

3. Abra la tabla de atributos de la capa y dando clic derecho en la columna de atributos del campo `altitud`, cree una estadística que incluya un histograma de 12 bandas y muestre la localización de la media, la mediana, la desviación estándar y el gráfico de distribución normal. En esta gráfica podrá analizar que mayoritariamente las estaciones se encuentran en cotas bajas. Seleccione las 6 primeras barras, en el estadístico podrá observar que de las 440 estaciones, 409 se encuentran entre las cotas 1 y 600 m.s.n.m. En el mapa podrá observar las localizaciones de estas estaciones y en la zona del costado derecho podrá observar que por encima de la cota 600 existen pocas estaciones.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0SimboogyElevationConventionalStatistic.png)

4. Cargue al proyecto los modelos digitales de elevación ASTER (ASTGTMV003Mosaic.tif), SRTM (SRTMV003MosaicArcGISPro.tif) y ALOS (APFBSRT1MosaicArcGISPro.tif), represente estos modelos por relieve sombreado utilizando el esquema de color contínuo de negro a blanco.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0DEMShadedRelief.png)

5. Utilizando la herramienta _Geoprocessing / Spatial Analyst Tools / Extraction / Extract Multi Values to Points_, obtenga simultáneamente los valores de elevación de los 3 modelos digitales de elevación. Nombre los campos de atributos de salida como `DEMASTER`, `DEMSRTM` y `DEMALOS`. 

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0ExtractMultiValuesToPoints.png)

> El procedimiento anterior puede ser desarrollado manualmente para cada DEM a través de la herramienta Zonal Statistics As Table.

6. Para cada uno de los campos de atributos `DEMASTER`, `DEMSRTM` y `DEMALOS`, genere estadísticas detalladas y evalue los rangos de valores.

Las elevaciones de las estaciones obtenidas a partir del DEM ASTER, presentan valores entre 5 y 2567 m.s.n.m. con media en 214.7 m.s.n.m. y desviación estándar de 358.2 m.s.n.m. Seleccionando las 3 primeras bandas, podrá observar que de las 440 estaciones, 405 se encuentran entre 5 y 627 m.s.n.m. 
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0StationASTERStatistic.png)

Las elevaciones de las estaciones obtenidas a partir del DEM SRTM, presentan valores entre 0 y 2564 m.s.n.m. con media en 216.6 m.s.n.m. y desviación estándar de 357.4 m.s.n.m. Seleccionando las 3 primeras bandas, podrá observar que de las 440 estaciones, 405 se encuentran entre 0 y 636 m.s.n.m. 
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0StationSRTMStatistic.png)

Las elevaciones preliminares de las estaciones obtenidas a partir del DEM ALOS, presentan valores entre -9999 y 2568 m.s.n.m. con media en 192.1 m.s.n.m. y desviación estándar de 604.4 m.s.n.m. Como observa en la gráfica, 1 de las estaciones ha obtenido un valor de -9999 que indica que no se ha podido obtener la elevación a partir del DEM. 
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0StationALOSStatistic.png)

Desde la tabla de atributos, dando doble clic en la cabecera del campo `DEMALOS`, ordene ascendentemente las elevaciones y luego dando doble clic en el registro de la estación, localice la estación en pantalla acercando a escala 1:5000 que corresponde a _SAN FRANCISCO [15067170]_ y asigne manualmente el valor de la elevación utilizando como referencia la celda más próxima de la grilla ALOS que corresponde a 128 m.s.n.m.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0StationALOSStationManualValue.png)

Vuelva a la estadística de campo. Las elevaciones preliminares de las estaciones obtenidas a partir del DEM ALOS asignando manualmente la elevación a una de las estaciones, presentan valores entre -6 y 2568 m.s.n.m. con media en 215.2 m.s.n.m. y desviación estándar de 358.1 m.s.n.m. Seleccionando las 3 primeras bandas, podrá observar que de las 440 estaciones, 404 se encuentran entre 0 y 602 m.s.n.m. 
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0StationALOSStatisticFixed.png)

Tabla resumen de valores obtenidos de elevación.  

| Estadístico | IDEAM | ASTER | SRTM  | ALOS  |
|-------------|-------|-------|-------|-------|
| Mean        | 205   | 214.7 | 216.6 | 215.2 |
| Median      | 100   | 95    | 97    | 97    |
| STD. Dev.   | 329.2 | 358.2 | 357.4 | 358.1 |
| Rows        | 440   | 440   | 440   | 440   |
| Count       | 440   | 440   | 440   | 440   |
| Nulls       | 0     | 0     | 0     | 0     |
| Min         | 1     | 5     | 0     | -6    |
| Max         | 2700  | 2567  | 2564  | 2568  |
| Skewness    | 3.56  | 3.4   | 3.4   | 3.4   |
| Kurtosis    | 18.5  | 16.2  | 16.3  | 16.3  |

> Como puede observar en la tabla anterior, existe una diferencia importante entre el máximo de las elevaciones del IDEAM con respecto al máximo de las elevaciones obtenidas a través de los modelos digitales de elevación DEM.
> 
> Tenga en cuenta que las elevaciones han sido obtenidas en las localizaciones disponibles de la red de estaciones del catálogo nacional y estas localizaciones pueden ser imprecisas.

7. En la tabla de contenido, de clic derecho sobre la capa de estaciones CNE_IDEAM_OE_ZE.shp y seleccione la opción _Create Chart / Scatter Plot Matrix_ para crear un gráfico de dispersión para comparar los valores de las diferentes elevaciones obtenidas. En variables seleccione `altitud`, `DEMASTER`, `DEMSRTM` y `DEMALOS`, active la casilla de visualización de línea de tendencia y agregue histogramas en las diagonales. 

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0CreateScatterPlotMatrix.png)

Como puede observar en la siguiente ilustración, existe una alta correspondencia entre los valores de las elevaciones obtenidas a partir de las grillas DEM y dispersión y valores atípicos (outliers) al comparar las elevaciones del IDEAM con las obtenidas satelitalmente.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0ElevationScatterPlotMatrix.png)

En el panel _Matrix Layout_, represente en la esquina superior derecha los valores del parámetro estadístico R². Como puede observar en la gráfica, el coeficiente de determinación entre los datos obtenidos satelitalmente es 1 y entre los datos satelitales vs. los datos IDEAM es de 0.79.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0ElevationScatterPlotMatrixRSquare.png)

> El R-cuadrado es una medida estadística de qué tan cerca están los datos de la línea de regresión ajustada. También se conoce como coeficiente de determinación, o coeficiente de determinación múltiple si se trata de regresión múltiple. [^1]

En el panel _Matrix Layout_, represente en la esquina superior derecha los valores del coeficiente de correlación de Pearson _r_. Como puede observar en la gráfica, el valor de _r_ entre los datos obtenidos satelitalmente es 1 y entre los datos satelitales vs. los datos IDEAM es de 0.89.

> En estadística, el coeficiente de correlación de Pearson es una medida de dependencia lineal entre dos variables aleatorias cuantitativas. A diferencia de la covarianza, la correlación de Pearson es independiente de la escala de medida de las variables. [^2]

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0ElevationScatterPlotMatrixRPearson.png)

8. En el panel _Matrix Layout_, represente en la esquina superior derecha el `Preview Plot` y seleccione en la gráfica la combinación entre altitud del IDEAM y los valores de ALOS. Ahora, manualmente y con ayuda de la tecla <kbd>Ctrl</kbd>, seleccione todas aquellas estaciones que están muy alejadas de la tendencia lineal mostrada.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0ElevationScatterPlotMatrixOutliers.png)

9. Abra la tabla de atributos, filtre las estaciones seleccionadas y realice visualmente un análisis de las diferencias entre los valores de elevación registrados en el IDEAM vs. los obtenidos a partir de los DEM. Podrá observar que todas estas estaciones presentan una gran diferencia de elevación y que los valores reportados por el IDEAM no corresponden a elevaciones homogéneas comparando con los datos obtenidos satelitalmente.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0ElevationScatterPlotMatrixOutliersTable.png)

> Para el desarrollo del caso de estudio utilizaremos las elevaciones obtenidas a través del modelo digital de elevación ALOS PALSAR, lo anterior debido a que este modelo contiene mediciones cada 12.5m.  

10. Para la clasificación por pisos térmicos, crear en la tabla de atributos del archivo de formas _CNE_IDEAM_OE_ZE.shp_ los siguientes campos de atributos:

| Field      | Tipo     | Descripción                                                                         |
|------------|----------|-------------------------------------------------------------------------------------|
| TherLCv    | Float    | Rango de elevación según la clasificación convencional con cortes cada 1000 m.s.n.m |
| TherLCvTxt | Text 100 | Etiqueta del rango de elevación según la clasificación convencional                 |
| TherLCl    | Float    | Rango de elevación según la clasificación Caldas con cortes variable                |
| TherLClTxt | Text 100 | Etiqueta del rango de elevación según la clasificación Caldas                       |

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0AddField.png)

11. Utilizando _Calculate Field_ desde la cabecera de los campos de atributos y utilizando el siguiente script en Python, calcule el rango de elevación al cual pertenece cada estación y su etiqueta de datos a partir de las elevaciones obtenidas del modelo digital de elevación ALOS PALSAR.

Pre-Logic Script Code para Python 2 sobre ArcGIS for Desktop y Python 3 sobre ArcGIS Pro:
```
# -*- coding: UTF-8 -*-
# Parameters
thermal_level_caldas = False  # True for Caldas classification, False for conventional classification range
thermal_level_ref_conv = [[1000,'Cálido, 24°C+, <= 1000 meters'],
                          [2000,'Templado, 18°C+, <= 2000 meters'],
                          [3000,'Frío, 12°C+, <= 3000 meters'],
                          [4000,'Páramo, 0°C, <= 4000 meters'],
                          [99999,'Glacial, 0°C-, > 4000 meters']] # Elevation value in meters
thermal_level_ref_caldas = [[800,'Cálido, T>=24°C, <=800meter'],
                            [1800,'Templado, 24°C>T>18°C, <=1800meter'],
                            [2800,'Frío, 18°C>T>12°C, <=2800meter'],
                            [3700,'Muy Frío, 12°C>T>6°C, <=3700meter'],
                            [4700,'Extremadamente Frio, 6°C>T>0°C, <=4700meter'],
                            [99999,'Nival, T<0°C, >4700meter']] # Elevation value in meters

# Thermal level system
if thermal_level_caldas == True:
    thermal_level_ref = thermal_level_ref_caldas
else:
    thermal_level_ref = thermal_level_ref_conv

def thermal_level_f(elevation):
    for i in thermal_level_ref[:]:
        if elevation <= i[0]:
            return i[0],i[1]
```

> Para utilizar la clasificación convencional definir `thermal_level_caldas = False` y para la clasificación Caldas definir `thermal_level_caldas = True`

Para calcular cada uno de los campos utilizar:

| Field      | Llamado de función            | thermal_level_caldas |
|------------|-------------------------------|----------------------|
| TherLCv    | thermal_level_f(!DEMALOS!)[0] | False                |
| TherLCvTxt | thermal_level_f(!DEMALOS!)[1] | False                |
| TherLCl    | thermal_level_f(!DEMALOS!)[0] | True                 |
| TherLClTxt | thermal_level_f(!DEMALOS!)[1] | True                 |

Ejemplo de cálculo para TherLCv:  
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0CalculateFieldTherLCv.png)

Realice el cálculo de los demás campos y verifique la tabla de atributos.
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0CalculateFieldThermalLevelTable.png)

Simbolice las estaciones por valores únicos a partir del campo de atributos `TherLCl` de la clasificación numérica Caldas.
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0SimbologyUniqueValueTherLCv.png)

Desde la simbología de representación por valores únicos para los campos de atributos TherLCv y TherLCl, obtenga el total de estaciones para cada rango utilizando la opción _More / Show Count_. 

Resultados para cortes convencionales

| Valor de corte | Etiqueta                        | Estaciones |
|:---------------|:--------------------------------|------------|
| 1000           | Cálido, 24°C+, <= 1000 meters   | 416        |
| 2000           | Templado, 18°C+, <= 2000 meters | 20         |
| 3000           | Frío, 12°C+, <= 3000 meters     | 4          |
| 4000           | Páramo, 0°C, <= 4000 meters     | 0          |
| 99999          | Glacial, 0°C-, > 4000 meters    | 0          |

Resultados para cortes Francisco José de Caldas, año 1802

| Valor de corte | Etiqueta                                    | Estaciones |
|:---------------|:--------------------------------------------|------------|
| 800            | Cálido, T>=24°C, <=800meter                 | 411        |
| 1800           | Templado, 24°C>T>18°C, <=1800meter          | 24         |
| 2800           | Frío, 18°C>T>12°C, <=2800meter              | 5          |
| 3700           | Muy Frío, 12°C>T>6°C, <=3700meter           | 0          |
| 4700           | Extremadamente Frio, 6°C>T>0°C, <=4700meter | 0          |
| 99999          | Nival, T<0°C, >4700meter                    | 0          |

Como observa en las gráficas y tablas anteriores, las estaciones de la zona de estudio se encuentran predominantemente en el piso térmico Cálido y algunas de ellas se encuentran en el piso térmico templado y muy pocas en el piso térmico frío sobre la cordillera oriental de Colombia. 


### Análisis de densidad y cobertura

Para estimar la densidad promedio de estaciones por km² y el cubrimiento promedio en km² por estación dentro del área aferente de la zona de estudio y dentro del polígono de la zona hidrográfica 28 correspondientes al Cesar para todas las estaciones y para las estaciones asociadas a cada uno de los parámetros climatológicos, siga este procedimiento:

1. Utilizando la herramienta _Geoprocessing / Data Management Tools / Calculate Geometry Attributes_, calcule el área espacial y el perímetro del polígono de aferencia _ZonaEstudioBufferStation.shp_, utilice el sistema de proyección de coordenadas _MAGNA_Colombia_CTM12_. Para el polígono de aferencia el área espacial es 48740.36 km².

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0CalculateGeometryAttributes.png)

2. En la tabla de atributos del polígono aferente, cree los siguientes atributos:

| Field      | Tipo   | Descripción                                                                                                                                                                                          |
|------------|--------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Stations   | Long   | Número de estaciones seleccionadas en la zona de estudio (440 estaciones)                                                                                                                            |
| StatnsRain | Long   | Número de estaciones seleccionadas en la zona de estudio para obtención de datos de precipitación con longitud hipotética de series igual o superior a 10 años (139 estaciones )                     |
| StatnsTemp | Long   | Número de estaciones seleccionadas en la zona de estudio para obtención de datos de temperatura del aire cerca del suelo con longitud hipotética de series igual o superior a 5 años (42 estaciones) |
| StatnsEvap | Long   | Número de estaciones seleccionadas en la zona de estudio para obtención de datos de evaporación potencial con longitud hipotética de series igual o superior a 5 años (41 estaciones)                |
| DnStations | Double | Densidad en estaciones por km² para toda la zona de estudio                                                                                                                                          |
| DnStRain   | Double | Densidad en estaciones por km² para obtención de datos de precipitación                                                                                                                              |
| DnStTemp   | Double | Densidad en estaciones por km² para obtención de datos de temperatura del aire cerca del suelo                                                                                                       |
| DnStEvap   | Double | Densidad en estaciones por km² para obtención de datos de evaporación potencial                                                                                                                      |

> El número de estaciones seleccionadas ha sido obtenido en la actividad: [Catálogo nacional de estaciones - CNE y selección para la zona de estudio](https://github.com/rcfdtools/R.LTWB/tree/main/Section03/CNEStation)
>
> Para las estaciones registradoras de nivel de lámina de agua, no se presenta un análisis de densidad debido a que su localización se realiza sobre puntos de interés particulares sobre una corriente de agua y no bajo criterios de densidad espacial.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0AddFieldDensity.png)

3. En la tabla de atributos, asigne el número de estaciones en los campos `Stations=440`, `StatnsRain=139`, `StatnsTemp=42` y `StatnsEvap=41`. 

4. Utilizando la herramienta _Calculate Field_ disponible en la cabecera de cada campo de atributos, calcule las densidades de los campos DnStations, DnStRain, DnStTemp y DnStEvap con la siguiente expresión:

<div align="center">

D = n / A

</div>

donde,  
D: densidad en estaciones / km²  
n: número de estaciones  
A: área en km²  

Manualmente, calcule la cobertura geográfica de cada estación con la expresión:

<div align="center">

C = 1 / D

</div>

donde,  
C: cobertura de área en km² por cada estación  
D: densidad en estaciones / km²  

Manualmente, calcule el radio de acción promedio en km de cada estación utilizando la siguiente expresión:

<div align="center">

r = √ ( A / π)

</div>

donde,  
r: radio de acción en km  
A: área de cobertura en km² de cada estación  
π: número de Pi. 3.1415926535897932384626433832795  

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0CalculateFieldDensity.png)

Valores de densidad y cobertura obtenidos

| Atributo   | Descripción                                                                                    | D, Estn/km²       | Cobertura, km²/Estn | Radio de acción, km |  
|------------|:-----------------------------------------------------------------------------------------------|-------------------|---------------------|---------------------|
| DnStations | Densidad en estaciones por km² para toda la zona de estudio                                    | 0.00902742680521  | 110.77              | 5.94                |
| DnStRain   | Densidad en estaciones por km² para obtención de datos de precipitación                        | 0.002852          | 350.63              | 10.57               |
| DnStTemp   | Densidad en estaciones por km² para obtención de datos de temperatura del aire cerca del suelo | 0.000861708922316 | 1160.49             | 19.22               |
| DnStEvap   | Densidad en estaciones por km² para obtención de datos de evaporación potencial                | 0.000841          | 1189.06             | 19.46               |

Como observa en la tabla, los valores de densidad corresponden a valores inferiores a 1e-3 lo cual dimensionalmente no permite obtener un indicio claro de sí el número de estaciones es suficiente para realizar un análisis espacial adecuado de los diferentes parámetros climatológicos, por otra parte, la cobertura es un indicado significativo a partir del cual se puede deducir que para la red completa de estaciones seleccionada, la cobertura en km² por cada estación es de 110.77 que visualmente en el mapa de localización corresponde a un área de cubrimiento significativamente grande. Para los parámetros climáticos particulares, las coberturas de cada estación son mucho mayores y de hasta 1189.06 km²/estación, lo que indica que respecto a la red completa su densidad es aproximadamente 10 veces menos. En el caso de los radios de acción, los valores obtenidos se ajustan a los lineamientos establecidos por la [Organización Meteorológica Munidal - OMM](https://public.wmo.int/es) que para datos puviométricos recomienda que el radio de acción sea de al menos 12.5 km y para las estaciones seleccionadas el valor obtenido es 10.57 km, con respecto a los datos de temperatura y evaporación correspondientes principalmente a estaciones climatológicas ordinarias, la recomendación de la OMM es de un radio de 25 km y para las estaciones de la zona de estudio el mayor valor obtenido para estos parámetros es de 19.46 km.

De acuerdo a la WMO, para las estaciones:

* Climatológica principal y Agro-meteorológica (CP-AM), la distancia media recomendada entre estaciones es de 150km para un radio de acción de 75km.
* Climatológica ordinaria (CO - AU), la distancia media recomendada entre estaciones es de 50km para un radio de acción de 25km.
* Meteorológica especial (ME) y Pluviométrica (PM - PG), la distancia media recomendada entre estaciones es de 25km para un radio de acción de 12.5km.

A partir de este momento, ya dispone de la red de estaciones de la zona de estudio con diferentes elevaciones y su clasificación por diferentes pisos térmicos.


### Actividades complementarias:pencil2:

En la siguiente tabla se listan las actividades complementarias que deben ser desarrolladas y documentadas por el estudiante en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (mostrar nombre completo, código y enlace a su cuenta de GitHub), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.

| Actividad | Alcance                                                                                                                                              |
|:---------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------|
|     1     | Realice el procedimiento presentado en esta clase en ArcGIS for Desktop y en QGIS para las estaciones de la zona de estudio.                         | 
|     2     | Investigue y documente otros métodos de clasificación por nivel térmico que se apliquen en otros países diferentes a los citados en las referencias. | 
 

### Referencias

* [IDEAM Colombia - Clasificación de los climas (clima-text.pdf)](http://atlas.ideam.gov.co/basefiles/clima-text.pdf)
* [IDEAM Colombia - Clasificación climática de Caldas](http://www.ideam.gov.co/documents/10182/599272/Clasificacion+Climatica+de+Caldas+2014.pdf/d4ffa383-e60b-4ec5-8aa2-1b553d23b44f?version=1.0)
* [Pisos térmicos en Costa Rica](https://www.mep.go.cr/sites/default/files/recursos/recursos-interactivos/clima_tiempo/pdf/pisos_termicos.pdf)
* [Diseño de la red hidrometeorológica nacional IDEAM - Colombia](http://sgi.ideam.gov.co/documents/412030/561097/M-GDI-H-G001+GU%C3%8DA+DISE%C3%91O+DE+LA+RED+HIDROMETEOROL%C3%93GICA+NACIONAL.pdf/9da0e118-58cc-43eb-87e0-8c6316dc691c?version=1.0)
* [Propuesta Metodológica para el Rediseño de una Red Meteorológica en un Sector de la Región Andina Colombiana](https://hemeroteca.unad.edu.co/index.php/publicaciones-e-investigacion/article/view/1281/2031)
* [ArcGIS Pro tarda mucho tiempo en abrir mi proyecto](https://github.com/rcfdtools/R.LTWB/discussions/13):lady_beetle:


### Control de versiones

| Versión    | Descripción         | Autor                                      | Horas |
|------------|:--------------------|--------------------------------------------|:-----:|
| 2022.08.10 | Versión inicial.    | [rcfdtools](https://github.com/rcfdtools)  |       |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Anterior](https://github.com/rcfdtools/R.LTWB/tree/main/Section03/CNEStation) | [:house: Inicio](https://github.com/rcfdtools/R.LTWB/wiki) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/999) | [Siguiente]() |
|--------------------------------------------------------------------------------|------------------------------------------------------------|-------------------------------------------------------------------------|---------------|

[^1]: https://blog.minitab.com/es/analisis-de-regresion-como-puedo-interpretar-el-r-cuadrado-y-evaluar-la-bondad-de-ajuste#:~:text=El%20R%2Dcuadrado%20es%20una,se%20trata%20de%20regresi%C3%B3n%20m%C3%BAltiple.
[^2]: https://es.wikipedia.org/wiki/Coeficiente_de_correlaci%C3%B3n_de_Pearson