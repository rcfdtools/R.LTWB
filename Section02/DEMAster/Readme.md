## Descarga de modelo digital de elevación - DEM - NASA ASTER GDEM v2, v3 (30m)
Keywords: 

Los sensores remotos japoneses Advanced Spaceborne Thermal Emission and Reflection Radiometer o ASTER, proveen imágenes de alta resolución del Planeta Tierra y las capturas están compuestos por 14 diferentes bandas del espectro electromagnético en el rango visible de la luz termal infrarroja. Las imágenes son capturadas en resoluciones entre 15 y 90 metros permitiendo crear mapas detallados de la temperatura y elevación de la tierra.

A partir del segundo semestre de 2019, los modelos de terreno ASTER GDEM v2 han sido reemplazados por la versión 3 integrada de todo el mundo. Como novedad, la v3 no presenta los problemas de sobre elevaciones debida a nubes.


### Objetivos

* Descargar las imágenes del mosaico de terreno para la zona de estudio.
* Cargar y visualizar las imágenes en herramientas GIS.
* Visualizar perfiles de terreno.


### Requerimientos

* ArcGIS for Desktop 10+
* ArcGIS Pro (opcional)
* QGIS 3+ (opcional)
* Cuenta de usuario en [Eathdata](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/UserCreation) de la NASA.
* [Polígono envolvente que delimita la zona de estudio ](https://github.com/rcfdtools/R.LTWB/tree/main/Section01/CaseStudy) [(.shp)](https://github.com/rcfdtools/R.LTWB/blob/main/.shp/ZonaEstudioEnvelope.shp).


### Procedimiento de descarga

1. Ingresar al servicio web de la NASA: https://search.earthdata.nasa.gov y dar clic en Earthdata login.

> Realizar el ingreso de usuario usando _LOG IN_ o realizar el registro de nuevo usuario dando clic en _REGISTER_, [Ver instrucciones detalladas.](https://github.com/rcfdtools/R.LTWB/tree/main/Section02/UserCreation)

3. Delimitar en la vista satelital la extensión de la zona a descargar, para ello podrá utilizar diferentes métodos como:

| Método    | Descripción                                                                                                                                                                                            |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Polygon   | Acercarse a la zona requerida y mediante clics definir un polígono de delimitación.                                                                                                                    |
| Rectangle | Especificando las esquinas SW y NE en valores de latitud y longitud en grados decimales. Por ejemplo, para el Departamento del Cesar en Colombia deberá ingresar SW: 7,-75 NE: 11,-72.                 |
| Point     | Coordenada de un punto indicando la latitud y longitud en grados decimales referenciados en el sistema de proyección de coordenadas WGS84 o dando clic en pantalla.                                    |
| Circle    | Especificando un punto central y el radio de aferencia. En pantalla se puede realizar manualmente localizando el puntero cerca a la localización requerida y clic definiendo manualmente el radio.     |
| File      | Permite seleccionar un archivo que contenga el o los polígonos que delimiten la zona de estudio. Los formatos admisibles son ESRI Shapefile, Keyhole Markup Languaje (.kml or .kmz), GeoJSON y GeoRSS. |

Para 

En la casilla de búsqueda ingresar ASTER ó ASTER Global Digital Elevation Model V003.

Para nuestro ejercicio realizar la búsqueda a partir de la opción rectangle especificando las coordenadas SW: 7,-75 NE: 11,-72 pero restando internamente un 0.1 grados alrededor del rectángulo. SW: 7.1,-74.9 NE: 10.9,-72.1. Lo anterior para seleccionar únicamente las cuadriculas internas de la zona de estudio. Opcionalmente podrá realizar la descarga de cualquier zona de interés.

Verifique en el mapa de previsualización, que las celdas solicitadas corresponden al polígono de la zona de estudio y de clic en la opción de descarga de datos.

Cada archivo o cuadrante seleccionado será uno de los 22600 cuadrantes de la superficie terrestre que han sido divididos en grados de 1º x 1º que aproximadamente cubren 111.11km x 111.11km de área.

Requerimientos

Cuenta de usuario en Eathdata de la NASA.

Paquete de datos

ASTERGDEMv2.zip: Imagenes del modelo de terreno ASTER GDEM v2.

ASTERGDEMv3.zip: Imágenes preliminares del modelo de terreno ASTER GDEM v3. Se recomienda descargar los cuadrantes de la versión definitiva de este modelo, disponible actualmente en EarthData de la NASA.).
Delimitar en la vista satelital, la extensión de la zona a descargar. Para ello podrá utilizar diferentes métodos como:

Polygon: Acercarse a la zona requerida y mediante clics definir un polígono de delimitación.
Rectangle: Especificando las dos esquinas SW y NE, en valores de longitud en grados decimales. Por ejemplo, para el Departamento del Cesar en Colombia deberá ingresar SW: 7,-75 NE: 11,-72.
Point o coordenada de un punto indicando la latitud y longitud en grados decimales referenciados en el sistema de proyección de coordenadas WGS84 o dando clic en pantalla.
Grid Coordinates: Permite ingresar las coordenadas de localización de descarga en un sistema diferente al nativo WGS84.
File: Permite seleccionar un archivo que contenga los polígonos que delimiten la zona de estudio. Los formatos admisibles son ESRI Shapefile, Keyhole Markup Languaje (.kml or .kmz), GeoJSON y GeoRSS.
En la casilla de búsqueda ingresar ASTER ó ASTER Global Digital Elevation Model V003.

Para nuestro ejercicio realizar la búsqueda a partir de la opción rectangle especificando las coordenadas SW: 7,-75 NE: 11,-72 pero restando internamente un 0.1 grados alrededor del rectángulo. SW: 7.1,-74.9 NE: 10.9,-72.1. Lo anterior para seleccionar únicamente las cuadriculas internas de la zona de estudio. Opcionalmente podrá realizar la descarga de cualquier zona de interés.

Verifique en el mapa de previsualización, que las celdas solicitadas corresponden al polígono de la zona de estudio y de clic en la opción de descarga de datos.

​​​​​​​Cada archivo o cuadrante seleccionado será uno de los 22600 cuadrantes de la superficie terrestre que han sido divididos en grados de 1º x 1º que aproximadamente cubren 111.11km x 111.11km de área.


Paquete de datos

ASTERGDEMv2.zip: Imagenes del modelo de terreno ASTER GDEM v2.

ASTERGDEMv3.zip: Imágenes preliminares del modelo de terreno ASTER GDEM v3. Se recomienda descargar los cuadrantes de la versión definitiva de este modelo, disponible actualmente en EarthData de la NASA.


### Visualización y representación 3D

#### Instrucciones en ArcGIS for Desktop (10.2.2)


#### Instrucciones en ArcGIS Pro (3.0.0)


#### Instrucciones en QGIS (3.26.0)



### Autores

* Creado por r.cfdtools@gmail.com (xxx horas)


### Compatibilidad

* Esta actividad puede ser desarrollada con cualquier herramienta SIG que disponga de herramientas de visualización 3D.



### Control de versiones


| Versión      | Descripción      |
|--------------|------------------|
| 2022.07.09   | Versión inicial. |


### Licencia, cláusulas y condiciones de uso

R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License).


| [Actividad anterior]() | [Inicio](https://github.com/rcfdtools/R.LTWB/wiki) | [Actividad siguiente]()  |
|------------------------|----------------------------------------------------|----------------------------------------------------------------------------------------|

_¡Encontraste útil este microcontenido!, apoya su difusión marcando este repositorio con una ⭐_

[^1]: 
