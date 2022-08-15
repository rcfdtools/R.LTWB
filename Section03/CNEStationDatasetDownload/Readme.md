## Obtención de series de datos discretos climatológicos de estaciones terrestres
Keywords: `IDEAM` `Weather Station` 

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationDatasetDownload/Graph/CNEStationDatasetDownload.png)

Para la creación de los mapas requeridos para la realización del balance hidrológico, es necesario a partir de las estaciones seleccionadas para la zona de estudio, obtener las series de valores discretos de precipitación total mensual, temperatura máxima diaria, temperatura mínima diaria y evaporación total diaria. Para la comparación de los caudales obtenidos, también son requeridas las series de caudal medio mensual.                       


### Objetivos

* A partir de las estaciones identificadas y seleccionadas para la zona de estudio, obtener las series o registros de las estaciones a partir de los datos disponibles en el portal DHIME del IDEAM.
* Integrar los datos descargados en archivos de texto separados por comas .csv en un único archivo.


### Requerimientos

* [Microsoft Excel from Office 64 bits.](https://aka.ms/office-install) 
* [Glosario de variables IDEAM.](https://github.com/rcfdtools/R.LTWB/blob/main/.datasets/GlosarioVariables.xlsx) [:mortar_board:Aprender.](https://github.com/rcfdtools/R.LTWB/tree/main/Section03/CNEStation)
* [Listado de estaciones seleccionadas de precipitación en la zona de estudio.](https://github.com/rcfdtools/R.LTWB/blob/main/.datasets/CNE_IDEAM_OE_ZE_Precipitacion.dbf) [:mortar_board:Aprender.](https://github.com/rcfdtools/R.LTWB/tree/main/Section03/CNEStation)
* [Listado de estaciones seleccionadas de temperatura del aire en la zona de estudio.](https://github.com/rcfdtools/R.LTWB/blob/main/.datasets/CNE_IDEAM_OE_ZE_TemperaturaAire.dbf) [:mortar_board:Aprender.](https://github.com/rcfdtools/R.LTWB/tree/main/Section03/CNEStation)
* [Listado de estaciones seleccionadas de evaporación potencial en la zona de estudio.](https://github.com/rcfdtools/R.LTWB/blob/main/.datasets/CNE_IDEAM_OE_ZE_Evaporacion.dbf) [:mortar_board:Aprender.](https://github.com/rcfdtools/R.LTWB/tree/main/Section03/CNEStation)
* [Listado de estaciones seleccionadas de caudal en la zona de estudio.](https://github.com/rcfdtools/R.LTWB/blob/main/.datasets/CNE_IDEAM_OE_ZE_NivelCaudal.dbf) [:mortar_board:Aprender.](https://github.com/rcfdtools/R.LTWB/tree/main/Section03/CNEStation)


### Diagrama general de procesos

El siguiente diagrama representa los procesos generales requeridos para el desarrollo de esta actividad.

<div align="center">
<br><img alt="R.LTWB" src="https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationDatasetDownload/Graph/CNEStationDatasetDownloadFlowchart.svg" width="75%"><br>
<sub>Convenciones generales en diagramas: clases de entidad en azul, dataset en gris oscuro, grillas en color verde, geo-procesos en rojo y procesos manuales en amarillo. Líneas con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>


### Conceptos generales 


#### Glosario de variables IDEAM


#### Nivel de aprobación de cada dato[^1]

| Código | Nivel de aprobación |
|:------:|:-------------------:|
|  900   |     Preliminar      |
|  1100  |     En revisión     |
|  1200  |     Definitivo      |

> La información validada o definitiva al encontrarse certificada, ha surtido el proceso de validación técnica necesaria que garantiza la calidad del dato y determina la oficialidad de la información que podrá ser utilizada para toma de decisiones. Para el desarrollo del caso de estudio, usaremos la información IDEAM en todos los niveles de aprobación disponibles.


### Procedimiento general manual

1. Dentro de la carpeta _D:\R.LTWB\\.datasets_, cree una nueva carpeta con el nombre _IDEAM_, y un nuevo libro de Microsoft Excel con el nombre CNEStationDatasetDownload.xlsx. Dentro del libro de Excel, crear 4 hojas y nombrar como: `Precipitacion`, `TemperaturaAire`, `EvaporacionPotencial` y `Caudal`.

2. Desde Excel, abra los siguientes archivos de estaciones seleccionadas que fueron exportados a formato DBase File .dbf, copie y pegue a las hojas del libro de Excel:

| Parámetro             | Archivo .dbf estaciones                                                                                                            | Hoja Excel           | Estaciones |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------|----------------------|------------|
| Precipitación         | [CNE_IDEAM_OE_ZE_Precipitacion.dbf](https://github.com/rcfdtools/R.LTWB/blob/main/.datasets/CNE_IDEAM_OE_ZE_Precipitacion.dbf)     | Precipitacion        | 139        |
| Temperatura del aire  | [CNE_IDEAM_OE_ZE_TemperaturaAire.dbf](https://github.com/rcfdtools/R.LTWB/blob/main/.datasets/CNE_IDEAM_OE_ZE_TemperaturaAire.dbf) | TemperaturaAire      | 42         |
| Evaporación potencial | [CNE_IDEAM_OE_ZE_Evaporacion.dbf](https://github.com/rcfdtools/R.LTWB/blob/main/.datasets/CNE_IDEAM_OE_ZE_Evaporacion.dbf)         | EvaporacionPotencial | 41         |
| Caudal                | [CNE_IDEAM_OE_ZE_NivelCaudal.dbf](https://github.com/rcfdtools/R.LTWB/blob/main/.datasets/CNE_IDEAM_OE_ZE_NivelCaudal.dbf)         | Caudal               | 65         |

3. En cada hoja del libro de Excel, agregue las siguientes dos columnas:

| Columna | Descripción                                                                                                    |
|---------|----------------------------------------------------------------------------------------------------------------|
| Ready   | Para marcación de cuales estaciones con series de datos descargables se encuentran en el servicio DHIME. `Y/N` |
| File    | Nombre del archivo descargado.                                                                                 |

> El propósito de estas columnas es registrar para cuáles estaciones fue posible realizar la descarga de series y en que archivo de la secuencia de descarga se encuentran los datos obtenidos. 

4. En cada hoja, mueva las columnas `DEPARTAMEN` y `MUNICIPIO` después de la columna `COIDGO`. En el menú _Data_, seleccione la opción _Filter_ y desde el menú _View_, congele la primera fila correspondiente a las etiquetas de columna.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationDatasetDownload/Screenshot/MicrosoftExcelCNEStationDatasetDownload.png)

> Debido a que los datos se han copiado desde archivos .dbf, es posible que debido a la codificación de texto, no se visualicen correctamente las tildes y eñes.

5. Ingrese al portal [DHIME](http://dhime.ideam.gov.co/atencionciudadano/) del [IDEAM - Colombia](http://www.ideam.gov.co/), acepte los términos de referencia y de clic en _Aceptar_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationDatasetDownload/Screenshot/DHIMETerminos.png)


### Descarga de series de precipitación

6. En la pestaña _Consultar_, defina los siguientes parámetros:

* Periodo
  * Fecha Inicial: `31/12/1899`, correspondiente a fecha a partir de la cual se pueden obtener registros desde el servicio DHIME.
  * Fecha Final: `01/01/2022`, para la obtención de series utilizaremos años cronológicos completos cuyo último registro corresponde al 31 de diciembre de cada año. Dentro del servicio DHIME, es necesario incluir el 01 de enero del año inmediatamente siguiente debido a que el proceso de filtrado se realiza para valores menores qué. 
* Serie de Tiempo y Frecuencia: `Estándar`, debido a que la descarga a realizar corresponde a series de datos mensuales para los datos de precipitación.
* Parámetro: `PRECIPITACIÓN`.
* Variable: `Lista Completa` seleccionando `Precipitación total mensual`

> Las descargas a partir de la fecha final también pueden ser realizadas a partir de [años hidrológicos](https://es.wikipedia.org/wiki/A%C3%B1o_hidrol%C3%B3gico) completos que pueden corresponder a periodos del 01 de junio al 31 de mayo del año inmediatamente siguiente o a las fracciones de invierno a verano o ciclos estacionales dependiendo de la zona geográfica.


### Referencias

* http://dhime.ideam.gov.co/atencionciudadano/
* http://www.ideam.gov.co/
* https://es.wikipedia.org/wiki/A%C3%B1o_hidrol%C3%B3gico


### Control de versiones

| Versión    | Descripción     | Autor                                      | Horas |
|------------|:----------------|--------------------------------------------|:-----:|
| 2022.08.15 | Versión inical. | [rcfdtools](https://github.com/rcfdtools)  |  4.5  |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Anterior](https://github.com/rcfdtools/R.LTWB/tree/main/Section03/CNEStationElevation) | [:house: Inicio](https://github.com/rcfdtools/R.LTWB/wiki) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/9999) | [Siguiente]() |
|--------------------------------------------------------------------------------|------------------------------------------------------------|--------------------------------------------------------------------------|---------------|

[^1]: http://dhime.ideam.gov.co/atencionciudadano/