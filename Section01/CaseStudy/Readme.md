## Caso de estudio  
Keywords: `Case study` `Colombia` `Cesar` `IDEAM` `Weather` `Zona hidrogeográfica` `Station`

Definición de la zona de estudio para la aplicación de la metodología y el desarrollo de las diferentes secciones y actividades.

![CaseStudy.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Graph/CaseStudy.png)

> En la ilustración COD_ZH corresponde al código de la Zona Hidrográfica.

### Alcance

Para la realización del Balance Hidrológico de Largo Plazo o LTWB (Long-term water balance), se ha definido como caso de estudio la Zonificación Hidrográfica de Colombia y la Red de Estaciones terrestres Hidroclomatológicas del Instituto de Hidrología, Meteorología y Estudios Ambientales - IDEAM de Colombia. A nivel particular se estudiará a detalle la zona hidrográfica 28 denominada Cesar que hace parte del área hidrográfica principal 2, correspondiente a Magdalena - Cauca que se compone de las siguientes subzonas:

| SZH  | Subzona Hidrográfica |
|------|----------------------|
| 2801 | Alto Cesar           |
| 2802 | Medio Cesar          |
| 2804 | Río Ariguaní         |
| 2805 | Bajo Cesar           |

> Estudiantes que aplicaron para curso con certificación desarrollan casos de estudio individuales asignados para zonas hidrográficas específicas.  


#### Red de estaciones

El [Instituto de Hidrología, Meteorología y Estudios Ambientales - IDEAM](http://www.ideam.gov.co/) de Colombia, adscrito al [Ministerio de Medio Ambiente - Minambiente](https://www.minambiente.gov.co/), es la entidad nacional encargada registrar y mantener la información hidrometeorológica del país, incluida la localización y clasificación de la red de estaciones que hace parte del [Catálogo Nacional de Estaciones - CNE](http://bart.ideam.gov.co/cneideam/CNE_IDEAM.xls). A través del servicio de [Solicitud de Información](http://www.ideam.gov.co/solicitud-de-informacion) o a través del portal [DHIME](http://dhime.ideam.gov.co/atencionciudadano/) del IDEAM desde la pestaña _Recursos_, personas naturales o jurídicas, pueden obtener no solamente los catálogos, sino también las capas geográficas y los registros discretos registrados en cada estación. 

> Debido a que es necesario incluir diferentes estaciones alcrededor de la zona hidrográgica de estudio para garantizar la extensión espacial de los mapas interpolados para cada variable climatológica requerida, en esta actividad no se especifica el listado de las estaciones a utilizar y en la sección 3 de este curso se presenta el proceso detallado de selección espacial de estas estaciones.

![CNE_IDEAM.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Graph/CNE_IDEAM.png)

> En la ilustración CNE_IDEAM corresponde a las estaciones del Catálogo Nacional de Estaciones del IDEAM y CNE_IDEAM_ZE corresponde al grupo de estaciones prototipo en la zona de estudio.

#### Zonificación hidrográfica de Colombia

La zonificación hidrográfica de Colombia desde el punto de vista hidrológico, tiene sus inicios en el HIMAT mediante la Resolución 0337 del 1978, la cual establece que el país está conformado por cinco Áreas hidrográficas (1-Caribe, 2- Magdalena - Cauca, 3- Orinoco, 4- Amazonas y 5-Pacífico) que a su vez están divididas en Zonas Hidrográficas y subdivididas en Subzonas Hidrográficas. En ese entonces, el propósito de la zonificación fue de adoptar un sistema de codificación para estaciones Hidrometerológicas. Posteriormente, el IDEAM introduce esta zonificación para otros fines, tales como estudios y análisis hidrológicos relacionados con los informes ambientales, p.ej, el Índice de Aridez, el Escurrimiento y el Rendimiento Hídrico.[^1]

La zonificación de cuencas hidrográficas corresponde a tres niveles de jerarquía: áreas, zonas y subzonas hidrográficas. Las áreas hidrográficas corresponden a las regiones hidrográficas o vertientes que, en sentido estricto, son las grandes cuencas que agrupan un conjunto de ríos con sus afluentes que desembocan en un mismo mar. Ahora bien, en Colombia se distinguen cuatro vertientes, dos de ellas asociadas a ríos de importancia continental (vertiente del Orinoco y vertiente del Amazonas) y las vertientes del Atlántico y del Pacífico. Se delimita adicionalmente como áea hidrográfica la cuenca Magdalena-Cauca, que aunque tributa y forma parte de la vertiente del Atlántico, tiene importancia socioeconómica por su alto poblamiento y aporte al producto interno bruto.[^2]

| AH  | Área Hidrográfica |
|-----|-------------------|
| 1   | Caribe            |
| 2   | Magdalena-Cauca   |
| 3   | Orinoco           |
| 4   | Amazonas          |
| 5   | Pacífico          |

![ZonaHidrografica2013.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Graph/ZonaHidrografica2013.png)

Las cuencas hidrográficas que entregan o desembocan sus aguas superficiales directamente de una área hidrográfica se denominaran zonas hidrográficas. Agrupan varias cuencas que se presentan como un subsistema hídrico con características de relieve y drenaje homogéneo y sus aguas tributan a través de un afluente principal hacia un área hidrográfica. Están integradas por cuencas de las partes altas, medias o bajas de una zona hidrográfica que captan agua y sedimentos de los tributarios de diferente orden tales como nacimientos de agua, arroyos, quebradas y ríos. Las cuencas que tributan sus aguas a su vez a las zonas hidrográficas se denomina subzonas hidrográficas. Ahora bien, respecto a la toponimia con que se identifican zonas y subzonas hidrográficas, a estas unidades se les asignó la toponimia de acuerdo con el nombre de la corriente más representativa o río principal o con el nombre heredado de la zonificación del HIMAT, que puede corresponder al espacio geográfico o región a la cual drenan las aguas superficiales.[^2]

| AH  | Área Hidrográfica | ZH  | Zona Hidrográfica                  |
|-----|-------------------|-----|------------------------------------|
| 1   | Caribe            | 11  | Atrato - Darién                    |
| 1   | Caribe            | 12  | Caribe - Litoral                   |
| 1   | Caribe            | 13  | Sinú                               |
| 1   | Caribe            | 15  | Caribe - La Guajira                |
| 1   | Caribe            | 16  | Catatumbo                          |
| 1   | Caribe            | 17  | Islas del Caribe                   |
| 2   | Magdalena - Cauca | 21  | Alto Magdalena                     |
| 2   | Magdalena - Cauca | 22  | Saldaña                            |
| 2   | Magdalena - Cauca | 23  | Medio Magdalena                    |
| 2   | Magdalena - Cauca | 24  | Sogamoso                           |
| 2   | Magdalena - Cauca | 25  | Bajo Magdalena - Cauca - San Jorge |
| 2   | Magdalena - Cauca | 26  | Cauca                              |
| 2   | Magdalena - Cauca | 27  | Nechí                              |
| 2   | Magdalena - Cauca | 28  | Cesar                              |
| 2   | Magdalena - Cauca | 29  | Bajo Magdalena                     |
| 3   | Orinoco           | 31  | Inírida                            |
| 3   | Orinoco           | 32  | Guaviare                           |
| 3   | Orinoco           | 33  | Vichada                            |
| 3   | Orinoco           | 34  | Tomo                               |
| 3   | Orinoco           | 35  | Meta                               |
| 3   | Orinoco           | 36  | Casanare                           |
| 3   | Orinoco           | 37  | Arauca                             |
| 3   | Orinoco           | 38  | Orinoco Directos                   |
| 3   | Orinoco           | 39  | Apure                              |
| 4   | Amazonas          | 41  | Guainía                            |
| 4   | Amazonas          | 42  | Vaupés                             |
| 4   | Amazonas          | 43  | Apaporis                           |
| 4   | Amazonas          | 44  | Caquetá                            |
| 4   | Amazonas          | 45  | Yarí                               |
| 4   | Amazonas          | 46  | Caguán                             |
| 4   | Amazonas          | 47  | Putumayo                           |
| 4   | Amazonas          | 48  | Amazonas - Directos                |
| 4   | Amazonas          | 49  | Napo                               |
| 5   | Pacífico          | 51  | Mira                               |
| 5   | Pacífico          | 52  | Patía                              |
| 5   | Pacífico          | 53  | Tapaje - Dagua - Directos          |
| 5   | Pacífico          | 54  | San Juan                           |
| 5   | Pacífico          | 55  | Baudó - Directos Pacífico          |
| 5   | Pacífico          | 56  | Pacífico - Directos                |
| 5   | Pacífico          | 57  | Islas del Pacífico                 |

> En el presente análisis no se han incluido resultados para la ZH - zona hidrográfica 57, correspondiente a las Islas del Pacífico, debido a que la capa geográfica SZH - subzonas hidrográficas no contiene el polígono de delimitación. 

### Delimitación de la zona de estudio con ArcGIS

El proceso de delimitación se realiza a partir de la cobertura de Subzonas hidrográficas de Colombia, este mapa representa las unidades de análisis para el ordenamiento ambiental de territorio definidas por el IDEAM en convenio con el Instituto Geográfico Agustín Codazzi (IGAC), a escala 1:500.000. [^3]

Procedimiento:

1. Ingrese al portal http://www.ideam.gov.co/en/capas-geo y en el cuadro de búsqueda escriba _Zonificación Hidrográfica_, observará que a 2022.07.07 existen dos versiones de la capa de zonificación correspondientes al año 2010 y 2013. Realice la descarga del archivo de formas Shapefile del año 2013, consulte sus metadatos y el catálogo de objetos disponible.

> La descarga permite obtener el archivo comprimido `Zonificacion_Hidrografica_2013.zip` que contiene la capa geográfica en formato Shapefile, un mapa de muestra en formato .pdf, la ficha de representación gráfica y otros elementos complementarios. 

![IDEAMZonificacionHidrograficaDescarga.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/IDEAMZonificacionHidrograficaDescarga.png)

Catálogo de objetos en Subzonas [^4]
| Nombre       | Alias          | Definición                                                                   | Tipo de dato |
|--------------|----------------|------------------------------------------------------------------------------|--------------|
| OBJECTID     | OBJECTID       | Identificador de objeto geográfico.                                          | Texto        |
| Shape        | Shape          | Tipo de geometría.                                                           | Geometría    |
| COD_AH       | Código Area    | Código del Area hidrográfica a la que corresponde.                           | Entero       |
| COD_ZH       | Código Zona    | Código de la Zona hidrográfica a la que corresponde.                         | Entero       |
| COD_SZH      | Código Subzona | Código de Subzona hidrográfica a la que corresponde.                         | Entero       |
| NOM_AH       | Nombre Área    | Nombre del área hidrográfica a la que corresponde. Dominio Área Hidográfica. | Texto        |
| NOM_ZH       | Nombre Zona    | Nombre de la zona hidrográfica a la que corresponde.                         | Texto        |
| NOM_SZH      | Nombre Subzona | Nombre de la Subzona hidrográfica a la que corresponde.                      | Texto        |
| Shape_Length | Shape_Length   | Perímetro en las unidades del sistema de referencia espacial.                | Entero       |
| Shape_Area   | Shape_Area     | Área en las unidades del sistema de referencia espacial.                     | Entero       |
| RULEID       | RULEID         | Id único asignado por el sistema a la representación gráfica.                | Entero       |
| Override     | Override       | Representación gráfica.                                                      | Blob         |

2. Descomprima solo los datos contenidos en la carpeta `/shape` dentro de la carpeta `D:\R.LTWB\.shp`

3. En ArcGIS, cree un mapa nuevo en blanco y agregue el mapa de Subzonas Hidrográficas. Simbolice por categorías de valores únicos a partir del campo `NOM_ZH` correspondiente a la Zona Hidrográfica y rotule las zonas a partir del campo de atributos `COD_SZH` correspondiente a los códigos de las subzonas. Guarde el mapa como CaseStudy.mxd en la carpeta `D:\R.LTWB\.Map`

![ArcGISDesktop10.2.2ZonaHidrografica2013.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/ArcGISDesktop10.2.2ZonaHidrografica2013.png)

4. A partir de las Subzonas Hidrográficas, filtre los polígonos de correspondientes al caso de estudio, p.ej. los de la Subzona 28 correspondiente a Cesar.

![ArcGISDesktop10.2.2ZonaHidrografica2013Query.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/ArcGISDesktop10.2.2ZonaHidrografica2013Query.png)

5. Utilizando la herramienta `Dissolve` disponible en el menú `Geoprocessing`, disuelva los polígonos de la zona de estudio para obtener un único polígono perimetral. Nombrar como `ZonaEstudio.shp`. Simbolice solo por contorno utilizando borde externo negro en grosor 3.

![ArcGISDesktop10.2.2ZonaHidrografica2013Dissolve.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/ArcGISDesktop10.2.2ZonaHidrografica2013Dissolve.png)

6. En la Tabla de Contenido, asigne en las propiedades de Layers o Capas el sistema de proyección de coordenadas MAGNA_Colombia_CTM12 correspondiente al identificador EPSG 9377 ó ESRI 103599.

> La versión de ArcGIS for Desktop no incluye el sistema de proyección del origen único nacional CTM12 o 9377 por lo que la asignación debe ser realizada a través de un archivo de proyección de coordenadas .prj. La definición de un sistema proyectado permitirá realizar el cálculo de áreas y perímetros en unidades del sistema internacional. En la carpeta `\.ProjectionFile` de este repositorio se encuentran diferentes archivos de proyección inluído `MAGNA_OrigenNacional.prj` correspondiente al CRS requerido.

![ArcGISDesktop10.2.2CRS9377.png](https://github.com/rcfdtools/R.LTWB/blob/main/Section01/CaseStudy/Screenshot/ArcGISDesktop10.2.2CRS9377.png)

7. En la tabla de atributos de la capa geográfica `ZonaEstudio.shp`, cree dos campos de atributos numéricos dobles y nómbrelos como Akm2 y Pkm correspondientes al área en km² y perímetro en km y cree un campo de texto con longitud de 55 caracteres nombrándolo como ZH. Utilizando el calculador de geometría obtenga el área y el perímetro y asigne manualmente el código y nombre de la subzona en el campo ZH. Rotule indicando la zona, área y perímetro utilizando la siguiente expresión:





### Autores

* Creado por r.cfdtools@gmail.com (2.5 horas)


### Compatibilidad

* Las herramientas computacionales requeridas, librerías, complementos y sus versiones son especificadas en cada actividad del curso.


### Control de versiones


| Versión      | Descripción                                                                       |
|--------------|-----------------------------------------------------------------------------------|
| v.2022.07.06 | Versión inicial con definición general del caso de estudio y mapas de referencia. |


### Licencia, cláusulas y condiciones de uso

R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License).


| [Actividad anterior]() | [Inicio](https://github.com/rcfdtools/R.LTWB/wiki) | [Actividad siguiente]()  |
|------------------------|----------------------------------------------------|----------------------------------------------------------------------------------------|

_¡Encontraste útil este microcontenido!, apoya su difusión marcando este repositorio con una ⭐_

[^1]: http://www.ideam.gov.co/web/agua/zonificacion-hidrografica
[^2]: http://documentacion.ideam.gov.co/openbiblio/bvirtual/022655/MEMORIASMAPAZONIFICACIONHIDROGRAFICA.pdf
[^3]: http://geoservicios.ideam.gov.co/geonetwork/srv/eng/catalog.search#/metadata/7696695f-ae9c-4780-a6d0-d3cd1808819a
[^4]: http://geoservicios.ideam.gov.co/CatalogoObjetos/queryByUUID?uuid=bcd645c9-0f11-4770-926e-1e1fdfbf5ce6