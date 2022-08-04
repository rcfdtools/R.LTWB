## Catálogo nacional de estaciones - CNE y selección para la zona de estudio
Keywords: `IDEAM` `Weather Station` `Display XY Data` `Buffer` `Select By Location` `Python`

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
| FECHA_INSTALACION    | datetime64  | Fecha de instalación. FECHA_INST en archivos Shapefile.                                                                                                                                                                                        |
| altitud              | int64       | Altitud o cota sobre el nivel del mar en metros.                                                                                                                                                                                               |
| latitud              | float64     | Latitud en grados decimales.                                                                                                                                                                                                                   |
| longitud             | float64     | Longitud en grados decimales.                                                                                                                                                                                                                  |
| DEPARTAMENTO         | object      | Departamento o zonificación política. Equivalente a estados en otros países. DEPARTAMEN en archivos Shapefile.                                                                                                                                 |
| MUNICIPIO            | object      | Municipio o subzonificación política. Equivalente a condado en otros países.                                                                                                                                                                   |
| AREA_OPERATIVA       | object      | Área operativa que administra la estación. AREA_OPERA en archivos Shapefile.                                                                                                                                                                   |
| AREA_HIDROGRAFICA    | object      | Área hidrográfica a la cual pertenece. AREA_HIDRO en archivos Shapefile.                                                                                                                                                                       |
| ZONA_HIDROGRAFICA    | object      | Zona hidrográfica a la cual pertenece. ZONA_HIDRO en archivos Shapefile.                                                                                                                                                                       |
| observacion          | object      | Observaciones generales. observacio en archivos Shapefile.                                                                                                                                                                                     |
| CORRIENTE            | object      | Corriente, cauce o río próximo o sobre la cuál está localizada la estación.                                                                                                                                                                    |
| FECHA_SUSPENSION     | datetime64  | Fecha de suspensión. FECHA_SUSP en archivos Shapefile.                                                                                                                                                                                         |
| SUBZONA_HIDROGRAFICA | object      | Subzona hidrográfica a la cual pertenece.SUBZONA_HI en archivos Shapefile.                                                                                                                                                                     |
| ENTIDAD              | object      | Entidad encargada.                                                                                                                                                                                                                             |
| subred               | object      | Subred a la cual pertenece.                                                                                                                                                                                                                    |

> Los atributos presentados en la tabla, su tipo de escritura y notación han sido tomados del archivo original y no se encuentran normalizados a 11 caracteres para garantizar la compatibilidad con el formato .dbf. Se puede observar que los datos volcados en el archivo CNE_IDEAM.xls han sido generados utilizando la herramienta _Table to Table_ de ArcGIS desde una Geodatabase que permite la definición de atributos con más de 11 caracteres. 
> 
> Los atributos del catálogo nacional de estaciones y de otras entidades son equivalentes. Catálogos exportados a archivos de formas Shapefile utilizan máximo 10 caracteres en la definición de atributos.


### Definiciones generales del catálogo nacional de estaciones

Tomado de [Anexo 2 - Definiciones CNE](http://www.ideam.gov.co/documents/10182/557765/Definiciones+CNE.pdf) del IDEAM.


#### Categorías de las estaciones

| Categoría                        | Abrv. | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|:---------------------------------|:-----:|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Estación Agrometeorológica       |  AM   | En esta estación se realizan observaciones meteorológicas y otras observaciones que ayudan a determinar las relaciones entre el clima, por una parte y la vida de las plantas y los animales por la otra. Incluye el mismo programa de observaciones de la estación climatológica principal, más registros de temperatura a varias profundidades (hasta un metro) y en la capa cercana al suelo (0, 10 y 20 cm sobre el suelo).                                                                                     |
| Estación Climatológica Ordinaria |  CO   | Es aquella en la cual se hacen observaciones de precipitación, temperatura del aire, temperaturas máxima y mínima a 2 metros y humedad primordialmente. Poseen muy poco instrumental registrador. Algunas llevan instrumentos adicionales tales como tanque de evaporación, heliógrafo y anemómetro.                                                                                                                                                                                                                |
| Estación Climatológica Principal |  CP   | Es aquella en la cual se hacen observaciones de precipitación, temperatura del aire, temperaturas máxima y mínima a 2 metros, humedad, viento, radiación, brillo solar, evaporación, temperaturas extremas del tanque de evaporación, cantidad de nubes y fenómenos especiales. Gran parte de estos parámetros se obtienen de instrumentos registradores.                                                                                                                                                           |
| Estación Limnigráfica            |  LG   | Estación donde se mide el nivel de una corriente hídrica mediante un aparato registrador de nivel y que grafica una curva llamada limnigrama.                                                                                                                                                                                                                                                                                                                                                                       |
| Estación Limnimétrica            |  LM   | Estación donde se mide el nivel de una corriente hídrica mediante un aparato (mira dividida en centímetros) que mide altura del agua, sin registrarla. Una persona toma el dato y lo registra en una libreta.                                                                                                                                                                                                                                                                                                       |
| Estación Mareográfica            |  MG   | Estaciones para observación del estado del mar. Mide nivel, temperatura y salinidad de las aguas marinas.                                                                                                                                                                                                                                                                                                                                                                                                           |
| Estación Meteorológica especial  |  ME   | Estación instalada para realizar seguimiento a un fenómeno o un fin específico, por ejemplo, las heladas.                                                                                                                                                                                                                                                                                                                                                                                                           |
| Estación Pluviográfica           |  PG   | Es aquella que registra en forma mecánica y continua la precipitación, en una gráfica que permite conocer la cantidad, duración, intensidad y periodo en que ha ocurrido la lluvia. Actualmente se utilizan los pluviógrafos de registro diario.                                                                                                                                                                                                                                                                    |
| Estación Pluviométrica           |  PM   | Es una estación meteorológica dotada de un pluviómetro o recipiente que permite medir la cantidad de lluvia caída entre dos observaciones consecutivas.                                                                                                                                                                                                                                                                                                                                                             |
| Estación Radio Sonda             |  RS   | La estación de radiosonda tiene por finalidad la medición directa de parámetros atmosféricos tales como temperatura del aire, presión atmosférica, humedad relativa y dirección y velocidad del viento en las capas altas de la atmósfera (tropósfera y baja estratósfera), mediante el rastreo, por medios electrónicos, de la trayectoria de un globo meteorológico que asciende libremente y que lleva un dispositivo con los sensores que miden y transmiten la señal con los datos.                            |
| Estación Sinóptica Principal     |  SP   | En este tipo de estación se efectúan observaciones de los principales elementos meteorológicos en horas convenidas internacionalmente. Los datos se toman horariamente y corresponden a nubosidad, dirección y velocidad de los vientos, presión atmosférica, temperatura del aire, tipo y altura de las nubes, visibilidad, fenómenos especiales, características de humedad, precipitación, temperaturas extremas, capas significativas de nubes, recorrido del viento y secuencia de los fenómenos atmosféricos. |
| Estación Sinóptica Secundaria    |  SS   | Al igual que en la estación anterior, las observaciones se realizan a horas convenidas internacionalmente y los datos corresponden comúnmente a visibilidad, fenómenos especiales, tiempo atmosférico, nubosidad, estado del suelo, precipitación, temperatura del aire, humedad del aire, presión y viento.                                                                                                                                                                                                        |


#### Observaciones según la categoría de la estación :new:

En la siguiente tabla preliminar desarrollada por [rcfdtools](https://github.com/rcfdtools), se presentan los tipos de observaciones que pueden ser realizadas por las estaciones dependiendo de su categoría.

| Observación / Categoría                        | AM  | CO  | CP  | LG  | LM  | MG  | ME  | PG  | PM  | RS  | SP  | SS  |
|:-----------------------------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Precipitación                                  | ✓   | ✓   | ✓   |     |     |     |     | ✓   | ✓   |     | ✓   | ✓   |
| Temperatura del aire cerca al suelo            | ✓   | ✓   | ✓   |     |     |     |     |     |     |     | ✓   | ✓   |
| Temperatura máxima del aire a 2 metros         | ✓   | ✓   | ✓   |     |     |     |     |     |     |     |     |     |
| Temperatura mínima del aire a 2 metros         | ✓   | ✓   | ✓   |     |     |     |     |     |     |     |     |     |
| Temperatura del aire en capa alta de atmósfera |     |     |     |     |     |     |     |     |     | ✓   |     |     |
| Temperatura extrema del tanque de evaporación  | ✓   |     | ✓   |     |     |     |     |     |     |     |     |     |
| Temperatura del suelo a varias profundidades   | ✓   |     |     |     |     |     |     |     |     |     |     |     |
| Temperatura del agua                           |     |     |     |     |     | ✓   |     |     |     |     |     |     |
| Temperaturas extremas                          |     |     |     |     |     |     |     |     |     |     | ✓   |     |
| Evaporación                                    | ✓   | ✓   | ✓   |     |     |     |     |     |     |     |     |     |
| Brillo solar                                   | ✓   |     | ✓   |     |     |     |     |     |     |     |     |     |
| Radiación solar                                | ✓   |     | ✓   |     |     |     |     |     |     |     |     |     |
| Humedad del aire cerca al suelo                | ✓   | ✓   | ✓   |     |     |     |     |     |     |     | ✓   | ✓   |
| Humedad relativa en capa alta de atmósfera     |     |     |     |     |     |     |     |     |     | ✓   |     |     |
| Humedad - Características                      |     |     |     |     |     |     |     |     |     |     | ✓   |     |
| Viento - Dirección                             | ✓   |     | ✓   |     |     |     |     |     |     |     | ✓   | ✓   |
| Viento - Velocidad                             | ✓   |     | ✓   |     |     |     |     |     |     |     | ✓   | ✓   |
| Viento - Recorrido                             | ✓   |     | ✓   |     |     |     |     |     |     |     | ✓   | ✓   |
| Viento - Dirección en capa alta de atmósfera   |     |     |     |     |     |     |     |     |     | ✓   |     |     |
| Viento - Velocidad en capa alta de atmósfera   |     |     |     |     |     |     |     |     |     | ✓   |     |     |
| Presión en capa alta de atmósfera              |     |     |     |     |     |     |     |     |     | ✓   |     |     |
| Presión atmosférica cercana al suelo           |     |     |     |     |     |     |     |     |     |     | ✓   | ✓   |
| Nubosidad - Octas                              | ✓   |     | ✓   |     |     |     |     |     |     |     | ✓   | ✓   |
| Nubosidad - Tipo                               |     |     |     |     |     |     |     |     |     |     | ✓   |     |
| Nubosidad - Altura de nubes                    |     |     |     |     |     |     |     |     |     |     | ✓   |     |
| Nubosidad - Capas significativas               |     |     |     |     |     |     |     |     |     |     | ✓   |     |
| Visibilidad                                    |     |     |     |     |     |     |     |     |     |     | ✓   | ✓   |
| Nivel lámina agua                              |     |     |     | ✓   | ✓   | ✓   |     |     |     |     |     |     |
| Heladas                                        |     |     |     |     |     |     | ✓   |     |     |     |     |     |
| Secuencia fenómenos atmosféricos               |     |     |     |     |     |     |     |     |     |     | ✓   | ✓   |
| Tiempo atmosférico                             |     |     |     |     |     |     |     |     |     |     |     | ✓   |
| Estado del suelo                               |     |     |     |     |     |     |     |     |     |     |     | ✓   |
| Salinidad agua marina                          |     |     |     |     |     | ✓   |     |     |     |     |     |     |
| Fenómenos especiales                           | ✓   |     | ✓   |     |     |     | ✓   |     |     |     | ✓   | ✓   |
| Tanque evaporación (no siempre)                |     | ✓   | ✓   |     |     |     |     |     |     |     |     |     |
| Heliógrafo (no siempre)                        |     | ✓   |     |     |     |     |     |     |     |     |     |     |
| Anenómetro (no siempre)                        |     | ✓   |     |     |     |     |     |     |     |     |     |     |


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
|  1100  |     En revisión     |
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


### Procedimiento general descarga del catálogo nacional de estaciones CNE

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

> Para el cargue de archivos de Microsoft Excel en formato .xls, se requiere del [Driver de Microsoft Access Database Engine](https://www.microsoft.com/en-us/download/confirmation.aspx?id=54920)[^2].


### Creación del polígono para selección de estaciones

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


### Selección, exportación e integración de estaciones dentro y al rededor de la zona de estudio

7. Desde el menú _Map / Selection / Select By Location_, seleccione todas aquellas estaciones del catálogo nacional de estaciones y de otras entidades que se intersecan con la zona de estudio. Para la zona de estudio y la versión descargada de los catálogos, se han seleccionado 315 estaciones del CNE y 125 de otras entidades.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0SelectByLocation.png)

8. Exporte las estaciones seleccionadas a nuevas capas geográficas, clic derecho en CNE_IDEAM / _Data / Export Features_ y nombrar como _[CNE_IDEAM_ZE.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/CNE_IDEAM_ZE.zip)_ dentro de la carpeta _.shp_. Repita este procedimiento para la capa de eventos de las estaciones de otras entidades y nombre como _[CNE_OE_ZE.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/CNE_OE_ZE.zip)_.

> En ArcGIS for Desktop, el procedimiento de exportación se realiza dando clic derecho en la capa y seleccionando la opción _Data / Export Data_. Para el caso de la capa de eventos de las estaciones de otras entidades, se recomienda primiero exportar la capa de eventos en un archivo Shapefile y luego efectuar la selección y exportación de las estaciones de la zona de estudio.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0CNE_IDEAM_ZEExportFeatures.png)  
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0CNE_OE_ZEExportFeatures.png)  
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0CNEZEExportFeaturesMap.png)

9. Con la herramienta _Geoprocessing / Data Management Tools / General / Merge_, combine los archivos de formas _CNE_IDEAM_ZE.shp_ y _CNE_OE_ZE.shp_ en un único archivo y nombre como _[CNE_IDEAM_OE_ZE.shp](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/CNE_IDEAM_OE_ZE.zip)_. Asegúrese de marcar la casilla `Add source information to output` para obtener el campo de atributos `MERGE_SRC` que describe la capa fuente y de clic en la opción _Reset_ ubicada a la derecha de `Field Map` . La red de estaciones contendrá en total 440 estaciones (315 IDEAM + 125 otras entidades).

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0CNE_IDEAM_OE_ZEMerge.png)


### Estudio de longitud hipotética de series

10. Una vez obtenida la red de estaciones integrada sobre la zona de estudio, es necesario estudiar la longitud hipotética de las series a partir de las fechas de instalación y suspensión registradas en el catálogo. 

> Este procedimiento es importante debido a que para la descarga de las series de datos registradas en las estaciones, es necesario primero conocer la homogeneidad en las longitudes hipotética de los registros que deberían tener las estaciones a partir de su fecha de puesta en operación y recolección de datos. Por ejemplo, si la mayoría de las estaciones tienen un registro continuo y actual de al menos 20 años y en las estaciones de la zona de estudio existen estaciones recientes o antiguas suspendidas con registros cortos (p. ej. 5 años), se podrían descartar estas estaciones del análisis, siempre y cuando no correspondan a estaciones en la zona de frontera geográfica de la zona en estudio.

En la capa _CNE_IDEAM_OE_ZE.shp_, crear los siguientes campos de atributos:

| Campo    | Tipo           | Descripción                                                                                 |
|:---------|:---------------|---------------------------------------------------------------------------------------------|
| LYearS   | Numérico doble | Campo para longitud hipotética de serie a partir de las fechas de instalación y suspensión. |
| LYearSTW | Numérico doble | Campo para longitud hipotética de serie a partir de una ventana de tiempo definida.         |

En la tabla de atributos dar clic en el botón _Field: Add_ y desde el modo de edición agregar los campos indicados, luego desde el Menú superior _Fields_, dar clic en _Save_. 

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0AddField.png)

> En ArcGIS for Desktop, desde las propiedades de la tabla de atributos seleccionar la opción _Add Field_.

**Cálculo independiente del campo LYears**

El cálculo del campo `LYearS` puede ser realizado dando clic en la cabecera del campo y seleccionando la opción _Calculate Field_ utilizando la instrucción Python 3 `(!FECHA_INST!-!FECHA_SUSP!)/365`, sin embargo, no podrá ser aplicada a estaciones que se encuentran suspendidas debido a que el campo fecha de suspensión contendrá valores nulos, por lo que Python devolverá un error y no realizará el cálculo solicitado.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0CalculareFieldLYearSError.png)

> En ArcGIS for Desktop puede usar la expresión VBScript `( [FECHA_SUSP] - [FECHA_INST] )/365`.

Configuración regional requerida: en el _Panel de Control / Region_, establezca el formato de fechas cortas como d/MM/yyyy.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/Windows11ControlPanlRegionFormat.png)

Para realizar correctamente este cálculo, es necesario considerar la fecha final de los registros de las estaciones que se encuentran en operación, para este ejemplo, la fecha de corte corresponde al último día del año inmediatamente anterior correspondiente a 2021.12.31 considerando que para el análisis climatológico, únicamente utilizaremos datos de años hidrologicamente completos. La longitud de series en años usando Python a través de Calculate Field para el campo LYearS, puede ser realizada a través de Code Block utilizando las siguientes instrucciones:

Pre-Logic Script Code para Python 2 sobre ArcGIS for Desktop y Python 3 sobre ArcGIS Pro: 
```
from datetime import datetime
date_format = '%d/%m/%Y'
tw_end_date = '31/12/2021' # Time window end
is_python3 = True # True for Python 3, False for Python2
if is_python3:
    tw_end_date = datetime.strptime(tw_end_date, date_format)
def len_years_serie(installation_date, suspension_date):
    if not installation_date:
        installation_date = tw_end_date
        suspension_date = tw_end_date
    if not suspension_date:
        suspension_date = tw_end_date
    if is_python3:
        diff_date = suspension_date - installation_date
    else:
        diff_date = datetime.strptime(suspension_date, date_format) - datetime.strptime(installation_date, date_format)
    return float(diff_date.days)/365
```

LYearS:
```
len_years_serie(!FECHA_INST!, !FECHA_SUSP!)
```

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0CalculareFieldLYearSPython.png)

En ArcGIS for Desktop pudede dar clic derecho sobre la cabecera del campo `LYearS` y seleccionar la opción _Field Calculator_ o desde _ArcToolBox / Data Management Tools / Fields / Calculate Field_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISDesktop10.2.2CalculareFieldLYearSPython.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISDesktop10.2.2CalculareFieldLYearSPythonA.png)

> La variable booleana `is_python3` es utilizada para definir la versión de Python desde la cual se hace el llamado del Script.
> 
> Python 2 sobre ArcGIS for Desktop transfiere como texto las variables FECHA_INST y FECHA_SUSP en formato unicode, es por ello que deben ser convertidas a formato de fecha para poder calcular la diferencia en días. Cuando en la tabla de atributos las fechas son almacenadas como cadenas de texto, puede definir la variable `is_python3 = False` para realizar el cálculo de diferencias en Python 2 o 3.

De clic derecho en la cabecera del campo `LYearS` y seleccione la opción _Statistics_, obtendrá un resumen estadístico y una gráfica con las longitudes hipotéticas en años para cada estación. Como puede observar, la media de las longitudes es de 24.8 años con una alta desviación estándar correspondiente a 22.6 años y múltiples estaciones tienen registros cortos de menos de 10 años.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0LYearSStatistics.png)

Utilizando la tecla <kbd>Ctrl</kbd> + <kbd>clic</kbd>, seleccione las barras correspondientes a los valores de la media y superiores, obtendrá que 158 estaciones contienen longitudes hipotéticas iguales o superiores a 38.3 años dentro y al rededor de la zona de estudio.    

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0LYearSStatisticsA.png)

**Cálculo simultáneo de campos LYears y LYearsTW**

Para realizar el cálculo de longitudes hipotéticas de series a partir de una ventana de tiempo definida, p. ej. del 01/01/1980 al 31/12/2021 correspondiente a 42.027397 años, utilizar el siguiente código.

Pre-Logic Script Code para Python 2 sobre ArcGIS for Desktop: 
```
from datetime import datetime
date_format = '%d/%m/%Y'
tw_start_date = '01/01/1980' # Time-window start. Use '' for set 01/01/1900
tw_end_date = '31/12/2021' # Time-window end. Use '' for use the current date and prevent over-time wrong suspension dates
if not tw_start_date: tw_start_date = '01/01/1900'
if not tw_end_date: tw_end_date = str(datetime.today().date())
def len_years_serie(installation_date, suspension_date):
    if installation_date:
        if datetime.strptime(installation_date, date_format) <= datetime.strptime(tw_start_date, date_format):
            tw_installation_date = tw_start_date
        else:
            tw_installation_date = installation_date
        if suspension_date:
            if datetime.strptime(suspension_date, date_format) >= datetime.strptime(tw_end_date, date_format):
                tw_suspension_date = tw_end_date
            else:
                tw_suspension_date = suspension_date
            diff_date = datetime.strptime(suspension_date, date_format) - datetime.strptime(installation_date, date_format)
            tw_diff_date = datetime.strptime(tw_suspension_date, date_format) - datetime.strptime(tw_installation_date, date_format)
        else:
            diff_date = datetime.strptime(tw_end_date, date_format) - datetime.strptime(installation_date, date_format)
            tw_diff_date = datetime.strptime(tw_end_date, date_format) - datetime.strptime(tw_installation_date, date_format)
        diff_date = float(diff_date.days)/365
        tw_diff_date = float(tw_diff_date.days)/365
        if diff_date < 0: diff_date = 0
        if tw_diff_date < 0: tw_diff_date = 0
    else:
        diff_date = 0
        tw_diff_date = 0
    return diff_date, tw_diff_date # First value is complete length. Second value is time window length
```

Pre-Logic Script Code para Python 3 sobre ArcGIS Pro: 
```
from datetime import datetime
date_format = '%d/%m/%Y'
tw_start_date = datetime.strptime('01/01/1980', date_format)# Time-window start. Use '' for set 01/01/1900
tw_end_date = datetime.strptime('31/12/2021', date_format) # Time-window end. Use '' for use the current date and prevent over-time wrong suspension dates
if not tw_start_date: tw_start_date = datetime.strptime('01/01/1900', date_format)
if not tw_end_date: tw_end_date = str(datetime.today().date())
def len_years_serie(installation_date, suspension_date):
    if installation_date:
        if installation_date <= tw_start_date:
            tw_installation_date = tw_start_date
        else:
            tw_installation_date = installation_date
        if suspension_date:
            if suspension_date >= tw_end_date:
                tw_suspension_date = tw_end_date
            else:
                tw_suspension_date = suspension_date
            diff_date = suspension_date - installation_date
            tw_diff_date = tw_suspension_date - tw_installation_date
        else:
            diff_date = tw_end_date - installation_date
            tw_diff_date = tw_end_date - tw_installation_date
        diff_date = float(diff_date.days)/365
        tw_diff_date = float(tw_diff_date.days)/365
        if diff_date < 0: diff_date = 0
        if tw_diff_date < 0: tw_diff_date = 0
    else:
        diff_date = 0
        tw_diff_date = 0
    return diff_date, tw_diff_date # First value is complete length. Second value is time window length
```

LYearS:
```
len_years_serie(!FECHA_INST!, !FECHA_SUSP!)[0]
```

LYearSTW:
```
len_years_serie(!FECHA_INST!, !FECHA_SUSP!)[1]
```

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISDesktop10.2.2CalculareFieldLYearSTWPython.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0CalculareFieldLYearSPythonA.png)
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0CalculareFieldLYearSTWPython.png)

Desde las propiedades de la capa _CNE_IDEAM_OE_ZE.shp_ y a través del _Definition Query_, filtre todas aquellas estaciones cuya longitud hipotética de registro dentro de la ventana de tiempo sea mayor a cero `LYearSTW > 0`.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0LYearSTWDefinitionQuery.png)

De clic derecho en la cabecera del campo `LYearSTW` y seleccione la opción _Statistics_, obtendrá un resúmen estadístico y una gráfica con las longitudes hipotéticas en años para cada estación dentro de la ventana de tiempo establecida. Como puede observar, la media de las longitudes hipotéticas es de 29.8 años con una desviación estándar de 16.1 años. Utilizando la tecla <kbd>Ctrl</kbd> + <kbd>clic</kbd>, seleccione las barras del histograma a partir de la media, obtendrá 174 de 263 estaciones con registros iguales o superiores a 29.5 años de registro y podrá observar simultáneamente su localización dentro y al rededor de la zona de estudio.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0LYearSTWStatistics.png)

Simbolice las estaciones por categoría a partir del campo `CATEGORIA` para las estaciones con longitudes hipotéticas dentro de la ventana de tiempo establecida y cree una gráfica de barras por categoría, podrá observar que el mayor número de estaciones corresponde a la categoría Pluviométricas.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0BarGraphCategoria.png)


### Identificación de estaciones con datos de precipitación

Las longitudes hipotéticas de registros en estaciones evaluadas previamente, corresponden a diferentes categorías. En el caso específico de la precipitación, los registros pueden ser obtenidos de estaciones Agrometeorológicas, Climatológicas Ordinarias, Climatológicas Principales, Pluviográficas, Pluviométricas, Sinópticas Principales y Sinópticas Secundarias.

Desde las propiedades de la capa _CNE_IDEAM_OE_ZE.shp_ y a través del _Definition Query_, filtre las estaciones de las categorías indicadas y represente por símbolos graduados en 3 clases por cortes naturales a partir de las longitudes hipotéticas de series dentro de la ventana de tiempo calculada en el campo `LYearSTW`. Visualice a escala 1:2,250,000 (en monitores FHD 1920 x 1080p). Podrá observar que para las categorías indicadas se obtienen 325 estaciones.

Expresión SQL: `CATEGORIA IN ('Agrometeorológica', 'Climática Ordinaria', 'Climática Principal', 'Pluviográfica', 'Pluviométrica', 'Sinóptica Principal', 'Sinóptica Secundaria')`

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0LYearSTWRainQuery1.png)

Desde las propiedades de la capa _CNE_IDEAM_OE_ZE.shp_ y a través del _Definition Query_, filtre todas aquellas estaciones cuya longitud hipotética de registro dentro de la ventana de tiempo sea mayor a 10, 15, 20, 25, 30, 35 años para las categorías indicadas y evalúe mediante una estadística sobre el campo `LYearSTW`, la media de las longitudes hipotéticas de las series y obtenga los estadísticos característicos.

Expresión SQL para series >= 10 años : `LYearSTW >= 10 And CATEGORIA IN ('Agrometeorológica', 'Climática Ordinaria', 'Climática Principal', 'Pluviográfica', 'Pluviométrica', 'Sinóptica Principal', 'Sinóptica Secundaria')`

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0LYearSTWRainQueryCategory.png)

| Series >= 10 y 25 años                                                                                                                                                                                                                                                                                                            | Series >= 15 y 30 años                                                                                                                                                                                                                                                                                                            | Series >= 20 y 35 años                                                                                                                                                                                                                                                                                                            |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Longitud hipotética en años >= 10<br>Cubrimiento: sobre toda la zona de estudio<br>Estaciones encontradas: 139<br>Media: 37.1 años<br>Mínimo: 10.3 años<br>Máximo: 42 años<br>Desv. Est.: 9 años<br>![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0LYearSTWRain10.png)    | Longitud hipotética en años >= 15<br>Cubrimiento: sobre toda la zona de estudio<br>Estaciones encontradas: 132<br>Media: 38.4 años<br>Mínimo: 15 años<br>Máximo: 42 años<br>Desv. Est.: 7.1 años<br>![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0LYearSTWRain15.png)    | Longitud hipotética en años >= 20<br>Cubrimiento: sobre toda la zona de estudio<br>Estaciones encontradas: 124<br>Media: 39.8 años<br>Mínimo: 22.1 años<br>Máximo: 42 años<br>Desv. Est.: 4.6 años<br>![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0LYearSTWRain20.png)  |
| Longitud hipotética en años >= 25<br>Cubrimiento: sobre toda la zona de estudio<br>Estaciones encontradas: 119<br>Media: 40.5 años<br>Mínimo: 26.6 años<br>Máximo: 42 años<br>Desv. Est.: 3.17 años<br>![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0LYearSTWRain25.png) | Longitud hipotética en años >= 30<br>Cubrimiento: sobre toda la zona de estudio<br>Estaciones encontradas: 116<br>Media: 40.8 años<br>Mínimo: 30.5 años<br>Máximo: 42 años<br>Desv. Est.: 2.54 años<br>![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0LYearSTWRain30.png) | Longitud hipotética en años >= 35<br>Cubrimiento: sobre toda la zona de estudio<br>Estaciones encontradas: 109<br>Media: 41.3 años<br>Mínimo: 35.1 años<br>Máximo: 42 años<br>Desv. Est.: 1.58 años<br>![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0LYearSTWRain35.png) |

Simboloce las estaciones por categorías y cree un gráfico de barras que represente las estaciones y la longitud hipotética de las series en la ventana de tiempo definida >= 10 años, ordene descendentemente. Podrá observar que mayoritariamente las estaciones pluviométricas y climáticas ordinarias son las que pueden contener los registros más extensos.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0LYearSTWRainQueryCategoryGraph.png)

Para el desarrollo del caso de estudio, utilizaremos las estaciones con registros de precipitación cuyas longitudes hipotéticas sean >= a 10 años que mayoritariamente se encuentran en el último rango de cortes naturales con valores superiores a 26.649315 años. En actividades posteriores analizaremos el traslapo entre las series reales y evaluaremos que estaciones requerirán ser completadas y/o extendidas.


### Identificación de estaciones con datos de temperatura del aire cerca al suelo

En el caso específico de la temperatura del áire cerca a la superficie del suelo, los registros pueden ser obtenidos de estaciones Agrometeorológicas, Climatológicas Ordinarias, Climatológicas Principales, Sinópticas Principales y Sinópticas Secundarias.

Desde las propiedades de la capa _CNE_IDEAM_OE_ZE.shp_ y a través del _Definition Query_, filtre las estaciones de las categorías indicadas y represente por símbolos graduados en 3 clases por cortes naturales a partir de las longitudes hipotéticas de series dentro de la ventana de tiempo calculada en el campo `LYearSTW`. Visualice a escala 1:2,250,000 (en monitores FHD 1920 x 1080p). Podrá observar que para las categorías indicadas se obtienen 71 estaciones.

Expresión SQL: `CATEGORIA IN ('Agrometeorológica', 'Climática Ordinaria', 'Climática Principal', 'Sinóptica Principal', 'Sinóptica Secundaria')`

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0LYearSTWTemperatureAirQuery1.png)

Desde las propiedades de la capa _CNE_IDEAM_OE_ZE.shp_ y a través del _Definition Query_, filtre todas aquellas estaciones cuya longitud hipotética de registro dentro de la ventana de tiempo sea mayor a 5 años para las categorías indicadas y evalúe mediante una estadística sobre el campo `LYearSTW`, la media de las longitudes hipotéticas de las series y obtenga los estadísticos característicos.

Expresión SQL para series >= 5 años : `LYearSTW >= 5 And CATEGORIA IN ('Agrometeorológica', 'Climática Ordinaria', 'Climática Principal', 'Sinóptica Principal', 'Sinóptica Secundaria')`

| Series >= 5 años                                                                                                                                                                                                                                                                                                                     |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Longitud hipotética en años >= 5<br>Cubrimiento: sobre toda la zona de estudio<br>Estaciones encontradas: 42<br>Media: 23.8 años<br>Mínimo: 5 años<br>Máximo: 42 años<br>Desv. Est.: 15.7 años<br>![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0LYearSTWTemperatureAir5.png) |

Como observa, existen dentro y al rededor de la zona de estudio tan solo 42 estaciones con longitudes hipotéticas de registro superiores a 5 años, de las cuales 19 tienen longitudes por encima de la media.

> Es importante considerar que existen estaciones sobre y alrededor de la zona de estudio, sin embargo, un factor importante a considerar es el rango de elevaciones de las estaciones debido a la alta correlación que existe entre estos dos parámetros.

Representando las estaciones por símbolos graduados, podrá observar que el rango disponible de elevaciones a partir del campo `altitud` registrado por el IDEAM corresponde a valores entre 18 y 2256 m.s.n.m. y en la Serranía del Perijá al este de la zona de estudio, las elevaciones de terreno son mayores. De las 42 estaciones disponibles, tan solo 1 se encuentra por encima de los 2000 m.s.n.m.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0LYearSTWTemperatureAirQueryElevation.png)

Simboloce las estaciones por categorías y cree un gráfico de barras que represente las estaciones y la longitud hipotética de las series en la ventana de tiempo definida >= 5 años, ordene descendentemente. Podrá observar que mayoritariamente las estaciones climáticas ordinarias y climáticas principales son las que pueden contener los registros más extensos.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0LYearSTWTemperatureAirQueryCategoryGraph.png)


### Identificación de estaciones con datos de evaporación potencial

En el caso específico de la evaporación potencial, los registros pueden ser obtenidos de estaciones Agrometeorológicas, Climatológicas Ordinarias y Climatológicas Principales.

Desde las propiedades de la capa _CNE_IDEAM_OE_ZE.shp_ y a través del _Definition Query_, filtre las estaciones de las categorías indicadas y represente por símbolos graduados en 3 clases por cortes naturales a partir de las longitudes hipotéticas de series dentro de la ventana de tiempo calculada en el campo `LYearSTW`. Visualice a escala 1:2,250,000 (en monitores FHD 1920 x 1080p). Podrá observar que para las categorías indicadas se obtienen 70 estaciones.

Expresión SQL: `CATEGORIA IN ('Agrometeorológica', 'Climática Ordinaria', 'Climática Principal')`

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0LYearSTWEvaporationQuery.png)

Desde las propiedades de la capa _CNE_IDEAM_OE_ZE.shp_ y a través del _Definition Query_, filtre todas aquellas estaciones cuya longitud hipotética de registro dentro de la ventana de tiempo sea mayor a 5 años para las categorías indicadas y evalúe mediante una estadística sobre el campo `LYearSTW`, la media de las longitudes hipotéticas de las series y obtenga los estadísticos característicos.

Expresión SQL para series >= 5 años : `LYearSTW >= 5 And CATEGORIA IN ('Agrometeorológica', 'Climática Ordinaria', 'Climática Principal')`

| Series >= 5 años                                                                                                                                                                                                                                                                                                                   |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Longitud hipotética en años >= 5<br>Cubrimiento: sobre toda la zona de estudio<br>Estaciones encontradas: 41<br>Media: 24.2 años<br>Mínimo: 5 años<br>Máximo: 42 años<br>Desv. Est.: 15.6 años<br>![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0LYearSTWEvaporation5.png)  |

Como observa, existen dentro y al rededor de la zona de estudio tan solo 41 estaciones con longitudes hipotéticas de registro superiores a 5 años, de las cuales 19 tienen longitudes por encima de la media.

Simboloce las estaciones por categorías y cree un gráfico de barras que represente las estaciones y la longitud hipotética de las series en la ventana de tiempo definida >= 5 años, ordene descendentemente. Podrá observar que mayoritariamente las estaciones climáticas ordinarias y climáticas principales son las que pueden contener los registros más extensos.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0LYearSTWEvaporationQueryCategoryGraph.png)


### Identificación de estaciones con datos de nivel de lámina de agua en ríos

Una vez sea realizado el balance hidrológico de largo plazo y se obtengan los caudales medios, estos podrán ser comparados con los registros medios de las series de caudales obtenidos a partir de los datos obtenidos en estaciones limnimétricas y/o limnigráficas. 

Desde las propiedades de la capa _CNE_IDEAM_OE_ZE.shp_ y a través del _Definition Query_, filtre las estaciones de las categorías indicadas y represente por símbolos graduados en 3 clases por cortes naturales a partir de las longitudes hipotéticas de series dentro de la ventana de tiempo calculada en el campo `LYearSTW`. Visualice a escala 1:2,250,000 (en monitores FHD 1920 x 1080p). Podrá observar que para las categorías indicadas se obtienen 65 estaciones.

Expresión SQL: `CATEGORIA IN ('Limnimétrica', 'Limnigráfica')`

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0LYearSTWWaterLevelQuery.png)

Desde las propiedades de la capa _CNE_IDEAM_OE_ZE.shp_ y a través del _Definition Query_, filtre todas aquellas estaciones cuya longitud hipotética de registro dentro de la ventana de tiempo sea mayor a 5 años para las categorías indicadas y evalúe mediante una estadística sobre el campo `LYearSTW`, la media de las longitudes hipotéticas de las series y obtenga los estadísticos característicos.

Expresión SQL para series >= 5 años : `LYearSTW >= 5 And CATEGORIA IN ('Limnimétrica', 'Limnigráfica')`

| Series >= 5 años                                                                                                                                                                                                                                                                                                                 |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Longitud hipotética en años >= 5<br>Cubrimiento: sobre toda la zona de estudio<br>Estaciones encontradas: 65<br>Media: 37.3 años<br>Mínimo: 7.3 años<br>Máximo: 42 años<br>Desv. Est.: 10 años<br>![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0LYearSTWWaterLevel5.png) |

Como observa, existen dentro y al rededor de la zona de estudio 65 estaciones con longitudes hipotéticas de registro superiores a 5 años, de las cuales 51 tienen longitudes por encima de la media.

Simboloce las estaciones por categorías y cree un gráfico de barras que represente las estaciones y la longitud hipotética de las series en la ventana de tiempo definida >= 5 años, ordene descendentemente. Podrá observar que las estaciones limnimétricas y limnigráficas poseen registros extensos.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStation/Screenshot/ArcGISPro3.0.0LYearSTWWaterLevelQueryCategoryGraph.png)


### Solución de errores :lady_beetle:

* [ArcGIS Pro tarda mucho tiempo en abrir mi proyecto.](https://github.com/rcfdtools/R.LTWB/discussions/13) 


### Referencias

* http://dhime.ideam.gov.co/atencionciudadano/


### Control de versiones

| Versión    | Descripción                                                                                                                                                                                                                                                                                                                                  | Autor                                      | Horas |
|------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|:-----:|
| 2022.08.04 | Gráficos de análisis de estaciones con registros de precipitación para longitudes hipotéticas mayores a 10, 15, 20, 25, 30, 35 años. Análisis de temperatura, evaporación potencial y altura de lámina de agua para longitudes >= 5 años. Documentación.                                                                                     | [rcfdtools](https://github.com/rcfdtools)  |   6   |
| 2022.08.03 | Cálculo de longitud hipotética de series dentro de la ventana de tiempo definida sobre Python 2 y 3 en ArcGIS for Desktop y ArcGIS Pro. Gráficas de análisis genera de series. Documentación.  Tabla con tipos de observaciones que pueden ser realizadas por las estaciones dependiendo de su categoría.                                    | [rcfdtools](https://github.com/rcfdtools)  |  4.5  |
| 2022.08.02 | Definición de longitud de aferencia a partir de la menor dimensión horizontal o vertical, creación de buffer, selección de estaciones por localización, exportación de estaciones IDEAM y otras entidades, unión de estaciones en capa única, cálculo de longitud hipotética de serie sobre Python 2 y 3 en ArcGIS for Desktop y ArcGIS Pro. | [rcfdtools](https://github.com/rcfdtools)  |   6   |
| 2022.08.31 | Versión inicial con descarga CNE IDEAM y otras entidades, revisión catálogo de objetos.                                                                                                                                                                                                                                                      | [rcfdtools](https://github.com/rcfdtools)  |   4   |

_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Anterior](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/StrDEM)  | [:house: Inicio](https://github.com/rcfdtools/R.LTWB/wiki) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/999) | [Siguiente]() |
|-----------------------------------------------------------------------------|------------------------------------------------------------|-------------------------------------------------------------------------|---------------|

[^1]: http://dhime.ideam.gov.co/atencionciudadano/
[^2]: https://pro.arcgis.com/en/pro-app/latest/help/data/excel/prepare-to-work-with-excel-in-arcgis-pro.htm