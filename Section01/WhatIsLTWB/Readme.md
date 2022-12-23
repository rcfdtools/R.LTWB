## ¿Qué son y para qué sirven los balances hidrológicos de largo plazo – LTWB?
Keywords: `Long-term-water-balance` `Hydrology` `Evapotranspiration` `Rain` `Area`

![R.LTWB](Graph/WhatIsLTWB.png)

Explicación general de la metodología para la realización de balances hidrológicos e identificación de información base requerida. En esta clase también se listan algunas de las aplicaciones generales de los caudales medios de largo plazo en la realización de estudios de ingeniería y estudios ambientales

Para la ejecución completa de un balance hidrológico de largo plazo a nivel anual, es necesario definir primero el límite espacial de la zona de estudio para luego obtener los mapas de terreno, redes de drenaje y series hidroclimatológicas necesarias para la producción de mapas continuos. 


## Utilidad y campo de aplicación de los LTWB en ingeniería

Los balances hidrológicos de largo plazo son frecuentemente utilizados en estudios hidrológicos y ambientales debido a través de ellos se puede realizar: 

* Estimación del caudal medio superficial disponible en cuencas hidrográficas o en localizaciones particulares de la red de drenaje.
* Obtención de ecuaciones características relacionando áreas de aportación vs. caudales medios.
* Estimación de isorendimientos medios.
* Estimación de caudales ecológicos.
* Estimación de caudales para concesión por captación y vertimiento.
* Valores de referencia para el diseño de estructuras ecológicas.


## Metodología para estimación del caudal medio

Para la estimación de caudales medios, se realiza un balance hidrológico de largo plazo en cada una de las celdas que cubre la zona de estudio. Se denomina de largo plazo, debido a que se asume que luego de ser saturado el suelo, la escorrentía se produce por los excedentes obtenidos de precipitación que no son evapotranspirados.

> Es importante tener en cuenta que en algunas zonas particulares, se pueden obtener déficits debido a que el valor estimado o medido de la evapotranspiración puede ser mayor al valor de precipitación disponible.

La siguiente expresión permite determinar el caudal medio en cada celda de terreno, en el que, al valor estimado de precipitación, se le resta la abstracción correspondiente a la evapotranspiración real. El valor correspondiente al área sobre el cual se estima el caudal corresponde al total de celdas convergentes multiplicadas por el tamaño de cada pixel, el cual es definido por la resolución espacial de las grillas utilizadas.

<div align="center">

Qm = (( P – E ) * A) / t

</div>

Donde,

* Qm: caudal medio, m³/s
* P: precipitación, mm/año
* E: evapotranspiración real, mm/año
* A: área de cada celda, m²
* t: tiempo en segundos en un año, (365 dias x 24 horas x 60 minutos x 60 segundos = 31.536.000.000)


### Precipitación [^1]

La precipitación es normalmente, la única fuente de humedad que tiene la capa superficial del suelo y por eso es conveniente que su medida y cálculo se hagan con gran precisión, pues de ello depende, en gran manera, la exactitud de todos los cálculos del balance hídrico.

La cantidad media de precipitación en una cuenca o en cualquier otra zona, se obtiene a partir de los datos de pluviómetros, pluviógrafos o totalizadores instalados en la zona en estudio. Cuanto más corto sea el período de cálculo del balance hídrico, más densa debe ser la red de medida de la precipitación.

Para calcular balances hídricos medios son necesarias series extensas de precipitación (alrededor de 25 - 50 años). Para estimar los datos que faltan es aconsejable establecer relaciones de datos observados en estaciones vecinas o usar correlaciones.


### Evapotranspiración [^2]

En los balances hidrológicos de largoplazo, la evapotranspiración real es la cantidad de agua, expresada en mm/año, que es efectivamente evaporada desde la superficie del suelo y transpirada por la cubierta vegetal. 

En general cuando se aborda el punto de la evapotranspiración real se hace referencia a la que se obtiene en un balance de humedad en el suelo. En un balance hídrico, la evapotranspiración potencial (o de referencia) solo se lleva a cabo cuando el suelo dispone de bastante agua para suplirla, de modo que en los períodos sin humedad en el suelo el valor de la pérdida de humedad puede ser menor que el calculado, es lo que se conoce como evapotranspiración real, que para un mes en concreto sería la suma de la precipitación en ese periodo y la reserva de agua del suelo al inicio del mismo. Únicamente cuando el valor anterior supera a la evaporación potencial (o referencia), puede satisfacerse esta y, en este caso, coincide con la real, el exceso de agua permanece como reserva del suelo. En los períodos más húmedos, dicho exceso, puede superar a la capacidad de reserva y existirá una evacuación de la sobrante por drenaje o escorrentía superficial si la permeabilidad del suelo es inferior a la intensidad de la precipitación.

Cuanto mayor es la evapotranspiración real de una zona mayor es la formación de biomasa vegetal en la misma, si bien existe una limitación en función de la fertilidad del suelo, que podría constituirse en el factor limitante del crecimiento. 


### Referencias

* [Unesco. (1981). Métodos de cálculo del balance hídrico.](https://unesdoc.unesco.org/ark:/48223/pf0000137771)
* [UPM. Evapotranspiración real](http://ocw.upm.es/pluginfile.php/675/mod_label/intro/Evapotranspiracion-real.pdf)


### Compatibilidad

* Este curso puede ser desarrollado con cualquier software SIG que disponga de herramientas para reacondicionamiento de modelos de terreno, creación de mosaicos, algebra de mapas y herramientas de análisis espacial. Algunas de las actividades han sido desarrolladas utilizando QGIS, ArcGIS for Desktop y ArcGIS Pro.
 


### Control de versiones

| Versión    | Descripción     | Autor                                      | Horas |
|------------|:----------------|--------------------------------------------|:-----:|
| 2022.12.22 | Versión inicial | [rcfdtools](https://github.com/rcfdtools)  |   0   |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Actividad anterior](../xxxx) | [Inicio](../../) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/99999) | [Actividad siguiente]()  |
|-------------------------------|------------------|---------------------------------------------------------------------------|--------------------------|

[^1]: Tomado o adaptado de: [Unesco. (1981). Métodos de cálculo del balance hídrico.](https://unesdoc.unesco.org/ark:/48223/pf0000137771)
[^2]: Tomado o adaptado de: http://ocw.upm.es/pluginfile.php/675/mod_label/intro/Evapotranspiracion-real.pdf