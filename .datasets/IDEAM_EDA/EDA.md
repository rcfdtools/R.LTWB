## Exploración y análisis de series - EDA - Representación gráfica

* Archivo de resultados: D:/R.LTWB/.datasets/IDEAM_EDA/EDA.md
* Fecha y hora de inicio de ejecución: 2022-10-27 17:01:01.250626
* Python versión: 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)]
* Python rutas: ['D:\\R.LTWB\\.src', 'D:\\R.LTWB', 'D:\\R.GISPython.wiki', 'D:\\R.GISPython', 'D:\\R.HydroTools']
* matplotlib versión: 3.6.0
* Print table samples: True
* Start year: 1980
* End year: 2021
* Encuentra este script en https://github.com/rcfdtools/R.LTWB/tree/main/Section03/EDA
* Cláusulas y condiciones de uso en https://github.com/rcfdtools/R.LTWB/blob/main/LICENSE.md
* Créditos: r.cfdtools@gmail.com


### General dataframe information with 514927 IDEAM records

Dataframe records head sample

|    |   CodigoEstacion | NombreEstacion                                  |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   | Fecha               |   Valor |   Grado |   Calificador |   NivelAprobacion |
|---:|-----------------:|:------------------------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|:--------------------|--------:|--------:|--------------:|------------------:|
|  0 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 1987-12-01 00:00:00 |   202   |      50 |           nan |               900 |
|  1 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 1988-01-01 00:00:00 |     0   |      50 |           nan |               900 |
|  2 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 1988-02-01 00:00:00 |    18.9 |      50 |           nan |               900 |

Dataframe records tail sample

|        |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio    | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   | Fecha               |   Valor |   Grado |   Calificador |   NivelAprobacion |
|-------:|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|:--------------------|--------:|--------:|--------------:|------------------:|
| 514924 |         25021090 | SANTA ROSA [25021090] |   9.09333 |   -74.3139 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Fernando | 1974-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 2020-12-01 00:00:00 |      90 |      50 |           nan |               900 |
| 514925 |         25021090 | SANTA ROSA [25021090] |   9.09333 |   -74.3139 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Fernando | 1974-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 2021-01-01 00:00:00 |       0 |      50 |           nan |               900 |
| 514926 |         25021090 | SANTA ROSA [25021090] |   9.09333 |   -74.3139 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Fernando | 1974-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      | 2021-02-01 00:00:00 |       0 |      50 |           nan |               900 |


### Analysis from 1980 to 2021 for Precipitación total mensual (Etiqueta == "PTPM_TT_M"): 55363 (10.75%)

Pivot table: [Pivot_PTPM_TT_M.csv](Pivot_PTPM_TT_M.csv)
![R.LTWB](Graph/Plot_PTPM_TT_M_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] (339 rec.)**

</div>

Latitude: 8.954222

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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                                  |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1987-12-01 00:00:00 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |   202   |      50 |           nan |               900 |
| 1988-01-01 00:00:00 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     0   |      50 |           nan |               900 |
| 1988-02-01 00:00:00 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    18.9 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25025330_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025330_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025330_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025330_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: GLORIA LA [23210020] (297 rec.)**

</div>

Latitude: 8.630556

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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                          | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:---------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1995-05-01 00:00:00 |         23210020 | GLORIA LA [23210020] |   8.63056 |   -73.8042 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Cesar          | La Gloria   | 1995-05-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     183 |       4 |           nan |               900 |
| 1995-06-01 00:00:00 |         23210020 | GLORIA LA [23210020] |   8.63056 |   -73.8042 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Cesar          | La Gloria   | 1995-05-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     211 |      50 |           nan |               900 |
| 1995-07-01 00:00:00 |         23210020 | GLORIA LA [23210020] |   8.63056 |   -73.8042 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Cesar          | La Gloria   | 1995-05-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     257 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_23210020_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_23210020_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_23210020_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_23210020_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: LA GLORIA [23215060] (146 rec.)**

</div>

Latitude: 8.615278

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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                          | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:---------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1983-10-01 00:00:00 |         23215060 | LA GLORIA [23215060] |   8.61528 |   -73.8006 |        35 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Cesar          | La Gloria   | 1995-05-15 00:00:00 | 2018-06-19 10:35:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |   126.2 |      50 |           nan |               900 |
| 1983-11-01 00:00:00 |         23215060 | LA GLORIA [23215060] |   8.61528 |   -73.8006 |        35 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Cesar          | La Gloria   | 1995-05-15 00:00:00 | 2018-06-19 10:35:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |   114   |      50 |           nan |               900 |
| 1983-12-01 00:00:00 |         23215060 | LA GLORIA [23215060] |   8.61528 |   -73.8006 |        35 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Cesar          | La Gloria   | 1995-05-15 00:00:00 | 2018-06-19 10:35:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    40.8 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_23215060_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_23215060_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_23215060_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_23215060_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: MATA LA [23215050] (467 rec.)**

</div>

Latitude: 8.614444

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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                          | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:---------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         23215050 | MATA LA [23215050] |   8.61444 |   -73.6364 |       163 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Cesar          | La Gloria   | 1983-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      50 |       4 |           nan |               900 |
| 1980-02-01 00:00:00 |         23215050 | MATA LA [23215050] |   8.61444 |   -73.6364 |       163 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Cesar          | La Gloria   | 1983-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      14 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         23215050 | MATA LA [23215050] |   8.61444 |   -73.6364 |       163 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Cesar          | La Gloria   | 1983-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       9 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_23215050_TimeSerie.png)
