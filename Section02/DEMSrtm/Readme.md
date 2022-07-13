## Descarga y procesamiento de modelo digital de elevación - DEM - SRTM v3.0 1 arcsec (30m), SRTM v3.0 3 arcsec (90m)
Keywords: `NASA` `SRTM` `Cygwin` `Shell script .sh` `Earthdata` `Mosaic to New Raster`

![DEMAster.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/DEMSrtm/Screenshot/DEMSrtm.png)

Shuttle Radar Topography Mission (SRTM), dispone de mapas topográficos de alta resolución para uso público desde el año 2015 y pueden ser utilizados para la creación de los mapas de dirección y acumulación de flujo.

A partir del segundo semestre de 2019, el modelo de terreno SRTM v3, ya se encuentra disponible para descarga por el servidor EarthData de la NASA, buscar como "NASA Shuttle Radar Topography Mission Global 1 arc second V003".

### Objetivos

* Descargar manualmente imágenes de terreno para la zona de estudio.
* Descargar masivamente imágenes desde la consola Cygwin a través del script download.sh.
* Cargar y visualizar imágenes satelitales en herramientas SIG.
* Crear y reproyectar el mosaico de terreno a partir de las imágenes individuales obtenidas.

> La resolución aproximada de los modelos digitales de elevación SRTM versión 3 es de 30 y 90 metros.

> Para aprender a visualizar perfiles de elevación, crear representaciones 3D y mapas de sombreado de colinas - Hillshade utilizando ArcGIS for Desktop, ArcGIS Pro y QGIS, consulte la actividad [Descarga y procesamiento del modelo digital de elevación - DEM - NASA ASTER GDEM v3 (30m)](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/DEMAster).


### Requerimientos

* ArcGIS Pro 2+
* [Cygwin terminal for Windows](https://www.cygwin.com/)
* Cuenta de usuario [NASA Eathdata](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/UserCreation).
* [Polígono envolvente que delimita la zona de estudio. ](https://github.com/rcfdtools/R.LTWB/tree/main/Section01/CaseStudy) [(.shp)](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudioEnvelope.shp).


### Procedimiento de descarga

1. Ingresar al servicio web de la NASA: https://search.earthdata.nasa.gov y dar clic en Earthdata login.

> Realizar el ingreso de usuario usando _LOG IN_ o realizar el registro de nuevo usuario dando clic en _REGISTER_. [(Ver instrucciones detalladas.)](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/UserCreation)

2. Delimitar en la vista satelital la extensión de la zona a descargar, para ello podrá utilizar diferentes métodos como:

| Método    | Descripción                                                                                                                                                                                                            |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Polygon   | Acercarse a la zona requerida y mediante clics definir un polígono de delimitación.                                                                                                                                    |
| Rectangle | Cree un rectángulo especificando las esquinas SW y NE en valores de latitud y longitud en grados decimales, p. ej. para el Departamento del Cesar en Colombia deberá ingresar SW: 7,-75 NE: 11,-72.                    |
| Point     | Coordenada de un punto indicando la latitud y longitud en grados decimales referenciados en el sistema de proyección de coordenadas WGS84 o dando clic en pantalla.                                                    |
| Circle    | Circunferencia especificando un punto central y el radio de aferencia. En pantalla se puede realizar manualmente localizando el puntero cerca a la localización requerida y clic definiendo manualmente el radio.      |
| File      | Permite seleccionar un archivo comprimido .zip que contenga el o los polígonos que delimiten la zona de estudio. Los formatos admisibles son ESRI Shapefile, Keyhole Markup Languaje (.kml or .kmz), GeoJSON y GeoRSS. |

Para el caso de estudio, utilizaremos el método _File_ para definir la máscara de selección de elementos a descargar.

Desde la carpeta _.shp_ contenida en _D:\R.LTWB_, seleccione y comprima en formato .zip los archivos _ZonaEstudioEnvelope.dbf, ZonaEstudioEnvelope.prj, ZonaEstudioEnvelope.shp_ y _ZonaEstudioEnvelope.shx_ que conforman el Shapefile del polígono envolvente de la zona de estudio. Este archivo de formas tiene embebido el sistema de coordenadas geográfico GCS_MAGNA que puede ser interpretado directamente por Earthdata.

> Para archivos de formas que utilicen un sistema de coordenadas proyectado, será necesario crear un mapa nuevo en blanco en ArcGIS o QGIS, asignar el sistema de proyección de coordenadas geográfico WGS84 correspondiente al EPSG 4326, cargar y exportar la capa ZonaEstudioEnvelope.shp utilizando el sistema de coordenadas del proyecto, nombrando el archivo exportado como ZonaEstudioEnvelopeWGS84.shp

![EarthdataSearchByShapefile.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/DEMSrtm/Screenshot/EarthdataSearchByShapefile.png)

> Para búsquedas a partir de la opción rectangle especificando las coordenadas, p. ej. SW: 7,-75 NE: 11,-72 se resta internamente 0.1 grados alrededor del rectángulo SW: 7.1,-74.9 NE: 10.9,-72.1. Lo anterior para seleccionar únicamente las cuadrículas internas.

3. En la casilla de búsqueda ingresar _NASA Shuttle Radar Topography Mission Global 1 arc second V003_ para descargas en resolución de 30 metros o _NASA Shuttle Radar Topography Mission Global 3 arc second V003_ para descargas en resolución de 90 metros. Para la zona de estudio, es necesario descargar 9 cuadrículas.

Como puede observar, las cuadrículas son ortogonales y no contienen traslapos debido a que corresponde a un modelo ya procesado y recortado. Para la zona de estudio, la información del modelo digital de elevación ha sido obtenida, procesada e integrada desde 2000.02.11 hasta 2000.02.21.

![EarthdataSearchResults.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/DEMSrtm/Screenshot/EarthdataSearchResults.png)

Cada archivo o cuadrante seleccionado será uno de los 22600 cuadrantes de la superficie terrestre que han sido divididos en grados de 1º x 1º que aproximadamente cubren 111.11km x 111.11km de superficie.

4. Verifique en el mapa de previsualización que las celdas solicitadas corresponden al polígono de la zona de estudio y de clic en la opción de descarga de datos _Download All_. Seleccione _Direct Download_ para obtener los 9 archivos requeridos que tienen un peso aproximado de 100.9 MB y de clic en _Done_ y _Download Data_.

![EarthdataSearchDirectDownload.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/DEMSrtm/Screenshot/EarthdataSearchDirectDownload.png)

En la ventana de descarga de clic derecho y seleccione la opción _Open link in new tab_ en los archivos .zip correspondientes a los archivos [.hgt](https://gdal.org/drivers/raster/srtmhgt.html) del modelo digital de elevación. 

![EarthdataSearchDirectDownloadLink.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/DEMSrtm/Screenshot/EarthdataSearchDirectDownloadLink.png)

Listado de enlaces obtenidos  
* https://e4ftl01.cr.usgs.gov//DP133/SRTM/SRTMGL1.003/2000.02.11/N09W075.SRTMGL1.hgt.zip
* https://e4ftl01.cr.usgs.gov//DP133/SRTM/SRTMGL1.003/2000.02.11/N09W074.SRTMGL1.hgt.zip
* https://e4ftl01.cr.usgs.gov//DP133/SRTM/SRTMGL1.003/2000.02.11/N08W075.SRTMGL1.hgt.zip
* https://e4ftl01.cr.usgs.gov//DP133/SRTM/SRTMGL1.003/2000.02.11/N08W074.SRTMGL1.hgt.zip
* https://e4ftl01.cr.usgs.gov//DP133/SRTM/SRTMGL1.003/2000.02.11/N10W074.SRTMGL1.hgt.zip
* https://e4ftl01.cr.usgs.gov//DP133/SRTM/SRTMGL1.003/2000.02.11/N10W073.SRTMGL1.hgt.zip
* https://e4ftl01.cr.usgs.gov//DP133/SRTM/SRTMGL1.003/2000.02.11/N09W073.SRTMGL1.hgt.zip
* https://e4ftl01.cr.usgs.gov//DP133/SRTM/SRTMGL1.003/2000.02.11/N08W073.SRTMGL1.hgt.zip
* https://e4ftl01.cr.usgs.gov//DP133/SRTM/SRTMGL1.003/2000.02.11/N10W075.SRTMGL1.hgt.zip

Descomprima los archivos .zip descargados en la carpeta _.dem/SRTM_ del directorio _D:\R.LTWB_

> Tenga en cuenta que las imágenes obtenidas utilizan el sistema de referencia espacial geográfico GCS_WGS_1984 y que las elevaciones de cada celda o pixel corresponden a valores enteros en metros.

5. Descarga mediante shell script .sh con Cygwin [^1]

> Earthdata directions for Linux: You must first make the script an executable by running the line 'chmod 777 download.sh' from the command line. After that is complete, the file can be executed by typing './download.sh'. For a detailed walk through of this process, please reference this How To guide.

> Earthdata directions for Windows: The file can be executed within Windows by first installing a Unix-like command line utility such as Cygwin. After installing Cygwin (or a similar utility), run the line 'chmod 777 download.sh' from the utility's command line, and then execute by typing './download.sh'.

Desde https://www.cygwin.com/, descargue e instale _Cygwin_ para Windows en la ruta _C:\cygwin64_ y ejecute la aplicación _Cygwin64 Terminal_ e ingrese los siguientes comandos:

* `chmod 777 'D:/R.LTWB/.src/downloadSRTM.sh'` para establecer los permisos de lectura, escritura y ejecución por cualquier usuario con acceso a la consola y al archivo.
* `cd 'D:/R.LTWB/.dem/SRTM'` para ingresar al directorio ASTER de modelos digitales de elevación.
* `ls` para listar el contenido del directorio. Podrá observar que no existen archivos GeoTiFF correspondientes al modelo de terreno ni archivos de cookies.
* `'D:/R.LTWB/.src/downloadSRTM.sh'` para ejecutar _downloadSRTM.sh_ y obtener los archivos del modelo de terreno y almacenarlos en el directorio _.dem_

En la consola deberá ingresar su nombre de usuario y contraseña Earthdata para iniciar la descarga.

Al finalizar la ejecución ejecute nuevamente el comando `ls` para listar los archivos descargados o verifique manualmente el directorio de descarga _.dem/SRTM_

Shell script [downloadSRTM.sh](https://github.com/rcfdtools/R.LTWB/blob/main/.src/downloadSRTM.sh) de Earthdata
```
#!/bin/bash

GREP_OPTIONS=''

cookiejar=$(mktemp cookies.XXXXXXXXXX)
netrc=$(mktemp netrc.XXXXXXXXXX)
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
    echo "https://e4ftl01.cr.usgs.gov//DP133/SRTM/SRTMGL1.003/2000.02.11/N09W075.SRTMGL1.hgt.zip"
    echo
    exit 1
}

prompt_credentials
  detect_app_approval() {
    approved=`curl -s -b "$cookiejar" -c "$cookiejar" -L --max-redirs 5 --netrc-file "$netrc" https://e4ftl01.cr.usgs.gov//DP133/SRTM/SRTMGL1.003/2000.02.11/N09W075.SRTMGL1.hgt.zip -w %{http_code} | tail  -1`
    if [ "$approved" -ne "302" ]; then
        # User didn't approve the app. Direct users to approve the app in URS
        exit_with_error "Please ensure that you have authorized the remote application by visiting the link below "
    fi
}

setup_auth_curl() {
    # Firstly, check if it require URS authentication
    status=$(curl -s -z "$(date)" -w %{http_code} https://e4ftl01.cr.usgs.gov//DP133/SRTM/SRTMGL1.003/2000.02.11/N09W075.SRTMGL1.hgt.zip | tail -1)
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
https://e4ftl01.cr.usgs.gov//DP133/SRTM/SRTMGL1.003/2000.02.11/N09W075.SRTMGL1.hgt.zip
https://e4ftl01.cr.usgs.gov//DP133/SRTM/SRTMGL1.003/2000.02.11/N09W074.SRTMGL1.hgt.zip
https://e4ftl01.cr.usgs.gov//DP133/SRTM/SRTMGL1.003/2000.02.11/N08W075.SRTMGL1.hgt.zip
https://e4ftl01.cr.usgs.gov//DP133/SRTM/SRTMGL1.003/2000.02.11/N08W074.SRTMGL1.hgt.zip
https://e4ftl01.cr.usgs.gov//DP133/SRTM/SRTMGL1.003/2000.02.11/N10W074.SRTMGL1.hgt.zip
https://e4ftl01.cr.usgs.gov//DP133/SRTM/SRTMGL1.003/2000.02.11/N10W073.SRTMGL1.hgt.zip
https://e4ftl01.cr.usgs.gov//DP133/SRTM/SRTMGL1.003/2000.02.11/N09W073.SRTMGL1.hgt.zip
https://e4ftl01.cr.usgs.gov//DP133/SRTM/SRTMGL1.003/2000.02.11/N08W073.SRTMGL1.hgt.zip
https://e4ftl01.cr.usgs.gov//DP133/SRTM/SRTMGL1.003/2000.02.11/N10W075.SRTMGL1.hgt.zip
EDSCEOF
```
> Modificando el listado de hiperenlaces contenido al final del script download.sh en la sección _fetch_urls_, podrá ingresar los cuadrantes requeridos para cualquier zona del mundo y realizar la descarga masiva de estos archivos.


### Creación y reproyección de mosaico

Luego de los procesos de obtención de las imágenes satelitales, es necesaria la construcción de un mosaico único a partir de las imágenes individuales obtenidas para cada modelo de terreno. El balance hidrológico de largo plazo podrá ser realizado utilizando diferentes modelos de terreno y permitirá comparar la oferta hídrica obtenida utilizando diferentes superficies.

> Para conocer como realizar este procedimiento en ArcGIS for Desktop y QGIS, consulte la actividad [Descarga y procesamiento del modelo digital de elevación - DEM - NASA ASTER GDEM v3 (30m)](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/DEMAster)

#### Instrucciones en ArcGIS Pro (3.0.0)

1. Abra el mapa ArcGISPro.aprx localizado en la carpeta _.map\ArcGISPro_, agregue las 9 imágenes del modelo de elevación SRTM v3 y agrupe como _DEM SRTM v3_. Verifique que el sistema de proyección de coordenadas del mapa esté establecido con MAGNA_Colombia_CTM12 correspondiente al identificador ESRI 103599.

![ArcGISPro3.0.0LoadCoordinates.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/DEMSrtm/Screenshot/ArcGISPro3.0.0LoadCoordinates.png)

2. Utilizando la herramienta _Mosaic to New Raster_, cree el mosaico a partir de las 9 imágenes independientes. Nombre como _SRTMV003MosaicArcGISPro.tif_.

![ArcGISPro3.0.0MosaicToNewRaster.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/DEMSrtm/Screenshot/ArcGISPro3.0.0MosaicToNewRaster.png)

3. Simbolice el mosaico en modo de relieve sombreado o _Shaded Relief_ con _Z Scale Factor en 2_.

![ArcGISPro3.0.0ShadedRelief.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section02/DEMSrtm/Screenshot/ArcGISPro3.0.0ShadedRelief.png)

En este momento ya dispone de una grilla integrada de elevación SRTM que cubre toda la zona de estudio.


### Autores

* Creado por r.cfdtools@gmail.com


### Referencias

* https://gdal.org/drivers/raster/srtmhgt.html
* https://doi.org/10.5067/MEaSUREs/SRTM/SRTMGL1.003
* https://lpdaac.usgs.gov
* https://www2.jpl.nasa.gov/srtm/index.html
* [NASA Shuttle Radar Topography Mission Global 3 arc second number V003](https://search.earthdata.nasa.gov/search/granules?p=C204582037-LPDAAC_ECS)
* [NASA Shuttle Radar Topography Mission Global 3 arc second V003](https://search.earthdata.nasa.gov/search/granules?p=C204582034-LPDAAC_ECS)
* [NASA Shuttle Radar Topography Mission Global 1 arc second number V003](NASA Shuttle Radar Topography Mission Global 1 arc second number V003)


### Compatibilidad

* Esta actividad puede ser desarrollada con cualquier herramienta SIG que disponga de herramientas para la creación de mosaicos o unión de imagenes.
* Para la descarga puede utilizar cualquier navegador de Internet actualizado.
* Descargas mediante script pueden ser realizadas en Linux, subsistemas de Linux para Windows o desde terminales emuladoras como Cygwin.


### Control de versiones

| Versión     | Descripción                                         | Dedicación, hr |
|-------------|-----------------------------------------------------|----------------|
| 2022.07.13  | Creación de mosaico - Instrucciones en ArcGIS Pro.  | 2h            |
| 2022.07.12  | Versión inicial con descarga manual y con script.   | 1h             |


### Licencia, cláusulas y condiciones de uso

R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License).


| [Actividad anterior]() | [Inicio](https://github.com/rcfdtools/R.LTWB/wiki) | [Actividad siguiente]()  |
|------------------------|----------------------------------------------------|----------------------------------------------------------------------------------------|

_¡Encontraste útil este microcontenido!, apoya su difusión marcando este repositorio con una ⭐_
 
[^1]: Script .sh tomado de la ventana de descarga de https://search.earthdata.nasa.gov/ 
