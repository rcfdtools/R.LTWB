## Análisis y representación de elevaciones en estaciones terrestres
Keywords: `IDEAM` `Weather Station` `Bar graph` `Select By Location` `Scatter plot` `Definition Query` `Normal distribution` `Statistics` `Extract Multi Values to Points`

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Graph/CNEStation.png)

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

6. Para cada uno de los campos de atributos `DEMASTER`, `DEMSRTM` y `DEMALOS`, genere una estadística y evalue los rangos de valores.


![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0StationASTERStatistic.png)





### Actividades complementarias:pencil2:

En la siguiente tabla se listan las actividades complementarias que deben ser desarrolladas y documentadas por el estudiante en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (mostrar nombre completo, código y enlace a su cuenta de GitHub), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.

| Actividad | Alcance                                                                                                                      |
|:---------:|:-----------------------------------------------------------------------------------------------------------------------------|
|     1     | Realice el procedimiento presentado en esta clase en ArcGIS for Desktop y en QGIS para las estaciones de la zona de estudio. | 
|     2     | Realice el procedimiento presentado en esta clase en ArcGIS Pro para las estaciones del área continental de Colombia.        | 
 

### Referencias

* http://dhime.ideam.gov.co/atencionciudadano/
* http://www.ideam.gov.co/solicitud-de-informacion
* [ArcGIS Pro tarda mucho tiempo en abrir mi proyecto](https://github.com/rcfdtools/R.LTWB/discussions/13):lady_beetle:


### Control de versiones

| Versión    | Descripción         | Autor                                      | Horas |
|------------|:--------------------|--------------------------------------------|:-----:|
| 2022.08.10 | Versión inicial.    | [rcfdtools](https://github.com/rcfdtools)  |       |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Anterior](https://github.com/rcfdtools/R.LTWB/tree/main/Section03/CNEStation) | [:house: Inicio](https://github.com/rcfdtools/R.LTWB/wiki) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/999) | [Siguiente]() |
|--------------------------------------------------------------------------------|------------------------------------------------------------|-------------------------------------------------------------------------|---------------|

[^1]: http://dhime.ideam.gov.co/atencionciudadano/
[^2]: https://pro.arcgis.com/en/pro-app/latest/help/data/excel/prepare-to-work-with-excel-in-arcgis-pro.htm