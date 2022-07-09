## Descarga de modelo digital de elevación - DEM - NASA ASTER GDEM v2, v3 (30m)
Keywords: `NASA` `jpl` `ArcScene` `3D view` `Cygwin` `Shell script .sh` `Earthdata`

Los sensores remotos japoneses Advanced Spaceborne Thermal Emission and Reflection Radiometer o ASTER, proveen imágenes de alta resolución del Planeta Tierra y las capturas están compuestos por 14 diferentes bandas del espectro electromagnético en el rango visible de la luz termal infrarroja. Las imágenes son capturadas en resoluciones entre 15 y 90 metros permitiendo crear mapas detallados de la temperatura y elevación de la tierra.

A partir del segundo semestre de 2019, los modelos de terreno ASTER GDEM v2 han sido reemplazados por la versión 3 integrada de todo el mundo. Como novedad, la v3 no presenta los problemas de sobre elevaciones debida a nubes.


### Objetivos

* Descargar manualmente las imágenes del mosaico de terreno para la zona de estudio.
* Descargar automáticamente imágenes desde la consola Cygwin a través del script download.sh de Earthdata.
* Cargar y visualizar las imágenes en herramientas GIS.
* Visualizar perfiles de terreno.


### Requerimientos

* ArcGIS for Desktop 10+
* ArcGIS Pro (opcional)
* QGIS 3+ (opcional)
* [Cygwin terminal for Windows](https://www.cygwin.com/)
* Cuenta de usuario en [Eathdata](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/UserCreation) de la NASA.
* Polígono envolvente que delimita la zona de estudio. [[Ver clase]](https://github.com/rcfdtools/R.LTWB/tree/main/Section01/CaseStudy) [[Shapefile]](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudioEnvelope.shp).


### Procedimiento de descarga

1. Ingresar al servicio web de la NASA: https://search.earthdata.nasa.gov y dar clic en Earthdata login.

> Realizar el ingreso de usuario usando _LOG IN_ o realizar el registro de nuevo usuario dando clic en _REGISTER_, [Ver instrucciones detalladas.](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/UserCreation)

3. Delimitar en la vista satelital la extensión de la zona a descargar, para ello podrá utilizar diferentes métodos como:

| Método    | Descripción                                                                                                                                                                                                            |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Polygon   | Acercarse a la zona requerida y mediante clics definir un polígono de delimitación.                                                                                                                                    |
| Rectangle | Cree un rectángulo especificando las esquinas SW y NE en valores de latitud y longitud en grados decimales, p. ej. para el Departamento del Cesar en Colombia deberá ingresar SW: 7,-75 NE: 11,-72.                    |
| Point     | Coordenada de un punto indicando la latitud y longitud en grados decimales referenciados en el sistema de proyección de coordenadas WGS84 o dando clic en pantalla.                                                    |
| Circle    | Circunferencia especificando un punto central y el radio de aferencia. En pantalla se puede realizar manualmente localizando el puntero cerca a la localización requerida y clic definiendo manualmente el radio.      |
| File      | Permite seleccionar un archivo comprimido .zip que contenga el o los polígonos que delimiten la zona de estudio. Los formatos admisibles son ESRI Shapefile, Keyhole Markup Languaje (.kml or .kmz), GeoJSON y GeoRSS. |

Para el caso de estudio, utilizaremos el método File para definir la máscara de selección de elementos a descargar.

Desde la carpeta _.shp_ contenida en _D:\R.LTWB_, seleccione y comprima en formato .zip los archivos _ZonaEstudioEnvelope.dbf, ZonaEstudioEnvelope.prj, ZonaEstudioEnvelope.shp_ y _ZonaEstudioEnvelope.shx_ que conforman el Shapefile del polígono envolvente de la zona de estudio. Este archivo de formas tiene embebido el sistema de coordenadas geográfico GCS_MAGNA que puede ser interpretado directamente por Earthdata.

> Para archivos de formas que utilicen un sistema de coordenadas proyectado, será necesario crear un mapa nuevo en blanco en ArcGIS o QGIS, asignar el sistema de proyección de coordenadas geográfico WGS84 correspondiente al EPSG 4326, cargar y exportar la capa ZonaEstudioEnvelope.shp utilizando el sistema de coordenadas del proyecto, nombrando el archivo exportado como ZonaEstudioEnvelopeWGS84.shp

![EarthdataSearchByShapefile.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/DEMAster/Screenshot/EarthdataSearchByShapefile.png)

> Para búsquedas a partir de la opción rectangle especificando las coordenadas, p. ej. SW: 7,-75 NE: 11,-72 se resta internamente 0.1 grados alrededor del rectángulo SW: 7.1,-74.9 NE: 10.9,-72.1. Lo anterior para seleccionar únicamente las cuadrículas internas.

4. En la casilla de búsqueda ingresar _ASTER_ ó _ASTER Global Digital Elevation Model V003_. Para la zona de estudio, es necesario descargar 9 cuadrículas.

Como puede observar, las cuadrículas son ortogonales y no contienen traslapos debido a que corresponde a un modelo ya procesado y recortado. Para la zona de estudio, la información del modelo digital de elevación ha sido obtenida, procesada e integrada desde 2000.03.01 hasta 2013.11.30.

![EarthdataSearchResults.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/DEMAster/Screenshot/EarthdataSearchResults.png)

Cada archivo o cuadrante seleccionado será uno de los 22600 cuadrantes de la superficie terrestre que han sido divididos en grados de 1º x 1º que aproximadamente cubren 111.11km x 111.11km de área.

5. Verifique en el mapa de previsualización que las celdas solicitadas corresponden al polígono de la zona de estudio y de clic en la opción de descarga de datos _Download All_. Seleccione _Direct Download_ para obtener los 9 archivos requeridos que tienen un peso aproximado de 213.1 MB y de clic en _Done_ y _Download Data_.

![EarthdataSearchDirectDownload.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/DEMAster/Screenshot/EarthdataSearchDirectDownload.png)

En la ventana de descarga de clic derecho y seleccione la opción _Open link in new tab_ en los archivos _dem.tif correspondientes a los archivos GeoTIFF del modelo digital de elevación. 

> Los archivos _num.tif corresponden a validación y marcación de celdas ajustadas y no son requeridos para el ensamble del mosaico del modelo de elevación.

Listado de enlaces obtenidos  
* https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N09W074_dem.tif
* https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N09W074_num.tif
* https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N08W075_dem.tif
* https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N08W075_num.tif
* https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N08W073_dem.tif
* https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N08W073_num.tif
* https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N08W074_dem.tif
* https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N08W074_num.tif
* https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N09W075_dem.tif
* https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N09W075_num.tif
* https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N09W073_dem.tif
* https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N09W073_num.tif
* https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N10W075_dem.tif
* https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N10W075_num.tif
* https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N10W073_dem.tif
* https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N10W073_num.tif
* https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N10W074_dem.tif
* https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N10W074_num.tif

![EarthdataSearchDirectDownloadLink.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/DEMAster/Screenshot/EarthdataSearchDirectDownloadLink.png)

Copie los archivos descargados en la carpeta _.dem_ del directorio _D:\R.LTWB_

6. Descarga mediante shell script .sh con Cygwin [^1]

Con el propósito de realizar la descarga desde la consola de comandos a través de un script .sh, renombre la carpeta que contiene los archivos descargados manualmente desde Earthdata .dem a .dem1 y cree una carpeta nueva vacía con el nombre .dem.

> Linux: You must first make the script an executable by running the line 'chmod 777 download.sh' from the command line. After that is complete, the file can be executed by typing './download.sh'. For a detailed walk through of this process, please reference this How To guide.

> Windows: The file can be executed within Windows by first installing a Unix-like command line utility such as Cygwin. After installing Cygwin (or a similar utility), run the line 'chmod 777 download.sh' from the utility's command line, and then execute by typing './download.sh'.

Desde https://www.cygwin.com/, descargue e instale _Cygwin_ para Windows en la ruta _C:\cygwin64_. Ejecute la aplicación _Cygwin64 Terminal_ e ingrese los siguientes comandos:

* `chmod 777 'D:/R.LTWB/.src/download.sh'` para establecer los permisos de lectura, escritura y ejecución por cualquier usuario con acceso a la consola y al archivo.
* `cd 'D:/R.LTWB/.dem'` para ingresar al directorio de modelos digitales de elevación.
* `ls` para listar el contenido del directorio. Podrá observar que no existen archivos GeoTiFF correspondientes al modelo de terreno ni archivos de cookies.
* `'D:/R.LTWB/.src/download.sh'` para ejecutar _download.sh_ y obtener los archivos del modelo de terreno y almacenarlos en el directorio _.dem_

En la consola deberá ingresar su nombre de usuario y contraseña Earthdata para iniciar la descarga.

![Cygwin64Commands.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/DEMAster/Screenshot/Cygwin64Commands.png)

Al finalizar la ejecución ejecute nuevamente el comando `ls` para listar los archivos descargados o verifique manualmente el directorio de descarga _.dem_

Archivo [donwload.sh](https://github.com/rcfdtools/R.LTWB/blob/main/.src/download.sh) de Earthdata
```
#!/bin/bash

GREP_OPTIONS=''

cookiejar=$(mktemp cookies.XXX) #Original was XXXXXXXXXX
netrc=$(mktemp netrc.XXX)
chmod 0600 "$cookiejar" "$netrc"
function finish {
  rm -rf "$cookiejar" "$netrc"
}

trap finish EXIT
WGETRC="$wgetrc"

prompt_credentials() {
    echo "Enter your Earthdata Login or other provider supplied credentials"
    read -p "Username (r.ltwb): " username
    username=${username:-r.ltwb}
    read -s -p "Password: " password
    echo "machine urs.earthdata.nasa.gov login $username password $password" >> $netrc
    echo
}

exit_with_error() {
    echo
    echo "Unable to Retrieve Data"
    echo
    echo $1
    echo
    echo "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N09W074_dem.tif"
    echo
    exit 1
}

prompt_credentials
  detect_app_approval() {
    approved=`curl -s -b "$cookiejar" -c "$cookiejar" -L --max-redirs 5 --netrc-file "$netrc" https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N09W074_dem.tif -w %{http_code} | tail  -1`
    if [ "$approved" -ne "302" ]; then
        # User didn't approve the app. Direct users to approve the app in URS
        exit_with_error "Please ensure that you have authorized the remote application by visiting the link below "
    fi
}

setup_auth_curl() {
    # Firstly, check if it require URS authentication
    status=$(curl -s -z "$(date)" -w %{http_code} https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N09W074_dem.tif | tail -1)
    if [[ "$status" -ne "200" && "$status" -ne "304" ]]; then
        # URS authentication is required. Now further check if the application/remote service is approved.
        detect_app_approval
    fi
}

setup_auth_wget() {
    # The safest way to auth via curl is netrc. Note: there's no checking or feedback
    # if login is unsuccessful
    touch ~/.netrc
    chmod 0600 ~/.netrc
    credentials=$(grep 'machine urs.earthdata.nasa.gov' ~/.netrc)
    if [ -z "$credentials" ]; then
        cat "$netrc" >> ~/.netrc
    fi
}

fetch_urls() {
  if command -v curl >/dev/null 2>&1; then
      setup_auth_curl
      while read -r line; do
        # Get everything after the last '/'
        filename="${line##*/}"

        # Strip everything after '?'
        stripped_query_params="${filename%%\?*}"

        curl -f -b "$cookiejar" -c "$cookiejar" -L --netrc-file "$netrc" -g -o $stripped_query_params -- $line && echo || exit_with_error "Command failed with error. Please retrieve the data manually."
      done;
  elif command -v wget >/dev/null 2>&1; then
      # We can't use wget to poke provider server to get info whether or not URS was integrated without download at least one of the files.
      echo
      echo "WARNING: Can't find curl, use wget instead."
      echo "WARNING: Script may not correctly identify Earthdata Login integrations."
      echo
      setup_auth_wget
      while read -r line; do
        # Get everything after the last '/'
        filename="${line##*/}"

        # Strip everything after '?'
        stripped_query_params="${filename%%\?*}"

        wget --load-cookies "$cookiejar" --save-cookies "$cookiejar" --output-document $stripped_query_params --keep-session-cookies -- $line && echo || exit_with_error "Command failed with error. Please retrieve the data manually."
      done;
  else
      exit_with_error "Error: Could not find a command-line downloader.  Please install curl or wget"
  fi
}

fetch_urls <<'EDSCEOF'
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N09W074_dem.tif
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N09W074_num.tif
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N08W075_dem.tif
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N08W075_num.tif
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N08W073_dem.tif
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N08W073_num.tif
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N08W074_dem.tif
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N08W074_num.tif
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N09W075_dem.tif
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N09W075_num.tif
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N09W073_dem.tif
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N09W073_num.tif
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N10W075_dem.tif
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N10W075_num.tif
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N10W073_dem.tif
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N10W073_num.tif
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N10W074_dem.tif
https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N10W074_num.tif
EDSCEOF
```
> Modificando el listado de hiperenlaces contenido al final del script download.sh en la sección _fetch_urls_, podrá ingresar los cuadrantes requeridos para cualquier zona del mundo y realizar la descarga masiva de estos archivos.


### Visualización y representación 3D


#### Instrucciones en ArcGIS for Desktop (10.2.2)


#### Instrucciones en ArcGIS Pro (3.0.0)


#### Instrucciones en QGIS (3.26.0)



### Autores

* Creado por r.cfdtools@gmail.com (6 horas)


### Referencias

* Montenegro Gambini, Julio. El Modelo Digital Global ASTER GDEM, caracterización y aplicaciones en distintas áreas. Laboratorio Nacional de Hidráulica. Lima, Perú. Abril del 2012.
* https://doi.org/10.5067/ASTER/ASTGTM.003
* https://lpdaac.usgs.gov
* https://asterweb.jpl.nasa.gov/
* [ASTER Global Water Bodies Database NetCDF V001](https://search.earthdata.nasa.gov/search/granules?p=C1575734501-LPDAAC_ECS)
* [ASTER Global Digital Elevation Model Attributes NetCDF V003](https://search.earthdata.nasa.gov/search/granules?p=C1575733858-LPDAAC_ECS)
* [ASTER Global Digital Elevation Model NetCDF V003](https://search.earthdata.nasa.gov/search/granules?p=C1575731655-LPDAAC_ECS)


### Compatibilidad

* Esta actividad puede ser desarrollada con cualquier herramienta SIG que disponga de herramientas de visualización 3D.


### Control de versiones


| Versión      | Descripción                                                                                                          |
|--------------|----------------------------------------------------------------------------------------------------------------------|
| 2022.07.09   | Versión inicial con descarga manual y descarga desde consola utilizando Cygwin y el script download.sh de Earthdata. |


### Licencia, cláusulas y condiciones de uso

R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License).


| [Actividad anterior]() | [Inicio](https://github.com/rcfdtools/R.LTWB/wiki) | [Actividad siguiente]()  |
|------------------------|----------------------------------------------------|----------------------------------------------------------------------------------------|

_¡Encontraste útil este microcontenido!, apoya su difusión marcando este repositorio con una ⭐_

[^1]: Script .sh tomado de la ventana de descarga de https://search.earthdata.nasa.gov/ 
