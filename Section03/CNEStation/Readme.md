## Catálogo nacional de estaciones - CNE
Keywords: `IDEAM` `Weather Station`

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/CNEStation.png)

Luego de la definición del caso de estudio realizada en la Sección 1, es necesario identificar la red de estaciones terrestres que serán utilizadas para el estudio de las diferentes variables hidroclimatológicas en la zona estudio.                                                                                                                                                      

> En la ilustración, _CNE_IDEAM_ corresponde a las estaciones del Catálogo Nacional de Estaciones del IDEAM y _CNE_IDEAM_ZE_ corresponde al grupo de estaciones prototipo en la zona de estudio.
 

### Objetivos

* Descargar el catálogo nacional de estaciones - CNE del IDEAM Colombia.
* Identificar los atributos contenidos en el catálogo de objetos del CNE.
* 
*  


### Requerimientos

* [ArcGIS for Desktop 10+](https://desktop.arcgis.com/es/desktop/)
* [ArcGIS Pro 2+](https://pro.arcgis.com/en/pro-app/latest/get-started/download-arcgis-pro.htm) (opcional)
* [QGIS 3+](https://qgis.org/) (opcional)
* [Zona de estudio por disolución de los polígonos de la zona hidrográfica 28 - Cesar. ](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudio.zip)[:blue_book:Aprender.](https://github.com/rcfdtools/R.LTWB/tree/main/Section01/CaseStudy)
* [Zona de estudio - envolvente regular de los polígonos de la zona hidrográfica 28 - Cesar. ](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudioEnvelope.zip)[:blue_book:Aprender.](https://github.com/rcfdtools/R.LTWB/tree/main/Section01/CaseStudy)

> xxxxxxxxxxxxxxDebido a que es necesario incluir diferentes estaciones al rededor de la zona hidrográgica de estudio para garantizar la extensión espacial de los mapas interpolados para cada variable climatológica requerida, en esta actividad no se especifica el listado de las estaciones a utilizar y en la sección 3 de este curso se presenta el proceso detallado de selección espacial de estas estaciones.


### Procedimiento general

<div align="center">
<br><img alt="R.LTWB" src="https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Graph/CNEStationFlowchart.png" width="65%"><br>
<sub>Convenciones generales en diagramas: clases de entidad en azul, dataset en gris oscuro, grillas en color verde, geo-procesos en rojo y procesos manuales en amarillo. Líneas con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>

El [Instituto de Hidrología, Meteorología y Estudios Ambientales - IDEAM](http://www.ideam.gov.co/) de Colombia, adscrito al [Ministerio de Medio Ambiente - Minambiente](https://www.minambiente.gov.co/), es la entidad nacional encargada registrar y mantener la información hidrometeorológica del país, incluida la localización y clasificación de la red de estaciones que hace parte del [Catálogo Nacional de Estaciones - CNE](http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls). A través del servicio de [Solicitud de Información](http://www.ideam.gov.co/solicitud-de-informacion) o a través del portal [DHIME](http://dhime.ideam.gov.co/atencionciudadano/) del IDEAM desde la pestaña _Recursos_, personas naturales o jurídicas, pueden obtener no solamente los catálogos, sino también las capas geográficas y los registros discretos registrados en cada estación. 


![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/CNEStation.png)