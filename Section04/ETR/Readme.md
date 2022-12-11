## Mapa de evapotranspiración real - ETR
Keywords: `ETR` `Cenicafé` `Budyco` `Turc` `Dekop` `Raster-calculator`

![R.LTWB](Graph/ETP.png)

En esta actividad se presentan diferentes metodologías para la obtención de mapas de evapotranspiración real a partir de métodos de regionalización como Budyco, Turc y Dekop.


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
<br><img alt="R.LTWB" src="Graph/ETRBudyko.svg" width="70%"><br>
<sub>Convenciones generales en diagramas: clases de entidad en azul, dataset en gris oscuro, grillas en color verde, geo-procesos en rojo, procesos automáticos o semiautomáticos en guiones rojos y procesos manuales en amarillo. Líneas conectoras con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>


<div align="center">
<br><img alt="R.LTWB" src="Graph/Budyko.svg" width="70%"><br><br>
</div>




1. En ArcGIS Pro, abra el proyecto _ArcGISProSection04.aprx_ que se encuentra en la ruta _D:\R.LTWB\\.map_ y que fué creado en la primera actividad de la sección 4 de este curso.

![R.LTWB](Screenshot/ArcGISPro3.0.3OpenProject.png)

> Tenga en cuenta que previamente asignamos al mapa el sistema de coordenadas 9377 de Colombia, correspondiente a MAGNA-SIRGAS Origen-Nacional y que en la actividad anterior agregamos al proyecto el modelo digital de elevación ALOS PALSAR que ha sido referenciado con este mismo sistema.

2. Utilizando la herramienta _Geoprocessing / Raster Calculator_, cree el mapa de evapotranspiración potencial a partir del modelo digital de elevación ALOS PALSAR, utilice la siguiente expresión y nombre de archivo de salida dentro de la carpeta `D:\R.LTWB\.grid`:

* Expresión Raster Calculator: `1700.17*Exp((-0.0002*"APFBSRT1MosaicArcGISProZE.tif"))`
* Mapa: ETPCenicafe.tif
* Grilla: [Part1](../../.grid/ETPCenicafe.part01.rar), [Part2](../../.grid/ETPCenicafe.part02.rar), [Part3](../../.grid/ETPCenicafe.part03.rar)  

> Debido al tamaño del archivo generado (aproximadamente 1.1 GB), la grilla ha sido comprimida en archivos .rar en partes de 95 MB.

Luego de creados los mapas, modifique la simbología de representación utilizando el esquema de color _Plasma_ y establezca transparencia en 50%.

![R.LTWB](Screenshot/ArcGISPro3.0.3ETPCenicafe.png)

En el mapa creado, podrá observar que los valores de evapotranspiración obtenidos se encuentran entre 542.69 y 1715.57 mm/año.

> Es importante tener en cuenta que el mapa obtenido corresponde a estimaciones compuestas que no han sido segmentadas por fenómeno climatológico (El Niño, La Niña, Neutro).

En este momento dispone de la grilla de evapotranspiración potencial, requerida para la generación de los mapas de evapotranspiración real.


### Actividades complementarias:pencil2:

En la siguiente tabla se listan las actividades complementarias que deben ser desarrolladas y documentadas por el estudiante en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (mostrar nombre completo, código y enlace a su cuenta de GitHub), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.


| Actividad | Alcance                                                                                                                                                                                                                                                                                    |
|:---------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1     | Investigue y documente otras ecuaciones regionales a partir de las cuales se puedan construir mapas de evapotranspiración potencial.                                                                                                                                                       |
|     2     | A partir de las ecuaciones regionales investigadas, cree los mapas de evapotranspiración potencial y con algebra de mapas realice el análisis de diferencias. Evalúe e implemente en su caso de estudio, los mapas que mejor representen su zona de estudio. |


### Referencias

* http://julianrojo.weebly.com/uploads/1/2/0/0/12008328/metodos_estimacion_de_et.pdf
* https://hess.copernicus.org/articles/23/4983/2019/


### Compatibilidad

* Esta actividad puede ser desarrollada con cualquier software SIG que disponga de herramientas de algebra de mapas.


### Control de versiones

| Versión    | Descripción                                                         | Autor                                     | Horas |
|------------|:--------------------------------------------------------------------|-------------------------------------------|:-----:|
| 2022.12.10 | Documentación general. Ilustración cabecera y diagrama de procesos. | [rcfdtools](https://github.com/rcfdtools) |   2   |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Actividad anterior](../Temperature) | [Inicio](../../Readme.md) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/30) | [Actividad siguiente]()  |
|--------------------------------------|---------------------------|------------------------------------------------------------------------|--------------------------|

[^1]: http://julianrojo.weebly.com/uploads/1/2/0/0/12008328/metodos_estimacion_de_et.pdf