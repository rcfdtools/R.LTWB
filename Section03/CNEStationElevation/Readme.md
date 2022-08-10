## Análisis y representación de elevaciones en estaciones terrestres
Keywords: `IDEAM` `Weather Station` `Bar graph` `Select By Location` `Chart` `Scatter Plot Matrix` `Definition Query` `Normal distribution` `Statistics` `Extract Multi Values to Points`

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Graph/CNEStationElevation.svg)

Los catálogos de estaciones terrestres contienen el atributo de elevación asociada a cada estación que debe ser validado a partir de los modelos digitales de elevación DEM para su uso posterior en la implementación de métodos de imputación de datos faltantes por relaciones espaciales.                       


### Objetivos

* Obtener las cotas de las estaciones a partir de los modelos satelitales digitales de elevación ASTER, SRTM y ALOS.
* Analizar la correspondencia entre las elevaciones presentadas en el campo `altitud` del IDEAM y las elevaciones obtenidas a partir de modelos satelitales.
* Clasificar las estaciones terrestres por piso térmico a partir de cortes convencionales cada 1000 m.s.n.m y los cortes definidos por Caldas en 1802.
* Estimar la densidad promedio de estaciones por km² y el cubrimiento promedio en km² por estación dentro del área aferente de la zona de estudio y dentro del polígono de la zona hidrográfica 28 correspondiente al Cesar.
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

2. Simbolice las estaciones por colores graduados a partir del campo `altitud` del IDEAM por el método de representación `Intervalo Definido` en 3 clases utilizando tamaños de intervalo cada 1000 m.s.n.m y utilice el esquema de color contínuo `Yellow to Red`. Desde el menú desplegable de más opciones `More`, active la visualización de estadísticos, podrá observar que para las 440 estaciones utilizadas en la zona de estudio, el rango de las elevaciones se encuentra entre 1 y 2700 m.s.n.m con elevaciones medias de 204.98 m.s.n.m y desviación estándar de 328.84 m.s.n.m, lo que indica que mayoritariamente las estaciones utilizadas se encuentran en la zona de llanura para la zona hidrográfica en estudio.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0SimboogyElevationConventional.png)

En el panel de simbología, de clic en la pestaña Histogram, podrá observar las barras o bandas que representan las estacionen en cada clase y la localización del valor promedio.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0SimboogyElevationConventionalHistogram.png)

3. Abra la tabla de atributos de la capa y dando clic derecho en la columna de atributos del campo `altitud`, cree una estadística que incluya un histograma de 12 bandas y muestre la localización de la media, la mediana, la desviación estándar y el gráfico de distribución normal. En esta gráfica podrá analizar que mayoritariamente las estaciones se encuentran en cotas bajas. Seleccione las 6 primeras barras, en el estadístico podrá observar que de las 440 estaciones, 409 se encuentan entre las cotas 1 y 600 m.s.n.m. En el mapa podrá observar las localizaciones de estas estaciones y en la zona del costado derecho podrá observar que por encima de la cota 600 existen pocas estaciones.

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

Desde la tabla de atributos, dando doble clic en la cabecera del campo `DEMALOS`, ordene ascendentemente las elevaciones y luego dando doble clic en el registro de la estación, localice la estación en pantalla acercado a escala 1:5000 que corresponde a _SAN FRANCISCO [15067170]_ y asigne manualmente el valor de la elevación utilizando como referencia la celda más próxima de la grilla ALOS que corresponde a 128 m.s.n.m.

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

> Como puede observar en la tabla anterior, existe una diferencia importante entre el máximo de las elevaciones del IDEAM con respecto al máximo de las elevaciones obtenida a través de los modelo digitales de elevación DEM.

7. En la tabla de contenido, de clic derecho sobre la capa de estaciones CNE_IDEAM_OE_ZE.shp y seleccione la opción _Create Chart / Scatter Plot Matrix_ para crear un gráfico de dispersión para comparar los valores de las diferentes elevaciones obtenidas. En variables seleccione `altitud`, `DEMASTER`, `DEMSRTM` y `DEMALOS`, active la casilla de visualización de línea de tendencia y agregue histogramas en las diagonales. 

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0CreateScatterPlotMatrix.png)

Como puede observar en la siguiente ilustración, existe una alta correspondencia entre los valores de las elevaciones obtenidas a partir de las grilla DEM y dispersión y valores atípicos (outliers) al comparar las elevaciones del IDEAM con las obtenidas satelitalmente.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0ElevationScatterPlotMatrix.png)

En el panel _Matrix Layout_, represente en la esquina superior derecha los valores del parámetro estadístico R². Como puede observar en la gráfica, el coeficiente de determinación entre los datos obtenidos satelitalmente es 1 y entre los datos satelitales vs. los datos IDEAM es de 0.79.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0ElevationScatterPlotMatrixRSquare.png)

> El R-cuadrado es una medida estadística de qué tan cerca están los datos de la línea de regresión ajustada. También se conoce como coeficiente de determinación, o coeficiente de determinación múltiple si se trata de regresión múltiple. [^1]

En el panel _Matrix Layout_, represente en la esquina superior derecha los valores del coeficiente de correlación de Pearson _r_. Como puede observar en la gráfica, el valor de _r_ entre los datos obtenidos satelitalmente es 1 y entre los datos satelitales vs. los datos IDEAM es de 0.89.

> En estadística, el coeficiente de correlación de Pearson es una medida de dependencia lineal entre dos variables aleatorias cuantitativas. A diferencia de la covarianza, la correlación de Pearson es independiente de la escala de medida de las variables. [^2]

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0ElevationScatterPlotMatrixRPearson.png)

8. En el panel _Matrix Layout_, represente en la esquina superior derecha el `Preview Plot` y seleccione en la gráfica la combinación entre altitud del IDEAM y los valores de ALOS. Ahora, manualmente y con ayuda de la tecla <kbd>Ctrl</kbd>, seleccione todas aquellas estaciones que estan muy alejadas de la tendencia lineal mostrada.

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