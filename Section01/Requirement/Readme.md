## Requerimientos
Keywords: `Requirements` `ArcGIS-for-Desktop` `ArcGIS-Pro` `QGIS` `HEC-HMS` `HEC-GeoHMS` `Python`

![R.LTWB](Graph/Requirement.png)

En esta actividad se listan los requerimientos académicos y computacionales para el desarrollo de las diferentes actividades del curso, se define y crea la estructura de directorios y se realiza la instalación y configuración de las herramientas requeridas.


### Objetivos

* Instalar y configurar las herramientas computacionales requeridas para el desarrollo del caso de estudio.
* Establecer los requisitos académicos mínimos y listar algunos recursos complementarios para su nivelación.


### Requerimientos computacionales generales

* [ArcGIS Pro 2+](https://pro.arcgis.com/en/pro-app/latest/get-started/download-arcgis-pro.htm)
* [ArcGIS for Desktop 10+](https://desktop.arcgis.com/es/desktop/) (opcional)
* [ArcGIS Pro 3.0.0 setup requires .NET Desktop Runtime 6.0.6](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) 
* Para el cargue de archivos de Microsoft Excel en formato .xls, se requiere del [Driver de Microsoft Access Database Engine](https://www.microsoft.com/en-us/download/confirmation.aspx?id=54920).
* [QGIS 3+](https://qgis.org/) (opcional)
* QGIS plugin: [Profile tool](https://plugins.qgis.org/plugins/profiletool/)
* QGIS plugin: [QGis2threejs](https://plugins.qgis.org/plugins/Qgis2threejs/)
* QGIS plugin: [HCMGIS](https://plugins.qgis.org/plugins/HCMGIS/)
* [Arc Hydro Tools Pro](http://downloads.esri.com/archydro/archydro/setup/Pro/)
* [Cygwin terminal for Windows](https://www.cygwin.com/)
* [HEC-HMS 4.9+](https://www.hec.usace.army.mil/software/hec-hms/) 
* [HEC-GeoHMS 10.2](https://www.hec.usace.army.mil/software/hec-geohms/downloads.aspx) for ArcGIS for Desktop 10.2.2
* [Microsoft Excel from Office 64 bits](https://aka.ms/office-install)
* [Notepad++](https://notepad-plus-plus.org)
* [Python 3+](https://www.python.org/)
* [Pandas para Python 3+](https://pandas.pydata.org/)

> Las herramientas computacionales específicas requeridas, librerías, complementos y sus versiones, son especificadas en cada actividad del curso.


### Servicios y plataformas

* Cuenta de usuario en [Eathdata](../../Section02/UserCreation) de la NASA.
* Cuenta de usuario [Esri](https://www.esri.com/en-us/home).


### Requisitos académicos

* Conocimientos básicos en sistemas de información geográfica
* Conocimientos básicos en hidrología
* Conocimientos básicos de programación usando Python


### Estructura de directorios

En la siguiente tabla encontrará la estructura y descripción general de las carpetas a utilizar durante el desarrollo de las actividades del curso, relacionadas con el caso de estudio general y el caso asignado bajo la modalidad de curso certificado.

| Directorio                               | Descripción                                                                                                                                                           | Subdirectorios                                                           | Formato                                                          |
|------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------|
| [.datasets](../../.datasets)             | Tablas y series de datos base y generados                                                                                                                             | CHIPS, ENSOONI, IDEAM, IDEAM_Agg, IDEAM_EDA, IDEAM_Impute, IDEAM_Outlier | .xls, .xlsx, .dbf, .csv, .png, .md, .zip                         |
| [.dem](../../.dem)                       | Grillas base y grillas producidas de los modelos digitales de terreno                                                                                                 | ALOS, ASTER, SRTM                                                        | .tif, .rar                                                       |
| [.gdb](../../.gdb)                       | GDB descargada del Instituto Geográfico Agustín Codazzi - IGAC de Colombia - Suramérica                                                                               | N/A                                                                      | .gdb                                                             |
| [.grid](../../.grid)                     | Grillas en formato GeoTIFF producidas en la sección 4 y 5 de este curso, relacionadas con el análisis espacial de variables climatológicas y mapas de isorendimientos | N/A                                                                      | .tif, .rar                                                       |
| [.icons](../../.icons)                   | Iconografía general de este repositorio                                                                                                                               | N/A                                                                      | .png, .cdr, .glb, .svg                                           |
| [.map](../../.map)                       | Mapas de documento y proyectos geográficos creados en aplicaciones SIG                                                                                                | ArcGISPro, ArcGISProSection03, ArcGISProSection04, ArcGISProSection05    | .mxd, .sxd, .aprx, .qgz, .zip                                    |
| [.projectionfile](../../.projectionfile) | Archivos independientes de proyección de coordenadas en formato .prj aplicables a Colombia - Suramérica                                                               | N/A                                                                      | .prj                                                             |
| [.refs](../../.refs)                     | Documentos y artículos de uso libre descargados y citados en la documentación o en las referencias particulares de las diferentes actividades                         | GitHubRefs                                                               | .pdf, .zip                                                       |
| [.shp](../../.shp)                       | Vectores base y vectores producidos en formato Shapefile (.shp)                                                                                                       | N/A                                                                      | .shp, .zip                                                       |
| [.src](../../.src)                       | Scripts independientes de uso general en lenguaje Python y Shell script                                                                                               | N/A                                                                      | .py, .sh, .zip                                                   |
| [.temp](../../.temp)                     | Archivos ejemplo y archivos temporales generados en procesos intermedios                                                                                              | N/A                                                                      | .xlsx, .md                                                       |
| [HECGeoHMS](../../HECGeoHMS)             | _/Layers_, contiene los archivos generados durante el proceso de preprocesamiento hidrológico de los modelos digitales de elevación - DEM                             | Layers                                                                   | .mxd, .tif, .rar                                                 |
| [HECHMS](../../HECHMS)                   | Archivos del modelo prototipo hidrológico HEC-HMS, utilizados para el reacondicionamiento del modelo digital de elevación ASTER GDEM                                  | maps                                                                     | .basin, .sqlite, .access, ,dss, .hms, .log, .out, .terrain, .xml |



### Configuración del sistema operativo

Para la correcta ejecución de las herramientas computacionales a utilizar durante el desarrollo de las actividades del curso, es recomendable realizar los siguientes ajustes en Microsoft Windows.

1. En el escritorio de Microsoft Windows, oprima la combinación de teclas <kbd>Windows</kbd>+<kbd>R</kbd> para abrir la ventana de ejecución de comandos e ingrese _Control_. 

![R.LTWB](Screenshot/Windows11RunControl.png)

2. En el _Panel de Control_ de clic en la opción _View by:_ y seleccione _Large Icons_, luego de clic en la opción _Region_. Verifique y establezca el formato de fecha como `d/M/yyyy` y hora como `HH:mm`.

![R.LTWB](Screenshot/Windows11ControlPanel.png)

3. En _Región_ de clic en el botón _Configuración adicional..._

![R.LTWB](Screenshot/Windows11ControlPanelAdditionalSettings.png)

4. En _Configuración adicional..._ establezca la siguiente configuración y de clic en el botón _Apply_ y _Ok_

* Separador decimal: punto
* Símbolo de separación de miles: coma
* Separador de listas: coma

![R.LTWB](Screenshot/Windows11ControlPanelAdditionalSettingsSymbol.png)

5. Una vez establecida la configuración regional, abra el Explorador de Windows y en el menú _View / Show_, seleccione la opción _File name extensions_ que le permitirá visualizar las extensiones de todos los archivos. Esta opción es especialmente útil al buscar archivos específicos que tienen el mismo nombre y diferentes extesiones, tales como los archivos de formas Shapefile que utilizan nativamente las extensiones .shp, shx, .dbf y .prj.

![R.LTWB](Screenshot/Windows11FileNameExtensions.png)

> Opcionalmente, puede activar la visualización de archivos ocultos que le permitirá eliminar archivos temporales no visibles regularmente a usuarios.


### Instalación y configuración de ArcGIS for Desktop


### Instalación y configuración de ArcGIS Pro

La apertura de proyectos existentes puede ser realizada correctamente si su sistema operativo dispone del [Driver de Microsoft Access Database Engine](https://www.microsoft.com/en-us/download/confirmation.aspx?id=54920). Cuando la apertura de un proyecto de ArcGIS Pro presenta demoras excesivas se debe a que no se han podido resolver los permisos de lectura sobre los datos o que no se dispone de los drivers necesarios para la apertura de archivos provenientes de Microsoft Excel.

1. Ingrese al portal    

https://www.esri.com/en-us/arcgis/products/arcgis-pro/trial#students

### Instalación y configuración de QGIS


### Instalación y configuración de Python con entornos virtuales


### Referencias

* 



### Control de versiones

| Versión     | Descripción                                              | Autor                                      | Horas  |
|-------------|:---------------------------------------------------------|--------------------------------------------|:------:|
| 2022.07.13  | Versión inicial con lista preliminar de requerimientos.  | [rcfdtools](https://github.com/rcfdtools)  |  0.5   |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Anterior](../WhatIsLTWB) | [:house: Inicio](../../Readme.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.LTWB/discussions/9999) | [Siguiente](../CaseStudy) |
|---------------------------|-----------------------------------|-------------------------------------------------------------------------------------|---------------------------|