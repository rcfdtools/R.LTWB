## Exploración y análisis de series - EDA - Representación gráfica

* Archivo de resultados: D:/R.LTWB/.datasets/IDEAM_EDA/EDA.md
* Fecha y hora de inicio de ejecución: 2022-10-27 11:03:58.506974
* Python versión: 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)]
* Python rutas: ['D:\\R.LTWB\\.src', 'D:\\R.LTWB', 'D:\\R.HydroTools.wiki', 'D:\\R.HydroTools', 'D:\\R.GISPython']
* matplotlib versión: 3.6.0
* Encuentra este script en https://github.com/rcfdtools/R.LTWB/tree/main/Section03/EDA
* Cláusulas y condiciones de uso en https://github.com/rcfdtools/R.LTWB/blob/main/LICENSE.md
* Créditos: r.cfdtools@gmail.com


### General dataframe information with 514927 IDEAM records

Station records sample for head

|    |   CodigoEstacion | NombreEstacion                                  |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   | Fecha               |   Valor |   Grado |   Calificador |   NivelAprobacion |
|---:|-----------------:|:------------------------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|:--------------------|--------:|--------:|--------------:|------------------:|
|  0 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 1987-12-01 00:00:00 |   202   |      50 |           nan |               900 |
|  1 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 1988-01-01 00:00:00 |     0   |      50 |           nan |               900 |
|  2 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 1988-02-01 00:00:00 |    18.9 |      50 |           nan |               900 |
|  3 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 1988-03-01 00:00:00 |    36.7 |      50 |           nan |               900 |
|  4 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 1988-04-01 00:00:00 |   189.4 |      50 |           nan |               900 |
|  5 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 1988-07-01 00:00:00 |   241.9 |      50 |           nan |               900 |
|  6 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 1988-08-01 00:00:00 |   319.7 |      50 |           nan |               900 |
|  7 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 1988-09-01 00:00:00 |   220.8 |      50 |           nan |               900 |
|  8 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 1988-10-01 00:00:00 |   264   |      50 |           nan |               900 |
|  9 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 1988-11-01 00:00:00 |   295.7 |      50 |           nan |               900 |
| 10 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 1988-12-01 00:00:00 |    85.7 |      50 |           nan |               900 |
| 11 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 1989-02-01 00:00:00 |    47.6 |      50 |           nan |               900 |

Station records sample for tail

|        |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio    | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   | Fecha               |   Valor |   Grado |   Calificador |   NivelAprobacion |
|-------:|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|:--------------------|--------:|--------:|--------------:|------------------:|
| 514915 |         25021090 | SANTA ROSA [25021090] |   9.09333 |   -74.3139 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Fernando | 1974-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 2020-03-01 00:00:00 |       0 |      50 |           nan |               900 |
| 514916 |         25021090 | SANTA ROSA [25021090] |   9.09333 |   -74.3139 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Fernando | 1974-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 2020-04-01 00:00:00 |     105 |      50 |           nan |               900 |
| 514917 |         25021090 | SANTA ROSA [25021090] |   9.09333 |   -74.3139 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Fernando | 1974-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 2020-05-01 00:00:00 |     110 |      50 |           nan |               900 |
| 514918 |         25021090 | SANTA ROSA [25021090] |   9.09333 |   -74.3139 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Fernando | 1974-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 2020-06-01 00:00:00 |     205 |      50 |           nan |               900 |
| 514919 |         25021090 | SANTA ROSA [25021090] |   9.09333 |   -74.3139 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Fernando | 1974-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 2020-07-01 00:00:00 |     329 |      50 |           nan |               900 |
| 514920 |         25021090 | SANTA ROSA [25021090] |   9.09333 |   -74.3139 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Fernando | 1974-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 2020-08-01 00:00:00 |     320 |      50 |           nan |               900 |
| 514921 |         25021090 | SANTA ROSA [25021090] |   9.09333 |   -74.3139 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Fernando | 1974-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 2020-09-01 00:00:00 |     518 |      50 |           nan |               900 |
| 514922 |         25021090 | SANTA ROSA [25021090] |   9.09333 |   -74.3139 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Fernando | 1974-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 2020-10-01 00:00:00 |     105 |      50 |           nan |               900 |
| 514923 |         25021090 | SANTA ROSA [25021090] |   9.09333 |   -74.3139 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Fernando | 1974-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 2020-11-01 00:00:00 |     243 |      50 |           nan |               900 |
| 514924 |         25021090 | SANTA ROSA [25021090] |   9.09333 |   -74.3139 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Fernando | 1974-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 2020-12-01 00:00:00 |      90 |      50 |           nan |               900 |
| 514925 |         25021090 | SANTA ROSA [25021090] |   9.09333 |   -74.3139 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Fernando | 1974-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 2021-01-01 00:00:00 |       0 |      50 |           nan |               900 |
| 514926 |         25021090 | SANTA ROSA [25021090] |   9.09333 |   -74.3139 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Fernando | 1974-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 2021-02-01 00:00:00 |       0 |      50 |           nan |               900 |


### Analysis from 1980 to 2021 for Etiqueta == "PTPM_TT_M": 55363 (10.75%)


**PTPM_TT_M - Station: 25025330 (339 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 339     |
| mean  | 164.522 |
| std   | 130.426 |
| min   |   0     |
| 25%   |  59.8   |
| 50%   | 142     |
| 75%   | 252.9   |
| max   | 693     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25025330_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25025330_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025330_DensityKDE.png)


**PTPM_TT_M - Station: 23210020 (297 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 297     |
| mean  | 159.691 |
| std   | 137.871 |
| min   |   0     |
| 25%   |  45     |
| 50%   | 130     |
| 75%   | 241     |
| max   | 649     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_23210020_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_23210020_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_23210020_DensityKDE.png)


**PTPM_TT_M - Station: 23215060 (146 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 146     |
| mean  | 136.245 |
| std   | 106.68  |
| min   |   0     |
| 25%   |  46.55  |
| 50%   | 122.9   |
| 75%   | 196.125 |
| max   | 422     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_23215060_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_23215060_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_23215060_DensityKDE.png)


**PTPM_TT_M - Station: 23215050 (467 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  467     |
| mean  |  233.842 |
| std   |  212.824 |
| min   |    0     |
| 25%   |   74.5   |
| 50%   |  182.3   |
| 75%   |  332.85  |
| max   | 1094.2   |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_23215050_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_23215050_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_23215050_DensityKDE.png)


**PTPM_TT_M - Station: 25020670 (466 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 466     |
| mean  | 146.059 |
| std   | 129.158 |
| min   |   0     |
| 25%   |  33     |
| 50%   | 118     |
| 75%   | 238.5   |
| max   | 814     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25020670_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25020670_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020670_DensityKDE.png)


**PTPM_TT_M - Station: 25021640 (443 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 443     |
| mean  | 145.321 |
| std   | 132.377 |
| min   |   0     |
| 25%   |  38.35  |
| 50%   | 115.5   |
| 75%   | 213.5   |
| max   | 717     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25021640_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25021640_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021640_DensityKDE.png)


**PTPM_TT_M - Station: 25021590 (206 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 206     |
| mean  | 136.508 |
| std   | 112.785 |
| min   |   0     |
| 25%   |  36.5   |
| 50%   | 125.8   |
| 75%   | 208.725 |
| max   | 512.2   |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25021590_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25021590_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021590_DensityKDE.png)


**PTPM_TT_M - Station: 25020090 (501 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 501     |
| mean  | 163.094 |
| std   | 143.448 |
| min   |   0     |
| 25%   |  44.7   |
| 50%   | 139     |
| 75%   | 246.6   |
| max   | 870.6   |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25020090_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25020090_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020090_DensityKDE.png)


**PTPM_TT_M - Station: 25020650 (436 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  436     |
| mean  |  156.154 |
| std   |  178.632 |
| min   |    0     |
| 25%   |   30.675 |
| 50%   |  115     |
| 75%   |  226.925 |
| max   | 1585     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25020650_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25020650_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020650_DensityKDE.png)


**PTPM_TT_M - Station: 25020660 (502 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 502     |
| mean  | 155.621 |
| std   | 132.496 |
| min   |   0     |
| 25%   |  49.175 |
| 50%   | 127.1   |
| 75%   | 230     |
| max   | 679     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25020660_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25020660_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020660_DensityKDE.png)


**PTPM_TT_M - Station: 28040150 (466 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 466     |
| mean  | 116.057 |
| std   |  94.465 |
| min   |   0     |
| 25%   |  42.25  |
| 50%   | 107     |
| 75%   | 163.75  |
| max   | 710     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28040150_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28040150_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040150_DensityKDE.png)


**PTPM_TT_M - Station: 28040360 (503 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 503      |
| mean  | 124.758  |
| std   |  95.0967 |
| min   |   0      |
| 25%   |  52.5    |
| 50%   | 116      |
| 75%   | 174      |
| max   | 840      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28040360_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28040360_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040360_DensityKDE.png)


**PTPM_TT_M - Station: 29060150 (488 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 488     |
| mean  | 134.827 |
| std   | 133.877 |
| min   |   0     |
| 25%   |  21.75  |
| 50%   | 100.5   |
| 75%   | 217.25  |
| max   | 861     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060150_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060150_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060150_DensityKDE.png)


**PTPM_TT_M - Station: 29060560 (442 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 442      |
| mean  |  97.6916 |
| std   | 101.206  |
| min   |   0      |
| 25%   |  16      |
| 50%   |  68.5    |
| 75%   | 150      |
| max   | 718      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060560_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060560_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060560_DensityKDE.png)


**PTPM_TT_M - Station: 29060040 (499 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 499     |
| mean  | 119.442 |
| std   | 115.678 |
| min   |   0     |
| 25%   |  28     |
| 50%   |  97     |
| 75%   | 172.5   |
| max   | 757.5   |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060040_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060040_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060040_DensityKDE.png)


**PTPM_TT_M - Station: 29060200 (483 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 483     |
| mean  | 118.879 |
| std   | 114.639 |
| min   |   0     |
| 25%   |  24     |
| 50%   | 100     |
| 75%   | 178.5   |
| max   | 685     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060200_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060200_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060200_DensityKDE.png)


**PTPM_TT_M - Station: 28040100 (493 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 493     |
| mean  | 144.448 |
| std   | 109.05  |
| min   |   0     |
| 25%   |  54     |
| 50%   | 137     |
| 75%   | 209     |
| max   | 741     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28040100_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28040100_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040100_DensityKDE.png)


**PTPM_TT_M - Station: 25021630 (460 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 460      |
| mean  | 111.086  |
| std   |  78.2969 |
| min   |   0      |
| 25%   |  49      |
| 50%   |  99      |
| 75%   | 165.25   |
| max   | 370      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25021630_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25021630_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021630_DensityKDE.png)


**PTPM_TT_M - Station: 28040140 (484 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 484      |
| mean  |  96.3804 |
| std   |  86.5089 |
| min   |   0      |
| 25%   |  23.9    |
| 50%   |  76.15   |
| 75%   | 145      |
| max   | 435      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28040140_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28040140_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040140_DensityKDE.png)


**PTPM_TT_M - Station: 29060100 (504 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 504     |
| mean  | 130.562 |
| std   | 109.441 |
| min   |   0     |
| 25%   |  40     |
| 50%   | 117.5   |
| 75%   | 189     |
| max   | 665     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060100_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060100_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060100_DensityKDE.png)


**PTPM_TT_M - Station: 29060350 (461 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 461     |
| mean  | 107.534 |
| std   | 115.366 |
| min   |   0     |
| 25%   |   5.4   |
| 50%   |  76.7   |
| 75%   | 171     |
| max   | 711     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060350_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060350_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060350_DensityKDE.png)


**PTPM_TT_M - Station: 29060030 (503 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 503     |
| mean  | 112.185 |
| std   | 120.076 |
| min   |   0     |
| 25%   |   5.5   |
| 50%   |  84.2   |
| 75%   | 174.5   |
| max   | 750     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060030_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060030_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060030_DensityKDE.png)


**PTPM_TT_M - Station: 29060140 (503 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  503     |
| mean  |  131.782 |
| std   |  154.306 |
| min   |    0     |
| 25%   |    7.5   |
| 50%   |   87     |
| 75%   |  201     |
| max   | 1116     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060140_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060140_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060140_DensityKDE.png)


**PTPM_TT_M - Station: 29060060 (492 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 492     |
| mean  | 214.417 |
| std   | 188.986 |
| min   |   0     |
| 25%   |  50     |
| 50%   | 180     |
| 75%   | 325     |
| max   | 944     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060060_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060060_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060060_DensityKDE.png)


**PTPM_TT_M - Station: 29060190 (420 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 420     |
| mean  | 106.892 |
| std   | 119.315 |
| min   |   0     |
| 25%   |   4.75  |
| 50%   |  71.5   |
| 75%   | 158.25  |
| max   | 794     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060190_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060190_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060190_DensityKDE.png)


**PTPM_TT_M - Station: 29060170 (503 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 503      |
| mean  |  79.0485 |
| std   |  92.832  |
| min   |   0      |
| 25%   |   0      |
| 50%   |  46      |
| 75%   | 134.15   |
| max   | 534.1    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060170_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060170_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060170_DensityKDE.png)


**PTPM_TT_M - Station: 29065020 (490 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 490     |
| mean  | 102.09  |
| std   | 105.756 |
| min   |   0     |
| 25%   |   9.475 |
| 50%   |  74.05  |
| 75%   | 158.575 |
| max   | 563.1   |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29065020_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29065020_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29065020_DensityKDE.png)


**PTPM_TT_M - Station: 29060270 (501 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 501      |
| mean  |  86.9663 |
| std   |  99.7629 |
| min   |   0      |
| 25%   |   0      |
| 50%   |  56      |
| 75%   | 132      |
| max   | 519      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060270_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060270_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060270_DensityKDE.png)


**PTPM_TT_M - Station: 29060240 (441 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  441     |
| mean  |  105.639 |
| std   |  136.714 |
| min   |    0     |
| 25%   |    0     |
| 50%   |   67     |
| 75%   |  170     |
| max   | 1016     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060240_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060240_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060240_DensityKDE.png)


**PTPM_TT_M - Station: 29065010 (122 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 122      |
| mean  |  93.5492 |
| std   |  92.2916 |
| min   |   0      |
| 25%   |  11.1    |
| 50%   |  70.65   |
| 75%   | 151.225  |
| max   | 366.7    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29065010_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29065010_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29065010_DensityKDE.png)


**PTPM_TT_M - Station: 29060180 (500 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  500     |
| mean  |  116.55  |
| std   |  151.057 |
| min   |    0     |
| 25%   |    0     |
| 50%   |   69.5   |
| 75%   |  168     |
| max   | 1075     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060180_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060180_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060180_DensityKDE.png)


**PTPM_TT_M - Station: 29060340 (490 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 490     |
| mean  | 192.753 |
| std   | 165.79  |
| min   |   0     |
| 25%   |  52.5   |
| 50%   | 165.5   |
| 75%   | 282.75  |
| max   | 875     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060340_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060340_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060340_DensityKDE.png)


**PTPM_TT_M - Station: 29060330 (252 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 252     |
| mean  | 131.828 |
| std   | 139.738 |
| min   |   0     |
| 25%   |  11.5   |
| 50%   |  97     |
| 75%   | 208.25  |
| max   | 615     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060330_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060330_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060330_DensityKDE.png)


**PTPM_TT_M - Station: 29060220 (258 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 258     |
| mean  | 114.547 |
| std   | 152.219 |
| min   |   0     |
| 25%   |   0     |
| 50%   |  64.5   |
| 75%   | 157.75  |
| max   | 941     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060220_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060220_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060220_DensityKDE.png)


**PTPM_TT_M - Station: 29065030 (412 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 412     |
| mean  | 121.007 |
| std   | 122.086 |
| min   |   0     |
| 25%   |  11.3   |
| 50%   |  96.5   |
| 75%   | 179.975 |
| max   | 637.9   |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29065030_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29065030_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29065030_DensityKDE.png)


**PTPM_TT_M - Station: 29060250 (499 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 499      |
| mean  |  82.9495 |
| std   | 102.98   |
| min   |   0      |
| 25%   |   0      |
| 50%   |  50      |
| 75%   | 122.05   |
| max   | 627.6    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060250_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060250_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060250_DensityKDE.png)


**PTPM_TT_M - Station: 29060550 (360 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 360      |
| mean  |  97.5958 |
| std   | 110.703  |
| min   |   0      |
| 25%   |   0      |
| 50%   |  68      |
| 75%   | 160.05   |
| max   | 652      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060550_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060550_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060550_DensityKDE.png)


**PTPM_TT_M - Station: 29060290 (249 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 249     |
| mean  | 103.559 |
| std   | 124.612 |
| min   |   0     |
| 25%   |   0     |
| 50%   |  60     |
| 75%   | 149     |
| max   | 627     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060290_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060290_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060290_DensityKDE.png)


**PTPM_TT_M - Station: 29060070 (502 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 502     |
| mean  | 199.184 |
| std   | 159.074 |
| min   |   0     |
| 25%   |  61.5   |
| 50%   | 179     |
| 75%   | 306     |
| max   | 927     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060070_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060070_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060070_DensityKDE.png)


**PTPM_TT_M - Station: 29060230 (370 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 370     |
| mean  | 101.154 |
| std   | 108.271 |
| min   |   0     |
| 25%   |   6     |
| 50%   |  72     |
| 75%   | 158.5   |
| max   | 549     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060230_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060230_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060230_DensityKDE.png)


**PTPM_TT_M - Station: 29060160 (489 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 489     |
| mean  |  83.846 |
| std   | 104.429 |
| min   |   0     |
| 25%   |   0     |
| 50%   |  40     |
| 75%   | 136.1   |
| max   | 655.1   |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060160_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060160_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060160_DensityKDE.png)


**PTPM_TT_M - Station: 29060210 (501 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 501      |
| mean  |  70.4112 |
| std   |  85.1528 |
| min   |   0      |
| 25%   |   1.2    |
| 50%   |  39.4    |
| 75%   | 108.6    |
| max   | 549.8    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060210_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060210_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060210_DensityKDE.png)


**PTPM_TT_M - Station: 29060280 (484 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 484      |
| mean  |  69.8316 |
| std   |  89.7702 |
| min   |   0      |
| 25%   |   0      |
| 50%   |  35.2    |
| 75%   | 110.625  |
| max   | 630.2    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060280_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060280_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060280_DensityKDE.png)


**PTPM_TT_M - Station: 29060310 (504 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 504      |
| mean  |  79.7937 |
| std   | 116.537  |
| min   |   0      |
| 25%   |   0      |
| 50%   |  33      |
| 75%   | 128      |
| max   | 930      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060310_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060310_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060310_DensityKDE.png)


**PTPM_TT_M - Station: 29060120 (504 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 504      |
| mean  |  30.9839 |
| std   |  60.6528 |
| min   |   0      |
| 25%   |   0      |
| 50%   |   6      |
| 75%   |  30      |
| max   | 485      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060120_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060120_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060120_DensityKDE.png)


**PTPM_TT_M - Station: 15015020 (339 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 339      |
| mean  |  59.7829 |
| std   |  74.2829 |
| min   |   0      |
| 25%   |   0.5    |
| 50%   |  30.1    |
| 75%   |  85.2    |
| max   | 407      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_15015020_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_15015020_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15015020_DensityKDE.png)


**PTPM_TT_M - Station: 16060010 (504 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  504     |
| mean  |  304.344 |
| std   |  206.676 |
| min   |    0     |
| 25%   |  146.25  |
| 50%   |  284.5   |
| 75%   |  426.25  |
| max   | 1005     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_16060010_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_16060010_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16060010_DensityKDE.png)


**PTPM_TT_M - Station: 16070030 (309 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  309     |
| mean  |  390.891 |
| std   |  245.702 |
| min   |    0     |
| 25%   |  216     |
| 50%   |  359     |
| 75%   |  524     |
| max   | 1351     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_16070030_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_16070030_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070030_DensityKDE.png)


**PTPM_TT_M - Station: 16070040 (472 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  472     |
| mean  |  353.798 |
| std   |  208.838 |
| min   |    8     |
| 25%   |  204.5   |
| 50%   |  341     |
| 75%   |  485.25  |
| max   | 1173     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_16070040_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_16070040_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070040_DensityKDE.png)


**PTPM_TT_M - Station: 16050240 (327 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  327     |
| mean  |  178.577 |
| std   |  136.351 |
| min   |    0     |
| 25%   |   82     |
| 50%   |  156     |
| 75%   |  246     |
| max   | 1150     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_16050240_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_16050240_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16050240_DensityKDE.png)


**PTPM_TT_M - Station: 16070020 (154 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  154     |
| mean  |  393.565 |
| std   |  269.214 |
| min   |    0     |
| 25%   |  162.25  |
| 50%   |  366     |
| 75%   |  557.5   |
| max   | 1210     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_16070020_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_16070020_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070020_DensityKDE.png)


**PTPM_TT_M - Station: 16070010 (437 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  437     |
| mean  |  410.432 |
| std   |  267.691 |
| min   |    0     |
| 25%   |  196     |
| 50%   |  396     |
| 75%   |  578     |
| max   | 1444     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_16070010_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_16070010_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070010_DensityKDE.png)


**PTPM_TT_M - Station: 25020220 (503 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 503     |
| mean  | 125.969 |
| std   | 101.616 |
| min   |   0     |
| 25%   |  43.3   |
| 50%   | 111.1   |
| 75%   | 189.85  |
| max   | 534     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25020220_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25020220_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020220_DensityKDE.png)


**PTPM_TT_M - Station: 25020240 (502 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 502     |
| mean  | 136.406 |
| std   | 120.364 |
| min   |   0     |
| 25%   |  43     |
| 50%   | 112.5   |
| 75%   | 194     |
| max   | 735     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25020240_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25020240_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020240_DensityKDE.png)


**PTPM_TT_M - Station: 25021240 (504 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 504     |
| mean  | 169.907 |
| std   | 147.9   |
| min   |   0     |
| 25%   |  46.875 |
| 50%   | 141.85  |
| 75%   | 265     |
| max   | 696.6   |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25021240_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25021240_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021240_DensityKDE.png)


**PTPM_TT_M - Station: 25025250 (453 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 453     |
| mean  | 135.746 |
| std   | 116.256 |
| min   |   0     |
| 25%   |  35     |
| 50%   | 115.4   |
| 75%   | 196.6   |
| max   | 549.9   |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25025250_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25025250_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025250_DensityKDE.png)


**PTPM_TT_M - Station: 25021580 (188 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 188     |
| mean  | 144.556 |
| std   | 116.792 |
| min   |   0     |
| 25%   |  52.75  |
| 50%   | 109.5   |
| 75%   | 217.75  |
| max   | 494     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25021580_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25021580_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021580_DensityKDE.png)


**PTPM_TT_M - Station: 25020250 (501 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 501     |
| mean  | 142.694 |
| std   | 118.441 |
| min   |   0     |
| 25%   |  48     |
| 50%   | 117.9   |
| 75%   | 208.9   |
| max   | 644.3   |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25020250_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25020250_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020250_DensityKDE.png)


**PTPM_TT_M - Station: 25020690 (504 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 504     |
| mean  | 153.358 |
| std   | 146.017 |
| min   |   0     |
| 25%   |  37     |
| 50%   | 112     |
| 75%   | 233.5   |
| max   | 753     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25020690_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25020690_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020690_DensityKDE.png)


**PTPM_TT_M - Station: 25020920 (418 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  418     |
| mean  |  139.157 |
| std   |  173.081 |
| min   |    0     |
| 25%   |   30     |
| 50%   |   88.5   |
| 75%   |  184.475 |
| max   | 1274     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25020920_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25020920_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020920_DensityKDE.png)


**PTPM_TT_M - Station: 25020260 (495 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  495     |
| mean  |  221.96  |
| std   |  172.012 |
| min   |    0     |
| 25%   |   89     |
| 50%   |  205     |
| 75%   |  318.5   |
| max   | 1163     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25020260_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25020260_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020260_DensityKDE.png)


**PTPM_TT_M - Station: 25020270 (500 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 500     |
| mean  | 168.683 |
| std   | 144.303 |
| min   |   0     |
| 25%   |  48     |
| 50%   | 136     |
| 75%   | 262     |
| max   | 627     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25020270_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25020270_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020270_DensityKDE.png)


**PTPM_TT_M - Station: 28025090 (500 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 500      |
| mean  | 123.833  |
| std   |  97.4444 |
| min   |   0      |
| 25%   |  45.3    |
| 50%   | 110.3    |
| 75%   | 187.725  |
| max   | 504.6    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28025090_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28025090_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025090_DensityKDE.png)


**PTPM_TT_M - Station: 25020230 (482 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 482     |
| mean  | 164.951 |
| std   | 141.109 |
| min   |   0     |
| 25%   |  56.225 |
| 50%   | 137     |
| 75%   | 241.5   |
| max   | 926     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25020230_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25020230_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020230_DensityKDE.png)


**PTPM_TT_M - Station: 28020230 (266 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 266     |
| mean  | 125.781 |
| std   | 120.656 |
| min   |   0     |
| 25%   |  24.775 |
| 50%   | 110.1   |
| 75%   | 179.875 |
| max   | 675.7   |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28020230_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28020230_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020230_DensityKDE.png)


**PTPM_TT_M - Station: 25020280 (467 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 467     |
| mean  | 127.036 |
| std   | 118.767 |
| min   |   0     |
| 25%   |  35     |
| 50%   | 102     |
| 75%   | 185     |
| max   | 749     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25020280_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25020280_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020280_DensityKDE.png)


**PTPM_TT_M - Station: 28040310 (357 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 357     |
| mean  | 114.399 |
| std   |  94.932 |
| min   |   0     |
| 25%   |  40     |
| 50%   | 101     |
| 75%   | 165     |
| max   | 521     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28040310_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28040310_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040310_DensityKDE.png)


**PTPM_TT_M - Station: 28040350 (504 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 504      |
| mean  | 110.536  |
| std   |  99.4701 |
| min   |   0      |
| 25%   |  31.8    |
| 50%   |  93.6    |
| 75%   | 160.8    |
| max   | 673.4    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28040350_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28040350_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040350_DensityKDE.png)


**PTPM_TT_M - Station: 28020080 (470 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 470     |
| mean  | 115.409 |
| std   | 105.649 |
| min   |   0     |
| 25%   |  30.25  |
| 50%   |  94     |
| 75%   | 172.5   |
| max   | 733     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28020080_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28020080_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020080_DensityKDE.png)


**PTPM_TT_M - Station: 28020420 (448 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 448     |
| mean  | 122.556 |
| std   | 108.867 |
| min   |   0     |
| 25%   |  34.5   |
| 50%   | 102     |
| 75%   | 188     |
| max   | 567     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28020420_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28020420_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020420_DensityKDE.png)


**PTPM_TT_M - Station: 28025080 (347 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 347      |
| mean  | 127.758  |
| std   |  98.1071 |
| min   |   0      |
| 25%   |  46.6    |
| 50%   | 113      |
| 75%   | 188.65   |
| max   | 496.9    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28025080_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28025080_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025080_DensityKDE.png)


**PTPM_TT_M - Station: 25021650 (442 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 442     |
| mean  | 132.213 |
| std   | 129.695 |
| min   |   0     |
| 25%   |  32.25  |
| 50%   | 102.6   |
| 75%   | 198.5   |
| max   | 910     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25021650_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25021650_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021650_DensityKDE.png)


**PTPM_TT_M - Station: 28040030 (499 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  499     |
| mean  |  116.19  |
| std   |  125.578 |
| min   |    0     |
| 25%   |   28     |
| 50%   |   90     |
| 75%   |  156.8   |
| max   | 1053     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28040030_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28040030_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040030_DensityKDE.png)


**PTPM_TT_M - Station: 28020460 (498 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 498     |
| mean  | 128.521 |
| std   | 108.515 |
| min   |   0     |
| 25%   |  46.25  |
| 50%   | 104.5   |
| 75%   | 192.75  |
| max   | 591     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28020460_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28020460_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020460_DensityKDE.png)


**PTPM_TT_M - Station: 28020150 (431 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 431      |
| mean  | 108.619  |
| std   |  88.2291 |
| min   |   0      |
| 25%   |  42      |
| 50%   |  89.2    |
| 75%   | 159      |
| max   | 518      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28020150_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28020150_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020150_DensityKDE.png)


**PTPM_TT_M - Station: 28035040 (492 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 492     |
| mean  | 107.14  |
| std   |  84.195 |
| min   |   0     |
| 25%   |  33.375 |
| 50%   |  97.45  |
| 75%   | 154.225 |
| max   | 425     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28035040_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28035040_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28035040_DensityKDE.png)


**PTPM_TT_M - Station: 28040270 (484 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 484      |
| mean  | 107.482  |
| std   |  89.9329 |
| min   |   0      |
| 25%   |  30      |
| 50%   |  98      |
| 75%   | 159      |
| max   | 560      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28040270_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28040270_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040270_DensityKDE.png)


**PTPM_TT_M - Station: 28025070 (504 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 504     |
| mean  | 131.555 |
| std   | 104.05  |
| min   |   0     |
| 25%   |  47.95  |
| 50%   | 114.7   |
| 75%   | 194.45  |
| max   | 550.8   |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28025070_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28025070_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025070_DensityKDE.png)


**PTPM_TT_M - Station: 28040070 (494 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 494      |
| mean  | 111.56   |
| std   |  88.4919 |
| min   |   0      |
| 25%   |  40      |
| 50%   | 100      |
| 75%   | 165      |
| max   | 415      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28040070_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28040070_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040070_DensityKDE.png)


**PTPM_TT_M - Station: 28040400 (358 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 358      |
| mean  | 103.43   |
| std   |  86.8242 |
| min   |   0      |
| 25%   |  34.25   |
| 50%   |  85      |
| 75%   | 148      |
| max   | 398      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28040400_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28040400_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040400_DensityKDE.png)


**PTPM_TT_M - Station: 28020600 (468 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 468     |
| mean  | 112.204 |
| std   |  97.752 |
| min   |   0     |
| 25%   |  33.75  |
| 50%   |  86     |
| 75%   | 172.85  |
| max   | 609     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28020600_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28020600_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020600_DensityKDE.png)


**PTPM_TT_M - Station: 28020440 (492 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 492     |
| mean  | 127.331 |
| std   | 101.811 |
| min   |   0     |
| 25%   |  45     |
| 50%   | 109.4   |
| 75%   | 192     |
| max   | 610.6   |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28020440_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28020440_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020440_DensityKDE.png)


**PTPM_TT_M - Station: 28020310 (281 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 281     |
| mean  | 180.133 |
| std   | 148.914 |
| min   |   0     |
| 25%   |  63     |
| 50%   | 145     |
| 75%   | 261     |
| max   | 723     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28020310_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28020310_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020310_DensityKDE.png)


**PTPM_TT_M - Station: 28030190 (504 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 504      |
| mean  |  93.3151 |
| std   |  86.66   |
| min   |   0      |
| 25%   |  14.475  |
| 50%   |  82.8    |
| 75%   | 144.55   |
| max   | 450.8    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28030190_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28030190_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28030190_DensityKDE.png)


**PTPM_TT_M - Station: 28040200 (187 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 187      |
| mean  |  96.7465 |
| std   |  74.8121 |
| min   |   0      |
| 25%   |  33.5    |
| 50%   |  91      |
| 75%   | 146.5    |
| max   | 374      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28040200_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28040200_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040200_DensityKDE.png)


**PTPM_TT_M - Station: 28020590 (448 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 448      |
| mean  | 103.627  |
| std   |  91.3379 |
| min   |   0      |
| 25%   |  29      |
| 50%   |  83.3    |
| 75%   | 156      |
| max   | 542      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28020590_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28020590_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020590_DensityKDE.png)


**PTPM_TT_M - Station: 28010370 (501 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 501     |
| mean  | 108.373 |
| std   |  94.421 |
| min   |   0     |
| 25%   |  26     |
| 50%   |  88     |
| 75%   | 171     |
| max   | 508     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28010370_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28010370_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010370_DensityKDE.png)


**PTPM_TT_M - Station: 28040060 (140 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 140     |
| mean  | 105.394 |
| std   |  98.432 |
| min   |   0     |
| 25%   |  30     |
| 50%   |  72.5   |
| 75%   | 152.75  |
| max   | 500     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28040060_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28040060_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040060_DensityKDE.png)


**PTPM_TT_M - Station: 28025020 (494 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 494      |
| mean  | 110.783  |
| std   |  82.2089 |
| min   |   0      |
| 25%   |  42.025  |
| 50%   | 104.8    |
| 75%   | 165.05   |
| max   | 421.2    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28025020_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28025020_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025020_DensityKDE.png)


**PTPM_TT_M - Station: 28020410 (457 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 457     |
| mean  | 107.139 |
| std   | 101.903 |
| min   |   0     |
| 25%   |  27.9   |
| 50%   |  82     |
| 75%   | 156     |
| max   | 757     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28020410_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28020410_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020410_DensityKDE.png)


**PTPM_TT_M - Station: 28010070 (432 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 432     |
| mean  | 116.327 |
| std   | 106.916 |
| min   |   0     |
| 25%   |  32.75  |
| 50%   |  98.3   |
| 75%   | 179.75  |
| max   | 581     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28010070_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28010070_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010070_DensityKDE.png)


**PTPM_TT_M - Station: 28035010 (462 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 462     |
| mean  | 110.852 |
| std   |  91.875 |
| min   |   0     |
| 25%   |  30.25  |
| 50%   |  95.75  |
| 75%   | 168.375 |
| max   | 479.6   |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28035010_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28035010_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28035010_DensityKDE.png)


**PTPM_TT_M - Station: 28010360 (470 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  470     |
| mean  |  172.4   |
| std   |  212.311 |
| min   |    0     |
| 25%   |   20     |
| 50%   |  102.05  |
| 75%   |  252.425 |
| max   | 1647.3   |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28010360_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28010360_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010360_DensityKDE.png)


**PTPM_TT_M - Station: 28035020 (474 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 474      |
| mean  |  98.4741 |
| std   |  84.522  |
| min   |   0      |
| 25%   |  21.025  |
| 50%   |  85.35   |
| 75%   | 152.45   |
| max   | 464.2    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28035020_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28035020_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28035020_DensityKDE.png)


**PTPM_TT_M - Station: 28040170 (106 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 106     |
| mean  | 115.199 |
| std   | 121.212 |
| min   |   0     |
| 25%   |  18.15  |
| 50%   |  60.5   |
| 75%   | 200.25  |
| max   | 505     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28040170_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28040170_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040170_DensityKDE.png)


**PTPM_TT_M - Station: 28010020 (359 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 359      |
| mean  |  78.6925 |
| std   |  88.7822 |
| min   |   0      |
| 25%   |  10      |
| 50%   |  55      |
| 75%   | 125      |
| max   | 713      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28010020_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28010020_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010020_DensityKDE.png)


**PTPM_TT_M - Station: 28010040 (498 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 498     |
| mean  | 151.934 |
| std   | 128.693 |
| min   |   0     |
| 25%   |  48.325 |
| 50%   | 130.1   |
| 75%   | 220.625 |
| max   | 748.7   |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28010040_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28010040_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010040_DensityKDE.png)


**PTPM_TT_M - Station: 28040010 (504 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  504     |
| mean  |  178.377 |
| std   |  153.483 |
| min   |    0     |
| 25%   |   53.75  |
| 50%   |  157.5   |
| 75%   |  261.25  |
| max   | 1193     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28040010_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28040010_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040010_DensityKDE.png)


**PTPM_TT_M - Station: 28030220 (401 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 401      |
| mean  |  85.2723 |
| std   |  91.6286 |
| min   |   0      |
| 25%   |   1.3    |
| 50%   |  58.3    |
| 75%   | 135      |
| max   | 525      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28030220_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28030220_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28030220_DensityKDE.png)


**PTPM_TT_M - Station: 28025040 (171 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 171      |
| mean  |  96.6094 |
| std   |  90.3915 |
| min   |   0      |
| 25%   |  26.1    |
| 50%   |  68.8    |
| 75%   | 143.5    |
| max   | 360.6    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28025040_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28025040_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025040_DensityKDE.png)


**PTPM_TT_M - Station: 29060090 (501 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 501     |
| mean  | 109.604 |
| std   |  77.811 |
| min   |   0     |
| 25%   |  42     |
| 50%   | 106     |
| 75%   | 168     |
| max   | 382     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_29060090_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_29060090_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060090_DensityKDE.png)


**PTPM_TT_M - Station: 28010140 (255 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 255     |
| mean  | 131.152 |
| std   | 134.891 |
| min   |   0     |
| 25%   |  24     |
| 50%   |  89     |
| 75%   | 194     |
| max   | 630     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28010140_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28010140_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010140_DensityKDE.png)


**PTPM_TT_M - Station: 28010090 (474 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 474      |
| mean  |  92.6331 |
| std   |  95.1618 |
| min   |   0      |
| 25%   |  10      |
| 50%   |  71.5    |
| 75%   | 138      |
| max   | 631      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28010090_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28010090_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010090_DensityKDE.png)


**PTPM_TT_M - Station: 28045010 (228 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 228     |
| mean  | 129.799 |
| std   | 131.563 |
| min   |   0     |
| 25%   |   0     |
| 50%   |  93.3   |
| 75%   | 224.7   |
| max   | 502.1   |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28045010_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28045010_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28045010_DensityKDE.png)


**PTPM_TT_M - Station: 28010130 (122 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  122     |
| mean  |  230.704 |
| std   |  218.823 |
| min   |    0     |
| 25%   |   60     |
| 50%   |  162     |
| 75%   |  342.25  |
| max   | 1009     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28010130_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28010130_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010130_DensityKDE.png)


**PTPM_TT_M - Station: 15060080 (503 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 503      |
| mean  |  98.771  |
| std   |  93.6652 |
| min   |   0      |
| 25%   |  15      |
| 50%   |  83      |
| 75%   | 148.5    |
| max   | 722      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_15060080_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_15060080_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060080_DensityKDE.png)


**PTPM_TT_M - Station: 15060150 (504 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 504      |
| mean  |  72.1262 |
| std   |  80.4786 |
| min   |   0      |
| 25%   |   8      |
| 50%   |  46.1    |
| 75%   | 107.375  |
| max   | 383      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_15060150_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_15060150_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060150_DensityKDE.png)


**PTPM_TT_M - Station: 28010200 (471 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 471      |
| mean  |  82.41   |
| std   |  90.3403 |
| min   |   0      |
| 25%   |   5.4    |
| 50%   |  52      |
| 75%   | 129.4    |
| max   | 556      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28010200_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28010200_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010200_DensityKDE.png)


**PTPM_TT_M - Station: 15060070 (387 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 387     |
| mean  | 103.287 |
| std   | 105.964 |
| min   |   0     |
| 25%   |  15     |
| 50%   |  82     |
| 75%   | 150     |
| max   | 655     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_15060070_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_15060070_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060070_DensityKDE.png)


**PTPM_TT_M - Station: 15065040 (243 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 243      |
| mean  |  65.5008 |
| std   |  59.54   |
| min   |   0      |
| 25%   |  10.8    |
| 50%   |  53      |
| 75%   | 107.75   |
| max   | 237.7    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_15065040_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_15065040_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15065040_DensityKDE.png)


**PTPM_TT_M - Station: 28010280 (15 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  15      |
| mean  |  52.2667 |
| std   |  55.7577 |
| min   |   2      |
| 25%   |  12.5    |
| 50%   |  26      |
| 75%   |  77      |
| max   | 169      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28010280_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28010280_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010280_DensityKDE.png)


**PTPM_TT_M - Station: 15060050 (487 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 487      |
| mean  |  87.9507 |
| std   |  83.7311 |
| min   |   0      |
| 25%   |  12.1    |
| 50%   |  74      |
| 75%   | 138.1    |
| max   | 489.2    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_15060050_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_15060050_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060050_DensityKDE.png)


**PTPM_TT_M - Station: 28015070 (499 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 499      |
| mean  |  98.0299 |
| std   |  84.267  |
| min   |   0      |
| 25%   |  28.35   |
| 50%   |  87.9    |
| 75%   | 150.7    |
| max   | 456.1    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28015070_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28015070_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28015070_DensityKDE.png)


**PTPM_TT_M - Station: 28010340 (492 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 492      |
| mean  |  99.5524 |
| std   |  92.5377 |
| min   |   0      |
| 25%   |  16.975  |
| 50%   |  82.5    |
| 75%   | 154      |
| max   | 457      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28010340_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28010340_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010340_DensityKDE.png)


**PTPM_TT_M - Station: 25025090 (466 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 466     |
| mean  | 164.917 |
| std   | 134.386 |
| min   |   0     |
| 25%   |  53.3   |
| 50%   | 139.15  |
| 75%   | 246.2   |
| max   | 609.3   |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25025090_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25025090_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025090_DensityKDE.png)


**PTPM_TT_M - Station: 28040320 (487 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 487      |
| mean  | 124.416  |
| std   |  96.7825 |
| min   |   0      |
| 25%   |  50.5    |
| 50%   | 107      |
| 75%   | 172.5    |
| max   | 491      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28040320_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28040320_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040320_DensityKDE.png)


**PTPM_TT_M - Station: 25021620 (468 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 468     |
| mean  | 116.16  |
| std   |  92.907 |
| min   |   0     |
| 25%   |  44.75  |
| 50%   | 101.5   |
| 75%   | 161     |
| max   | 716     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25021620_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25021620_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021620_DensityKDE.png)


**PTPM_TT_M - Station: 25021040 (503 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 503     |
| mean  | 161.868 |
| std   | 139.083 |
| min   |   0     |
| 25%   |  45     |
| 50%   | 139     |
| 75%   | 245.5   |
| max   | 739     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25021040_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25021040_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021040_DensityKDE.png)


**PTPM_TT_M - Station: 25021200 (484 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 484     |
| mean  | 190.166 |
| std   | 168.025 |
| min   |   0     |
| 25%   |  50     |
| 50%   | 149     |
| 75%   | 284.5   |
| max   | 934     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25021200_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25021200_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021200_DensityKDE.png)


**PTPM_TT_M - Station: 25021500 (492 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 492      |
| mean  |  99.214  |
| std   |  74.7592 |
| min   |   0      |
| 25%   |  41      |
| 50%   |  88      |
| 75%   | 145      |
| max   | 368      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25021500_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25021500_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021500_DensityKDE.png)


**PTPM_TT_M - Station: 25021380 (477 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 477     |
| mean  | 167.207 |
| std   | 139.418 |
| min   |   0     |
| 25%   |  53     |
| 50%   | 140     |
| 75%   | 257     |
| max   | 724     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25021380_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25021380_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021380_DensityKDE.png)


**PTPM_TT_M - Station: 25020900 (492 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 492     |
| mean  | 131.34  |
| std   | 114.881 |
| min   |   0     |
| 25%   |  30     |
| 50%   | 106     |
| 75%   | 207     |
| max   | 510     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25020900_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25020900_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020900_DensityKDE.png)


**PTPM_TT_M - Station: 25025300 (470 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 470      |
| mean  | 110.96   |
| std   |  92.9367 |
| min   |   0      |
| 25%   |  35.225  |
| 50%   |  90.9    |
| 75%   | 163.8    |
| max   | 459.2    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25025300_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25025300_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025300_DensityKDE.png)


**PTPM_TT_M - Station: 28040300 (480 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 480      |
| mean  | 114.796  |
| std   |  97.6011 |
| min   |   0      |
| 25%   |  39      |
| 50%   |  96      |
| 75%   | 162      |
| max   | 564      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_28040300_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_28040300_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040300_DensityKDE.png)


**PTPM_TT_M - Station: 25021540 (490 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 490     |
| mean  | 178.49  |
| std   | 144.689 |
| min   |   0     |
| 25%   |  66.25  |
| 50%   | 144.5   |
| 75%   | 264.925 |
| max   | 721     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25021540_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25021540_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021540_DensityKDE.png)


**PTPM_TT_M - Station: 25020880 (490 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 490     |
| mean  | 193.8   |
| std   | 160.698 |
| min   |   0     |
| 25%   |  60     |
| 50%   | 163.5   |
| 75%   | 291     |
| max   | 764     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25020880_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25020880_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020880_DensityKDE.png)


**PTPM_TT_M - Station: 25020890 (483 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 483     |
| mean  | 155.821 |
| std   | 128.157 |
| min   |   0     |
| 25%   |  49     |
| 50%   | 130     |
| 75%   | 244     |
| max   | 593     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25020890_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25020890_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020890_DensityKDE.png)


**PTPM_TT_M - Station: 25021320 (491 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 491     |
| mean  | 160.853 |
| std   | 141.005 |
| min   |   0     |
| 25%   |  48     |
| 50%   | 133     |
| 75%   | 240     |
| max   | 744     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25021320_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25021320_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021320_DensityKDE.png)


**PTPM_TT_M - Station: 25020870 (497 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 497     |
| mean  | 155.739 |
| std   | 135.675 |
| min   |   0     |
| 25%   |  45     |
| 50%   | 136     |
| 75%   | 233     |
| max   | 835     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25020870_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25020870_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020870_DensityKDE.png)


**PTPM_TT_M - Station: 25021090 (475 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 475     |
| mean  | 157.96  |
| std   | 141.425 |
| min   |   0     |
| 25%   |  40     |
| 50%   | 125     |
| 75%   | 240.9   |
| max   | 680     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_PTPM_TT_M_25021090_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_PTPM_TT_M_25021090_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021090_DensityKDE.png)


### Analysis from 1980 to 2021 for Etiqueta == "TMX_CON": 185849 (36.09%)


**TMX_CON - Station: 28045020 (1050 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 1050       |
| mean  |   33.8226  |
| std   |    2.13222 |
| min   |   27.2     |
| 25%   |   32.25    |
| 50%   |   33.8     |
| 75%   |   35.4     |
| max   |   39.2     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_28045020_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_28045020_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28045020_DensityKDE.png)


**TMX_CON - Station: 28025090 (12953 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 12953       |
| mean  |    34.3336  |
| std   |     2.09333 |
| min   |    23.8     |
| 25%   |    33       |
| 50%   |    34.4     |
| 75%   |    35.8     |
| max   |    42.3     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_28025090_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_28025090_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28025090_DensityKDE.png)


**TMX_CON - Station: 25025250 (11758 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 11758       |
| mean  |    33.787   |
| std   |     2.07519 |
| min   |    26.6     |
| 25%   |    32.4     |
| 50%   |    34       |
| 75%   |    35       |
| max   |    42.6     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_25025250_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_25025250_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_25025250_DensityKDE.png)


**TMX_CON - Station: 25025330 (7606 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 7606      |
| mean  |   33.2243 |
| std   |    2.0554 |
| min   |   23.2    |
| 25%   |   31.8    |
| 50%   |   33      |
| 75%   |   34.6    |
| max   |   41.6    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_25025330_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_25025330_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_25025330_DensityKDE.png)


**TMX_CON - Station: 28045040 (784 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 784       |
| mean  |  34.5605  |
| std   |   2.25236 |
| min   |  26       |
| 25%   |  33       |
| 50%   |  34.6     |
| 75%   |  36       |
| max   |  41.8     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_28045040_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_28045040_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28045040_DensityKDE.png)


**TMX_CON - Station: 28035040 (9424 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 9424       |
| mean  |   36.1116  |
| std   |    2.03179 |
| min   |   26       |
| 25%   |   35       |
| 50%   |   36.4     |
| 75%   |   37.4     |
| max   |   42.4     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_28035040_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_28035040_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28035040_DensityKDE.png)


**TMX_CON - Station: 23215060 (960 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 960       |
| mean  |  32.7978  |
| std   |   1.77501 |
| min   |  27       |
| 25%   |  31.6     |
| 50%   |  32.8     |
| 75%   |  34       |
| max   |  37.4     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_23215060_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_23215060_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_23215060_DensityKDE.png)


**TMX_CON - Station: 28025070 (13398 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 13398       |
| mean  |    34.4325  |
| std   |     2.35604 |
| min   |    24.1     |
| 25%   |    32.8     |
| 50%   |    34.4     |
| 75%   |    36.2     |
| max   |    42.8     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_28025070_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_28025070_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28025070_DensityKDE.png)


**TMX_CON - Station: 28025080 (7076 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 7076       |
| mean  |   33.5969  |
| std   |    2.05285 |
| min   |   26.4     |
| 25%   |   32.2     |
| 50%   |   33.6     |
| 75%   |   35       |
| max   |   40       |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_28025080_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_28025080_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28025080_DensityKDE.png)


**TMX_CON - Station: 28035010 (8442 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 8442       |
| mean  |   35.0506  |
| std   |    2.25909 |
| min   |   25       |
| 25%   |   33.6     |
| 50%   |   35.2     |
| 75%   |   36.6     |
| max   |   42.4     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_28035010_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_28035010_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28035010_DensityKDE.png)


**TMX_CON - Station: 28025502 (11456 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 11456       |
| mean  |    34.6493  |
| std   |     2.18198 |
| min   |    24.8     |
| 25%   |    33.2     |
| 50%   |    34.7     |
| 75%   |    36.2     |
| max   |    41.8     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_28025502_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_28025502_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28025502_DensityKDE.png)


**TMX_CON - Station: 28035020 (12136 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 12136       |
| mean  |    34.7338  |
| std   |     2.21035 |
| min   |    25.4     |
| 25%   |    33.2     |
| 50%   |    34.8     |
| 75%   |    36.4     |
| max   |    41.8     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_28035020_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_28035020_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28035020_DensityKDE.png)


**TMX_CON - Station: 28015030 (1127 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 1127       |
| mean  |   34.5657  |
| std   |    1.85704 |
| min   |   26.3     |
| 25%   |   33.4     |
| 50%   |   34.6     |
| 75%   |   35.8     |
| max   |   40.4     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_28015030_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_28015030_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28015030_DensityKDE.png)


**TMX_CON - Station: 28035070 (42 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 42       |
| mean  | 37.1095  |
| std   |  1.26738 |
| min   | 34       |
| 25%   | 36.6     |
| 50%   | 37.4     |
| 75%   | 38       |
| max   | 39.2     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_28035070_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_28035070_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28035070_DensityKDE.png)


**TMX_CON - Station: 28025020 (12966 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 12966       |
| mean  |    32.6602  |
| std   |     2.08594 |
| min   |    24.6     |
| 25%   |    31.3     |
| 50%   |    32.7     |
| 75%   |    34.2     |
| max   |    39.7     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_28025020_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_28025020_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28025020_DensityKDE.png)


**TMX_CON - Station: 28025040 (2613 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 2613       |
| mean  |   29.7907  |
| std   |    1.74453 |
| min   |   22.4     |
| 25%   |   28.6     |
| 50%   |   30       |
| 75%   |   31       |
| max   |   39.2     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_28025040_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_28025040_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28025040_DensityKDE.png)


**TMX_CON - Station: 15065040 (3465 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 3465       |
| mean  |   34.0803  |
| std   |    1.83791 |
| min   |   25.1     |
| 25%   |   33       |
| 50%   |   34.2     |
| 75%   |   35.4     |
| max   |   39.4     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_15065040_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_15065040_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_15065040_DensityKDE.png)


**TMX_CON - Station: 28015070 (12645 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 12645       |
| mean  |    33.7017  |
| std   |     2.18347 |
| min   |    23.8     |
| 25%   |    32.2     |
| 50%   |    33.6     |
| 75%   |    35.2     |
| max   |    42.2     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_28015070_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_28015070_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28015070_DensityKDE.png)


**TMX_CON - Station: 25025090 (8486 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 8486      |
| mean  |   33.5555 |
| std   |    1.8415 |
| min   |   26.4    |
| 25%   |   32.4    |
| 50%   |   33.6    |
| 75%   |   34.8    |
| max   |   40      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_25025090_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_25025090_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_25025090_DensityKDE.png)


**TMX_CON - Station: 25025002 (7701 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 7701       |
| mean  |   34.3217  |
| std   |    2.06657 |
| min   |   23       |
| 25%   |   33       |
| 50%   |   34.2     |
| 75%   |   35.6     |
| max   |   44       |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_25025002_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_25025002_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_25025002_DensityKDE.png)


**TMX_CON - Station: 29065020 (9406 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 9406       |
| mean  |   34.1372  |
| std   |    1.63127 |
| min   |   26       |
| 25%   |   33       |
| 50%   |   34.2     |
| 75%   |   35.2     |
| max   |   39.8     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_29065020_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_29065020_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_29065020_DensityKDE.png)


**TMX_CON - Station: 29065030 (10537 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 10537      |
| mean  |    33.3129 |
| std   |     1.4911 |
| min   |    24.8    |
| 25%   |    32.4    |
| 50%   |    33.4    |
| 75%   |    34.2    |
| max   |    38.6    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_29065030_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_29065030_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_29065030_DensityKDE.png)


**TMX_CON - Station: 25025300 (10066 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 10066      |
| mean  |    34.5617 |
| std   |     2.3698 |
| min   |    25.2    |
| 25%   |    32.8    |
| 50%   |    34.6    |
| 75%   |    36.2    |
| max   |    41.8    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_25025300_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_25025300_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_25025300_DensityKDE.png)


**TMX_CON - Station: 15015020 (8859 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 8859       |
| mean  |   33.0729  |
| std   |    1.48932 |
| min   |   25.4     |
| 25%   |   32.2     |
| 50%   |   33.2     |
| 75%   |   34.2     |
| max   |   38.4     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_15015020_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_15015020_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_15015020_DensityKDE.png)


**TMX_CON - Station: 29065010 (893 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 893       |
| mean  |  33.5259  |
| std   |   1.58034 |
| min   |  29.4     |
| 25%   |  32.4     |
| 50%   |  33.6     |
| 75%   |  34.6     |
| max   |  37.2     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMX_CON_29065010_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMX_CON_29065010_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_29065010_DensityKDE.png)


### Analysis from 1980 to 2021 for Etiqueta == "TMN_CON": 209823 (40.75%)


**TMN_CON - Station: 28025502 (12238 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 12238       |
| mean  |    23.8861  |
| std   |     1.27915 |
| min   |    18.4     |
| 25%   |    23       |
| 50%   |    23.8     |
| 75%   |    24.8     |
| max   |    28.6     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_28025502_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_28025502_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28025502_DensityKDE.png)


**TMN_CON - Station: 28025090 (11867 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 11867       |
| mean  |    22.4272  |
| std   |     1.67337 |
| min   |    15       |
| 25%   |    21.6     |
| 50%   |    22.8     |
| 75%   |    23.6     |
| max   |    27.4     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_28025090_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_28025090_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28025090_DensityKDE.png)


**TMN_CON - Station: 25025250 (12340 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 12340       |
| mean  |    22.3963  |
| std   |     1.63717 |
| min   |    17       |
| 25%   |    21.2     |
| 50%   |    22.4     |
| 75%   |    23.8     |
| max   |    27.1     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_25025250_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_25025250_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_25025250_DensityKDE.png)


**TMN_CON - Station: 28015030 (1404 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 1404       |
| mean  |   22.9291  |
| std   |    1.32774 |
| min   |   10       |
| 25%   |   22.2     |
| 50%   |   23       |
| 75%   |   23.8     |
| max   |   26.8     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_28015030_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_28015030_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28015030_DensityKDE.png)


**TMN_CON - Station: 25025330 (9275 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 9275      |
| mean  |   22.7791 |
| std   |    1.6933 |
| min   |   13.1    |
| 25%   |   21.8    |
| 50%   |   23      |
| 75%   |   24      |
| max   |   28.6    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_25025330_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_25025330_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_25025330_DensityKDE.png)


**TMN_CON - Station: 23215060 (1248 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 1248       |
| mean  |   23.6837  |
| std   |    1.20744 |
| min   |   16.6     |
| 25%   |   23       |
| 50%   |   23.8     |
| 75%   |   24.6     |
| max   |   26.8     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_23215060_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_23215060_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_23215060_DensityKDE.png)


**TMN_CON - Station: 28025070 (13818 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 13818       |
| mean  |    23.7666  |
| std   |     1.54724 |
| min   |    17.4     |
| 25%   |    22.8     |
| 50%   |    23.8     |
| 75%   |    25       |
| max   |    28.6     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_28025070_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_28025070_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28025070_DensityKDE.png)


**TMN_CON - Station: 28025020 (13452 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 13452       |
| mean  |    20.547   |
| std   |     1.73534 |
| min   |    12       |
| 25%   |    19.6     |
| 50%   |    20.8     |
| 75%   |    21.8     |
| max   |    26       |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_28025020_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_28025020_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28025020_DensityKDE.png)


**TMN_CON - Station: 28025040 (3231 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 3231       |
| mean  |   18.674   |
| std   |    2.11514 |
| min   |    8.4     |
| 25%   |   18       |
| 50%   |   19.2     |
| 75%   |   20       |
| max   |   27.4     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_28025040_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_28025040_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28025040_DensityKDE.png)


**TMN_CON - Station: 28025080 (7636 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 7636       |
| mean  |   21.7751  |
| std   |    1.87894 |
| min   |   15.2     |
| 25%   |   20.4     |
| 50%   |   22.2     |
| 75%   |   23.2     |
| max   |   27       |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_28025080_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_28025080_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28025080_DensityKDE.png)


**TMN_CON - Station: 28045020 (1052 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 1052       |
| mean  |   21.2974  |
| std   |    1.79272 |
| min   |   14.6     |
| 25%   |   20.2     |
| 50%   |   21.6     |
| 75%   |   22.6     |
| max   |   26.4     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_28045020_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_28045020_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28045020_DensityKDE.png)


**TMN_CON - Station: 28035020 (11824 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 11824       |
| mean  |    22.8005  |
| std   |     1.82844 |
| min   |    15.8     |
| 25%   |    21.8     |
| 50%   |    23       |
| 75%   |    24       |
| max   |    28.6     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_28035020_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_28035020_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28035020_DensityKDE.png)


**TMN_CON - Station: 28045040 (1274 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 1274       |
| mean  |   23.128   |
| std   |    1.26701 |
| min   |   14.6     |
| 25%   |   22.4     |
| 50%   |   23.2     |
| 75%   |   24       |
| max   |   26.6     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_28045040_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_28045040_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28045040_DensityKDE.png)


**TMN_CON - Station: 28035070 (42 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 42       |
| mean  | 22.0286  |
| std   |  1.01844 |
| min   | 20.6     |
| 25%   | 21.4     |
| 50%   | 21.8     |
| 75%   | 22.6     |
| max   | 25.6     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_28035070_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_28035070_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28035070_DensityKDE.png)


**TMN_CON - Station: 28035040 (13405 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 13405       |
| mean  |    24.269   |
| std   |     1.23846 |
| min   |    17.2     |
| 25%   |    23.4     |
| 50%   |    24.2     |
| 75%   |    25       |
| max   |    28.6     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_28035040_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_28035040_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28035040_DensityKDE.png)


**TMN_CON - Station: 28035010 (10557 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 10557       |
| mean  |    23.3278  |
| std   |     1.49337 |
| min   |    13.4     |
| 25%   |    22.6     |
| 50%   |    23.4     |
| 75%   |    24.2     |
| max   |    28.8     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_28035010_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_28035010_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28035010_DensityKDE.png)


**TMN_CON - Station: 15065040 (4949 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 4949       |
| mean  |   22.9664  |
| std   |    1.75384 |
| min   |   12.4     |
| 25%   |   22.2     |
| 50%   |   23.2     |
| 75%   |   24.2     |
| max   |   27.8     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_15065040_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_15065040_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_15065040_DensityKDE.png)


**TMN_CON - Station: 28015070 (12475 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 12475       |
| mean  |    22.34    |
| std   |     1.33165 |
| min   |    15.4     |
| 25%   |    21.5     |
| 50%   |    22.5     |
| 75%   |    23.2     |
| max   |    26.2     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_28015070_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_28015070_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28015070_DensityKDE.png)


**TMN_CON - Station: 25025002 (10733 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 10733       |
| mean  |    22.9428  |
| std   |     1.56303 |
| min   |    16.8     |
| 25%   |    22       |
| 50%   |    23       |
| 75%   |    24       |
| max   |    27.2     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_25025002_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_25025002_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_25025002_DensityKDE.png)


**TMN_CON - Station: 15015020 (9964 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 9964       |
| mean  |   22.1888  |
| std   |    1.60856 |
| min   |   16       |
| 25%   |   21.2     |
| 50%   |   22.4     |
| 75%   |   23.2     |
| max   |   26.8     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_15015020_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_15015020_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_15015020_DensityKDE.png)


**TMN_CON - Station: 25025090 (9774 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 9774       |
| mean  |   23.5651  |
| std   |    1.53376 |
| min   |   17       |
| 25%   |   22.6     |
| 50%   |   23.6     |
| 75%   |   24.8     |
| max   |   28       |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_25025090_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_25025090_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_25025090_DensityKDE.png)


**TMN_CON - Station: 29065020 (12983 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 12983       |
| mean  |    22.327   |
| std   |     1.85521 |
| min   |    14.2     |
| 25%   |    21.2     |
| 50%   |    22.6     |
| 75%   |    23.6     |
| max   |    27.4     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_29065020_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_29065020_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_29065020_DensityKDE.png)


**TMN_CON - Station: 29065030 (11526 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 11526       |
| mean  |    21.8104  |
| std   |     1.55983 |
| min   |    14       |
| 25%   |    20.8     |
| 50%   |    22       |
| 75%   |    23       |
| max   |    27       |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_29065030_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_29065030_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_29065030_DensityKDE.png)


**TMN_CON - Station: 25025300 (11693 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 11693       |
| mean  |    22.9902  |
| std   |     1.75271 |
| min   |    15.4     |
| 25%   |    22       |
| 50%   |    23.2     |
| 75%   |    24.2     |
| max   |    27.8     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_25025300_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_25025300_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_25025300_DensityKDE.png)


**TMN_CON - Station: 29065010 (1063 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 1063       |
| mean  |   21.3162  |
| std   |    1.60256 |
| min   |   15.2     |
| 25%   |   20.4     |
| 50%   |   21.4     |
| 75%   |   22.4     |
| max   |   25.2     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_TMN_CON_29065010_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_TMN_CON_29065010_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_29065010_DensityKDE.png)


### Analysis from 1980 to 2021 for Etiqueta == "EV_TT_D": 4821 (0.94%)


**EV_TT_D - Station: 29065130 (4821 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 4821     |
| mean  |  281.089 |
| std   |  625.398 |
| min   | -176     |
| 25%   |    0     |
| 50%   |    0     |
| 75%   |  139     |
| max   | 2529     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_EV_TT_D_29065130_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_EV_TT_D_29065130_Histogram.png)
![R.LTWB](Graph/Plot_EV_TT_D_29065130_DensityKDE.png)


### Analysis from 1980 to 2021 for Etiqueta == "Q_MEDIA_M": 21126 (4.1%)


**Q_MEDIA_M - Station: 25027400 (489 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 489      |
| mean  | 151.668  |
| std   |  70.7867 |
| min   |   4.846  |
| 25%   |  95.15   |
| 50%   | 151      |
| 75%   | 205      |
| max   | 328.7    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027400_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027400_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027400_DensityKDE.png)


**Q_MEDIA_M - Station: 25027360 (462 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  462     |
| mean  | 2790.92  |
| std   |  695.773 |
| min   | 1099.06  |
| 25%   | 2304.75  |
| 50%   | 2800.5   |
| 75%   | 3309     |
| max   | 4208.35  |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027360_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027360_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027360_DensityKDE.png)


**Q_MEDIA_M - Station: 25027620 (415 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 415      |
| mean  |  49.625  |
| std   |  38.9781 |
| min   |   1.309  |
| 25%   |  18.975  |
| 50%   |  38.6171 |
| 75%   |  72.32   |
| max   | 202.2    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027620_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027620_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027620_DensityKDE.png)


**Q_MEDIA_M - Station: 25027490 (504 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count |  504    |
| mean  | 3661.52 |
| std   | 1335.23 |
| min   | 1292    |
| 25%   | 2605    |
| 50%   | 3467    |
| 75%   | 4490.53 |
| max   | 7841.87 |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027490_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027490_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027490_DensityKDE.png)


**Q_MEDIA_M - Station: 25027390 (456 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count |  456    |
| mean  | 3334.22 |
| std   | 1006.61 |
| min   | 1250    |
| 25%   | 2557.75 |
| 50%   | 3251    |
| 75%   | 3985    |
| max   | 6532    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027390_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027390_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027390_DensityKDE.png)


**Q_MEDIA_M - Station: 25027330 (484 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count |  484    |
| mean  | 3977.16 |
| std   | 1256.45 |
| min   | 1171.66 |
| 25%   | 3003.75 |
| 50%   | 3845    |
| 75%   | 4853.25 |
| max   | 7464    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027330_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027330_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027330_DensityKDE.png)


**Q_MEDIA_M - Station: 25027410 (423 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count |  423    |
| mean  | 4282.86 |
| std   | 1514.27 |
| min   | 1507    |
| 25%   | 3054    |
| 50%   | 4174    |
| 75%   | 5356.16 |
| max   | 8177    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027410_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027410_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027410_DensityKDE.png)


**Q_MEDIA_M - Station: 25027320 (473 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  473     |
| mean  |  503.54  |
| std   |  278.127 |
| min   |   35.15  |
| 25%   |  288.8   |
| 50%   |  462.8   |
| 75%   |  681.7   |
| max   | 1489     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027320_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027320_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027320_DensityKDE.png)


**Q_MEDIA_M - Station: 25027420 (482 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count | 482     |
| mean  | 365.328 |
| std   | 206.827 |
| min   |   4.306 |
| 25%   | 197.85  |
| 50%   | 334.85  |
| 75%   | 521.858 |
| max   | 884.3   |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027420_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027420_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027420_DensityKDE.png)


**Q_MEDIA_M - Station: 25027630 (461 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count |  461     |
| mean  | 2922.8   |
| std   |  719.798 |
| min   |  894.8   |
| 25%   | 2348     |
| 50%   | 2849     |
| 75%   | 3513     |
| max   | 4625     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027630_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027630_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027630_DensityKDE.png)


**Q_MEDIA_M - Station: 28017120 (230 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 230       |
| mean  |  16.453   |
| std   |  13.6106  |
| min   |   2.48    |
| 25%   |   7.12875 |
| 50%   |  12.635   |
| 75%   |  20.425   |
| max   | 106.2     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_28017120_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_28017120_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017120_DensityKDE.png)


**Q_MEDIA_M - Station: 25027590 (339 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 339      |
| mean  |  53.8843 |
| std   |  39.6006 |
| min   |   0.723  |
| 25%   |  17.325  |
| 50%   |  44.15   |
| 75%   |  87.27   |
| max   | 158.1    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027590_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027590_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027590_DensityKDE.png)


**Q_MEDIA_M - Station: 28017150 (52 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 52       |
| mean  |  6.36198 |
| std   |  3.45506 |
| min   |  1.67986 |
| 25%   |  3.65216 |
| 50%   |  6.36845 |
| 75%   |  7.92197 |
| max   | 15.2573  |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_28017150_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_28017150_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017150_DensityKDE.png)


**Q_MEDIA_M - Station: 28027030 (439 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 439       |
| mean  |   4.1023  |
| std   |   6.57997 |
| min   |   0       |
| 25%   |   0.815   |
| 50%   |   2.055   |
| 75%   |   5.4085  |
| max   |  95.94    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_28027030_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_28027030_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027030_DensityKDE.png)


**Q_MEDIA_M - Station: 25027080 (449 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 449       |
| mean  |   4.61716 |
| std   |   7.4523  |
| min   |   0.018   |
| 25%   |   0.8775  |
| 50%   |   1.999   |
| 75%   |   4.948   |
| max   |  73.81    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027080_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027080_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027080_DensityKDE.png)


**Q_MEDIA_M - Station: 28027020 (399 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 399       |
| mean  |   2.40145 |
| std   |   2.89938 |
| min   |   0       |
| 25%   |   0.4485  |
| 50%   |   1.3     |
| 75%   |   3.4115  |
| max   |  17.66    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_28027020_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_28027020_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027020_DensityKDE.png)


**Q_MEDIA_M - Station: 28017110 (465 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 465       |
| mean  |   9.51238 |
| std   |  12.7092  |
| min   |   0.118   |
| 25%   |   3.361   |
| 50%   |   5.64    |
| 75%   |  10.0068  |
| max   | 116.79    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_28017110_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_28017110_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017110_DensityKDE.png)


**Q_MEDIA_M - Station: 25027890 (424 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 424       |
| mean  |   2.66422 |
| std   |   3.14918 |
| min   |   0.007   |
| 25%   |   0.5025  |
| 50%   |   1.33    |
| 75%   |   3.70275 |
| max   |  18.55    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027890_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027890_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027890_DensityKDE.png)


**Q_MEDIA_M - Station: 28017050 (263 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 263      |
| mean  |  20.0189 |
| std   |  28.2952 |
| min   |   3      |
| 25%   |   7.33   |
| 50%   |  13.44   |
| 75%   |  22.74   |
| max   | 252      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_28017050_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_28017050_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017050_DensityKDE.png)


**Q_MEDIA_M - Station: 28027040 (412 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 412         |
| mean  |   3.04977   |
| std   |   4.03069   |
| min   |   0.0190909 |
| 25%   |   0.67875   |
| 50%   |   1.585     |
| 75%   |   3.8395    |
| max   |  44         |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_28027040_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_28027040_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027040_DensityKDE.png)


**Q_MEDIA_M - Station: 28027050 (349 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 349      |
| mean  |  11.311  |
| std   |  22.5481 |
| min   |   0.161  |
| 25%   |   1.625  |
| 50%   |   4.267  |
| 75%   |  10.11   |
| max   | 294.1    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_28027050_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_28027050_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027050_DensityKDE.png)


**Q_MEDIA_M - Station: 28037060 (482 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 482       |
| mean  |   1.77203 |
| std   |   2.00638 |
| min   |   0.03    |
| 25%   |   0.5315  |
| 50%   |   1.04342 |
| 75%   |   2.36855 |
| max   |  17.87    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_28037060_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_28037060_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037060_DensityKDE.png)


**Q_MEDIA_M - Station: 28037020 (362 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 362       |
| mean  |   2.65542 |
| std   |   3.09609 |
| min   |   0       |
| 25%   |   0.444   |
| 50%   |   1.469   |
| 75%   |   3.7135  |
| max   |  20.24    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_28037020_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_28037020_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037020_DensityKDE.png)


**Q_MEDIA_M - Station: 28027160 (372 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 372       |
| mean  |   8.80949 |
| std   |   8.92743 |
| min   |   0.013   |
| 25%   |   2.68175 |
| 50%   |   6.026   |
| 75%   |  12.655   |
| max   |  69.15    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_28027160_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_28027160_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027160_DensityKDE.png)


**Q_MEDIA_M - Station: 28037040 (474 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 474        |
| mean  |   1.99652  |
| std   |   2.4448   |
| min   |   0.01     |
| 25%   |   0.367828 |
| 50%   |   1.01634  |
| 75%   |   2.6945   |
| max   |  13.28     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_28037040_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_28037040_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037040_DensityKDE.png)


**Q_MEDIA_M - Station: 28047020 (474 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 474        |
| mean  |   1.28277  |
| std   |   0.950413 |
| min   |   0.244    |
| 25%   |   0.658511 |
| 50%   |   1.03365  |
| 75%   |   1.539    |
| max   |   6.531    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_28047020_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_28047020_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047020_DensityKDE.png)


**Q_MEDIA_M - Station: 28037010 (437 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 437       |
| mean  |   3.03674 |
| std   |   4.55045 |
| min   |   0.009   |
| 25%   |   0.34    |
| 50%   |   1.402   |
| 75%   |   3.684   |
| max   |  30.45    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_28037010_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_28037010_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037010_DensityKDE.png)


**Q_MEDIA_M - Station: 28037090 (410 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 410         |
| mean  |  56.379     |
| std   |  51.3416    |
| min   |   0.0106789 |
| 25%   |  12.65      |
| 50%   |  41.18      |
| 75%   |  90.1875    |
| max   | 209.741     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_28037090_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_28037090_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037090_DensityKDE.png)


**Q_MEDIA_M - Station: 28037130 (422 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 422         |
| mean  |   4.41579   |
| std   |   5.69845   |
| min   |   0.0140806 |
| 25%   |   0.944     |
| 50%   |   2.01      |
| 75%   |   5.36175   |
| max   |  35.46      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_28037130_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_28037130_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037130_DensityKDE.png)


**Q_MEDIA_M - Station: 28037030 (474 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 474      |
| mean  |  33.6422 |
| std   |  38.3711 |
| min   |   1.221  |
| 25%   |   7.753  |
| 50%   |  20.465  |
| 75%   |  41.5703 |
| max   | 232.8    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_28037030_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_28037030_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037030_DensityKDE.png)


**Q_MEDIA_M - Station: 28047080 (96 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 96       |
| mean  | 16.3821  |
| std   |  6.47651 |
| min   |  6.365   |
| 25%   | 11.7875  |
| 50%   | 15.865   |
| 75%   | 18.8225  |
| max   | 47.38    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_28047080_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_28047080_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047080_DensityKDE.png)


**Q_MEDIA_M - Station: 28047040 (247 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 247       |
| mean  |   2.64994 |
| std   |   2.25132 |
| min   |   0.25    |
| 25%   |   1.2385  |
| 50%   |   1.997   |
| 75%   |   3.318   |
| max   |  13.65    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_28047040_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_28047040_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047040_DensityKDE.png)


**Q_MEDIA_M - Station: 15067210 (28 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 28       |
| mean  |  5.99268 |
| std   |  4.02808 |
| min   |  1.51655 |
| 25%   |  3.0025  |
| 50%   |  4.716   |
| 75%   |  8.31065 |
| max   | 17.14    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_15067210_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_15067210_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067210_DensityKDE.png)


**Q_MEDIA_M - Station: 15067020 (328 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 328       |
| mean  |   6.88666 |
| std   |   4.37317 |
| min   |   1.114   |
| 25%   |   3.963   |
| 50%   |   5.5075  |
| 75%   |   8.558   |
| max   |  27.85    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_15067020_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_15067020_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067020_DensityKDE.png)


**Q_MEDIA_M - Station: 28017080 (465 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 465         |
| mean  |   2.49671   |
| std   |   3.54568   |
| min   |   0.0238819 |
| 25%   |   0.606     |
| 50%   |   1.13      |
| 75%   |   2.725     |
| max   |  22.94      |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_28017080_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_28017080_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017080_DensityKDE.png)


**Q_MEDIA_M - Station: 15067200 (115 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 115       |
| mean  |   7.45147 |
| std   |   7.71757 |
| min   |   1.019   |
| 25%   |   2.61302 |
| 50%   |   4.30484 |
| 75%   |   9.2741  |
| max   |  38.9706  |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_15067200_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_15067200_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067200_DensityKDE.png)


**Q_MEDIA_M - Station: 15067080 (291 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 291        |
| mean  |   2.17867  |
| std   |   3.43166  |
| min   |   0.124    |
| 25%   |   0.575597 |
| 50%   |   0.977419 |
| 75%   |   2.45689  |
| max   |  31.85     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_15067080_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_15067080_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067080_DensityKDE.png)


**Q_MEDIA_M - Station: 15067130 (388 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 388         |
| mean  |   0.107405  |
| std   |   0.156455  |
| min   |   0.002     |
| 25%   |   0.016     |
| 50%   |   0.0363357 |
| 75%   |   0.125     |
| max   |   0.936     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_15067130_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_15067130_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067130_DensityKDE.png)


**Q_MEDIA_M - Station: 15067150 (148 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |       Valor |
|:------|------------:|
| count | 148         |
| mean  |   5.06216   |
| std   |   5.59392   |
| min   |   0.0811156 |
| 25%   |   1.54901   |
| 50%   |   2.6945    |
| 75%   |   6.2928    |
| max   |  25.5854    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_15067150_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_15067150_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067150_DensityKDE.png)


**Q_MEDIA_M - Station: 15067170 (156 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 156       |
| mean  |   9.50479 |
| std   |  12.6864  |
| min   |   0.516   |
| 25%   |   2.53293 |
| 50%   |   4.73477 |
| 75%   |  10.7563  |
| max   |  71.51    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_15067170_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_15067170_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067170_DensityKDE.png)


**Q_MEDIA_M - Station: 28017140 (41 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count |    41     |
| mean  | 18933.9   |
| std   | 23607.6   |
| min   |     0.562 |
| 25%   |     1.504 |
| 50%   |     3.513 |
| 75%   | 32296     |
| max   | 76114     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_28017140_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_28017140_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017140_DensityKDE.png)


**Q_MEDIA_M - Station: 28047010 (412 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 412       |
| mean  |  16.1567  |
| std   |   8.49034 |
| min   |   0.625   |
| 25%   |  11.3293  |
| 50%   |  14.845   |
| 75%   |  19.2775  |
| max   |  65.28    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_28047010_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_28047010_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047010_DensityKDE.png)


**Q_MEDIA_M - Station: 29067050 (393 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 393       |
| mean  |  12.6539  |
| std   |   9.55028 |
| min   |   1.572   |
| 25%   |   6.14022 |
| 50%   |  10.8     |
| 75%   |  16.3514  |
| max   |  94.89    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067050_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067050_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067050_DensityKDE.png)


**Q_MEDIA_M - Station: 25027020 (504 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |   Valor |
|:------|--------:|
| count |  504    |
| mean  | 4075.69 |
| std   | 1368.36 |
| min   | 1245.65 |
| 25%   | 3091.5  |
| 50%   | 3956.67 |
| 75%   | 4960.75 |
| max   | 9171    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027020_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027020_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027020_DensityKDE.png)


**Q_MEDIA_M - Station: 29067120 (444 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 444      |
| mean  |  28.2809 |
| std   |  18.1198 |
| min   |   4.831  |
| 25%   |  15.86   |
| 50%   |  24.445  |
| 75%   |  35.5075 |
| max   | 140.9    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067120_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067120_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067120_DensityKDE.png)


**Q_MEDIA_M - Station: 28047050 (451 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 451      |
| mean  |  13.5702 |
| std   |  13.6383 |
| min   |   0.127  |
| 25%   |   2.9885 |
| 50%   |   8.391  |
| 75%   |  20.35   |
| max   |  63.14   |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_28047050_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_28047050_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047050_DensityKDE.png)


**Q_MEDIA_M - Station: 29067060 (257 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 257      |
| mean  |  24.8152 |
| std   |  12.422  |
| min   |   4.068  |
| 25%   |  15.44   |
| 50%   |  22.37   |
| 75%   |  32.55   |
| max   |  88.67   |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067060_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067060_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067060_DensityKDE.png)


**Q_MEDIA_M - Station: 29067070 (426 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 426       |
| mean  |  13.4932  |
| std   |   9.06389 |
| min   |   2.06    |
| 25%   |   6.24475 |
| 50%   |  11.37    |
| 75%   |  18.18    |
| max   |  59.47    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067070_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067070_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067070_DensityKDE.png)


**Q_MEDIA_M - Station: 29067040 (446 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 446       |
| mean  |   1.91476 |
| std   |   1.48993 |
| min   |   0.106   |
| 25%   |   0.78925 |
| 50%   |   1.439   |
| 75%   |   2.73225 |
| max   |   7.354   |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067040_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067040_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067040_DensityKDE.png)


**Q_MEDIA_M - Station: 29067010 (448 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 448       |
| mean  |  17.5998  |
| std   |  11.6086  |
| min   |   2.966   |
| 25%   |   9.71225 |
| 50%   |  15.525   |
| 75%   |  21.6225  |
| max   | 119       |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067010_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067010_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067010_DensityKDE.png)


**Q_MEDIA_M - Station: 29067150 (481 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |      Valor |
|:------|-----------:|
| count | 481        |
| mean  |  15.9357   |
| std   |   9.25158  |
| min   |   0.479067 |
| 25%   |   8.836    |
| 50%   |  14.42     |
| 75%   |  21.58     |
| max   |  55.25     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067150_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067150_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067150_DensityKDE.png)


**Q_MEDIA_M - Station: 29067130 (476 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 476       |
| mean  |  17.6187  |
| std   |  14.6576  |
| min   |   1.95487 |
| 25%   |   7.617   |
| 50%   |  13.59    |
| 75%   |  22.0241  |
| max   |  97.6     |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067130_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067130_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067130_DensityKDE.png)


**Q_MEDIA_M - Station: 29067160 (397 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |     Valor |
|:------|----------:|
| count | 397       |
| mean  |   7.71179 |
| std   |   8.21195 |
| min   |   0.546   |
| 25%   |   2.326   |
| 50%   |   5.185   |
| 75%   |  10.81    |
| max   |  71.7432  |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067160_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067160_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067160_DensityKDE.png)


**Q_MEDIA_M - Station: 16067020 (244 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 244      |
| mean  | 115.375  |
| std   |  66.9092 |
| min   |  28.67   |
| 25%   |  64.19   |
| 50%   |  95.225  |
| 75%   | 154.075  |
| max   | 340.3    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_16067020_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_16067020_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16067020_DensityKDE.png)


**Q_MEDIA_M - Station: 16037040 (387 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 387      |
| mean  |  21.8745 |
| std   |  17.4017 |
| min   |   3.445  |
| 25%   |  11.475  |
| 50%   |  16.64   |
| 75%   |  27.555  |
| max   | 208.9    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_16037040_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_16037040_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16037040_DensityKDE.png)


**Q_MEDIA_M - Station: 16047020 (283 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 283      |
| mean  |  54.4958 |
| std   |  36.5487 |
| min   |  10.16   |
| 25%   |  29.87   |
| 50%   |  42.16   |
| 75%   |  67.44   |
| max   | 237.6    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_16047020_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_16047020_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16047020_DensityKDE.png)


**Q_MEDIA_M - Station: 16067010 (397 rec.)**

<div align="center">

Statistics table

</div>


<div align="center">

|       |    Valor |
|:------|---------:|
| count | 397      |
| mean  | 249.957  |
| std   | 137.419  |
| min   |  43.6941 |
| 25%   | 134.3    |
| 50%   | 225.4    |
| 75%   | 335.5    |
| max   | 914.8    |

</div>


<div align="center">

![R.LTWB](Graph/Plot_Q_MEDIA_M_16067010_TimeSerie.png)

</div>

![R.LTWB](Graph/Plot_Q_MEDIA_M_16067010_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16067010_DensityKDE.png)
