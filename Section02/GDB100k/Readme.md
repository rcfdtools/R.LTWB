## Descarga de GDB nacional del IGAC en escala 1:100.000 y fotorrestitución de redes de drenaje
Keywords: `IGAC` `GDB` `1:100000` `Pairwise Clip` `Clip`

![DEMAster.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/GDB100k/Screenshot/GDB25k.png)

Para los procesos de reacondicionamiento del modelo de terreno que garantice el flujo de todas las celdas del modelo hacia las celdas específicas de la red de drenaje, es necesaria la descarga y complementación de las líneas de drenaje pertenecientes a la zona de estudio.

Los drenajes corresponden al flujo de agua superficial que depende de la precipitación pluvial y/o afloramiento de aguas subterráneas y va a desembocar en otra corriente, en una laguna o en el mar. Los drenajes dispersos son aquellos que no desembocan en otro cuerpo de agua, o desaparecen al ser no fotointerpretables, por ejemplo en corrientes subterráneas.[^1]


### Objetivos

* Descargar la GDB IGAC a escala 1:100.000
* Identificar las redes de drenaje de la zona de estudio.
* Completar las redes de drenaje por ausencia de planchas catastrales.


### Requerimientos

* ArcGIS for Desktop 10+ (opcional)
* ArcGIS Pro 2+ (opcional)
* QGIS 3+ (opcional)


### Procedimiento de descarga

1. Ingrese al portal https://www.colombiaenmapas.gov.co/, en temática seleccione _Cartografía Básica_ y busque _Base de datos vectorial básica. Colombia. Escala 1:100.000_ del año 2022. En la parte inferior del _Detalle del Servicio_ seleccione en _Formato de descarga_ `Geodatabase` y de clic en _Descargar_, automáticamente iniciará la descarga a través de una orden de servicio. La GDB comprimida tiene un tamaño aproximado de 665 MB.

![IGACGDB100k.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/GDB100k/Screenshot/IGACGDB100k.png)

2. Descomprima la base de datos geográfica en la carpeta de descargas, abra el mapa D:\R.LTWB\.map\R.LTWB.mxd de ArcGIS for Desktop o D:\R.LTWB\.map\ArcGISPro\ArcGISPro.aprx de ArcGIS Pro, agregue el mapa base _World Light Gray Canvas Base_ y desde el dataset _Superficies_Agua_, agregue la capa _Drenaje_Sencillo_. Podrá observar que la capa se simboliza automáticamente en drenajes _Permanentes_ e _Intermitentes_ a partir del dominio _Estado_Drenaje_. La versión descargada contiene 426964 entidades para todo el territorio nacional.

![IGACDrenajeSencillo100k.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/GDB100k/Screenshot/IGACDrenajeSencillo100k.png)

3. Utilizando la herramienta de geoprocesamiento _Clip_ recorte la clase de entidad _Drenaje_Sencillo_ y guarde en un archivo de formas en formato Shapefile dentro de la carpeta _.shp_ de _D:\R.LTWB_ con el nombre _DrenajeSencilloIGAC100kZE.shp_. Para el recorte utilice el polígono envolvente de la zona de estudio denominado [ZonaEstudioEnvelope.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudioEnvelope.zip). La versión recortada contiene 15342 tramos de drenaje dentro de la zona de estudio.

> En ArcGIS Pro puede utilizar también la herramienta _Pairwise Clip_ que contiene funcionalidades extendidas de la herramienta _Clip_.

![IGACDrenajeSencillo100kExport.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/GDB100k/Screenshot/IGACDrenajeSencillo100kZEClip.png)

> Para el desarrollo del caso de estudio no se ha utilizado la digitalización de la Base de datos vectorial básica - Colombia a Escala 1:25.000 del año 2018 debido a que aún no se encuentran todas las planchas del país digitalizadas y almacenadas en la GDB disponible para descarga como se muestra en la siguiente imagen.

Información disponible a escala 1:25k
![IGACGDB25k.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/GDB100k/Screenshot/IGACGDB25k.png)

Catálogo de objetos en Drenaje_Sencillo para capa en formato Shapefile

| Nombre      | Alias       | Definición                                                                                          | Tipo de dato           |
|:------------|:------------|:----------------------------------------------------------------------------------------------------|:-----------------------|
| OBJECTID    | OBJECTID    | Identificador único de objeto.                                                                      | Numérico               |
| Shape       | Shape       | Tipo de geometría.                                                                                  | Geometría              |
| ESTADO_DRE  | TEDD        | Indica si el drenaje es permanente o intermitente. Subtipo.                                         | Texto                  |
| SYMBOL      | Symbol      | En este campo se especifica la geometría como se representará el objeto (punto, línea o polígono).  | Numérico y texto, 255  |
| PROYECTO    | PROYECTO    | Proyecto en el cual se desarrollaron los datos.                                                     | Numérico y texto, 255  |
| FECHA       | FECHA       | Fecha de realización de los datos.                                                                  | Dato                   |
| DISPERSION  | Dispersión  | Indica si el drenaje es disperso no no.                                                             | Dato                   |
| NOMBRE_GEO  | NMG         | Nombre de la entidad geográfica.                                                                    | Numérico y texto, 255  |
| PK_CUE      | PK_CUE      | Identificador único global de cada elemento.                                                        | Numérico               |
| RULEID      | RuleID      | Identificador único de la representación.                                                           | Texto                  |
| GLOBALID    | GLOBALID    | Identificador global en la base de datos espacial.                                                  | Texto                  |
| SHAPE_Leng  | SHAPE_Leng  | Longitud del elemento.                                                                              | Numérico               |

Estado de drenajes - Subtipos

| Code               | Description  |
|--------------------|--------------|
| 5101               | Permanente   | 
| 5102               | Intermitente |

4. Visualmente, identifique las zonas geográficas en las que no se encuentra completa la digitalización de los drenajes.


### Referencias

* http://www.ideam.gov.co/capas-geo
* http://www.siac.gov.co/catalogo-de-mapas
* http://visor.ideam.gov.co/geovisor/#!/profiles/3
* https://www.igac.gov.co/sites/igac.gov.co/files/anexo_1.1_catalogo_objetos_cartografiabasica_v1.0_.pdf


### Compatibilidad

* Esta actividad puede ser desarrollada con cualquier software SIG que disponga de herramientas para de digitalización con opciones de encajado o snapping.
* Para la descarga puede utilizar cualquier navegador de Internet actualizado.


### Control de versiones

| Versión     | Descripción                                                             | Autor                                      | Horas |
|-------------|:------------------------------------------------------------------------|--------------------------------------------|:-----:|
| 2022.07.17  | Versión inicial con descarga manual GDB IGAC Colombia escala 1:100.000. | [rcfdtools](https://github.com/rcfdtools)  |  x   |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Actividad anterior](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/DEMAlos) | [Inicio](https://github.com/rcfdtools/R.LTWB/wiki) | [Actividad siguiente]()  |
|------------------------|----------------------------------------------------|----------------------------------------------------------------------------------------|

[^1]: https://www.igac.gov.co/sites/igac.gov.co/files/anexo_1.1_catalogo_objetos_cartografiabasica_v1.0_.pdf ↩