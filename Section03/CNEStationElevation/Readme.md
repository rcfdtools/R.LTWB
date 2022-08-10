## Análisis y representación de elevaciones en estaciones terrestres
Keywords: `IDEAM` `Weather Station` `Bar graph` `Select By Location` `Scatter plot` `Definition Query` `Normal distribution` `Statistics`

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Graph/CNEStation.png)

Los catálogos de estaciones terrestres contienen el atributo de elevación asociada a cada estación que debe ser validado a partir de los modelos digitales de elevación DEM para su uso posterior en la implementación de métodos de imputación de datos faltantes por relaciones espaciales.                       


### Objetivos

* Obtener las cotas de las estaciones a partir de los modelos satelitales digitales de elevación ASTER, SRTM y ALOS.
* Analizar la correspondencia entre las elevaciones presentadas en el campo `altitud` del IDEAM y las elevaciones obtenidas a partir de modelos satelitales.
* Clasificar las estaciones terrestres por piso térmico a partir de cortes convencionales cada 1000 m.s.n.m y los cortes definidos por Caldas en 1802.
* Definir las elevaciones de las estaciones que posteriormente se utilizarán como referencia en los algoritmos de imputación o completado de datos faltantes a partir de relaciones geográficas. 


### Requerimientos

* [ArcGIS Pro 2+](https://pro.arcgis.com/en/pro-app/latest/get-started/download-arcgis-pro.htm)
* [ArcGIS for Desktop 10+](https://desktop.arcgis.com/es/desktop/) (opcional)
* [QGIS 3+](https://qgis.org/) (opcional)
* [Polígono que delimita la zona de estudio. ](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudio.zip)[:mortar_board:Aprender.](https://github.com/rcfdtools/R.LTWB/tree/main/Section01/CaseStudy)
* [Polígono envolvente que delimita la zona de estudio. ](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudioEnvelope.zip)[:mortar_board:Aprender.](https://github.com/rcfdtools/R.LTWB/tree/main/Section01/CaseStudy)
* [Capa integrada de estaciones terrestres del IDEAM y otras entidades. ](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/CNE_IDEAM_OE_ZE.zip)[:mortar_board:Aprender.](https://github.com/rcfdtools/R.LTWB/tree/main/Section03/CNEStation)


### Diagrama general de procedimientos

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

1. Ingresar al portal _http://dhime.ideam.gov.co/atencionciudadano/_, aceptar los términos y condiciones para descargar información del Banco de Datos del IDEAM, dar clic en la pestaña de recursos y descargar el Catálogo nacional de estaciones en formato Microsoft Excel y Shapefile, el Catálogo nacional de otras entidades y el Glosario de variables. Opcionalmente, el catálogo puede ser descargado desde el portal del IDEAM desde [Solicitud de Información](http://www.ideam.gov.co/solicitud-de-informacion). Copiar los archivos de Microsoft Excel _[CNE_IDEAM.xls]()_ y _[CNE_OE.xls]()_ en el directorio _D:\R.LTWB\\.datasets_, copiar y descomprimir el archivo [CNE_IDEAM.zip]() que contiene los puntos de localización de las estaciones en formato Shapefile dentro de la carpeta _D:\R.LTWB\\.shp_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/DHIMERecursos.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/IDEAMSolicitudInformacion.png)

2. En ArcGIS Pro, cree un proyecto nuevo en blanco en la ruta _D:\R.LTWB\\.map_ y nómbrelo como _ArcGISProSection03.aprx_. Automáticamente, serán generados el mapa de proyecto, la base de datos geográfica en formato .gdb, la carpeta para volcado de informes de registro de importación _ImportLog_ y la carpeta _Index_. Utilizando el Panel de catálogo y desde la sección Folders, realice la conexión a la carpeta D:\R.LTWB. 

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0NewMapProject.png)

3. Desde la carpeta _.shp_, agregue al mapa el archivo shapefile [CNE_IDEAM.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/CNE_IDEAM.zip), [ZonaEstudio.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudio.zip) y [ZonaEstudioEnvelope.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudioEnvelope.zip). Modifique la simbología de representación de _ZonaEstudioEnvelope_ sin relleno - línea contorno rojo - grosor 3 y _ZonaEstudio_ sin relleno - línea contorno negro - grosor 2. Simbolice las estaciones con puntos color gris 30% - sin contorno - tamaño 6, rotular por el campo `CODIGO` y acercar a la zona de estudio. 

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0CNEMap.png)

> Tenga en cuenca que automáticamente ha sido asignado el sistema de coordenadas geográficas MAGNA al proyecto debido a que el Shapefile del CNE contiene integrado este sistema. En cuanto al número de estaciones, para la versión descargada a 20220731, el CNE se compone de 4476 estaciones.

4. Desde la carpeta _.datasets_, agregue el archivo _CNE_OE.xls_ que contiene la localización de estaciones de otras entidades de Colombia y abra la tabla de atributos, podrá observar que a fecha 20220731 la tabla contiene 4620 registros. Dando clic derecho en la tabla y seleccionando la opción _Display XY Data_, cree una tabla de eventos geográficos para representar la localización de estas estaciones. Utilice el sistema de coordenadas _GCS_WGS_1984_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationElevation/Screenshot/ArcGISPro3.0.0CNEOEDisplayXYData.png)

Como puede observar en la ilustración, en el polígono envolvente de la zona de estudio existen múltiples estaciones del catálogo nacional del IDEAM y de otras entidades. 

> Para el cargue de archivos de Microsoft Excel en formato .xls, se requiere del [Driver de Microsoft Access Database Engine](https://www.microsoft.com/en-us/download/confirmation.aspx?id=54920)[^2].


### Actividades complementarias:pencil2:

En la siguiente tabla se listan las actividades complementarias que deben ser desarrolladas y documentadas por el estudiante en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (mostrar nombre completo, código y enlace a su cuenta de GitHub), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.

| Actividad | Alcance                                                                            |
|:---------:|:-----------------------------------------------------------------------------------|
|     1     | Realice el procedimiento presentado en esta clase en ArcGIS for Desktop y en QGIS. | 
 

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