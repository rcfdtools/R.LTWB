## Mapa de evapotranspiración real - ETR
Keywords: `ETR` `Cenicafé` `Budyco` `Turc` `Dekop` `Raster-calculator`

![R.LTWB](Graph/ETP.png)

En esta actividad y a partir de los mapas de precipitación total, temperatura y evapotranspiración potencial, generamos los mapas de evapotranspiración real utilizando las ecuaciones de Budyco, Turc y Dekop.


### Objetivos

* Utilizando la expresión de Budyko y a partir del mapa de evapotranspiración potencial obtenido con la ecuación de Cenicafé y de los mapas de precipitación compuesta y por fenómeno climatológico, crear el mapa de evapotranspiración real de la zona de estudio.
* Utilizando la expresión de Dekop y a partir del mapa de evapotranspiración potencial obtenido con la ecuación de Cenicafé y de los mapas de precipitación compuesta y por fenómeno climatológico, crear el mapa de evapotranspiración real de la zona de estudio.
* Utilizando la expresión de Turc y a partir del mapa de temperatura media obtenido con la ecuación de Cenicafé y de los mapas de precipitación compuesta y por fenómeno climatológico, crear el mapa de evapotranspiración real de la zona de estudio.


### Requerimientos

* [ArcGIS Pro 2+](https://pro.arcgis.com/en/pro-app/latest/get-started/download-arcgis-pro.htm)
* [ArcGIS for Desktop 10+](https://desktop.arcgis.com/es/desktop/) (opcional)
* [QGIS 3+](https://qgis.org/) (opcional)
* Mapas de precipitación total. [:mortar_board:Aprender.](../../Section04/Rain)
* Mapas de temperatura media. [:mortar_board:Aprender.](../../Section04/Rain)
* Mapa de evapotranspiración potencial. [:mortar_board:Aprender.](../../Section04/ETP)


### Procedimiento general ETR Budyko

<div align="center">
<br><img alt="R.LTWB" src="Graph/ETRBudyko.svg" width="50%"><br>
<sub>Convenciones generales en diagramas: clases de entidad en azul, dataset en gris oscuro, grillas en color verde, geo-procesos en rojo, procesos automáticos o semiautomáticos en guiones rojos y procesos manuales en amarillo. Líneas conectoras con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>

La expresión de Budyko (1974), permite transformar la evapotranspiración potencial en evapotranspiración real, 

<div align="center">
<br><img alt="R.LTWB" src="Graph/Budyko.png" width="70%"><br><br>
</div>

Donde,
* ETP: evapotranspiración potencial, mm/año
* P: precipitación total, mm/año 

1. En ArcGIS Pro, abra el proyecto _ArcGISProSection04.aprx_ que se encuentra en la ruta _D:\R.LTWB\\.map_ y que fué creado en la primera actividad de la sección 4 de este curso.

![R.LTWB](Screenshot/ArcGISPro3.0.3OpenProject.png)

> Tenga en cuenta que previamente asignamos al mapa el sistema de coordenadas 9377 de Colombia, correspondiente a MAGNA-SIRGAS Origen-Nacional y que en actividades anteriores generamos los mapas de temperatura y precipitación que han sido referenciados con este mismo sistema.

2. Utilizando la herramienta _Geoprocessing / Raster Calculator_, cree los mapas de evapotranspiración real, utilice las siguientes expresiones y nombres de archivo de salida dentro de la carpeta `D:\R.LTWB\.grid`:

| Mapa                   | Expresión Raster Calculator                                                                                                                                                                                               | Rango mm/año     | Grilla                                                                                                                                                                                                         |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ETRBudykoComposite.tif | `SquareRoot(("ETPCenicafe.tif"*"RainTotalComposite.tif"* TanH("RainTotalComposite.tif"/"ETPCenicafe.tif"))* ((1- CosH("ETPCenicafe.tif"/"RainTotalComposite.tif")) +(SinH("ETPCenicafe.tif"/"RainTotalComposite.tif"))))` | 507.01 - 1555.29 | [Part1](../../.grid/ETRBudycoComposite.part01.rar), [Part2](../../.grid/ETRBudycoComposite.part02.rar), [Part3](../../.grid/ETRBudycoComposite.part03.rar), [Part4](../../.grid/ETRBudycoComposite.part04.rar) |
| ETRBudykoNina.tif      | `SquareRoot(("ETPCenicafe.tif"*"RainTotalNina.tif"* TanH("RainTotalNina.tif"/"ETPCenicafe.tif"))* ((1- CosH("ETPCenicafe.tif"/"RainTotalNina.tif")) +(SinH("ETPCenicafe.tif"/"RainTotalNina.tif"))))`                     | 510.62 - 1568.72 | [Part1](../../.grid/ETRBudycoNina.part01.rar), [Part2](../../.grid/ETRBudycoNina.part02.rar), [Part3](../../.grid/ETRBudycoNina.part03.rar), [Part4](../../.grid/ETRBudycoNina.part04.rar)                     |


> Debido al tamaño de los archivos generados (aproximadamente 1.1 GB por cada grilla), las grilla han sido comprimidas en archivos .rar en partes de 95 MB.

Luego de creados los mapas, modifique la simbología de representación utilizando el esquema de color _Plasma_ y establezca transparencia en 50%.

ETR Budyko Compuesto
![R.LTWB](Screenshot/ArcGISPro3.0.3ETRBudykoComposite.png)

ETR Budyko La Niña
![R.LTWB](Screenshot/ArcGISPro3.0.3ETRBudykoNina.png)

ETR Budyko El Niño
![R.LTWB](Screenshot/ArcGISPro3.0.3ETRBudykoNino.png)

ETR Budyko Neutro
![R.LTWB](Screenshot/ArcGISPro3.0.3ETRBudykoNeutro.png)

> Es importante tener en cuenta que los mapas obtenidos corresponden a estimaciones segmentadas por fenómeno climatológico (El Niño, La Niña, Neutro), sin embargo, el mapa de ETR potencial utilizado corresponde a valores compuestos.

















En este momento dispone de la grilla de evapotranspiración potencial, requerida para la generación de los mapas de evapotranspiración real.


### Actividades complementarias:pencil2:

En la siguiente tabla se listan las actividades complementarias que deben ser desarrolladas y documentadas por el estudiante en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (mostrar nombre completo, código y enlace a su cuenta de GitHub), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.


| Actividad | Alcance                                                                                                                                                                                                                                                                                                  |
|:---------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1     | Investigue y documente otras ecuaciones regionales a partir de las cuales se puedan construir mapas de evapotranspiración real.                                                                                                                                                                          |
|     2     | A partir de las ecuaciones regionales investigadas, cree los mapas de evapotranspiración real y con algebra de mapas realice el análisis de diferencias respecto a los mapas obtenidos en esta actividad. Evalúe e implemente en su caso de estudio, los mapas que mejor representen su zona de estudio. |


### Referencias

* http://julianrojo.weebly.com/uploads/1/2/0/0/12008328/metodos_estimacion_de_et.pdf
* https://hess.copernicus.org/articles/23/4983/2019/


### Compatibilidad

* Esta actividad puede ser desarrollada con cualquier software SIG que disponga de herramientas de algebra de mapas.


### Control de versiones

| Versión    | Descripción                                                                            | Autor                                     | Horas |
|------------|:---------------------------------------------------------------------------------------|-------------------------------------------|:-----:|
| 2022.12.10 | Revisión general de ecuaciones y definición de expresiones para la calculadora ráster. | [rcfdtools](https://github.com/rcfdtools) |   1   |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Actividad anterior](../Temperature) | [Inicio](../../Readme.md) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/30) | [Actividad siguiente]()  |
|--------------------------------------|---------------------------|------------------------------------------------------------------------|--------------------------|

[^1]: http://julianrojo.weebly.com/uploads/1/2/0/0/12008328/metodos_estimacion_de_et.pdf