## Catálogo nacional de estaciones - CNE y selección para la zona de estudio
Keywords: `IDEAM` `Weather Station` `Display XY Data`

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
* [Zona de estudio - disolución de polígonos zona hidrográfica 28 - Cesar. ](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudio.zip)[:mortar_board:Aprender.](https://github.com/rcfdtools/R.LTWB/tree/main/Section01/CaseStudy)
* [Zona de estudio - envolvente regular de los polígonos de la zona hidrográfica 28 - Cesar. ](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudioEnvelope.zip)[:mortar_board:Aprender.](https://github.com/rcfdtools/R.LTWB/tree/main/Section01/CaseStudy)

> xxxxxxxxxxxxxxDebido a que es necesario incluir diferentes estaciones al rededor de la zona hidrográgica de estudio para garantizar la extensión espacial de los mapas interpolados para cada variable climatológica requerida, en esta actividad no se especifica el listado de las estaciones a utilizar y en la sección 3 de este curso se presenta el proceso detallado de selección espacial de estas estaciones.

El [Instituto de Hidrología, Meteorología y Estudios Ambientales - IDEAM](http://www.ideam.gov.co/) de Colombia, adscrito al [Ministerio de Medio Ambiente - Minambiente](https://www.minambiente.gov.co/), es la entidad nacional encargada registrar y mantener la información hidrometeorológica del país, incluida la localización y clasificación de la red de estaciones que hace parte del [Catálogo Nacional de Estaciones - CNE](http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls). A través del servicio de [Solicitud de Información](http://www.ideam.gov.co/solicitud-de-informacion) o a través del portal [DHIME](http://dhime.ideam.gov.co/atencionciudadano/) del IDEAM desde la pestaña _Recursos_, personas naturales o jurídicas, pueden obtener no solamente los catálogos, sino también las capas geográficas y los registros discretos registrados en cada estación.

### Atributos que componen el catálogo nacional de estaciones

Tomados directamente del archivo [CNE_IDEAM.xls](http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls) v20220731.

| Atributo             | Tipo        | Descripción                                                                                                                                                                                                                                    |
|:---------------------|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OBJECTID             | int64       | Identificador de objeto espacial proveniente de la GDB IDEAM.                                                                                                                                                                                  |
| CODIGO               | int64       | Código de la estación.                                                                                                                                                                                                                         |
| nombre               | object      | Nombre de la estación. Incluye el código de la estación entre corchetes.                                                                                                                                                                       |
| CATEGORIA            | object      | Categoría de la estación: Pluviométrica, Limnimétrica, Limnigráfica, Climática Ordinaria, Climática Principal, Pluviográfica, Meteorológica Especial, Agrometeorológica, Sinóptica Principal, Radio Sonda, Mareográfica, Sinóptica Secundaria. |
| TECNOLOGIA           | object      | Tecnología para captura, registro y transmisión: Convencional, Automática con Telemetría, Automática sin Telemetría.                                                                                                                           |
| ESTADO               | object      | Estado de funcionamiento: Activa, Suspendida, En Mantenimiento.                                                                                                                                                                                |
| FECHA_INSTALACION    | datetime64  | Fecha de instalación.                                                                                                                                                                                                                          |
| altitud              | int64       | Altitud o cota sobre el nivel del mar en metros.                                                                                                                                                                                               |
| latitud              | float64     | Latitud en grados decimales.                                                                                                                                                                                                                   |
| longitud             | float64     | Longitud en grados decimales.                                                                                                                                                                                                                  |
| DEPARTAMENTO         | object      | Departamento o zonificación política. Equivalente a estados en otros países.                                                                                                                                                                   |
| MUNICIPIO            | object      | Municipio o subzonificación política. Equivalente a condado en otros países.                                                                                                                                                                   |
| AREA_OPERATIVA       | object      | Área operativa que administra la estación.                                                                                                                                                                                                     |
| AREA_HIDROGRAFICA    | object      | Área hidrográfica a la cual pertenece.                                                                                                                                                                                                         |
| ZONA_HIDROGRAFICA    | object      | Zona hidrográfica a la cual pertenece.                                                                                                                                                                                                         |
| observacion          | object      | Observaciones generales.                                                                                                                                                                                                                       |
| CORRIENTE            | object      | Corriente, cauce o río próximo o sobre la cuál está localizada la estación.                                                                                                                                                                    |
| FECHA_SUSPENSION     | datetime64  | Fecha de suspensión.                                                                                                                                                                                                                           |
| SUBZONA_HIDROGRAFICA | object      | Subzona hidrográfica a la cual pertenece.                                                                                                                                                                                                      |
| ENTIDAD              | object      | Entidad encargada.                                                                                                                                                                                                                             |
| subred               | object      | Subred a la cual pertenece.                                                                                                                                                                                                                    |

> Los atributos presentados en la tabla, su tipo de escritura y notación han sido tomados del archivo original y no se encuentran normalizados a 11 caracteres para garantizar la compatibilidad con el formato .dbf. Se puede observar que los datos volcados en el archivo CNE_IDEAM.xls han sido generados utilizando la herramienta _Table to Table_ de ArcGIS desde una Geodatabase que permite la definición de atributos con más de 11 caracteres. 


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

2. En ArcGIS Pro, cree un proyecto nuevo en blanco en la ruta _D:\R.LTWB\\.map_ y nómbrelo como ArcGISProSection03. Automáticamente, serán generados el mapa de proyecto, la base de datos geográfica en formato .gdb, la carpeta para volcado de informes de registro de importación _ImportLog_ y la carpeta _Index_. Utilizando el Panel de catálogo y desde la sección Folders, realice la conexión a la carpeta D:\R.LTWB. 

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0NewMapProject.png)

3. Desde la carpeta _.shp_, agregue al mapa el archivo shapefile [CNE_IDEAM.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/CNE_IDEAM.zip), [ZonaEstudio.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudio.zip) y [ZonaEstudioEnvelope.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudioEnvelope.zip). Modifique la simbología de representación de _ZonaEstudioEnvelope_ sin relleno - línea contorno rojo - grosor 3 y _ZonaEstudio_ sin relleno - línea contorno negro - grosor 2. Simbolice las estaciones con puntos color gris 30% - sin contorno - tamaño 6, rotular por el campo `CODIGO` y acercar a la zona de estudio. 

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0CNEMap.png)

> Tenga en cuenca que automáticamente ha sido asignado el sistema de coordenadas geográficas MAGNA al proyecto debido a que el Shapefile del CNE contiene integrado este sistema. En cuanto al número de estaciones, para la versión descargada a 20220731, el CNE se compone de 4476 estaciones.

4. Desde la carpeta _.datasets_, agregue el archivo _CNE_OE.xls_ que contiene la localización de estaciones de otras entidades de Colombia y abra la tabla de atributos, podrá observar que a fecha 20220731 la tabla contiene 4620 registros. Dando clic derecho en la tabla y seleccionando la opción _Display XY Data_, cree una tabla de eventos geográficos para representar la localización de estas estaciones. Utilice el sistema de coordenadas _GCS_WGS_1984_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0CNEOEDisplayXYData.png)

Como puede observar en la ilustración, dentro de la zona de estudio existen múltiples estaciones del catálogo de otras entidades. 

> Para el cargue de archivos de Microsoft Excel en formato .xls, se requiere del Driver de Microsoft Access Database Engine[^2] que puede ser descargado desde https://www.microsoft.com/en-us/download/confirmation.aspx?id=54920

5. 


[^1]: http://dhime.ideam.gov.co/atencionciudadano/
[^2]: https://pro.arcgis.com/en/pro-app/latest/help/data/excel/prepare-to-work-with-excel-in-arcgis-pro.htm