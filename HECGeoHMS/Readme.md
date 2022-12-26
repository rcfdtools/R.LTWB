## Datasets

Esta carpeta contiene los archivos generados durante el proceso de preprocesamiento hidrológico, a través del cual se obtienen por modelo digital de terreno - DTM dentro de la carpeta _/Layers_, las grillas de:

| Prefijo / Sufijo | Descripción                                                             | ASTER GDEM | SRTM | ALOS PALSAR | 
|------------------|-------------------------------------------------------------------------|:----------:|:----:|:-----------:|
| AgreeDEM         | Reacondicionamiento de terreno a partir de la red de drenaje            |     ✓      |  ✓   |      ✓      |
| Fil              | Relleno de sumideros                                                    |     ✓      |  ✓   |      ✓      |
| Fdr              | Direcciones de flujo (formato ArcGIS, QGIS, rcfdtools en grillas ASTER) |     ✓      |  ✓   |      ✓      |
| Fac              | Acumulación de flujo                                                    |     ✓      |  ✓   |      ✓      |
| Str              | Celdas de drenajes                                                      |     ✓      |  ✓   |      ✓      |
| SinkLocations    | Celdas con sifones o empozamientos a rellenar usando Fil                |     ✓      |      |             |

> Archivos con tamaño superior a 100 MB, han sido comprimidos en partes de 95 MB para la publicación en este repositorio.

 
##

_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [:house: Inicio](https://github.com/rcfdtools/R.LTWB) |
|-------------------------------------------------------|