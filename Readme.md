<div align="center">
  <img alt="R.LTWB" src=".icons/R.LTWB.svg" width="250px">
  <br><b>Balance hidrológico de largo plazo para estimación de caudales medios usando SIG.</b><br>Long-term water balance by r.cfdtools@gmail.com<br><br>  
</div>


<div align="center">
<br><img alt="R.LTWB" src=".icons/LTWB.png" width="75%"><br>
<sub>Fuente: propia, creada con el catálogo de objetos de Microsoft Paint 3D.</sub><br><br>
</div>

_Bienvenido al curso de Balance hidrológico de largo plazo - LTWB para estimación de caudales medios usando SIG_. En este curso aprenderá a generar grillas de caudales medios acumulados distribuidos de largo plazo y grillas de isorendimientos medios a partir de modelos de terreno, de grillas interpoladas de precipitación media y de mapas de evapotranspiración real, utilizando sistemas de información geográfica.

Este curso ha sido dividido en diferentes secciones y actividades secuenciales, a través de las cuales el estudiante desarrollará diferentes habilidades computacionales y analíticas, que podrá aplicar en proyectos de ingeniería y casos de estudio propios.

<div align="center"><a href="http://www.youtube.com/watch?feature=player_embedded&v=6eu-mLKVcOw" target="_blank"><img src=".icons/R.LTWB_PlayVideo.svg" alt="R.LTWB" width="240" border="0" /></a><sub><br>https://www.youtube.com/watch?v=6eu-mLKVcOw<br>Playlist: https://youtube.com/playlist?list=PLZGvAjHkhphDKXvnhkp0oQb22EHWVd0W8</sub><br><br></div>


## Objetivos generales

* Comprender la utilidad de los balances hidrológicos de largo plazo en los campos de ingeniería aplicada.
* Delimitar la zona de estudio para descargar y procesar las redes de drenaje y los modelos digitales de elevación ASTER GDEM, SRTM y ALOS PALSAR.
* Utilizando técnicas de hidrología computacional, reajustar los modelos digitales de elevación incrustando la red de drenaje, rellenar sumideros, determinar las direcciones de flujo, calcular las acumulaciones, demarcar los drenajes y obtener puntos característicos sobre toda la red de drenaje.
* A partir de la zona de estudio, identificar las estaciones hidroclimatológicas terrestres para analizar su densidad y cobertura.
* A partir de la red de estaciones, descargar y procesar series temporales a través de técnicas de ciencia de datos. El procesamiento incluye la exploración y análisis de series, su representación gráfica, la identificación y ajuste de valores atípicos, el completado y extendido para obtener series homogéneas.
* Comparar series terrestres con series obtenidas a través de sensores remotos satelitales.
* Segmentar las series compuestas en series por fenómeno climatológico (El Niño, La Niña y Neutro) a partir del indicador ENSO-ONI o El Niño-Oscilación del Sur, de la National Oceanic and Atmospheric Administration - NOAA de los Estados Unidos de América.
* A partir de series validadas y de la marcación de años por fenómeno climatológico, realizar agregaciones estadísticas a nivel multianual.
* Analizar y crear mapas continuos por fenómeno climatológico de las variables climatológicas requeridas para el balance hidrológico. Para la generación de los mapas de evapotranspiración potencial, utilizaremos ecuaciones regionales que dependen de la elevación del terreno, temperatura y precipitación total.
* Realizar balances hidrológicos de largo plazo distribuidos y para cuencas o zonas geográficas delimitadas como las subzonas hidrográficas del IDEAM - Colombia - Suramérica.
* A partir de los puntos característicos obtenidos sobre la red de drenaje, de sus áreas de aportación y de los mapas de caudal medio, obtener ecuaciones características compuestas y por fenómeno climatológico.
* Estimar y evaluar mapas de isorendimientos medios.
* Obtener habilidades en automatización de análisis de datos y de procesos geográficos utilizando el lenguaje de programación Python.
* Para las diferentes etapas de procesamiento de información hidroclimatológica, generar y publicar de forma automática, reportes detallados en formato Markdown.


## Metodología

El curso inicia con una introducción y explicación general de la metodología, requerimientos y herramientas computacionales a emplear. Luego, cada estudiante procede al desarrollo de las diferentes actividades prácticas documentadas en cada sección a través de un caso de estudio general, correspondiente a la estimación del balance hidrológico en la Zona Hidrográfica 28 del IDEAM, de la cuenca del Río Cesar - Colombia - Suramérica.

:1st_place_medal: Estudiantes que aplicaron bajo el esquema de certificación, desarrollan casos de estudio individuales para zonas hidrográficas específicas, las cuales son asignados por el instructor. Para el desarrollo de las diferentes entregas de avance, los estudiantes deben crear un repositorio siguiendo la misma estructura de este curso. Aprende como a través de la [:mortar_board:Guía para enseñanza e investigación colaborativa con GitHUB.](https://github.com/rcfdtools/R.TeachingResearchGuide)


## Dirigido a

Los contenidos presentados en este curso están dirigidos a estudiantes y profesionales de diferentes disciplinas que requieran aprender y/o fortalecer sus conocimientos en hidrología computacional y sistemas de información geográfica, tales como:

* Estudiantes de pregrado y posgrado en ingeniería.
* Ingenieros y especialistas.
* Técnicos y tecnólogos en ingeniería civil y afines. 
* Funcionarios públicos y/o gestores territoriales con conocimientos en hidrología.


## Sección 1 - Introducción y fundamentos [:hook:](Section01/Readme.md)

 En esta sección se presenta la utilidad de los LTWB en el campo de la ingeniería, se delimita el caso de estudio y se establecen los requerimientos generales para el desarrollo de las diferentes actividades prácticas incluidas en el curso.

| Actividad                                                                                           | Alcance                                                                                                                                                                                                                                                                                                            | Dedicación,<br>3.25 horas | 
|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------:|
| [¿Qué son y para qué sirven los balances hidrológicos de largo plazo – LTWB?](Section01/WhatIsLTWB) | Explicación general del procedimiento para la realización de balances hidrológicos e identificación de información base requerida. En esta clase también se listan algunas de las aplicaciones generales de los caudales medios de largo plazo en la realización de estudios de ingeniería y estudios ambientales. |           0.25            | 
| [Requerimientos](Section01/Requirement)                                                             | En esta actividad se listan los requerimientos académicos y computacionales generales para el desarrollo de las diferentes actividades del curso, se define y crea la estructura de directorios y se realiza la instalación y configuración de las principales herramientas requeridas.                            |             2             | 
| [Caso de estudio](Section01/CaseStudy)                                                              | Definición de la zona de estudio a partir de la cobertura de subzonas hidrográficas de Colombia - Suramérica, con creación de polígono envolvente. En esta actividad se define el sistema de proyección de coordenadas a utilizar en la creación y procesamiento de los diferentes mapas y capas geográficas.      |             1             | 


## Sección 2 - Descarga y procesamiento de modelos digitales de elevación [:hook:](Section02/Readme.md)

En esta sección realizaremos la descarga y procesamiento de diferentes tipos de modelos digitales de elevación, incluido el reacondicionamiento o ajuste a partir de la incrustación de los vectores de drenaje.

| Actividad                                                                                                                               | Alcance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Dedicación,<br>14.75 horas | 
|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------:|
| [Creación de usuario NASA Earthdata](Section02/UserCreation)                                                                            | Para la descarga de los modelos digitales de elevación y la información climatológica obtenida mediante sensores remotos, es necesaria la creación de una cuenta de usuario en el servidor EarthData de la NASA o Agencia Nacional de Aeronáutica y Administración Espacial de los Estados Unidos de América. Para la descarga de imágenes de modelos de elevación ASTER GDEM con resolución 12.5m, no es necesaria la creación de una cuenta independiente en el servidor Vertex de la Universidad de Alaska, se utiliza la misma cuenta del servicio EarthData.                                                                                                                                                                                                                                                                                                                                                                    |            0.25            |
| [Descarga y procesamiento de modelo digital de elevación - DEM - NASA ASTER GDEM v3 (30m)](Section02/DEMAster)                          | Los sensores remotos japoneses Advanced Spaceborne Thermal Emission and Reflection Radiometer o ASTER, proveen imágenes de alta resolución del Planeta Tierra y las capturas están compuestos por 14 diferentes bandas del espectro electromagnético en el rango visible de la luz termal infrarroja. Las imágenes son capturadas en resoluciones entre 15 y 90 metros permitiendo crear mapas detallados de la temperatura y elevación de la tierra.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |            1.25            |
| [Descarga y procesamiento de modelo digital de elevación - DEM - SRTM v3.0 1 arcsec (30m), SRTM v3.0 3 arcsec (90m)](Section02/DEMSrtm) | Shuttle Radar Topography Mission (SRTM), dispone de mapas topográficos de alta resolución para uso público desde el año 2015 y pueden ser utilizados para la creación de los mapas de dirección y acumulación de flujo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |             1              |
| [Descarga y procesamiento de modelo digital de elevación - DEM - ALOS PALSAR (12.5m)](Section02/DEMAlos)                                | ALOS Phased Array type L-band Synthetic Aperture Radar, es uno de los instrumentos de observación avanzada de la superficie terrestre, que permite entre otros, obtener un modelo digital de la tierra en alta resolución.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |            1.25            |
| [Descarga de GDB nacional del IGAC en escala 1:100k y fotorrestitución de redes de drenaje](Section02/GDB100k)                          | Para los procesos de reacondicionamiento del modelo de terreno que garantice el flujo de todas las celdas del modelo hacia celdas específicas de la red de drenaje, es necesaria la descarga y complementación de las líneas de drenaje pertenecientes a la zona de estudio.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |             2              |
| [Reacondicionamiento de terreno - DEM Reconditioning – AgreeDEM](Section02/AgreeDEM)                                                    | Para garantizar que la acumulación del flujo se realice sobre las celdas del modelo de terreno y por los cauces o drenajes obtenidos o digitalizados, es necesario reacondicionar los modelos digitales de elevación DEM incrustando los drenajes. Este procedimiento es especialmente requerido en zonas predominantemente planas o en zonas donde no puedan ser identificadas las celdas correspondientes a los drenajes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |             2              |
| [Relleno de sumideros o depresiones en modelos digitales de elevación – Fill Sinks – FIL](Section02/FillDEM)                            | Cuando una celda se encuentra rodeada por celdas de mayor elevación la escorrentía es retenida y no fluye. El relleno de sumideros eleva estas celdas utilizando como referencia los valores en altura de las celdas circundantes, garantizando que las celdas de la superficie del terreno drenen hacia una localización más baja.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |             2              |
| [Direcciones de Flujo – Flow Direction – FDR](Section02/FdrDEM)                                                                         | Esta grilla define la dirección de la máxima pendiente del terreno para cada celda utilizando el modelo de relleno de sumideros - FIL. Esta capa es usada para a través del algoritmo de acumulación, crear el mapa discreto de acumulación de celdas que convergen hacia celdas más bajas y da como resultado ocho posibles direcciones en cada celda.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |            1.5             |
| [Acumulación de Flujo - Flow Accumulation - FAC](Section02/FacDEM)                                                                      | Esta grilla representa para una celda dada, el número de celdas acumuladas aguas arriba de dicha celda. El área de drenaje en cualquier celda puede calcularse multiplicando el valor de acumulación por el área de cada celda.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |            1.5             |
| [Demarcación de drenajes – Stream Definition - STR y localización de nodos característicos](Section02/StrDEM)                           | A partir de grillas de acumulación de flujo, se pueden identificar las celdas que hacen parte de la red de drenaje principal. Para ello se especifica el área de aportación, p. ej. entre 1 y 4 km² o el número equivalente de celdas en función de su resolución, considerando que a menor área de aportación, mayor será el número de corrientes obtenidas. El procedimiento general para la definición de drenajes incluye la creación de una grilla binarizada con celdas a las que se les asigna 1 como valor de pixel. Es importante tener en cuenta que algunos de los tramos obtenidos, corresponderán a áreas de aportación inferiores al valor de aportación definido, específicamente en cuencas intermedias o cuencas de tránsito entre dos puntos de unión próximos. En esta actividad, también se obtienen los nodos característicos de la red y sus áreas de aportación para la posterior lectura de caudales medios. |             2              |


## Sección 3 - Descarga, procesamiento y análisis de datos hidroclimatológicos [:hook:](Section03/Readme.md)

En esta sección se obtienen, procesan y analizan los datos hidroclimatológicos requeridos para el balance y se realiza la segmentación de series por fenómeno climatológico. Complementariamente, implementaremos scripts en Python para automatizar varias de las actividades desarrolladas, facilitando su replicación a otros casos de estudio o a proyectos particulares.

| Actividad                                                                                                                       | Alcance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Dedicación,<br>18.5 horas |
|---------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------:|
| [Catálogo nacional de estaciones - CNE y selección de estaciones para la zona de estudio](Section03/CNEStation)                 | Luego de la definición del caso de estudio realizada en la Sección 1, es necesario identificar la red de estaciones terrestres que serán utilizadas para el análisis de las diferentes variables en la zona estudio.                                                                                                                                                                                                                                                                                                                                |             3             |
| [Análisis de elevaciones, densidad, cobertura y radio de acción de estaciones terrestres](Section03/CNEStationElevation)        | Los catálogos de estaciones terrestres contienen el atributo de elevación asociada a cada estación que debe ser validado a partir de los modelos digitales de elevación DEM para su uso posterior en la implementación de métodos de imputación de datos faltantes por relaciones espaciales.                                                                                                                                                                                                                                                       |             2             |
| [Obtención y unión de series de datos discretos climatológicos de estaciones terrestres](Section03/CNEStationDatasetDownload)   | Para la creación de los mapas requeridos para la realización del balance hidrológico, es necesario a partir de las estaciones seleccionadas para la zona de estudio, obtener las series de valores discretos de precipitación total mensual, temperatura máxima diaria, temperatura mínima diaria y evaporación total diaria. Para la comparación de los caudales obtenidos, también son requeridas las series de caudal medio mensual.                                                                                                             |            2.5            |
| [Obtención de series de datos discretos climatológicos satelitales y correlación con datos terrestres](Section03/RemoteSensing) | Para la validación o el contraste de información terrestre, se pueden obtener datos satelitales de precipitación diaria total, temperatura y evapotranspiración sobre las localizaciones específicas de la red climatológica utilizada. A partir de la información recopilada y validada para la red estaciones a usar en la zona de estudio y la conformación de series a partir de datos satelitales en las localizaciones específicas de la red, se correlacionan estos datos para evaluar si existe correspondencia y homogeneidad entre ellos. |             2             |
| [Exploración y análisis de series - EDA - Representación gráfica](Section03/EDA)                                                | Durante el proceso de revisión, validación y comprensión de los datos, es necesario utilizar diferentes técnicas que permitan identificar discontinuidades, cambios en el comportamiento temporal y en general revisar los estadísticos característicos de cada serie por parámetro.                                                                                                                                                                                                                                                                |             2             |
| [Identificación y procesamiento de datos atípicos - Outliers](Section03/Outlier)                                                | En esta actividad se obtienen los parámetros estadísticos de cada variable climatológica, se identifican y marcan los datos atípicos que luego serán ajustados o reemplazados por valores sintéticos obtenidos a través de métodos de completado o imputación.                                                                                                                                                                                                                                                                                      |             2             |
| [Completado y extendido de series - Imputación](Section03/Impute)                                                               | Este procedimiento de completado se realiza a partir de la generación de datos sintéticos utilizando diferentes métodos estadísticos y su propósito general es la conformación de series homogéneas y continuas para las diferentes variables en estudio.                                                                                                                                                                                                                                                                                           |             2             |
| [Análisis de cambio climático para segmentación de series](Section03/ENSOONI)                                                   | En esta actividad se realiza la identificación de años asociados a fenómenos climatológicos de El Niño, La Niña y Neutro.                                                                                                                                                                                                                                                                                                                                                                                                                           |             1             |
| [Agregación estadística para obtención de promedios multianuales compuestos y por fenómeno climatológico](Section03/Agg)        | Luego de validadas y completadas las series, y de realizada la marcación de años por fenómeno climatológico, se efectúa el proceso de agregación estadística para obtener los valores promedio multianuales requeridos en cada estación por parámetro hidro-climatológico para su interpolación espacial.                                                                                                                                                                                                                                           |             2             |


## Sección 4 - Análisis espacial de variables climatológicas [:hook:](Section04/Readme.md)

Durante el proceso de conformación de información para el desarrollo del balance hidrológico, es necesaria la construcción de mapas continuos e interpolados que representen espacialmente el comportamiento de las diferentes variables requeridas y fenómenos climatológicos asociados a nivel multianual.

| Actividad                                                   | Alcance                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Dedicación,<br>5 horas |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------:|
| [Mapa de precipitación total](Section04/Rain)               | A partir de la localización espacial de estaciones terrestres y de los valores obtenidos, validados, imputados y extendidos de las series de datos recopiladas, se generan los mapas continuos interpolados de precipitación para series compuestas y por fenómeno climatológico, necesarios para el balance hidrológico de largo plazo.                                                                                                                              |           1            |
| [Mapa de temperatura media](Section04/Temperature)          | A partir de las series agregadas de temperatura máxima y mínima a nivel anual, se estima la temperatura media anual en cada estación y se crea el mapa de temperatura requerido para la estimación de la evapotranspiración potencial.                                                                                                                                                                                                                                |          1.5           |
| [Mapa de evapotranspiración potencial - ETP](Section04/ETP) | El Centro Nacional de Investigaciones de Café - Cenicafé de Colombia - Suramérica, ha realizado diferentes estudios relacionados con variables climatológicas, obteniendo ecuaciones que describen el comportamiento de la evapotranspiración potencial en función de la altitud. La ecuación propuesta, permite calcular la evapotranspiración potencial (ETP) de forma sencilla, pues en dicha ecuación la ETP solo depende de la elevación sobre el nivel del mar. |          0.5           |
| [Mapa de evapotranspiración real - ETR](Section04/ETR)      | En esta actividad y a partir de los mapas de precipitación total, temperatura y evapotranspiración potencial, generamos los mapas de evapotranspiración real utilizando las ecuaciones de Budyco, Turc y Dekop.                                                                                                                                                                                                                                                       |           2            |


## Sección 5 - Balance hidrológico de largo plazo - LTWB [:hook:](Section05/Readme.md)

En esta sección ejecutaremos el balance hidrológico distribuido, realizaremos la lectura de caudales medios en los puntos característicos de la red de drenaje, crearemos el mapa de isorendimientos medios y desarrolaremos el balance a partir de cuencas o áreas de aportación delimitadas.

| Actividad                                                                                            | Alcance                                                                                                                                                                                                                                                                                                                                                                                                                       | Dedicación,<br>6.5 horas |
|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------:|
| [Balance hidrológico distribuido usando SIG](Section05/LTWB)                                         | Los balances hidrológicos de largo plazo pueden ser realizados en SIG a través de herramientas de acumulación de flujo. Para cada una de las celdas del mapa de direcciones de flujo o FDR, se calcula el número de celdas de drenaje convergentes a las cuales se les puede acumular el valor del potencial de escurrimiento de cada celda obtenido a partir de los valores de precipitación media y evapotranspiración real |           2.5            |
| [Lectura y análisis de caudales y áreas de aportación en nodos característicos](Section05/FlowPoint) | Una vez obtenida la red de puntos característicos para lectura de resultados que contienen el número de celdas aportantes y sus áreas de drenaje equivalentes, se procede a realizar la estadística zonal o la extracción de valores de mapas ráster a nodos para la obtención de caudales y ecuaciones características                                                                                                       |            2             |
| [Mapa de isorendimiento medio](Section05/FlowPerformance)                                            | Utilizando los valores de caudal medio, número de celdas y área de aportación en las diferentes localizaciones de la red de drenaje, se construye el mapa de isorendimientos medios y se obtienen ecuaciones características que permiten estimar rendimientos en función del área de aportación                                                                                                                              |           0.75           |
| [Balance hidrológico a partir de cuencas delimitadas](Section05/LTWBBasin)                           | Cuando existen zonas delimitadas como cuencas hidrográficas, es posible mediante estadísticos zonales, estimar manualmente el balance hidrológico a partir de los mapas de precipitación media y evapotranspiración real                                                                                                                                                                                                      |           1.25           |

> Los tiempos de dedicación corresponden a horas mínimas que el estudiante debe dedicar al desarrollo del caso de estudio con el cual se ejemplificó este curso y a las actividades complementarias indicadas al final de cada clase. Estudiantes bajo el esquema de certificación y caso de estudio asignado requerirán de al menos 96 horas de trabajo y horas complementarias, de acuerdo a su experticia en el manejo de las herramientas computacionales utilizadas. 


##

_:beginner: Ayuda / Colabora: a través de la pestaña _[Discussions](https://github.com/rcfdtools/R.LTWB/discussions)_ localizada en la parte superior de esta ventana, podrás encontrar y participar en los [_anuncios o noticias_](https://github.com/rcfdtools/R.LTWB/discussions/categories/announcements) publicados, enviarnos tus [_ideas_](https://github.com/rcfdtools/R.LTWB/discussions/categories/ideas) para actividades complementarias, participar en preguntas, respuestas y consultas específicas [_Q&A_](https://github.com/rcfdtools/R.LTWB/discussions/categories/q-a) y realizar [_publicaciones o consultas generales_](https://github.com/rcfdtools/R.LTWB/discussions/categories/general) públicas._

_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](LICENSE.md)._

_Clonación: para compatibilidad completa de las rutas utilizadas en los scripts y herramientas de R.LTWB, en Microsoft Windows clonar y/o descomprimir en _D:\R.LTWB_. Enlace para clonación https://github.com/rcfdtools/R.LTWB.git._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [:sun_with_face: Iniciar curso](Section01) | [:infinity: Otros cursos](https://github.com/rcfdtools) | [:notebook: Referencias](References.md) | [:label: Abreviaturas y definiciones](Definitios.md) |
|--------------------------------------------|---------------------------------------------------------|-----------------------------------------|------------------------------------------------------|
