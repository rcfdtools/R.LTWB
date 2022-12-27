## Source code files

Esta carpeta contiene scripts y librerías independientes de uso general


### Extensiones

* .py: script o librería de Python
* .sh: shell script for Linux 


### Scripts

| Script                                       | Descripción                                                                                                                                                                                               | Lenguaje     | Actividad                                                           |
|----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------|
| [downloadASTER.sh](downloadASTER.sh)         | Descarga automática de modelos digitales de elevación ASTER GDEM                                                                                                                                          | Shell script | [DEMAster](../Section02/DEMAster)                                   |
| [downloadSRTM.sh](downloadSRTM.sh)           | Descarga automática de modelos digitales de elevación SRTM                                                                                                                                                | Shell script | [DEMSrtm](../Section02/DEMSrtm)                                     |
| [downloadALOS.sh](downloadALOS.sh)           | Descarga automática de modelos digitales de elevación ALOS PALSAR                                                                                                                                         | Shell script | [DEMAlos](../Section02/DEMAlos)                                     |
| [CNEStationCSVJoin.py](CNEStationCSVJoin.py) | Descomprime múltiples archivos de series .csv contenidos en archivos .zip obtenidas manualmente del [IDEAM](http://dhime.ideam.gov.co/atencionciudadano/) y los une en un único archivo de registros .csv | Python       | [CNEStationDatasetDownload](../Section03/CNEStationDatasetDownload) |
| [ChirpsGetValue.py](ChirpsGetValue.py)       | Obtención de series de datos discretos climatológicos satelitales y correlación con datos terrestres                                                                                                      | Python       | [RemoteSensing](../Section03/RemoteSensing)                         |
| [EDA.py](EDA.py)                             | Exploración y análisis de series - EDA - Representación gráfica                                                                                                                                           | Python       | [EDA](../Section03/EDA)                                             |
| [Outlier.py](Outlier.py)                     | Identificación y procesamiento de datos atípicos - Outliers                                                                                                                                               | Python       | [Outlier](../Section03/Outlier)                                     |
| [Impute.py](Impute.py)                       | Completado y extendido de series - Imputación                                                                                                                                                             | Python       | [Impute](../Section03/Impute)                                       |
| [ENSOONI.py](ENSOONI.py)                     | Análisis de cambio climático para segmentación de series                                                                                                                                                  | Python       | [ENSOONI](../Section03/ENSOONI)                                     |
| [Agg.py](Agg.py)                             | Agregación estadística para obtención de promedios multianuales compuestos y por fenómeno climatológico                                                                                                   | Python       | [Agg](../Section03/Agg)                                             |
| [Test.py](Test.py)                           | Archivo para pruebas de ejecución                                                                                                                                                                         | Python       | N/A                                                                 |


##

_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [:house: Inicio](../Readme.md) |
|--------------------------------|