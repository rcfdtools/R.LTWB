## Descarga de GDB nacional del IGAC en escala 1:100.000 y fotorrestitución de redes de drenaje
Keywords: `IGAC` `GDB` `1:100000` `Pairwise Clip` `Clip` `Polygon to Centerline`

![GDB25k.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/GDB100k/Screenshot/GDB25k.png)

Para los procesos de reacondicionamiento del modelo de terreno que garantice el flujo de todas las celdas del modelo hacia celdas específicas de la red de drenaje, es necesaria la descarga y complementación de las líneas de drenaje pertenecientes a la zona de estudio.

Los drenajes corresponden al flujo de agua superficial que depende de la precipitación pluvial y/o afloramiento de aguas subterráneas y van a desembocar en otra corriente, en una laguna o en el mar. Los drenajes dispersos son aquellos que no desembocan en otro cuerpo de agua, o desaparecen al ser no fotointerpretables, por ejemplo en corrientes subterráneas.[^1]


### Objetivos

* Descargar la GDB IGAC a escala 1:100.000
* Identificar las redes de drenaje de la zona de estudio.
* Conocer el catálogo de objetos de la clase de entidad Drenaje_Sencillo del IGAC.
* Conocer los subtipos asociados al dominio de estados de drenaje del IGAC.
* Completar las redes de drenaje por ausencia de planchas catastrales.
* Extender los tramos de drenajes sencillos hasta el eje central de drenajes dobles.


### Requerimientos

* ArcGIS for Desktop 10+ (opcional)
* ArcGIS Pro 2+ (opcional)
* QGIS 3+ (opcional)


### Procedimiento de descarga

1. Ingrese al portal https://www.colombiaenmapas.gov.co/, en temática seleccione _Cartografía Básica_ y busque _Base de datos vectorial básica. Colombia. Escala 1:100.000_ del año 2022. En la parte inferior del _Detalle del Servicio_ seleccione en _Formato de descarga_ `Geodatabase` y de clic en _Descargar_, automáticamente iniciará la descarga a través de una orden de servicio. La GDB comprimida tiene un tamaño aproximado de 665 MB.

![IGACGDB100k.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/GDB100k/Screenshot/IGACGDB100k.png)

2. Descomprima la base de datos geográfica en la carpeta de descargas, abra el mapa D:\R.LTWB\.map\R.LTWB.mxd de ArcGIS for Desktop o D:\R.LTWB\.map\ArcGISPro\ArcGISPro.aprx de ArcGIS Pro, agregue el mapa base _World Light Gray Canvas Base_ y desde el dataset _Superficies_Agua_, agregue la capa _Drenaje_Sencillo_. Podrá observar que la capa se simboliza automáticamente en drenajes _Permanentes_ e _Intermitentes_ a partir del dominio _Estado_Drenaje_. La versión descargada contiene 426964 entidades para todo el territorio nacional.

![IGACDrenajeSencillo100k.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/GDB100k/Screenshot/IGACDrenajeSencillo100k.png)

> Tenga en cuenta que los drenajes restituídos pueden no estar actualizados de acuerdo a las condiciones particulares de la zona de estudio evaluada. Se recomienda verificar con imágenes satelitales recientes, la correspondencia entre las redes de drenaje digitalizadas por el IGAC y las redes de drenajes visibles en imágenes. Por ejemplo, en la zona de explotación minera a cielo abierto del Departamento del Cesar en Colombia, los drenajes sobre los polígonos de concesión pueden no corresponder a las condiciones actuales debido a realineamiento de cauces.

3. Utilizando la herramienta de geoprocesamiento _Clip_ recorte la clase de entidad _Drenaje_Sencillo_ y guarde en un archivo de formas en formato Shapefile dentro de la carpeta _.shp_ de _D:\R.LTWB_ con el nombre _DrenajeSencilloIGAC100kZE.shp_. Para el recorte, utilice como máscara el polígono envolvente de la zona de estudio denominado [ZonaEstudioEnvelope.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudioEnvelope.zip). La versión recortada contiene 15342 tramos de drenaje dentro de la zona de estudio.

> En ArcGIS Pro puede utilizar también la herramienta _Pairwise Clip_ que contiene funcionalidades extendidas de la herramienta _Clip_.

> En QGIS, utilice la herramienta _Processing Toolbox / Vector overlay / Clip_. 

![IGACDrenajeSencillo100kZEClip.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/GDB100k/Screenshot/IGACDrenajeSencillo100kZEClip.png)

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

4. Desde el dataset _Superficies_Agua_, agregue la capa _Drenaje_Doble_ y con la herramienta _Clip_ realice el recorte hasta el polígono envolvente de la zona de estudio y nombre como _DrenajeDobleIGAC100kZE.shp_. Para el caso de estudio y la versión descargada hemos obtenido 61 polígonos.

> Los drenajes dobles corresponden a superficies de agua digitalizadas como polígonos y son requeridos para completar la red de drenajes sencillos que será utilizada en el reacondicionamiento del modelo digital de elevación. 

 ![IGACDrenajeDoble100kZEClip.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/GDB100k/Screenshot/IGACDrenajeDoble100kZEClip.png)

5. A partir de los polígonos de los drenajes dobles y utilizando la herramienta de geoprocesamiento _Topographic Production Tools / Polygon to Centerline_ de ArcGIS Pro, cree las líneas centrales que demarcan cada drenaje sencillo y nombre la capa resultante como _DrenajeDobleIGAC100kZECenterline_ dentro de la GDB de ArcGIS Pro y seleccione en _Connecting Features_ la capa correspondiente a los drenajes sencillos de la zona de estudio, denominada previamente como _DrenajeSencilloIGAC100kZE.shp_ para obtener líneas conectoras desde los drenajes sencillos hasta las líneas centrales.

> Debido a que internamente esta herramienta debe crear campos de atributos que contienen los nombres de las capas de entrada, los nombres de atributos pueden contener más de 10 caracteres lo que generará un error de ejecución. Para obtener las líneas centrales, primero cree una capa geográfica de lineas centrales en la GDB de ArcGIS Pro y luego exporte a un archivo de formas shapefile.

> Para conocer como realizar este procedimiento en ArcGIS for Desktop, [clic aquí](https://support.esri.com/en/technical-article/000012414). El procedimiento consiste en convertir primero los polígonos a líneas utilizando la herramienta _ArcToolBox / Data Management Tools / Features / Polygon to Line_, luego eliminar los extremos que confinan cada polígono y finalmente con la herramienta _ArcToolBox / Cartography Tools / Generalization / Collapse Dual Lines To Centerline_ obtener una line central a lo largo de las lineas paralelas externas que delimitan cada drenaje doble.

![IGACDrenajeDoble100kZECenterline.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/GDB100k/Screenshot/IGACDrenajeDoble100kZECenterline.png)

6. Exporte la clase de entidad de líneas centrales de drenajes dobles a un archivo shapefile dentro de la carpeta _.shp_ nombrando como _DrenajeDobleIGAC100kZECenterline.shp_ y verifique que las líneas conectoras desde los drenajes sencillos hasta la línea central se encuentren a lo largo de toda la red. Podrá observar que no todas las conexiones laterales a los cuerpos dobles han sido trazadas.

![IGACDrenajeDoble100kZECenterlineExport.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/GDB100k/Screenshot/IGACDrenajeDoble100kZECenterlineExport.png)

7. Realice la unión de la capa de drenajes sencillos y las líneas centrales obtenidas de polígonos de los drenajes dobles en una nueva capa geográfica, para ello utilice la herramienta de geoprocesamiento _Data Management Tools / Merge_ y nombre la capa como _DrenajeSencilloIGAC100kZEMerge.shp_.

![IGACDrenajeSencillo100kZEMerge.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/GDB100k/Screenshot/IGACDrenajeSencillo100kZEMerge.png)

> En ArcGIS for Desktop utilice la herramienta _Merge_ disponible en el menú _Geoprocessing_.

> En QGIS utilice la herramienta xxxxxxxxxxxxxxxxx. 

8. Utilizando el editor geográfico, conecte o extienda manualmente las líneas de drenajes sencillos hasta el eje central de los drenajes dobles. 

> La extensión y conectividad de los tramos de drenajes sencillos hasta el eje central de los tramos de drenajes dobles es vital para garantizar que la acumulación de flujo por los cauces principales se realice de forma correcta. 

En la tabla de contenido de clic en List By Selection y únicamente active la capa _DrenajeSencilloIGAC100kZEMerge.shp_. Para facilitar la edición, en la visualización utilice como referencia de localización los tramos principales de la capa _DrenajeDobleIGAC100kZECenterline.shp_ 

![IGACDrenajeSencillo100kZEListBySelection.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/GDB100k/Screenshot/IGACDrenajeSencillo100kZEListBySelection.png)

En ArcGIS Pro, seleccione en la tabla de contenidos o _Contents_ la capa _DrenajeSencilloIGAC100kZEMerge.shp_ y en el Menú _Edit_ de clic en _Modify_ y seleccione la opción _Extend or Trim_. 

![IGACDrenajeSencillo100kZEExtend.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/GDB100k/Screenshot/IGACDrenajeSencillo100kZEExtend.png)

Extienda una a una las líneas laterales hasta el drenaje principal y conecte manualmente los tramos iniciales a través de la edición de los vértices. Rotule la capa utilizando el campo _NOMBRE_GEO_. Verifique y realice este procedimiento sobre toda la red y al finalizar de clic en el menú _Edit / Save_.

![IGACDrenajeSencillo100kZEExtend1.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/GDB100k/Screenshot/IGACDrenajeSencillo100kZEExtend1.png)

> Tenga en cuenta que pueden existir bucles en la red de drenaje correspondientes a tramos que se interconectan entre sí. Esto puede causar errores en los procesos de acumulación de flujo por lo que es conveniente evaluar a partir de imágenes satelitales, cuál es el tramo dominante y proceder manualmente a editar y a abrir estos bucles.  

![IGACDrenajeSencillo100kZELoop.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/GDB100k/Screenshot/IGACDrenajeSencillo100kZELoop.png)

7. Visualmente, identifique las zonas geográficas en las que no se encuentra completa la digitalización de drenajes, p. ej. en el casco urbano de Valledupar.


### Referencias

* http://www.ideam.gov.co/capas-geo
* http://www.siac.gov.co/catalogo-de-mapas
* http://visor.ideam.gov.co/geovisor/#!/profiles/3
* https://www.igac.gov.co/sites/igac.gov.co/files/anexo_1.1_catalogo_objetos_cartografiabasica_v1.0_.pdf
* http://sites.tufts.edu/gis/files/2013/11/Watershed-and-Drainage-Delineation-by-Pour-Point.pdf
* https://gisrsstudy.com/drainage-density-arcgis/
* https://pro.arcgis.com/en/pro-app/latest/tool-reference/topographic-production/polygon-to-centerline.htm


### Compatibilidad

* Esta actividad puede ser desarrollada con cualquier software SIG que disponga de herramientas para de digitalización con opciones de encajado o snapping.
* Para la descarga puede utilizar cualquier navegador de Internet actualizado.


### Control de versiones

| Versión     | Descripción                                                               | Autor                                      | Horas |
|-------------|:--------------------------------------------------------------------------|--------------------------------------------|:-----:|
| 2022.07.17  | Versión inicial con descarga manual GDB IGAC Colombia escala 1:100.000, . | [rcfdtools](https://github.com/rcfdtools)  |  x   |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Actividad anterior](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/DEMAlos) | [Inicio](https://github.com/rcfdtools/R.LTWB/wiki) | [Actividad siguiente]() |
|---------------------------------------------------------------------------------------|----------------------------------------------------|-------------------------|

[^1]: https://www.igac.gov.co/sites/igac.gov.co/files/anexo_1.1_catalogo_objetos_cartografiabasica_v1.0_.pdf ↩