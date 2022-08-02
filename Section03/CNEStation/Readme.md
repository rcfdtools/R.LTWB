## Catálogo nacional de estaciones - CNE y selección para la zona de estudio
Keywords: `IDEAM` `Weather Station` `Display XY Data` `Buffer` `Select By Location`

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Graph/CNEStation.png)

Luego de la definición del caso de estudio realizada en la Sección 1, es necesario identificar la red de estaciones terrestres que serán utilizadas para el estudio de las diferentes variables hidroclimatológicas en la zona estudio.                                                                                                                                                      

> En la ilustración, _CNE_IDEAM_ corresponde a las estaciones del Catálogo Nacional de Estaciones del IDEAM y _CNE_IDEAM_ZE_ corresponde al grupo de estaciones prototipo en la zona de estudio.
 

### Objetivos

* Descargar el catálogo nacional de estaciones - CNE del IDEAM Colombia.
* Identificar los atributos contenidos en el catálogo de objetos del CNE.


### Requerimientos

* [ArcGIS Pro 2+](https://pro.arcgis.com/en/pro-app/latest/get-started/download-arcgis-pro.htm)
* [ArcGIS for Desktop 10+](https://desktop.arcgis.com/es/desktop/) (opcional)
* [QGIS 3+](https://qgis.org/) (opcional)
* [Polígono que delimita la zona de estudio. ](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudio.zip)[:mortar_board:Aprender.](https://github.com/rcfdtools/R.LTWB/tree/main/Section01/CaseStudy)
* [Polígono envolvente que delimita la zona de estudio. ](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudioEnvelope.zip)[:mortar_board:Aprender.](https://github.com/rcfdtools/R.LTWB/tree/main/Section01/CaseStudy)

> xxxxxxxxxxxxxxDebido a que es necesario incluir diferentes estaciones al rededor de la zona hidrográgica de estudio para garantizar la extensión espacial de los mapas interpolados para cada variable climatológica requerida, en esta actividad no se especifica el listado de las estaciones a utilizar y en la sección 3 de este curso se presenta el proceso detallado de selección espacial de estas estaciones.

El [Instituto de Hidrología, Meteorología y Estudios Ambientales - IDEAM](http://www.ideam.gov.co/) de Colombia, adscrito al [Ministerio de Medio Ambiente - Minambiente](https://www.minambiente.gov.co/), es la entidad nacional encargada registrar y mantener la información hidrometeorológica del país, incluida la localización y clasificación de la red de estaciones que hace parte del [Catálogo Nacional de Estaciones - CNE](http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls). A través del servicio de [Solicitud de Información](http://www.ideam.gov.co/solicitud-de-informacion) o a través del portal [DHIME](http://dhime.ideam.gov.co/atencionciudadano/) del IDEAM desde la pestaña _Recursos_, personas naturales o jurídicas, pueden obtener no solamente los catálogos, sino también las capas geográficas y los registros discretos registrados en cada estación.

### Atributos que componen el catálogo nacional de estaciones

Tomados directamente del archivo [CNE_IDEAM.xls](http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls) v20220731.

| Atributo             | Tipo        | Descripción                                                                                                                                                                                                                                                                     |
|:---------------------|:------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OBJECTID             | int64       | Identificador de objeto espacial proveniente de la GDB IDEAM.                                                                                                                                                                                                                   |
| CODIGO               | int64       | Código de la estación.                                                                                                                                                                                                                                                          |
| nombre               | object      | Nombre de la estación. Incluye el código de la estación entre corchetes.                                                                                                                                                                                                        |
| CATEGORIA            | object      | Categoría de la estación: Pluviométrica, Limnimétrica, Limnigráfica, Climática Ordinaria, Climática Principal, Pluviográfica, Meteorológica Especial, Agrometeorológica, Sinóptica Principal, Radio Sonda, Mareográfica, Sinóptica Secundaria.                                  |
| TECNOLOGIA           | object      | Tecnología para captura, registro y transmisión: Convencional, Automática con Telemetría, Automática sin Telemetría.                                                                                                                                                            |
| ESTADO               | object      | Estado de funcionamiento: Activa, Suspendida, En Mantenimiento.                                                                                                                                                                                                                 |
| FECHA_INSTALACION    | datetime64  | Fecha de instalación. FECHA_INST en archivos Shapefile.                                                                                                                                                                                                                         |
| altitud              | int64       | Altitud o cota sobre el nivel del mar en metros.                                                                                                                                                                                                                                |
| latitud              | float64     | Latitud en grados decimales.                                                                                                                                                                                                                                                    |
| longitud             | float64     | Longitud en grados decimales.                                                                                                                                                                                                                                                   |
| DEPARTAMENTO         | object      | Departamento o zonificación política. Equivalente a estados en otros países. DEPARTAMEN en archivos Shapefile.                                                                                                                                                                  |
| MUNICIPIO            | object      | Municipio o subzonificación política. Equivalente a condado en otros países.                                                                                                                                                                                                    |
| AREA_OPERATIVA       | object      | Área operativa que administra la estación. AREA_OPERA en archivos Shapefile.                                                                                                                                                                                                    |
| AREA_HIDROGRAFICA    | object      | Área hidrográfica a la cual pertenece. AREA_HIDRO en archivos Shapefile.                                                                                                                                                                                                        |
| ZONA_HIDROGRAFICA    | object      | Zona hidrográfica a la cual pertenece. ZONA_HIDRO en archivos Shapefile.                                                                                                                                                                                                        |
| observacion          | object      | Observaciones generales. observacio en archivos Shapefile.                                                                                                                                                                                                                                                       |
| CORRIENTE            | object      | Corriente, cauce o río próximo o sobre la cuál está localizada la estación.                                                                                                                                                                                                     |
| FECHA_SUSPENSION     | datetime64  | Fecha de suspensión. FECHA_SUSP en archivos Shapefile.                                                                                                                                                                                                                                                           |
| SUBZONA_HIDROGRAFICA | object      | Subzona hidrográfica a la cual pertenece.SUBZONA_HI en archivos Shapefile.                                                                                                                                                                                                                                       |
| ENTIDAD              | object      | Entidad encargada.                                                                                                                                                                                                                                                              |
| subred               | object      | Subred a la cual pertenece.                                                                                                                                                                                                                                                     |

> Los atributos presentados en la tabla, su tipo de escritura y notación han sido tomados del archivo original y no se encuentran normalizados a 11 caracteres para garantizar la compatibilidad con el formato .dbf. Se puede observar que los datos volcados en el archivo CNE_IDEAM.xls han sido generados utilizando la herramienta _Table to Table_ de ArcGIS desde una Geodatabase que permite la definición de atributos con más de 11 caracteres. 
> 
> Los atributos del catálogo nacional de estaciones y de otras entidades son equivalentes. Catálogos exportados a archivos de formas Shapefile utilizan máximo 10 caracteres en la definición de atributos.


### Definiciones generales del catálogo nacional de estaciones

Tomado de [Anexo 2 - Definiciones CNE](http://www.ideam.gov.co/documents/10182/557765/Definiciones+CNE.pdf) del IDEAM.


#### Categorías de las estaciones

| Categoría                        | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|:---------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Estación Agrometeorológica       | En esta estación se realizan observaciones meteorológicas y otras observaciones que ayudan a determinar las relaciones entre el clima, por una parte y la vida de las plantas y los animales por la otra. Incluye el mismo programa de observaciones de la estación climatológica principal, más registros de temperatura a varias profundidades (hasta un metro) y en la capa cercana al suelo (0, 10 y 20 cm sobre el suelo).                                                                                     |
| Estación Climatológica Ordinaria | Es aquella en la cual se hacen observaciones de precipitación, temperatura del aire, temperaturas máxima y mínima a 2 metros y humedad primordialmente. Poseen muy poco instrumental registrador. Algunas llevan instrumentos adicionales tales como tanque de evaporación, heliógrafo y anemómetro.                                                                                                                                                                                                                |
| Estación Climatológica Principal | Es aquella en la cual se hacen observaciones de precipitación, temperatura del aire, temperaturas máxima y mínima a 2 metros, humedad, viento, radiación, brillo solar, evaporación, temperaturas extremas del tanque de evaporación, cantidad de nubes y fenómenos especiales. Gran parte de estos parámetros se obtienen de instrumentos registradores.                                                                                                                                                           |
| Estación Limnigráfica            | Estación donde se mide el nivel de una corriente hídrica mediante un aparato registrador de nivel y que grafica una curva llamada limnigrama.                                                                                                                                                                                                                                                                                                                                                                       |
| Estación Limnimétrica            | Estación donde se mide el nivel de una corriente hídrica mediante un aparato (mira dividida en centímetros) que mide altura del agua, sin registrarla. Una persona toma el dato y lo registra en una libreta.                                                                                                                                                                                                                                                                                                       |
| Estación Mareográfica            | Estaciones para observación del estado del mar. Mide nivel, temperatura y salinidad de las aguas marinas.                                                                                                                                                                                                                                                                                                                                                                                                           |
| Estación meteorológica especial  | Estación instalada para realizar seguimiento a un fenómeno o un fin específico, por ejemplo, las heladas.                                                                                                                                                                                                                                                                                                                                                                                                           |
| Estación Pluviográfica           | Es aquella que registra en forma mecánica y continua la precipitación, en una gráfica que permite conocer la cantidad, duración, intensidad y periodo en que ha ocurrido la lluvia. Actualmente se utilizan los pluviógrafos de registro diario.                                                                                                                                                                                                                                                                    |
| Estación Pluviométrica           | Es una estación meteorológica dotada de un pluviómetro o recipiente que permite medir la cantidad de lluvia caída entre dos observaciones consecutivas.                                                                                                                                                                                                                                                                                                                                                             |
| Estación Radio Sonda             | La estación de radiosonda tiene por finalidad la medición directa de parámetros atmosféricos tales como temperatura del aire, presión atmosférica, humedad relativa y dirección y velocidad del viento en las capas altas de la atmósfera (tropósfera y baja estratósfera), mediante el rastreo, por medios electrónicos, de la trayectoria de un globo meteorológico que asciende libremente y que lleva un dispositivo con los sensores que miden y transmiten la señal con los datos.                            |
| Estación Sinóptica Principal     | En este tipo de estación se efectúan observaciones de los principales elementos meteorológicos en horas convenidas internacionalmente. Los datos se toman horariamente y corresponden a nubosidad, dirección y velocidad de los vientos, presión atmosférica, temperatura del aire, tipo y altura de las nubes, visibilidad, fenómenos especiales, características de humedad, precipitación, temperaturas extremas, capas significativas de nubes, recorrido del viento y secuencia de los fenómenos atmosféricos. |
| Estación Sinóptica Secundaria    | Al igual que en la estación anterior, las observaciones se realizan a horas convenidas internacionalmente y los datos corresponden comúnmente a visibilidad, fenómenos especiales, tiempo atmosférico, nubosidad, estado del suelo, precipitación, temperatura del aire, humedad del aire, presión y viento.                                                                                                                                                                                                        |

#### Estado de la estación

| Estado           | Descripción                                                                                                                                                                                 |
|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Activa           | Estación que se encuentra en operación y registra datos automáticos o tomados por un observador.                                                                                            |
| En mantenimiento | Estación que se encuentra en operación pero que temporalmente no registra datos automáticos o tomados por un observador por problemas en los equipos o como consecuencia de un siniestro.   |
| Suspendida       | Estación que se encuentra fuera de servicio de manera definitiva y no registra datos automáticos o tomados por un observador. Solo se puede consultar datos históricos en estas estaciones. |


####  Tecnología de la estación

| Estado                    | Descripción                                                                                                                                                                                                                                                                                                                                 |
|:--------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Convencional              | Estación donde la toma del dato la efectúa un observador y la registra en una libreta para luego enviarla a los técnicos para que se capture y procesen estos datos.                                                                                                                                                                        |
| Automática con telemetría | Estación que obtiene los datos de manera automática mediante sensores de diferente tipo y que tiene la capacidad de enviarlos de manera automática al centro de recepción por diferentes medios de transmisión (satelital, radiofrecuencia, GPRS, etc.)                                                                                     |
| Automática sin telemetría | Estación que obtiene los datos de manera automática mediante sensores de diferente tipo y que tiene la capacidad de almacenarlos en un dispositivo dentro de la misma estación. No puede enviar los datos de manera automática. Los datos debes ser obtenidos por una persona que se conecta al sitio donde la estación almacena los datos. |

> De acuerdo a la nota del Anexo 2 del IDEAM: se debe tener en cuenta que la red es de tipo dinámico; es decir, a través de su operación se han instalado y suspendido estaciones a lo largo del territorio nacional, conservando en todo caso los datos históricos registrados. Esto significa que la sumatoria de las estaciones del Catálogo corresponde al número total de estaciones que han hecho parte de la red a través de su historia de operación y registro de información.


#### Nivel de aprobación de cada dato[^1]

| Código | Novel de aprobación |
|:------:|:-------------------:|
|  900   |     Preliminar      |
|  1100  |     EN revisión     |
|  1200  |     Definitivo      |

> La información validada o definitiva al encontrarse certificada, ha surtido el proceso de validación técnica necesaria que garantiza la calidad del dato y determina la oficialidad de la información que podrá ser utilizada para toma de decisiones. Para el desarrollo del caso de estudio, usaremos la información IDEAM en todos los niveles de aprobación disponibles.


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

<div align="center">
<br><img alt="R.LTWB" src="https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Graph/CNEStationFlowchart.png" width="65%"><br>
<sub>Convenciones generales en diagramas: clases de entidad en azul, dataset en gris oscuro, grillas en color verde, geo-procesos en rojo y procesos manuales en amarillo. Líneas con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>

1. Ingresar al portal _http://dhime.ideam.gov.co/atencionciudadano/_, aceptar los términos y condiciones para descargar información del Banco de Datos del IDEAM, dar clic en la pestaña de recursos y descargar el Catálogo nacional de estaciones en formato Microsoft Excel y Shapefile, el Catálogo nacional de otras entidades y el Glosario de variables. Opcionalmente, el catálogo puede ser descargado desde el portal del IDEAM desde [Solicitud de Información](http://www.ideam.gov.co/solicitud-de-informacion). Copiar los archivos de Microsoft Excel _[CNE_IDEAM.xls]()_ y _[CNE_OE.xls]()_ en el directorio _D:\R.LTWB\\.datasets_, copiar y descomprimir el archivo [CNE_IDEAM.zip]() que contiene los puntos de localización de las estaciones en formato Shapefile dentro de la carpeta _D:\R.LTWB\\.shp_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/DHIMERecursos.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/IDEAMSolicitudInformacion.png)

2. En ArcGIS Pro, cree un proyecto nuevo en blanco en la ruta _D:\R.LTWB\\.map_ y nómbrelo como _ArcGISProSection03.aprx_. Automáticamente, serán generados el mapa de proyecto, la base de datos geográfica en formato .gdb, la carpeta para volcado de informes de registro de importación _ImportLog_ y la carpeta _Index_. Utilizando el Panel de catálogo y desde la sección Folders, realice la conexión a la carpeta D:\R.LTWB. 

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0NewMapProject.png)

3. Desde la carpeta _.shp_, agregue al mapa el archivo shapefile [CNE_IDEAM.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/CNE_IDEAM.zip), [ZonaEstudio.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudio.zip) y [ZonaEstudioEnvelope.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudioEnvelope.zip). Modifique la simbología de representación de _ZonaEstudioEnvelope_ sin relleno - línea contorno rojo - grosor 3 y _ZonaEstudio_ sin relleno - línea contorno negro - grosor 2. Simbolice las estaciones con puntos color gris 30% - sin contorno - tamaño 6, rotular por el campo `CODIGO` y acercar a la zona de estudio. 

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0CNEMap.png)

> Tenga en cuenca que automáticamente ha sido asignado el sistema de coordenadas geográficas MAGNA al proyecto debido a que el Shapefile del CNE contiene integrado este sistema. En cuanto al número de estaciones, para la versión descargada a 20220731, el CNE se compone de 4476 estaciones.

4. Desde la carpeta _.datasets_, agregue el archivo _CNE_OE.xls_ que contiene la localización de estaciones de otras entidades de Colombia y abra la tabla de atributos, podrá observar que a fecha 20220731 la tabla contiene 4620 registros. Dando clic derecho en la tabla y seleccionando la opción _Display XY Data_, cree una tabla de eventos geográficos para representar la localización de estas estaciones. Utilice el sistema de coordenadas _GCS_WGS_1984_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0CNEOEDisplayXYData.png)

Como puede observar en la ilustración, en el polígono envolvente de la zona de estudio existen múltiples estaciones del catálogo nacional del IDEAM y de otras entidades. 

> Para el cargue de archivos de Microsoft Excel en formato .xls, se requiere del Driver de Microsoft Access Database Engine[^2] que puede ser descargado desde https://www.microsoft.com/en-us/download/confirmation.aspx?id=54920

5. El polígono envolvente de la zona de estudio _ZonaEstudioEnvelope.shp_ fue creado a partir del borde externo de la zona hidrográfica 28 - Cesar Colombia que corresponde al [caso de estudio](https://github.com/rcfdtools/R.LTWB/tree/main/Section01/CaseStudy) con el cual se ejemplifica este curso. El proceso de selección de estaciones, generalmente requiere que sean incluidas estaciones adicionales al rededor de la envolvente de la zona a evaluar, lo anterior debido a que en los procesos de interpolación espacial de las variables climatológicas, es necesario disponer de información espacial dentro de los rangos de los valores evaluados en las series de datos y sin extrapolación. Para ello, al rededor de la envolvente se genera un buffer o área aferente, utilizando p. ej. 1/20 de la menor extensión horizontal o vertical del polígono que delimita la zona a evaluar.

Para conocer el tamaño de la extensión de _ZonaEstudioEnvelope.shp_, clic derecho en la tabla de contenido y _Properties_, ir a la pestaña _Source_ y ampliar la información de _Extent_. Para esta capa los límites geográficos expresados en grados decimales son: norte 10.940833°, sur 8.662500°, oeste -74.315834° y este -72.808322°.  

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0ZonaEstudioEnvelopeExtent.png)

* Ancho (este - oeste ) = -72.808322° - -74.315834° =  1.507512°  
* Alto (norte - sur) = 10.940833° - 8.662500° = 2.278333°  
* Menor dimensión = ancho 1.507512°  
* 1/20 menor dimensión = 0.0753756°

> La relación 1/20 dependerá de la densidad de las estaciones en la zona de frontera del polígono envolvente. Si existen pocas estaciones, se recomienda disminuir esta relación, p. ej. 1/10 o menos y si por contrario, la red es muy densa, aumentar la relación a 1/30 o más. Luego de crear el polígono, evaluar visualmente si las estaciones son suficientes para cubrir la extensión espacial del área hidrográfica en estudio, de lo contrario, ampliar el polígono.

6. Utilizando la herramienta _Geoprocessing / Analysis Tools / Proximity / Buffer_, cree un polígono aferente a la zona de estudio utilizando la relación 1/20 de la dimensión más corta correspondiente a 0.0753756°. Nombrar como _[ZonaEstudioBufferStation.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudioBufferStation.zip)_ en la carpeta _.shp_. Como puede observar, las esquinas obtenidas son redondeadas y debido a que este polígono únicamente será usado para seleccionar las estaciones de la zona de estudio y no para recortar los MDE o mapas interpolados, no es necesario generar un polígono envolvente.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0ZonaEstudioBufferStation.png)

7. Desde el menú _Map / Selection / Select By Location_, seleccione todas aquellas estaciones del catálogo nacional de estaciones y de otras entidades que se intersecan con la zona de estudio. Para la zona de estudio y la versión descargada de los catálogos, se han seleccionado 315 estaciones del CNE y 125 de otras entidades.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0SelectByLocation.png)

8. Exporte las estaciones seleccionadas a nuevas capas geográficas, clic derecho en CNE_IDEAM / _Data / Export Features_ y nombrar como _[CNE_IDEAM_ZE.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/CNE_IDEAM_ZE.zip)_ dentro de la carpeta _.shp_. Repita este procedimiento para la capa de eventos de las estaciones de otras entidades y nombre como _[CNE_OE_ZE.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/CNE_OE_ZE.zip)_.

> En ArcGIS for Desktop, el procedimiento de exportación se realiza dando clic derecho en la capa y seleccionando la opción _Data / Export Data_. Para el caso de la capa de eventos de las estaciones de otras entidades, se recomienda primiero exportar la capa de eventos en un archivo Shapefile y luego efectuar la selección y exportación de las estaciones de la zona de estudio.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0CNE_IDEAM_ZEExportFeatures.png)  
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0CNE_OE_ZEExportFeatures.png)  
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0CNEZEExportFeaturesMap.png)

9. Con la herramienta _Geoprocessing / Data Management Tools / General / Merge_, combine los archivos de formas _CNE_IDEAM_ZE.shp_ y _CNE_OE_ZE.shp_ en un único archivo y nombre como _[CNE_IDEAM_OE_ZE.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/CNE_IDEAM_OE_ZE.zip)_. La red de estaciones contendrá en total 440 estaciones (315 IDEAM + 125 otras entidades).

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0CNE_IDEAM_OE_ZEMerge.png)





### Referencias

* http://dhime.ideam.gov.co/atencionciudadano/


### Control de versiones

| Versión    | Descripción                                                                             | Autor                                      | Horas |
|------------|:----------------------------------------------------------------------------------------|--------------------------------------------|:-----:|
| 2022.07.02 | xxx                                                                                     | [rcfdtools](https://github.com/rcfdtools)  |  xx   |
| 2022.07.31 | Versión inicial con descarga CNE IDEAM y otras entidades, revisión catálogo de objetos. | [rcfdtools](https://github.com/rcfdtools)  |   4   |



_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Anterior](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/StrDEM)  | [:house: Inicio](https://github.com/rcfdtools/R.LTWB/wiki) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/999) | [Siguiente]() |
|-----------------------------------------------------------------------------|------------------------------------------------------------|-------------------------------------------------------------------------|---------------|

[^1]: http://dhime.ideam.gov.co/atencionciudadano/
[^2]: https://pro.arcgis.com/en/pro-app/latest/help/data/excel/prepare-to-work-with-excel-in-arcgis-pro.htm