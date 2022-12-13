## Balance hidrológico distribuido usando SIG
Keywords: `ETR` `Precipitation` `FDR` `Budyko` `Turc` `Dekop` `Raster-calculator` `FAC`

![R.LTWB](Graph/LTWB.png)

Los balances hidrológicos de largo plazo pueden ser realizados en SIG a través de herramientas de acumulación de flujo. Para cada una de las celdas del mapa de direcciones de flujo o FDR, se calcula el número de celdas de drenaje convergentes a las cuales se les puede acumular el valor del potencial de escurrimiento de cada celda obtenido a partir de los valores de precipitación media y evapotranspiración real.

Spatial Analyst Tools de ArcGIS for Desktop y ArcGIS Pro, dispone de un grupo de herramientas de hidrología entre las cuales se encuentra el acumulador de flujo por celdas o Flow Accumulation - FAC; esta herramienta permite a través de un mapa de direcciones de flujo o FDR y una grilla de pesos o valores, realizar no solamente la acumulación de celdas sino además la agregación de una variable adicional que para el caso de la obtención de caudales medios de largo plazo, corresponde al potencial de escurrimiento de cada celda a partir de la diferencia entre los valores de la precipitación media multianual y la evapotranspiración real - ETR.


### Objetivos

* Calcular el potencial de escurrimiento de cada celda del modelo digital de elevación - DEM, a partir de los mapas de precipitación total y evapotranspiración real compuesta y por fenómeno climatológico. Este potencial corresponde a los pesos que serán utilizadas en la acumulación de flujo - FAC.
* Realizar la acumulación de flujo y obtener los balances compuestos y por fenómeno climatológico.


### Requerimientos

* [ArcGIS Pro 2+](https://pro.arcgis.com/en/pro-app/latest/get-started/download-arcgis-pro.htm)
* [ArcGIS for Desktop 10+](https://desktop.arcgis.com/es/desktop/) (opcional)
* [QGIS 3+](https://qgis.org/) (opcional)
* Grilla de direcciones de flujo - FDR. [:mortar_board:Aprender.](../../Section02/FdrDEM)
* Mapas de precipitación total. [:mortar_board:Aprender.](../../Section04/Rain)
* Mapa de evapotranspiración real. [:mortar_board:Aprender.](../../Section04/ETR)


### Procedimiento general

<div align="center">
<br><img alt="R.LTWB" src="Graph/LTWB.svg" width="45%"><br>
<sub>Convenciones generales en diagramas: clases de entidad en azul, dataset en gris oscuro, grillas en color verde, geo-procesos en rojo, procesos automáticos o semiautomáticos en guiones rojos y procesos manuales en amarillo. Líneas conectoras con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>

Para la estimación de caudales medios se realiza un balance hidrológico de largo plazo en cada una de las celdas que cubre la zona de estudio. La siguiente expresión permite determinar el caudal medio en cada celda en el que, al valor estimado de precipitación por celda, se le resta la abstracción correspondiente a la evapotranspiración real. El valor correspondiente al área sobre el cual se estima el caudal corresponde al total de celdas convergentes multiplicadas por el tamaño de cada pixel el cual es definido por la resolución espacial de las grillas utilizadas.

<div align="center">

Qm = (( P – E ) * A) / t

</div>

Donde,

* Qm: caudal medio, m³/s
* P: precipitación, mm/año
* E: evapotranspiración real, mm/año
* A: área de cada celda, m²
* t: tiempo en segundos en un año, (365 dias x 24 horas x 60 minutos x 60 segundos = 31.536.000.000)

1. En ArcGIS Pro, cree un proyecto nuevo en blanco en la ruta _D:\R.LTWB\\.map_ y nómbrelo como _ArcGISProSection05.aprx_. Automáticamente, serán generados el mapa de proyecto, la base de datos geográfica en formato .gdb, la carpeta para volcado de informes de registro de importación _ImportLog_ y la carpeta _Index_. Utilizando el Panel de catálogo y desde la sección Folders, realice la conexión a la carpeta D:\R.LTWB. 

![R.LTWB](Screenshot/ArcGISPro3.0.3NewMapProject.png)

2. Desde la carpeta _.dem_ disponible en el catálogo, agregue al mapa la grilla del modelo digital de elevación - DEM ALOS PALSAR [APFBSRT1MosaicArcGISProZE.tif](../../.dem/ALOS). Modifique la simbología de representación a _Shaded Relief_ con el esquema de color _Black to White_.

![R.LTWB](Screenshot/ArcGISPro3.0.3DEMAlosPalsar.png)

> Tenga en cuenta que automáticamente ha sido asignado el sistema de coordenadas geográficas 9377 de Colombia, correspondiente a MAGNA-SIRGAS Origen-Nacional, debido a que el DEM contiene integrado este sistema.
> 
> Para la correcta interpolación espacial de los parámetros climatológicos, es necesario disponer de un sistema proyectado con unidades lineales en metros.
> 
> Recuerde que el tamaño de celdas en las grillas DEM ALOS PALSAR es de 12.5 metros.

3. Desde la carpeta _HECGeoHMS_ disponible en el catálogo, agregue al proyecto la grilla de direcciones de flujo denominada [ALOSFdr.tif](../../HECGeoHMS/Layers). Modifique la simbología de representación a _Unique Values_ con el esquema de color _Aspect_ y establezca transparencia en 50%.

![R.LTWB](Screenshot/ArcGISPro3.0.3DEMAlosPalsarFDR.png)

Recuerde que las direcciones de flujo en ArcGIS se definen como:

<div align="center">

| Orientación | ArcGIS |
|:-----------:|:------:|
|    Este     |   1    |
|   Sureste   |   2    |
|     Sur     |   4    |
|  Suroeste   |   8    |
|    Oeste    |   16   |
|  Noroeste   |   32   |
|    Norte    |   64   |
|  Nordeste   |  128   |
|  No drena   |  255   |

</div>

4. Desde la carpeta _.grid_ disponible en el catálogo, agregue al proyecto los 4 [Mapas de precipitación total](../../Section04/Rain) creados en la primera actividad de la sección 4 y que fueron nombrados como RainTotalComposite.tif, RainTotalNina.tif, RainTotalNino.tif y RainTotalNeutral.tif. Seleccione los 4 mapas y establezca transparencia del 50%. [:open_file_folder: Descargar archivos](../../.grid).

![R.LTWB](Screenshot/ArcGISPro3.0.3RainGrid.png)

5. Desde la carpeta _.grid_ disponible en el catálogo, agregue al proyecto los 12 [Mapas de evapotranspiración real - ETR](../../Section04/ETR) creados en la última actividad de la sección 4, correspondientes a series compuestas y por fenómeno climatológico usando las expresiones de Budyko, Dekop y Turc. Seleccione los 4 mapas y establezca transparencia del 50%. [:open_file_folder: Descargar archivos](../../.grid).

![R.LTWB](Screenshot/ArcGISPro3.0.3ETRGrid.png)

6. Utilizando la herramienta _Geoprocessing / Raster Calculator_, cree los mapas de potencial escurrimiento o grillas de pesos distribuidos, utilice las siguientes expresiones y nombres de archivo de salida dentro de la carpeta `D:\R.LTWB\.grid`:

| Mapa                       | Expresión Raster Calculator                                                              | Rango mm/año        | Grilla :open_file_folder:                                                                                                                                                                                                                                                              |
|:---------------------------|:-----------------------------------------------------------------------------------------|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RunoffPBudykoComposite.tif | `(("RainTotalComposite.tif"-"ETRBudykoComposite.tif")/1000) *(12.5*12.5)/(365*24*60*60)` | 1.71E-05 - 3.46E-07 | [Part1](../../.grid/RunoffPBudykoComposite.part01.rar), [Part2](../../.grid/RunoffPBudykoComposite.part02.rar), [Part3](../../.grid/RunoffPBudykoComposite.part03.rar), [Part4](../../.grid/RunoffPBudykoComposite.part04.rar), [Part5](../../.grid/RunoffPBudykoComposite.part05.rar) |
| RunoffPBudykoNina.tif      | `(("RainTotalNina.tif"-"ETRBudykoNina.tif")/1000) *(12.5*12.5)/(365*24*60*60)`           | 5.06E-07 - 1.94E-05 | [Part1](../../.grid/RunoffPBudykoNina.part01.rar), [Part2](../../.grid/RunoffPBudykoNina.part02.rar), [Part3](../../.grid/RunoffPBudykoNina.part03.rar), [Part4](../../.grid/RunoffPBudykoNina.part04.rar), [Part5](../../.grid/RunoffPBudykoNina.part05.rar) |
| RunoffPBudykoNino.tif      | `(("RainTotalNino.tif"-"ETRBudykoNino.tif")/1000) *(12.5*12.5)/(365*24*60*60)`           | xxxxxx - xxxxxx     | [Part1](../../.grid/RunoffPBudykoNino.part01.rar), [Part2](../../.grid/RunoffPBudykoNino.part02.rar), [Part3](../../.grid/RunoffPBudykoNino.part03.rar), [Part4](../../.grid/RunoffPBudykoNino.part04.rar), [Part5](../../.grid/RunoffPBudykoNino.part05.rar) |
| RunoffPBudykoNeutral.tif   | `(("RainTotalNeutral.tif"-"ETRBudykoNeutral.tif")/1000) *(12.5*12.5)/(365*24*60*60)`     | xxxxxx - xxxxxx     | [Part1](../../.grid/RunoffPBudykoNeutral.part01.rar), [Part2](../../.grid/RunoffPBudykoNeutral.part02.rar), [Part3](../../.grid/RunoffPBudykoNeutral.part03.rar), [Part4](../../.grid/RunoffPBudykoNeutral.part04.rar), [Part5](../../.grid/RunoffPBudykoNeutral.part05.rar) |

> Recuerde que el tamaño de celdas definido para la creación de los diferentes mapas de parámetros climatológicos fué de 12.5 metros correspondiente al mismo tamaño de celda de los modelos digital de elevación ALOS PALSAR.
> 
> Debido al tamaño de los archivos generados (aproximadamente 1.1 GB por cada grilla), las grillas han sido comprimidas en archivos .rar en partes de 95 MB.

Luego de creados los mapas, modifique la simbología de representación utilizando el esquema de color _Prediction_ y establezca transparencia en 50%.

Potencial de escurrimiento Budyko Compuesto, mm/año
![R.LTWB](Screenshot/ArcGISPro3.0.3RunoffPBudykoComposite.png)

Potencial de escurrimiento Budyko La Niña, mm/año
![R.LTWB](Screenshot/ArcGISPro3.0.3RunoffPBudykoNina.png)

Potencial de escurrimiento Budyko El Niño, mm/año
![R.LTWB](Screenshot/ArcGISPro3.0.3RunoffPBudykoNino.png)

Potencial de escurrimiento Budyko Neutro, mm/año
![R.LTWB](Screenshot/ArcGISPro3.0.3RunoffPBudykoNeutral.png)



En este momento dispone de grillas de evapotranspiración potencial, requeridas para el balance hidrológico de largo plazo.


### Actividades complementarias:pencil2:

En la siguiente tabla se listan las actividades complementarias que deben ser desarrolladas y documentadas por el estudiante en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (mostrar nombre completo, código y enlace a su cuenta de GitHub), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.


| Actividad | Alcance |
|:---------:|:--------|
|     1     | xxx     |
|     2     | xxx     |


### Referencias

* 


### Compatibilidad

* Esta actividad puede ser desarrollada con cualquier software SIG que disponga de herramientas de algebra de mapas.


### Control de versiones

| Versión    | Descripción | Autor                                     | Horas |
|------------|:------------|-------------------------------------------|:-----:|
| 2022.12.13 | xxx         | [rcfdtools](https://github.com/rcfdtools) |   5   |



_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Actividad anterior](../) | [Inicio](../../Readme.md) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/9999) | [Actividad siguiente](../../Section05) |
|---------------------------|---------------------------|--------------------------------------------------------------------------|----------------------------------------|
