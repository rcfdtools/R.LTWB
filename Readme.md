<div align="center">
  <img alt="R.LTWB" src="https://github.com/rcfdtools/R.LTWB/blob/main/.icons/R.LTWB.svg" width="250px">
  <br><b>Balance hidrológico de largo plazo para estimación de caudales medios usando SIG.</b><br>Long-term water balance by r.cfdtools@gmail.com<br><br>  
</div>

Es este curso aprenderá a generar grillas de caudales medios acumulados distribuidos de largo plazo y grillas de isorendimientos medios a partir de modelos de terreno, de grillas interpoladas de precipitación media y de mapas de evaporación real, utilizando sistemas de información geográfica.


## Sección 1 - Introducción y fundamentos

 En esta sección se presenta la introducción y fundamentos generales, el caso de estudio y los requerimientos generales para el desarrollo de las diferentes actividades prácticas.

| Actividad                                                       | Alcance                                                                                                                                                                                                                                                           |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bienvenida, introducción general y objetivos                    | En esta primera actividad se presenta una introducción general al curso y se definen los objetivos generales a desarrollar durante las clases y talleres.                                                                                                         |
| ¿Qué es un balance hidrológico de largo plazo – LTWB?           | Explicación general de la metodología para la realización de balances hidrológicos e identificación de información base requerida.                                                                                                                                |
| Utilidad y campo de aplicación de los LTWB en ingeniería        | En esta clase se listan algunas de las aplicaciones generales de los caudales medios de largo plazo en la realización de estudios de ingeniería y estudios ambientales.                                                                                           |
| [Requerimientos](Section01/Requirement)<br>(_Versión borrador_) | En esta actividad se listan los requerimientos académicos y computacionales para el desarrollo de las diferentes actividades del curso, se define y crea la estructura de directorios y se realiza la instalación y configuración de las herramientas requeridas. |
| [Caso de estudio](Section01/CaseStudy)                          | Definición de la zona de estudio a partir de la cobertura de subzonas hidrográficas de Colombia con creación de polígono envolvente. En esta actividad se define el sistema de proyección de coordenadas a utilizar en los diferentes mapas y capas geográficas.  |


## Sección 2 - Descarga y procesamiento de modelos digitales de elevación

En esta sección realizaremos la descarga y procesamiento de diferentes tipos de modelos digitales de elevación, incluido el reacondicionamiento o ajuste a partir de la incrustación de los vectores de drenaje.

| Actividad                                                                                                                               | Alcance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Creación de usuario NASA Earthdata](Section02/UserCreation)                                                                            | Para la descarga de los modelos de terreno y la información climatológica obtenida mediante sensores remotos, es necesaria la creación de una cuenta de usuario en el servidor EarthData de la NASA o Agencia Nacional de Aeronáutica y Administración Espacial de los Estados Unidos de América. Para la descarga de imágenes de modelos de terreno ASTER GDEM con resolución 12.5m, no es necesaria la creación de una cuenta independiente en el servidor Vertex de la Universidad de Alaska, se utiliza la misma cuenta del servicio EarthData.                                                                                                                                                                                                                                                                                                                                                                                |
| [Descarga y procesamiento de modelo digital de elevación - DEM - NASA ASTER GDEM v3 (30m)](Section02/DEMAster)                          | Los sensores remotos japoneses Advanced Spaceborne Thermal Emission and Reflection Radiometer o ASTER, proveen imágenes de alta resolución del Planeta Tierra y las capturas están compuestos por 14 diferentes bandas del espectro electromagnético en el rango visible de la luz termal infrarroja. Las imágenes son capturadas en resoluciones entre 15 y 90 metros permitiendo crear mapas detallados de la temperatura y elevación de la tierra.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Descarga y procesamiento de modelo digital de elevación - DEM - SRTM v3.0 1 arcsec (30m), SRTM v3.0 3 arcsec (90m)](Section02/DEMSrtm) | Shuttle Radar Topography Mission (SRTM), dispone de mapas topográficos de alta resolución para uso público desde el año 2015 y pueden ser utilizados para la creación de los mapas de dirección y acumulación de flujo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Descarga y procesamiento de modelo digital de elevación - DEM - ALOS PALSAR (12.5m)](Section02/DEMAlos)                                | ALOS Phased Array type L-band Synthetic Aperture Radar, es uno de los instrumentos de observación avanzada de la superficie terrestre, que permite entre otros, obtener un modelo digital de la tierra en alta resolución.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Descarga de GDB nacional del IGAC en escala 1:100k y fotorrestitución de redes de drenaje](Section02/GDB100k)                          | Para los procesos de reacondicionamiento del modelo de terreno que garantice el flujo de todas las celdas del modelo hacia celdas específicas de la red de drenaje, es necesaria la descarga y complementación de las líneas de drenaje pertenecientes a la zona de estudio.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Reacondicionamiento de terreno - DEM Reconditioning – AgreeDEM](Section02/AgreeDEM)                                                    | Para garantizar que la acumulación del flujo se realice sobre las celdas del modelo de terreno y por los cauces o drenajes obtenidos o digitalizados, es necesario reacondicionar los modelos digitales de elevación DEM incrustando los drenajes. Este procedimiento es especialmente requerido en zonas predominantemente planas o en zonas donde no puedan ser identificadas las celdas correspondientes a los drenajes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Relleno de sumideros o depresiones en modelos digitales de elevación – Fill Sinks – FIL](Section02/FillDEM)                            | Cuando una celda se encuentra rodeada por celdas de mayor elevación la escorrentía es retenida y no fluye. El relleno de sumideros eleva estas celdas utilizando como referencia los valores en altura de las celdas circundantes, garantizando que las celdas de la superficie del terreno drenen hacia una localización más baja.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Direcciones de Flujo – Flow Direction – FDR](Section02/FdrDEM)                                                                         | Esta grilla define la dirección de la máxima pendiente del terreno para cada celda utilizando el modelo de relleno de sumideros FIL. Esta capa es usada para a través del algoritmo de acumulación, crear el mapa discreto de acumulación de celdas que convergen hacia celdas más bajas y da como resultado ocho posibles direcciones en cada celda.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Acumulación de Flujo - Flow Accumulation - FAC](Section02/FacDEM)                                                                      | Esta grilla representa para una celda dada, el número de celdas acumuladas aguas arriba de dicha celda. El área de drenaje puede calcularse multiplicando el valor de acumulación por el área de cada celda.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Demarcación de drenajes – Stream Definition - STR y localización de nodos característicos](Section02/StrDEM)                           | A partir de grillas de acumulación de flujo, se pueden identificar las celdas que hacen parte de la red de drenaje principal. Para ello se especifica el área de aportación, p. ej. de 1 o 4 km² o el número equivalente de celdas en función de su resolución, considerando que a menor área de aportación, mayor será el número de corrientes obtenidas. El procedimiento general para la definición de drenajes incluye la creación de una grilla binarizada con celdas a las que se les asigna 1 como valor de pixel. Es importante tener en cuenta que algunos de los tramos obtenidos, corresponderán a áreas de aportación inferiores al valor de aportación definido, específicamente en cuencas intermedias o cuencas de tránsito entre dos puntos de unión próximos. En esta actividad, también se obtienen los nodos característicos de la red y sus áreas de aportación para la posterior lectura de caudales medios.  |


## Sección 3 - Descarga, procesamiento y análisis de datos hidroclimatológicos

En esta sección se obtienen, procesan y analizan los datos hidroclimatológicos requeridos para el balance y se realiza la segmentación de series por fenómeno climatológico. Complementariamente, implementaremos scripts en Python para automatizar varias de las actividades desarrolladas, facilitando su replicación a otros casos de estudio o a proyectos particulares.

| Actividad                                                                                                                       | Alcance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Catálogo nacional de estaciones - CNE y selección para la zona de estudio](Section03/CNEStation)                               | Luego de la definición del caso de estudio realizada en la Sección 1, es necesario identificar la red de estaciones terrestres que serán utilizadas para el estudio de las diferentes variables en la zona estudio.                                                                                                                                                                                                                                                                                                                                 |
| [Análisis de elevaciones, densidad, cobertura y radio de acción de estaciones terrestres](Section03/CNEStationElevation)        | Los catálogos de estaciones terrestres contienen el atributo de elevación asociada a cada estación que debe ser validado a partir de los modelos digitales de elevación DEM para su uso posterior en la implementación de métodos de imputación de datos faltantes por relaciones espaciales.                                                                                                                                                                                                                                                       |
| [Obtención y unión de series de datos discretos climatológicos de estaciones terrestres](Section03/CNEStationDatasetDownload)   | Para la creación de los mapas requeridos para la realización del balance hidrológico, es necesario a partir de las estaciones seleccionadas para la zona de estudio, obtener las series de valores discretos de precipitación total mensual, temperatura máxima diaria, temperatura mínima diaria y evaporación total diaria. Para la comparación de los caudales obtenidos, también son requeridas las series de caudal medio mensual.                                                                                                             |
| [Obtención de series de datos discretos climatológicos satelitales y correlación con datos terrestres](Section03/RemoteSensing) | Para la validación o el contraste de información terrestre, se pueden obtener datos satelitales de precipitación diaria total, temperatura y evapotranspiración sobre las localizaciones específicas de la red climatológica utilizada. A partir de la información recopilada y validada para la red estaciones a usar en la zona de estudio y la conformación de series a partir de datos satelitales en las localizaciones específicas de la red, se correlacionan estos datos para evaluar si existe correspondencia y homogeneidad entre ellos. |
| [Exploración y análisis de series - EDA - Representación gráfica](Section03/EDA)                                                | Durante el proceso de revisión, validación y comprensión de los datos, es necesario utilizar diferentes técnicas que permitan identificar discontinuidades, cambios en el comportamiento temporal y en general revisar los paramétricos de cada serie por parámetro.                                                                                                                                                                                                                                                                                |
| [Identificación y procesamiento de datos atípicos - Outliers](Section03/Outlier)                                                | En esta actividad se obtienen los parámetros estadísticos de cada variable climatológica, se identifican y marcan los datos atípicos que luego serán ajustados o reemplazados por valores sintéticos obtenidos a través de métodos de completado o imputación.                                                                                                                                                                                                                                                                                      |
| [Completado y extendido de series - Imputación](Section03/Impute)                                                               | Este procedimiento de completado se realiza a partir de la generación de datos sintéticos utilizando diferentes métodos estadísticos y su propósito general es la conformación de series homogéneas y continuas para las diferentes variables en estudio.                                                                                                                                                                                                                                                                                           |
| [Análisis de cambio climático para segmentación de series](Section03/ENSOONI)                                                   | En esta actividad se realiza la identificación de años asociados a fenómenos climatológicos de Niño, Niña y Neutro.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Agregación estadística para obtención de promedios multianuales compuestos y por fenómeno climatológico](Section03/Agg)        | Luego de validadas y completadas las series, y de realizada la marcación de años por fenómeno climatológico, se efectúa el proceso de agregación estadística para obtener los valores promedio multianuales requeridos en cada estación por parámetro hidro-climatológico para su interpolación espacial.                                                                                                                                                                                                                                           |


## Sección 4 - Análisis espacial de variables climatológicas

Durante el proceso de conformación de información para el desarrollo del balance hidrológico, es necesaria la construcción de mapas continuos e interpolados que representen espacialmente el comportamiento de las diferentes variables requeridas y fenómenos climatológicos asociados a nivel multianual.

| Actividad                                                   | Alcance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Mapa de precipitación total](Section04/Rain)               | A partir de la localización espacial de estaciones terrestres y de los valores obtenidos, validados, imputados y extendidos de las series de datos recopiladas, se generan los mapas continuos interpolados para series compuestas y por fenómeno climatológico, requeridos para el balance hidrológico de largo plazo.                                                                                                                                                                            |
| [Mapa de temperatura media](Section04/Temperature)          | A partir de las series agregadas de temperatura máxima y mínima a nivel anual, se estima la temperatura media anual en cada estación y se crea el mapa de temperatura requerido para la estimación de la evapotranspiración potencial.                                                                                                                                                                                                                                                             |
| [Mapa de evapotranspiración potencial - ETP](Section04/ETP) | El Centro Nacional de Investigaciones de Café - Cenicafé de Colombia - Suramérica, ha realizado diferentes estudios relacionados con variables climatológicas, obteniendo ecuaciones que describen el comportamiento de la evapotranspiración potencial en función de la altitud. La ecuación propuesta, permite calcular la evapotranspiración potencial (ETP) de forma sencilla, pues en dicha ecuación la ETP solo depende de la elevación sobre el nivel del mar. |
| [Mapa de evapotranspiración real - ETR](Section04/ETR)      | En esta actividad y a partir de los mapas de precipitación total, temperatura y evapotranspiración potencial, generamos los mapas de evapotranspiración real utilizando las ecuaciones de Budyco, Turc y Dekop.                                                                                                                                                                                                                                                                                    |


## Sección 5 - Balance hidrológico de largo plazo - LTWB

En esta sección ejecutaremos el balance hidrológico distribuido, identificaremos los puntos para lectura de caudales medios y áreas de aportación, realizaremos el mapa de isorendimientos y un balance a partir de cuencas ya delimitadas.

| Actividad                                                                                                                    | Alcance                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Balance hidrológico distribuido usando SIG](Section05/LTWB)                                                                 | Los balances hidrológicos de largo plazo pueden ser realizados en SIG a través de herramientas de acumulación de flujo. Para cada una de las celdas del mapa de direcciones de flujo o FDR, se calcula el número de celdas de drenaje convergentes a las cuales se les puede acumular el valor del potencial de escurrimiento de cada celda obtenido a partir de los valores de precipitación media y evapotranspiración real. |
| [Lectura y análisis de caudales y áreas de aportación en nodos característicos](Section05/FlowPoint)<br>(_Versión borrador_) | Una vez obtenida la red de puntos característicos para lectura de resultados que contienen el número de celdas aportantes y sus áreas de drenaje equivalentes, se procede a realizar la estadística zonal o la extracción de valores de mapas ráster a nodos para la obtención de caudales.                                                                                                                                    |
| Cálculo y creación del mapa de isorendimiento medio                                                                          | Utilizando los valores de caudal medio y área obtenida para los diferentes puntos de interés de la red de drenaje, se construye el mapa de isorendimientos medios y una función de regresión que permite estimar los caudales en función del área de aportación requerida aplicable a la zona de estudio.                                                                                                                      |
| Balance hidrológico a partir de cuencas delimitadas                                                                          | Cuando existen zonas delimitadas a partir de polígonos como cuencas hidrográficas, es posible estimar manualmente mediante estadísticos zonales, el balance hidrológico a partir de los valores de precipitación media y evapotranspiración real.                                                                                                                                                                              |

## Sección 6 - Modelos de pronóstico

Para finalizar, en esta sección implementaremos modelos de pronóstico para evaluar el posible comportamiento futuro de las variables climatológicas utilizadas y su implicación en el balance.

| Actividad                              | Alcance                                                                                                                                                                                                                                                                                                                          |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Modelos de correlación lineal múltiple | A través del conocimiento adquirido en los diferentes procesos realizados para la obtención de los mapas de balance y el estudio de las series utilizadas, se puede evidenciar la correlación entre las variables y los fenómenos evaluados, permitiendo entender su dinámica para la implementación de un modelo de pronóstico. |
| Modelos de inteligencia artificial     | Utilizando técnicas de inteligencia artificial para el análisis de series, implementar modelos que permitan realizar el pronóstico de las variables estudiadas para su posterior utilización en la realización de balances hidrológicos.                                                                                         |


##

_:beginner: Ayuda / Colabora: a través de la pestaña _[Discussions](https://github.com/rcfdtools/R.LTWB/discussions)_ localizada en la parte superior de esta ventana, podrás encontrar y participar en los [_anuncios o noticias_](https://github.com/rcfdtools/R.LTWB/discussions/categories/announcements) publicados, enviarnos tus [_ideas_](https://github.com/rcfdtools/R.LTWB/discussions/categories/ideas) para actividades complementarias, participar en preguntas, respuestas y consultas específicas [_Q&A_](https://github.com/rcfdtools/R.LTWB/discussions/categories/q-a) y realizar [_publicaciones o consultas generales_](https://github.com/rcfdtools/R.LTWB/discussions/categories/general) públicas._

_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](LICENSE.md)._

_Clonación: para compatibilidad completa de las rutas utilizadas en los scripts y herramientas de R.LTWB, en Microsoft Windows clonar y/o descomprimir en _D:\R.LTWB_. Enlace para clonación https://github.com/rcfdtools/R.LTWB.git._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [:sun_with_face: Iniciar curso](Section01) | [:infinity: Otros cursos](https://github.com/rcfdtools) |
|--------------------------------------------|---------------------------------------------------------|