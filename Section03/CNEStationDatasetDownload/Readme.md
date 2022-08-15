## Obtención de series de datos discretos climatológicos de estaciones terrestres
Keywords: `IDEAM` `Weather Station` `DHIME` `Rain` `Air Temperature` `Evaporation` `Water Flow`

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationDatasetDownload/Screenshot/CNEStationDatasetDownload.png)

Para la creación de los mapas requeridos para la realización del balance hidrológico, es necesario a partir de las estaciones seleccionadas para la zona de estudio, obtener las series de valores discretos de precipitación total mensual, temperatura máxima diaria, temperatura mínima diaria y evaporación total diaria. Para la comparación de los caudales obtenidos, también son requeridas las series de caudal medio mensual.                       


### Objetivos

* A partir de las estaciones identificadas y seleccionadas para la zona de estudio, obtener las series o registros de las estaciones a partir de los datos disponibles en el portal DHIME del IDEAM.
* Integrar los archivos de datos independientes descargados en archivos de texto separados por comas .csv, en un único archivo.


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

El libro de Excel del [glosario de variables del IDEAM - Colombia](https://github.com/rcfdtools/R.LTWB/blob/main/.datasets/GlosarioVariables.xlsx), se compone de 3 hojas de cálculo que contienen el listado de etiquetas básicas de los diferentes parámetros de la red hidroclimátológica y las etiquetas de las series diarias derivadas que corresponden a datos que se calculan a partir de las series básicas. La versión utilizada para ejemplificar esta clase corresponde a la fecha 2022.07.31. 

<div align="center">

#### Nivel de aprobación de cada dato[^1]

| Código | Nivel de aprobación |
|:------:|:-------------------:|
|  900   |     Preliminar      |
|  1100  |     En revisión     |
|  1200  |     Definitivo      |

</div>

> La información validada o definitiva al encontrarse certificada, ha surtido el proceso de validación técnica necesaria que garantiza la calidad del dato y determina la oficialidad de la información que podrá ser utilizada para toma de decisiones. Para el desarrollo del caso de estudio, usaremos la información IDEAM en todos los niveles de aprobación disponibles.


### Procedimiento general manual

1. Dentro de la carpeta _D:\R.LTWB\\.datasets_, cree una nueva carpeta con el nombre _IDEAM_, y un nuevo libro de Microsoft Excel con el nombre _CNEStationDatasetDownload.xlsx_. Dentro del libro de Excel, crear 4 hojas y nombrar como: `Precipitacion`, `TemperaturaAire`, `EvaporacionPotencial` y `Caudal`.

2. Desde Excel, abra los siguientes archivos de estaciones seleccionadas que fueron exportados a formato DBase File .dbf, copie y pegue todos los registros a las hojas del libro de Excel:

<div align="center">

| Parámetro             | Archivo .dbf estaciones                                                                                                            | Hoja Excel           | Estaciones |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------|----------------------|------------|
| Precipitación         | [CNE_IDEAM_OE_ZE_Precipitacion.dbf](https://github.com/rcfdtools/R.LTWB/blob/main/.datasets/CNE_IDEAM_OE_ZE_Precipitacion.dbf)     | Precipitacion        | 139        |
| Temperatura del aire  | [CNE_IDEAM_OE_ZE_TemperaturaAire.dbf](https://github.com/rcfdtools/R.LTWB/blob/main/.datasets/CNE_IDEAM_OE_ZE_TemperaturaAire.dbf) | TemperaturaAire      | 42         |
| Evaporación potencial | [CNE_IDEAM_OE_ZE_Evaporacion.dbf](https://github.com/rcfdtools/R.LTWB/blob/main/.datasets/CNE_IDEAM_OE_ZE_Evaporacion.dbf)         | EvaporacionPotencial | 41         |
| Caudal                | [CNE_IDEAM_OE_ZE_NivelCaudal.dbf](https://github.com/rcfdtools/R.LTWB/blob/main/.datasets/CNE_IDEAM_OE_ZE_NivelCaudal.dbf)         | Caudal               | 65         |

</div>

3. En cada hoja del libro de Excel, agregue las siguientes dos columnas:

<div align="center">

| Columna | Descripción                                                                                                    |
|---------|----------------------------------------------------------------------------------------------------------------|
| Ready   | Para marcación de cuales estaciones con series de datos descargables se encuentran en el servicio DHIME. `Y/N` |
| File    | Nombre del archivo descargado.                                                                                 |

</div>

> El propósito de estas columnas es registrar para cuáles estaciones fue posible realizar la descarga de series y en que archivo de la secuencia de descarga se encuentran los datos obtenidos. Posteriormente, realizaremos la lectura de los mismos parámetros a partir de información satelital, pero únicamente para las estaciones terrestres que disponen de información.

4. En cada hoja, mueva las columnas `DEPARTAMEN` y `MUNICIPIO` después de la columna `COIDGO`. En el menú _Data_, seleccione la opción _Filter_ y desde el menú _View_, congele la primera fila correspondiente a las etiquetas de columna. Ordene las estaciones por Departamento y código para facilitar la búsqueda y la descarga.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationDatasetDownload/Screenshot/MicrosoftExcelCNEStationDatasetDownload.png)

> Debido a que los datos se han copiado desde archivos .dbf, es posible que por la codificación de texto, no se visualicen correctamente las tildes y eñes.

5. Ingrese al portal [DHIME](http://dhime.ideam.gov.co/atencionciudadano/) del [IDEAM - Colombia](http://www.ideam.gov.co/), acepte los términos de referencia y de clic en _Aceptar_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationDatasetDownload/Screenshot/DHIMETerminos.png)


### Descarga de series de precipitación

6. En la pestaña _Consultar_, defina los siguientes parámetros:

* Periodo
  * Fecha Inicial: `31/12/1899`, correspondiente a fecha a partir de la cual se pueden obtener registros desde el servicio DHIME.
  * Fecha Final: `01/01/2022`, para la obtención de series utilizaremos años cronológicos completos cuyo último registro corresponde al 31 de diciembre de cada año. Dentro del servicio DHIME, es necesario incluir el 01 de enero del año inmediatamente siguiente debido a que el proceso de filtrado se realiza para valores menores qué. 
* Serie de Tiempo y Frecuencia: `Estándar`, debido a que la descarga a realizar corresponde a series de datos mensuales para los datos de precipitación.
* Parámetro: `PRECIPITACIÓN`.
* Variable: `Lista Completa` seleccionando `Precipitación total mensual` que de acuerdo al Glosario de Variables del IDEAM, corresponde a una _variable derivada_ debido a que requiere de un proceso de cálculo a partir de la sumatoria de los valores registrados horarios, diarios o de frecuencias inferiores. 

> Las descargas a partir de la definición de la fecha final, también pueden ser realizadas a partir de [años hidrológicos](https://es.wikipedia.org/wiki/A%C3%B1o_hidrol%C3%B3gico) que pueden corresponder a periodos del 01 de junio al 31 de mayo del año inmediatamente siguiente, fracciones de invierno a verano o ciclos estacionales dependiendo de la zona geográfica.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationDatasetDownload/Screenshot/DHIMEPrecipitacionParametros.png)

Glosario de variables del IDEAM - Series básicas
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationDatasetDownload/Screenshot/MicrosoftExcelGlosarioVariablesBasicasPrecipitacion.png)

Glosario de variables del IDEAM - Series derivadas
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationDatasetDownload/Screenshot/MicrosoftExcelGlosarioVariablesDerivadasPrecipitacion.png)

7. En la sección _Datos Estación_ de DHIME, seleccione el departamento de Bolivar y todos sus municipios. Desde el archivo de Excel y la hoja _Precipitacion_, seleccione el código de la primera estación y oprima las teclas <kbd>Ctrl</kbd> + <kbd>c</kbd>; en el navegador de Internet oprima <kbd>Ctrl</kbd> + <kbd>f</kbd> para abrir el cuadro de búsqueda, con <kbd>Ctrl</kbd> + <kbd>v</kbd> pegue el código y de <kbd>Enter</kbd>. Automáticamente será dirigido a la estación, marque la casilla de selección ubicada en la parte izquierda y repita el procedimiento hasta marcar 10 estaciones si estas se encuentran en el mismo Departamento. En el libro de Excel, ingrese `Y` en la columna `Ready` si la estación se encuentra disponible en DHIME y `N` si no aparece en la búsqueda.

> Para navegadores de Internet en español oprima <kbd>Ctrl</kbd> + <kbd>b</kbd> para realizar búsquedas.
> 
> DHIME permite realizar descargas simultáneas de registros para máximo 10 estaciones.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationDatasetDownload/Screenshot/DHIMEPrecipitacionDescarga.png)

Debido a que para el departamento de Bolivar solo descargaremos los datos de 7 estaciones, es necesario dar clic en el botón `Agregar a la Consulta` y luego dar clic en el botón `Agregar Otros` que permitirá agregar 3 estaciones más sin perder el periodo definido. Es necesario volver a seleccionar manualmente el parámetro para continuar la búsqueda y marcado de las estaciones.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationDatasetDownload/Screenshot/DHIMEPrecipitacionDescargaQueryAdd.png)

Seleccione y agregue las 3 primeras estaciones del departamento del Cesar registradas en el libro de Excel para completar el bloque de 10 estaciones. De clic en el botón `Agregar a la Consulta` que lo llevará a la pestaña de descargas y de clic en el botón `Descargar`. Obtendrá en la carpeta de descargas de su sistema operativo, un archivo comprimido en formato .zip con el nombre _datos.zip_ que contendrá dentro un archivo de texto separado por comas denominado _excel.csv.csv_. En el libro de Excel, registre el nombre del archivo descargado en la columna `File`.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationDatasetDownload/Screenshot/DHIMEPrecipitacionDescargaCSV.png)

> Dependiendo del tipo de frecuencia, de la longitud de la serie y del número de solicitudes simultáneas realizadas por otros usuarios al servidor DHIME, la descarga de cada archivo comprimido podrá tardar algunos segundos o minutos.

En el portal DHIME, de clic en el botón `Limpiar` y repita el procedimiento de descarga anterior hasta obtener los registros de precipitación de todas las estaciones requeridas para la zona de estudio. Recuerde registrar los valores correspondientes en las columnas `Ready` y `File` del libro de Excel.

Resumen de datos obtenidos para precipitación total mensual
* 139 seleccionadas, 131 descargables de IDEAM
* Comprimidos de datos.zip a datos (14).zip


### Descarga de series de temperatura del aire

8. Para la descarga de las series temporales de temperatura, utilice los siguientes parámetros:

* Periodo
  * Fecha Inicial: `31/12/1899`, correspondiente a fecha a partir de la cual se pueden obtener registros desde el servicio DHIME.
  * Fecha Final: `01/01/2022`, para la obtención de series utilizaremos años cronológicos completos cuyo último registro corresponde al 31 de diciembre de cada año. Dentro del servicio DHIME, es necesario incluir el 01 de enero del año inmediatamente siguiente debido a que el proceso de filtrado se realiza para valores menores qué. 
* Serie de Tiempo y Frecuencia: `Estándar`, debido a que la descarga a realizar corresponde a series de datos diarios.
* Parámetro: `TEMPERATURA`.
* Variable: `Lista Completa` seleccionando y descargando primero `Temperatura máxima diaria` y luego `Temperatura mínima diaria`, que de acuerdo al Glosario de Variables del IDEAM, corresponden a _variables básicas_ debido a que no requieren de un proceso de cálculo y son obtenidas directamente de un registrador. 

> DHIME no dispone de registros derivados de temperatura media mensual calculados a partir de los datos diarios, por lo que es necesario calcular los valores medios a partir de los datos máximos y mínimos.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationDatasetDownload/Screenshot/DHIMETemperaturaAireParametros.png)

Glosario de variables del IDEAM - Series básicas
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationDatasetDownload/Screenshot/MicrosoftExcelGlosarioVariablesBasicasTemperaturaAire.png)

Glosario de variables del IDEAM - Series derivadas
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationDatasetDownload/Screenshot/MicrosoftExcelGlosarioVariablesDerivadasTemperaturaAire.png)

Resumen de datos obtenidos para temperatura máxima diaria
* 42 seleccionadas, 25 descargables de IDEAM
* Comprimidos de datos (15).zip a datos (17).zip

Resumen de datos obtenidos para temperatura mínima diaria
* 42 seleccionadas, 25 descargables de IDEAM
* Comprimidos de datos (18).zip a datos (20).zip


### Descarga de series de evaporación potencial

9. Para la descarga de las series temporales de evaporación potencial, utilice los siguientes parámetros:

* Periodo
  * Fecha Inicial: `31/12/1899`, correspondiente a fecha a partir de la cual se pueden obtener registros desde el servicio DHIME.
  * Fecha Final: `01/01/2022`, para la obtención de series utilizaremos años cronológicos completos cuyo último registro corresponde al 31 de diciembre de cada año. Dentro del servicio DHIME, es necesario incluir el 01 de enero del año inmediatamente siguiente debido a que el proceso de filtrado se realiza para valores menores qué. 
* Serie de Tiempo y Frecuencia: `Estándar`, debido a que la descarga a realizar corresponde a series de datos diarios.
* Parámetro: `EVAPORACIÓN`.
* Variable: `Lista Completa` seleccionando y descargando `Evaporación total diaria`, que de acuerdo al Glosario de Variables del IDEAM, corresponde a una _variable básica_ debido a que no requieren de un proceso de cálculo y es obtenida directamente de un registrador. 

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationDatasetDownload/Screenshot/DHIMEEvaporacionParametros.png)

Glosario de variables del IDEAM - Series básicas
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationDatasetDownload/Screenshot/MicrosoftExcelGlosarioVariablesBasicasEvaporacion.png)

Glosario de variables del IDEAM - Series derivadas
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationDatasetDownload/Screenshot/MicrosoftExcelGlosarioVariablesDerivadasEvaporacion.png)

Resumen de datos obtenidos para evaporación total diaria
* 41 seleccionadas, 1 descargable de IDEAM correspondiente a la estación 29065130
* Comprimido de datos datos (21).zip

>Como puede observar en las imágenes de referencia, al seleccionar este parámetro no es posible descargar los datos derivados correspondientes a evaporación total mensual. 


### Descarga de series de caudal medio mensual

10. Para la descarga de las series temporales de caudal medio mensual, utilice los siguientes parámetros:

* Periodo
  * Fecha Inicial: `31/12/1899`, correspondiente a fecha a partir de la cual se pueden obtener registros desde el servicio DHIME.
  * Fecha Final: `01/01/2022`, para la obtención de series utilizaremos años cronológicos completos cuyo último registro corresponde al 31 de diciembre de cada año. Dentro del servicio DHIME, es necesario incluir el 01 de enero del año inmediatamente siguiente debido a que el proceso de filtrado se realiza para valores menores qué. 
* Serie de Tiempo y Frecuencia: `Estándar`, debido a que la descarga a realizar corresponde a series de datos medios mensuales.
* Parámetro: `CAUDAL`.
* Variable: `Lista Completa` seleccionando y descargando `Caudal medio mensual`, que de acuerdo al Glosario de Variables del IDEAM, corresponde a una _variable derivada_ debido a que requiere de un proceso de cálculo a partir del promedio de los valores registrados a nivel horario. 

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationDatasetDownload/Screenshot/DHIMECaudalParametros.png)

Glosario de variables del IDEAM - Series básicas
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationDatasetDownload/Screenshot/MicrosoftExcelGlosarioVariablesBasicasCaudal.png)

Glosario de variables del IDEAM - Series derivadas
![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationDatasetDownload/Screenshot/MicrosoftExcelGlosarioVariablesDerivadasCaudal.png)

Resumen de datos obtenidos para caudal medio mensual
* 65 seleccionadas, 57 descargables de IDEAM
* Comprimidos de datos (22).zip a datos (27).zip

Al finalizar la descarga de todos los registros para todos los parámetros requeridos, copie los archivos comprimidos en la carpeta _[D:\R.LTWB\\.datasets\IDEAM](https://github.com/rcfdtools/R.LTWB/tree/main/.datasets/IDEAM)_.

![R.LTWB](https://github.com/rcfdtools/R.LTWB/blob/main/Section03/CNEStationDatasetDownload/Screenshot/DatasetsIDEAM.png)


### Referencias

* http://dhime.ideam.gov.co/atencionciudadano/
* http://www.ideam.gov.co/
* https://es.wikipedia.org/wiki/A%C3%B1o_hidrol%C3%B3gico


### Control de versiones

| Versión    | Descripción                                                                                             | Autor                                      | Horas |
|------------|:--------------------------------------------------------------------------------------------------------|--------------------------------------------|:-----:|
| 2022.08.15 | Versión inical. Descarga completa de series para estaciones de la zona de estudio desde el portal DHIME | [rcfdtools](https://github.com/rcfdtools)  |   7   |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Anterior](https://github.com/rcfdtools/R.LTWB/tree/main/Section03/CNEStationElevation) | [:house: Inicio](https://github.com/rcfdtools/R.LTWB/wiki) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/9999) | [Siguiente]() |
|--------------------------------------------------------------------------------|------------------------------------------------------------|--------------------------------------------------------------------------|---------------|

[^1]: http://dhime.ideam.gov.co/atencionciudadano/