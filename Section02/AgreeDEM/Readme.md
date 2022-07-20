## Reacondicionamiento de terreno - DEM Reconditioning – AgreeDEM
Keywords: `DEM` `AgreeDEM`

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/AgreeDEM.png)

Para garantizar que la acumulación del flujo se realice sobre las celdas del modelo de terreno y por los cauces o drenajes obtenidos o digitalizados, es necesario reacondicionar el terreno incrustando los drenajes. Este procedimiento es especialmente requerido en zonas predominantemente planas o en zonas donde no puedan ser identificadas las celdas correspondientes a los drenajes.


### Objetivos

* 


### Requerimientos

* [ArcGIS Pro 2+](https://pro.arcgis.com/en/pro-app/latest/get-started/download-arcgis-pro.htm)
* [ArcGIS for Desktop 10+](https://desktop.arcgis.com/es/desktop/) (opcional)
* [QGIS 3+](https://qgis.org/) (opcional)
* HEC-HMS 4.9+


### Procedimiento general con HEC-HMS

<div align="center">
<br><img alt="R.LTWB" src="https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Graph/AgreeDEMFlowchart.png" width="80%"><br>
<sub>Convenciones del diagrama: Base de datos geográfica GDB en azul, Clases de entidad en gris, Geo-procesos en verde y Procesos manuales en amarillo.<br>Líneas con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>

1. En HEC-HMS, cree un proyecto nuevo en blanco definiendo _Metric_ en el sistema de unidades por defecto, guardar como _HECHMS_ en la carpeta _D:\R.LTWB\_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9CreateNewProject.png)

Automáticamente, obtendrá una carpeta con la estructura de directorios y archivos requeridos por este modelo que para la versión 4.9 contendrá:

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9CreateNewProjectStructure.png)

2. En el menú _Components – Create Component – Basin Model_, cree el modelo de cuencas, nombrar como _Basin 1_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9CreateBasinModel.png)

3. En la tabla de contenido localizada a la izquierda, seleccione _HECHMS – Basin Models – Basin 1_, luego en el menú _GIS – Coordinate System_ seleccione el sistema de proyección de coordenadas _MAGNA_OrigenNacional.prj_ localizado en el directorio _D:\R.LTWB\\.ProjectionFile_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/HECHMS4.9CoordinateSystem.png)



4. En el menú Components – Create Component – Terrain Data…, cree el terreno a partir del modelo digital de elevación - DEM seleccionando unidades verticales en metros, nombrar como Terrain 1.
5. En la tabla de contenido, seleccione HECHMS_v0 – Basin Models – Basin 1 y en la parte inferior, asocie el terreno creado al modelo de cuencas.
6. En el menú GIS – Terrain Reconditioning…, el primer paso se utiliza para crear paredes perimetrales de confinamiento utilizando el borde de una cuenca previamente digitalizada, el segundo paso permite modificar el terreno incrustando los drenajes; defina el número de celdas aferentes (p.ej, 5), la profundidad de suavizado lateral (p.ej, 10) y la profundidad de incrustación en el cauce (p.ej, 1000 para garantizar que en el paso de relleno de sumideros se mantenga la localización de las celdas correspondientes a los drenajes marcados), luego seleccione la red de drenaje en formato Shapefile. El modelo de terreno será almacenado en el directorio …\HECHMS_v0\gis\Basin_1


![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/AgreeDEM/Screenshot/IGACGDB100k.png)

En este momento ya dispone de la grilla de terreno reacondicionada requerida para el relleno de sumideros.


### Referencias

* 


### Compatibilidad

* Esta actividad puede ser desarrollada con cualquier software SIG que disponga de herramientas para de digitalización con opciones de encajado o snapping.
* 


### Control de versiones

| Versión    | Descripción     | Autor                                      | Horas |
|------------|:----------------|--------------------------------------------|:-----:|
| 2022.07.20 | Versión inicial | [rcfdtools](https://github.com/rcfdtools)  |   0   |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Actividad anterior](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/DEMAlos) | [Inicio](https://github.com/rcfdtools/R.LTWB/wiki) | [Actividad siguiente]() |
|---------------------------------------------------------------------------------------|----------------------------------------------------|-------------------------|

[^1]: 