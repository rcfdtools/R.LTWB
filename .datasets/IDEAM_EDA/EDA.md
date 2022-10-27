## Exploración y análisis de series - EDA - Representación gráfica

* Archivo de resultados: D:/R.LTWB/.datasets/IDEAM_EDA/EDA.md
* Fecha y hora de inicio de ejecución: 2022-10-27 16:31:51.679154
* Python versión: 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)]
* Python rutas: ['D:\\R.LTWB\\.src', 'D:\\R.LTWB', 'D:\\R.GISPython.wiki', 'D:\\R.GISPython', 'D:\\R.HydroTools']
* matplotlib versión: 3.6.0
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


### Analysis from 1980 to 2021 for Etiqueta == "PTPM_TT_M": 55363 (10.75%)

Pivot table: [Pivot_PTPM_TT_M.csv](Pivot_PTPM_TT_M.csv)
![R.LTWB](Graph/Plot_PTPM_TT_M_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25025330 (339 rec.)**

</div>


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



**PTPM_TT_M - Station: 23210020 (297 rec.)**

</div>


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



**PTPM_TT_M - Station: 23215060 (146 rec.)**

</div>


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



**PTPM_TT_M - Station: 23215050 (467 rec.)**

</div>


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
![R.LTWB](Graph/Plot_PTPM_TT_M_23215050_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_23215050_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_23215050_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25020670 (466 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020670 | RAYA LA [25020670] |   9.05028 |   -73.5597 |       500 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1972-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25020670 | RAYA LA [25020670] |   9.05028 |   -73.5597 |       500 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1972-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       5 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25020670 | RAYA LA [25020670] |   9.05028 |   -73.5597 |       500 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1972-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25020670_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020670_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020670_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020670_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25021640 (443 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1984-12-01 00:00:00 |         25021640 | SANTA ISABEL [25021640] |   8.71275 |   -73.7026 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pelaya      | 1984-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     0   |      50 |           nan |               900 |
| 1985-01-01 00:00:00 |         25021640 | SANTA ISABEL [25021640] |   8.71275 |   -73.7026 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pelaya      | 1984-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     0.8 |      50 |           nan |               900 |
| 1985-02-01 00:00:00 |         25021640 | SANTA ISABEL [25021640] |   8.71275 |   -73.7026 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pelaya      | 1984-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     2.8 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25021640_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021640_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021640_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021640_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25021590 (206 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion             |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25021590 | TAMALAMEQUE D C [25021590] |   8.86667 |   -73.8167 |        33 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Tamalameque | 1979-11-15 00:00:00 | 1998-06-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25021590 | TAMALAMEQUE D C [25021590] |   8.86667 |   -73.8167 |        33 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Tamalameque | 1979-11-15 00:00:00 | 1998-06-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      24 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25021590 | TAMALAMEQUE D C [25021590] |   8.86667 |   -73.8167 |        33 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Tamalameque | 1979-11-15 00:00:00 | 1998-06-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25021590_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021590_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021590_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021590_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25020090 (501 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020090 | TAMALAMEQUE [25020090] |   8.86039 |   -73.8154 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Tamalameque | 1960-02-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25020090 | TAMALAMEQUE [25020090] |   8.86039 |   -73.8154 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Tamalameque | 1960-02-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      24 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25020090 | TAMALAMEQUE [25020090] |   8.86039 |   -73.8154 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Tamalameque | 1960-02-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25020090_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020090_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020090_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020090_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25020650 (436 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020650 | TERROR EL HACIENDA [25020650] |   8.93878 |   -73.5602 |       250 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chimichagua | 1972-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      11 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25020650 | TERROR EL HACIENDA [25020650] |   8.93878 |   -73.5602 |       250 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chimichagua | 1972-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      38 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25020650 | TERROR EL HACIENDA [25020650] |   8.93878 |   -73.5602 |       250 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chimichagua | 1972-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25020650_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020650_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020650_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020650_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25020660 (502 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020660 | ZAPATOZA [25020660] |   9.00975 |    -73.754 |        90 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Curumaní    | 1972-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       1 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25020660 | ZAPATOZA [25020660] |   9.00975 |    -73.754 |        90 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Curumaní    | 1972-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      42 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25020660 | ZAPATOZA [25020660] |   9.00975 |    -73.754 |        90 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Curumaní    | 1972-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       2 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25020660_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020660_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020660_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020660_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28040150 (466 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040150 | BELLAVISTA [28040150] |   10.3081 |   -74.0392 |       140 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Algarrobo   | 1963-02-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       9 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28040150 | BELLAVISTA [28040150] |   10.3081 |   -74.0392 |       140 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Algarrobo   | 1963-02-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      56 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28040150 | BELLAVISTA [28040150] |   10.3081 |   -74.0392 |       140 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Algarrobo   | 1963-02-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28040150_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040150_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040150_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040150_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28040360 (503 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio             | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040360 | CABANA LA HACIENDA [28040360] |     9.861 |   -74.0767 |       100 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ariguaní (El Dificil) | 1979-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      10 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28040360 | CABANA LA HACIENDA [28040360] |     9.861 |   -74.0767 |       100 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ariguaní (El Dificil) | 1979-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      10 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28040360 | CABANA LA HACIENDA [28040360] |     9.861 |   -74.0767 |       100 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ariguaní (El Dificil) | 1979-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28040360_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040360_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040360_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040360_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060150 (488 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060150 | DESTINO EL [29060150] |   10.5737 |   -74.2241 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1967-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060150 | DESTINO EL [29060150] |   10.5737 |   -74.2241 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1967-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29060150 | DESTINO EL [29060150] |   10.5737 |   -74.2241 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1967-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060150_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060150_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060150_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060150_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060560 (442 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1984-12-01 00:00:00 |         29060560 | DONA MARIA [29060560] |   10.3844 |   -74.1779 |        50 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Fundación   | 1984-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1985-01-01 00:00:00 |         29060560 | DONA MARIA [29060560] |   10.3844 |   -74.1779 |        50 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Fundación   | 1984-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1985-02-01 00:00:00 |         29060560 | DONA MARIA [29060560] |   10.3844 |   -74.1779 |        50 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Fundación   | 1984-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060560_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060560_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060560_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060560_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060040 (499 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060040 | FUNDACION [29060040] |   10.5244 |   -74.1822 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Fundación   | 1958-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      15 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060040 | FUNDACION [29060040] |   10.5244 |   -74.1822 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Fundación   | 1958-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       5 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29060040 | FUNDACION [29060040] |   10.5244 |   -74.1822 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Fundación   | 1958-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060040_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060040_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060040_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060040_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060200 (483 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060200 | MARIA LA [29060200] |   10.5407 |    -74.187 |        30 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Aracataca   | 1974-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060200 | MARIA LA [29060200] |   10.5407 |    -74.187 |        30 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Aracataca   | 1974-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29060200 | MARIA LA [29060200] |   10.5407 |    -74.187 |        30 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Aracataca   | 1974-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060200_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060200_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060200_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060200_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28040100 (493 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040100 | MONTERRUBIO [28040100] |   10.2337 |   -74.2733 |       100 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Pivijai     | 1963-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      83 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28040100 | MONTERRUBIO [28040100] |   10.2337 |   -74.2733 |       100 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Pivijai     | 1963-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       8 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28040100 | MONTERRUBIO [28040100] |   10.2337 |   -74.2733 |       100 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Pivijai     | 1963-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28040100_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040100_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040100_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040100_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25021630 (460 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1982-07-01 00:00:00 |         25021630 | NUEVA GRANADA [25021630] |   9.80175 |   -74.3886 |       110 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Nueva Granada | 1982-06-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     123 |      50 |           nan |               900 |
| 1982-08-01 00:00:00 |         25021630 | NUEVA GRANADA [25021630] |   9.80175 |   -74.3886 |       110 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Nueva Granada | 1982-06-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     229 |      50 |           nan |               900 |
| 1982-09-01 00:00:00 |         25021630 | NUEVA GRANADA [25021630] |   9.80175 |   -74.3886 |       110 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Nueva Granada | 1982-06-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     187 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25021630_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021630_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021630_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021630_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28040140 (484 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio            | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:---------------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040140 | SAN ANGEL [28040140] |   10.0331 |   -74.2126 |       140 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Sabanas De San Ángel | 1963-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       6 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28040140 | SAN ANGEL [28040140] |   10.0331 |   -74.2126 |       140 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Sabanas De San Ángel | 1963-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      38 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28040140 | SAN ANGEL [28040140] |   10.0331 |   -74.2126 |       140 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Sabanas De San Ángel | 1963-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      25 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28040140_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040140_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040140_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040140_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060100 (504 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060100 | SANTA ROSA DE LIMA [29060100] |   10.4027 |    -74.108 |        75 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Fundación   | 1975-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      75 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060100 | SANTA ROSA DE LIMA [29060100] |   10.4027 |    -74.108 |        75 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Fundación   | 1975-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29060100 | SANTA ROSA DE LIMA [29060100] |   10.4027 |    -74.108 |        75 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Fundación   | 1975-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060100_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060100_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060100_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060100_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060350 (461 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion    |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060350 | BAYANO [29060350] |   10.6312 |   -74.2986 |        30 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1975-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060350 | BAYANO [29060350] |   10.6312 |   -74.2986 |        30 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1975-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29060350 | BAYANO [29060350] |   10.6312 |   -74.2986 |        30 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1975-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060350_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060350_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060350_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060350_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060030 (503 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060030 | BONGO EL [29060030] |   10.6488 |   -74.3755 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1975-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060030 | BONGO EL [29060030] |   10.6488 |   -74.3755 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1975-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29060030 | BONGO EL [29060030] |   10.6488 |   -74.3755 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1975-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060030_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060030_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060030_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060030_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060140 (503 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060140 | CARMEN EL [29060140] |   10.6755 |   -74.2064 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      14 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060140 | CARMEN EL [29060140] |   10.6755 |   -74.2064 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29060140 | CARMEN EL [29060140] |   10.6755 |   -74.2064 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060140_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060140_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060140_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060140_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060060 (492 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060060 | CENIZO EL [29060060] |   10.6516 |   -74.0732 |       450 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Aracataca   | 1959-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       8 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060060 | CENIZO EL [29060060] |   10.6516 |   -74.0732 |       450 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Aracataca   | 1959-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      15 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29060060 | CENIZO EL [29060060] |   10.6516 |   -74.0732 |       450 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Aracataca   | 1959-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       4 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060060_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060060_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060060_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060060_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060190 (420 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060190 | FLORIDA LA [29060190] |   10.6106 |   -74.2554 |        26 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1973-04-15 00:00:00 | 2019-02-07 11:43:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       6 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060190 | FLORIDA LA [29060190] |   10.6106 |   -74.2554 |        26 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1973-04-15 00:00:00 | 2019-02-07 11:43:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29060190 | FLORIDA LA [29060190] |   10.6106 |   -74.2554 |        26 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1973-04-15 00:00:00 | 2019-02-07 11:43:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060190_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060190_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060190_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060190_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060170 (503 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060170 | GAVILAN [29060170] |   10.6804 |   -74.3307 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1967-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060170 | GAVILAN [29060170] |   10.6804 |   -74.3307 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1967-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29060170 | GAVILAN [29060170] |   10.6804 |   -74.3307 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1967-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060170_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060170_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060170_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060170_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29065020 (490 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29065020 | PADELMA [29065020] |   10.7211 |   -74.1997 |        20 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     3.3 |       4 |           nan |               900 |
| 1980-02-01 00:00:00 |         29065020 | PADELMA [29065020] |   10.7211 |   -74.1997 |        20 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     0   |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29065020 | PADELMA [29065020] |   10.7211 |   -74.1997 |        20 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     0   |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29065020_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29065020_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29065020_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29065020_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060270 (501 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060270 | PALO ALTO [29060270] |   10.7225 |   -74.2719 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Puebloviejo | 1967-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060270 | PALO ALTO [29060270] |   10.7225 |   -74.2719 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Puebloviejo | 1967-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29060270 | PALO ALTO [29060270] |   10.7225 |   -74.2719 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Puebloviejo | 1967-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060270_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060270_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060270_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060270_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060240 (441 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060240 | UNION LA [29060240] |   10.7066 |   -74.2236 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-01-15 00:00:00 | 2019-02-07 11:43:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060240 | UNION LA [29060240] |   10.7066 |   -74.2236 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-01-15 00:00:00 | 2019-02-07 11:43:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29060240 | UNION LA [29060240] |   10.7066 |   -74.2236 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-01-15 00:00:00 | 2019-02-07 11:43:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060240_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060240_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060240_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060240_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29065010 (122 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion    |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29065010 | ZACAPA [29065010] |   10.5833 |     -74.25 |        30 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1967-07-15 00:00:00 | 1990-04-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |       4 |           nan |               900 |
| 1980-02-01 00:00:00 |         29065010 | ZACAPA [29065010] |   10.5833 |     -74.25 |        30 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1967-07-15 00:00:00 | 1990-04-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       1 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29065010 | ZACAPA [29065010] |   10.5833 |     -74.25 |        30 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1967-07-15 00:00:00 | 1990-04-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29065010_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29065010_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29065010_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29065010_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060180 (500 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060180 | ESPERANZA LA [29060180] |   10.7425 |   -74.3063 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Puebloviejo | 1975-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060180 | ESPERANZA LA [29060180] |   10.7425 |   -74.3063 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Puebloviejo | 1975-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29060180 | ESPERANZA LA [29060180] |   10.7425 |   -74.3063 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Puebloviejo | 1975-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060180_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060180_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060180_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060180_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060340 (490 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060340 | PALMOR EL [29060340] |   10.7734 |   -74.0256 |      1200 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1975-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      67 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060340 | PALMOR EL [29060340] |   10.7734 |   -74.0256 |      1200 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1975-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      15 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29060340 | PALMOR EL [29060340] |   10.7734 |   -74.0256 |      1200 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1975-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060340_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060340_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060340_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060340_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060330 (252 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1990-01-01 00:00:00 |         29060330 | PLAYA LA [29060330] |    10.762 |   -74.1205 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1990-01-15 00:00:00 | 2019-02-07 11:32:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |       4 |           nan |               900 |
| 1990-02-01 00:00:00 |         29060330 | PLAYA LA [29060330] |    10.762 |   -74.1205 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1990-01-15 00:00:00 | 2019-02-07 11:32:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      18 |      50 |           nan |               900 |
| 1990-03-01 00:00:00 |         29060330 | PLAYA LA [29060330] |    10.762 |   -74.1205 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1990-01-15 00:00:00 | 2019-02-07 11:32:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       3 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060330_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060330_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060330_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060330_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060220 (258 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060220 | POLY LA [29060220] |   10.8167 |   -74.1833 |        24 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1972-01-15 00:00:00 | 2002-02-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060220 | POLY LA [29060220] |   10.8167 |   -74.1833 |        24 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1972-01-15 00:00:00 | 2002-02-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       3 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29060220 | POLY LA [29060220] |   10.8167 |   -74.1833 |        24 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1972-01-15 00:00:00 | 2002-02-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060220_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060220_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060220_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060220_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29065030 (412 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29065030 | PRADO SEVILLA [29065030] |   10.7642 |   -74.1547 |        18 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1970-07-15 00:00:00 | 2019-02-07 11:32:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29065030 | PRADO SEVILLA [29065030] |   10.7642 |   -74.1547 |        18 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1970-07-15 00:00:00 | 2019-02-07 11:32:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29065030 | PRADO SEVILLA [29065030] |   10.7642 |   -74.1547 |        18 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1970-07-15 00:00:00 | 2019-02-07 11:32:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29065030_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29065030_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29065030_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29065030_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060250 (499 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060250 | PROYECTOS LOS [29060250] |   10.7367 |   -74.2371 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060250 | PROYECTOS LOS [29060250] |   10.7367 |   -74.2371 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29060250 | PROYECTOS LOS [29060250] |   10.7367 |   -74.2371 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060250_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060250_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060250_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060250_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060550 (360 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1984-04-01 00:00:00 |         29060550 | RUBY EL [29060550] |   10.8451 |   -74.1882 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1984-03-15 00:00:00 | 2019-02-07 11:33:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       4 |      50 |           nan |               900 |
| 1984-05-01 00:00:00 |         29060550 | RUBY EL [29060550] |   10.8451 |   -74.1882 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1984-03-15 00:00:00 | 2019-02-07 11:33:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     135 |      50 |           nan |               900 |
| 1984-06-01 00:00:00 |         29060550 | RUBY EL [29060550] |   10.8451 |   -74.1882 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1984-03-15 00:00:00 | 2019-02-07 11:33:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      96 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060550_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060550_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060550_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060550_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060290 (249 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060290 | SAN JUAN [29060290] |   10.7667 |   -74.1667 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1975-05-15 00:00:00 | 2002-02-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060290 | SAN JUAN [29060290] |   10.7667 |   -74.1667 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1975-05-15 00:00:00 | 2002-02-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29060290 | SAN JUAN [29060290] |   10.7667 |   -74.1667 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1975-05-15 00:00:00 | 2002-02-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060290_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060290_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060290_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060290_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060070 (502 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060070 | SAN PABLO [29060070] |   10.8082 |   -74.0268 |       800 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1960-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    24.3 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060070 | SAN PABLO [29060070] |   10.8082 |   -74.0268 |       800 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1960-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    29.1 |      50 |           nan |               900 |
| 1980-04-01 00:00:00 |         29060070 | SAN PABLO [29060070] |   10.8082 |   -74.0268 |       800 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1960-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |   131   |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060070_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060070_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060070_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060070_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060230 (370 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060230 | SARA LA [29060230] |   10.8362 |    -74.161 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1971-08-15 00:00:00 | 2019-02-07 11:33:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060230 | SARA LA [29060230] |   10.8362 |    -74.161 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1971-08-15 00:00:00 | 2019-02-07 11:33:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29060230 | SARA LA [29060230] |   10.8362 |    -74.161 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1971-08-15 00:00:00 | 2019-02-07 11:33:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060230_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060230_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060230_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060230_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060160 (489 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060160 | ENANO EL [29060160] |   10.9022 |   -74.1895 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1974-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060160 | ENANO EL [29060160] |   10.9022 |   -74.1895 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1974-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29060160 | ENANO EL [29060160] |   10.9022 |   -74.1895 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1974-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060160_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060160_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060160_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060160_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060210 (501 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060210 | PALMA LA [29060210] |   10.9668 |   -74.2047 |        23 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1967-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060210 | PALMA LA [29060210] |   10.9668 |   -74.2047 |        23 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1967-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29060210 | PALMA LA [29060210] |   10.9668 |   -74.2047 |        23 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1967-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060210_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060210_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060210_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060210_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060280 (484 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060280 | SAN ISIDRO [29060280] |   10.9008 |   -74.2206 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060280 | SAN ISIDRO [29060280] |   10.9008 |   -74.2206 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29060280 | SAN ISIDRO [29060280] |   10.9008 |   -74.2206 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060280_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060280_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060280_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060280_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060310 (504 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060310 | SEVILLANO [29060310] |   10.9331 |   -74.2524 |         5 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1979-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060310 | SEVILLANO [29060310] |   10.9331 |   -74.2524 |         5 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1979-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29060310 | SEVILLANO [29060310] |   10.9331 |   -74.2524 |         5 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1979-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060310_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060310_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060310_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060310_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060120 (504 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060120 | TASAJERA [29060120] |   10.9762 |   -74.3618 |         2 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Puebloviejo | 1965-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060120 | TASAJERA [29060120] |   10.9762 |   -74.3618 |         2 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Puebloviejo | 1965-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29060120 | TASAJERA [29060120] |   10.9762 |   -74.3618 |         2 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Puebloviejo | 1965-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060120_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060120_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060120_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060120_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 15015020 (339 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion   |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         15015020 | YE LA [15015020] |   10.9924 |   -74.2111 |        20 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1967-07-15 00:00:00 | 2019-02-07 11:34:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         15015020 | YE LA [15015020] |   10.9924 |   -74.2111 |        20 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1967-07-15 00:00:00 | 2019-02-07 11:34:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         15015020 | YE LA [15015020] |   10.9924 |   -74.2111 |        20 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1967-07-15 00:00:00 | 2019-02-07 11:34:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_15015020_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15015020_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15015020_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15015020_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 16060010 (504 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                          | Departamento       | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:---------------------------------------|:-------------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         16060010 | CNO LA RAYA [16060010] |   8.83472 |   -72.7917 |        75 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Tibú        | 1973-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      53 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         16060010 | CNO LA RAYA [16060010] |   8.83472 |   -72.7917 |        75 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Tibú        | 1973-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      16 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         16060010 | CNO LA RAYA [16060010] |   8.83472 |   -72.7917 |        75 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Tibú        | 1973-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       6 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_16060010_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16060010_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16060010_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16060010_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 16070030 (309 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                          | Departamento       | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:---------------------------------------|:-------------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         16070030 | HACHARIRA [16070030] |   8.87583 |   -72.9822 |        75 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | El Tarra    | 1973-04-15 00:00:00 | 2018-07-13 12:10:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     200 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         16070030 | HACHARIRA [16070030] |   8.87583 |   -72.9822 |        75 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | El Tarra    | 1973-04-15 00:00:00 | 2018-07-13 12:10:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      97 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         16070030 | HACHARIRA [16070030] |   8.87583 |   -72.9822 |        75 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | El Tarra    | 1973-04-15 00:00:00 | 2018-07-13 12:10:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_16070030_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070030_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070030_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070030_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 16070040 (472 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion   |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                          | Departamento       | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:---------------------------------------|:-------------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         16070040 | ORU [16070040]   |   8.64111 |   -72.9094 |       150 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Tibú        | 1973-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      67 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         16070040 | ORU [16070040]   |   8.64111 |   -72.9094 |       150 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Tibú        | 1973-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      59 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         16070040 | ORU [16070040]   |   8.64111 |   -72.9094 |       150 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Tibú        | 1973-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      34 |       4 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_16070040_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070040_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070040_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070040_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 16050240 (327 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                          | Departamento       | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:---------------------------------------|:-------------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1984-03-01 00:00:00 |         16050240 | PALACIO EL [16050240] |   8.61033 |   -73.3511 |      1280 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Convención  | 1984-03-15 00:00:00 | 2014-08-28 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       3 |      50 |           nan |               900 |
| 1984-04-01 00:00:00 |         16050240 | PALACIO EL [16050240] |   8.61033 |   -73.3511 |      1280 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Convención  | 1984-03-15 00:00:00 | 2014-08-28 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     166 |      50 |           nan |               900 |
| 1984-05-01 00:00:00 |         16050240 | PALACIO EL [16050240] |   8.61033 |   -73.3511 |      1280 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Convención  | 1984-03-15 00:00:00 | 2014-08-28 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     115 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_16050240_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16050240_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16050240_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16050240_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 16070020 (154 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                          | Departamento       | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:---------------------------------------|:-------------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1986-03-01 00:00:00 |         16070020 | PISTA LA [16070020] |   9.11667 |   -72.8667 |        50 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Tibú        | 1986-02-15 00:00:00 | 2019-01-21 08:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     144 |      50 |           nan |               900 |
| 1986-04-01 00:00:00 |         16070020 | PISTA LA [16070020] |   9.11667 |   -72.8667 |        50 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Tibú        | 1986-02-15 00:00:00 | 2019-01-21 08:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     415 |      50 |           nan |               900 |
| 1986-05-01 00:00:00 |         16070020 | PISTA LA [16070020] |   9.11667 |   -72.8667 |        50 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Tibú        | 1986-02-15 00:00:00 | 2019-01-21 08:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     729 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_16070020_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070020_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070020_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070020_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 16070010 (437 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                          | Departamento       | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:---------------------------------------|:-------------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         16070010 | PUERTO BARCO [16070010] |   8.99806 |   -72.8969 |        50 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Tibú        | 1973-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      50 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         16070010 | PUERTO BARCO [16070010] |   8.99806 |   -72.8969 |        50 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Tibú        | 1973-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      87 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         16070010 | PUERTO BARCO [16070010] |   8.99806 |   -72.8969 |        50 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Tibú        | 1973-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      18 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_16070010_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070010_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070010_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_16070010_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25020220 (503 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion    |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020220 | ASTREA [25020220] |   9.49294 |   -73.9729 |        50 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Astrea      | 1962-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25020220 | ASTREA [25020220] |   9.49294 |   -73.9729 |        50 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Astrea      | 1962-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      15 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25020220 | ASTREA [25020220] |   9.49294 |   -73.9729 |        50 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Astrea      | 1962-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       1 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25020220_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020220_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020220_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020220_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25020240 (502 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020240 | CANAL EL [25020240] |   9.41047 |   -73.8904 |        70 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chimichagua | 1963-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25020240 | CANAL EL [25020240] |   9.41047 |   -73.8904 |        70 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chimichagua | 1963-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      19 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25020240 | CANAL EL [25020240] |   9.41047 |   -73.8904 |        70 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chimichagua | 1963-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25020240_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020240_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020240_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020240_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25021240 (504 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25021240 | CHIMICHAGUA [25021240] |   9.26008 |   -73.8099 |       138 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chimichagua | 1972-07-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25021240 | CHIMICHAGUA [25021240] |   9.26008 |   -73.8099 |       138 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chimichagua | 1972-07-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      10 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25021240 | CHIMICHAGUA [25021240] |   9.26008 |   -73.8099 |       138 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chimichagua | 1972-07-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       5 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25021240_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021240_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021240_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021240_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25025250 (453 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25025250 | CHIRIGUANA [25025250] |   9.36103 |   -73.5934 |        40 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chiriguaná  | 1973-06-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    28.7 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25025250 | CHIRIGUANA [25025250] |   9.36103 |   -73.5934 |        40 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chiriguaná  | 1973-06-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    14.7 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25025250 | CHIRIGUANA [25025250] |   9.36103 |   -73.5934 |        40 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chiriguaná  | 1973-06-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     4.4 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25025250_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025250_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025250_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025250_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25021580 (188 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1981-01-01 00:00:00 |         25021580 | CURUMANI D C [25021580] |   9.18333 |   -73.5333 |       100 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Curumaní    | 1979-11-15 00:00:00 | 1996-08-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       2 |       4 |           nan |               900 |
| 1981-02-01 00:00:00 |         25021580 | CURUMANI D C [25021580] |   9.18333 |   -73.5333 |       100 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Curumaní    | 1979-11-15 00:00:00 | 1996-08-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     131 |      50 |           nan |               900 |
| 1981-03-01 00:00:00 |         25021580 | CURUMANI D C [25021580] |   9.18333 |   -73.5333 |       100 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Curumaní    | 1979-11-15 00:00:00 | 1996-08-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      94 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25021580_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021580_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021580_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021580_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25020250 (501 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020250 | CURUMANI [25020250] |   9.19719 |   -73.5419 |       100 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Curumaní    | 1963-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25020250 | CURUMANI [25020250] |   9.19719 |   -73.5419 |       100 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Curumaní    | 1963-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      36 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25020250 | CURUMANI [25020250] |   9.19719 |   -73.5419 |       100 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Curumaní    | 1963-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25020250_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020250_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020250_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020250_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25020690 (504 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020690 | POPONTE [25020690] |   9.42328 |   -73.4109 |       500 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Curumaní    | 1972-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      60 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25020690 | POPONTE [25020690] |   9.42328 |   -73.4109 |       500 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Curumaní    | 1972-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      28 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25020690 | POPONTE [25020690] |   9.42328 |   -73.4109 |       500 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Curumaní    | 1972-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       5 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25020690_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020690_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020690_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020690_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25020920 (418 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020920 | PRIMAVERA LA [25020920] |   9.21667 |   -73.4167 |       500 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Curumaní    | 1972-09-15 00:00:00 | 2019-02-07 11:35:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       5 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25020920 | PRIMAVERA LA [25020920] |   9.21667 |   -73.4167 |       500 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Curumaní    | 1972-09-15 00:00:00 | 2019-02-07 11:35:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      51 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25020920 | PRIMAVERA LA [25020920] |   9.21667 |   -73.4167 |       500 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Curumaní    | 1972-09-15 00:00:00 | 2019-02-07 11:35:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25020920_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020920_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020920_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020920_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25020260 (495 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020260 | RINCONHONDO [25020260] |   9.39703 |    -73.488 |       100 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chiriguaná  | 1963-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      43 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25020260 | RINCONHONDO [25020260] |   9.39703 |    -73.488 |       100 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chiriguaná  | 1963-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      33 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25020260 | RINCONHONDO [25020260] |   9.39703 |    -73.488 |       100 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chiriguaná  | 1963-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      19 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25020260_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020260_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020260_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020260_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25020270 (500 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion   |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020270 | SALOA [25020270] |   9.19317 |   -73.7313 |        90 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chimichagua | 1963-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      31 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25020270 | SALOA [25020270] |   9.19317 |   -73.7313 |        90 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chimichagua | 1963-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       6 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25020270 | SALOA [25020270] |   9.19317 |   -73.7313 |        90 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chimichagua | 1963-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25020270_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020270_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020270_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020270_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28025090 (500 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                 |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio       | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28025090 | CENTENARIO HACIENDA [28025090] |   9.85025 |   -73.2655 |       100 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1976-12-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     0   |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28025090 | CENTENARIO HACIENDA [28025090] |   9.85025 |   -73.2655 |       100 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1976-12-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    15.1 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28025090 | CENTENARIO HACIENDA [28025090] |   9.85025 |   -73.2655 |       100 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1976-12-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    13   |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28025090_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025090_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025090_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025090_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25020230 (482 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio           | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020230 | JAGUA LA [25020230] |   9.56217 |   -73.3395 |       170 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | La Jagua De Ibirico | 1963-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       2 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25020230 | JAGUA LA [25020230] |   9.56217 |   -73.3395 |       170 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | La Jagua De Ibirico | 1963-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      44 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25020230 | JAGUA LA [25020230] |   9.56217 |   -73.3395 |       170 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | La Jagua De Ibirico | 1963-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      13 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25020230_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020230_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020230_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020230_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28020230 (266 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28020230 | LLANOS LOS [28020230] |   9.73333 |      -73.3 |       100 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Becerrill   | 1962-09-15 00:00:00 | 2010-10-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28020230 | LLANOS LOS [28020230] |   9.73333 |      -73.3 |       100 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Becerrill   | 1962-09-15 00:00:00 | 2010-10-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28020230 | LLANOS LOS [28020230] |   9.73333 |      -73.3 |       100 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Becerrill   | 1962-09-15 00:00:00 | 2010-10-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       7 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28020230_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020230_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020230_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020230_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25020280 (467 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020280 | LOMA LA [25020280] |   9.60653 |    -73.612 |        30 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1963-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25020280 | LOMA LA [25020280] |   9.60653 |    -73.612 |        30 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1963-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      11 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25020280 | LOMA LA [25020280] |   9.60653 |    -73.612 |        30 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1963-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       2 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25020280_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020280_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020280_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020280_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28040310 (357 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040310 | MOLINO EL [28040310] |   9.77606 |   -73.7434 |       110 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1972-08-15 00:00:00 | 2016-06-01 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28040310 | MOLINO EL [28040310] |   9.77606 |   -73.7434 |       110 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1972-08-15 00:00:00 | 2016-06-01 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28040310 | MOLINO EL [28040310] |   9.77606 |   -73.7434 |       110 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1972-08-15 00:00:00 | 2016-06-01 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28040310_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040310_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040310_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040310_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28040350 (504 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040350 | PASO EL   [28040350] |   9.65697 |   -73.7437 |        30 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1972-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       4 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28040350 | PASO EL   [28040350] |   9.65697 |   -73.7437 |        30 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1972-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      14 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28040350 | PASO EL   [28040350] |   9.65697 |   -73.7437 |        30 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1972-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       5 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28040350_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040350_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040350_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040350_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28020080 (470 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                 |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio       | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28020080 | PLAYAS LAS HACIENDA [28020080] |   9.84808 |   -73.4622 |        60 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1959-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28020080 | PLAYAS LAS HACIENDA [28020080] |   9.84808 |   -73.4622 |        60 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1959-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      88 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28020080 | PLAYAS LAS HACIENDA [28020080] |   9.84808 |   -73.4622 |        60 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1959-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28020080_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020080_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020080_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020080_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28020420 (448 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28020420 | SAN GABRIEL [28020420] |   9.84461 |   -73.5477 |        70 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1972-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28020420 | SAN GABRIEL [28020420] |   9.84461 |   -73.5477 |        70 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1972-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      35 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28020420 | SAN GABRIEL [28020420] |   9.84461 |   -73.5477 |        70 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1972-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28020420_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020420_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020420_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020420_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28025080 (347 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28025080 | SOCOMBA [28025080] |   9.68667 |   -73.2406 |       170 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Becerrill   | 1976-12-15 00:00:00 | 2019-02-07 11:41:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    18.5 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28025080 | SOCOMBA [28025080] |   9.68667 |   -73.2406 |       170 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Becerrill   | 1976-12-15 00:00:00 | 2019-02-07 11:41:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    44.9 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28025080 | SOCOMBA [28025080] |   9.68667 |   -73.2406 |       170 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Becerrill   | 1976-12-15 00:00:00 | 2019-02-07 11:41:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     0   |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28025080_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025080_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025080_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025080_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25021650 (442 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1984-12-01 00:00:00 |         25021650 | YUCAL EL [25021650] |   9.55739 |   -73.8762 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Astrea      | 1984-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     0   |      50 |           nan |               900 |
| 1985-01-01 00:00:00 |         25021650 | YUCAL EL [25021650] |   9.55739 |   -73.8762 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Astrea      | 1984-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    54.9 |      50 |           nan |               900 |
| 1985-02-01 00:00:00 |         25021650 | YUCAL EL [25021650] |   9.55739 |   -73.8762 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Astrea      | 1984-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    19.7 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25021650_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021650_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021650_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021650_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28040030 (499 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040030 | BOSCONIA [28040030] |   9.97575 |   -73.8817 |       130 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Bosconia    | 1979-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      30 |       4 |           nan |               900 |
| 1980-02-01 00:00:00 |         28040030 | BOSCONIA [28040030] |   9.97575 |   -73.8817 |       130 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Bosconia    | 1979-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     110 |       4 |           nan |               900 |
| 1980-03-01 00:00:00 |         28040030 | BOSCONIA [28040030] |   9.97575 |   -73.8817 |       130 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Bosconia    | 1979-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |       4 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28040030_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040030_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040030_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040030_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28020460 (498 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio       | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28020460 | CODAZZI DC [28020460] |   10.0446 |   -73.2434 |        90 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1979-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |       4 |           nan |               900 |
| 1980-02-01 00:00:00 |         28020460 | CODAZZI DC [28020460] |   10.0446 |   -73.2434 |        90 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1979-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      19 |       4 |           nan |               900 |
| 1980-03-01 00:00:00 |         28020460 | CODAZZI DC [28020460] |   10.0446 |   -73.2434 |        90 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1979-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |       4 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28020460_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020460_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020460_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020460_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28020150 (431 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                   |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1986-01-01 00:00:00 |         28020150 | ESPERANZA LA HACIENDA [28020150] |     10.03 |   -73.6688 |        60 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1961-05-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |       4 |           nan |               900 |
| 1986-02-01 00:00:00 |         28020150 | ESPERANZA LA HACIENDA [28020150] |     10.03 |   -73.6688 |        60 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1961-05-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       5 |      50 |           nan |               900 |
| 1986-03-01 00:00:00 |         28020150 | ESPERANZA LA HACIENDA [28020150] |     10.03 |   -73.6688 |        60 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1961-05-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      49 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28020150_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020150_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020150_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020150_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28035040 (492 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28035040 | GUAYMARAL [28035040] |   9.90492 |   -73.6475 |        50 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1972-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     0   |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28035040 | GUAYMARAL [28035040] |   9.90492 |   -73.6475 |        50 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1972-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     0   |       4 |           nan |               900 |
| 1980-03-01 00:00:00 |         28035040 | GUAYMARAL [28035040] |   9.90492 |   -73.6475 |        50 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1972-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    14.2 |       4 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28035040_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28035040_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28035040_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28035040_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28040270 (484 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion               |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040270 | MANATURE HACIENDA [28040270] |   10.0351 |   -73.7885 |       150 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Bosconia    | 1968-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28040270 | MANATURE HACIENDA [28040270] |   10.0351 |   -73.7885 |       150 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Bosconia    | 1968-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      28 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28040270 | MANATURE HACIENDA [28040270] |   10.0351 |   -73.7885 |       150 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Bosconia    | 1968-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       4 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28040270_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040270_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040270_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040270_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28025070 (504 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion               |   Latitud |   Longitud |   Altitud | Categoria         | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio       | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------------|----------:|-----------:|----------:|:------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28025070 | MOTILONIA CODAZZI [28025070] |   10.0018 |   -73.2494 |       180 | Agrometeorológica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1956-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     0   |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28025070 | MOTILONIA CODAZZI [28025070] |   10.0018 |   -73.2494 |       180 | Agrometeorológica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1956-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    14.7 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28025070 | MOTILONIA CODAZZI [28025070] |   10.0018 |   -73.2494 |       180 | Agrometeorológica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1956-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    14.6 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28025070_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025070_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025070_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025070_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28040070 (494 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040070 | PALMARIGUANI [28040070] |   9.93008 |   -73.9549 |        80 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Bosconia    | 1963-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       5 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28040070 | PALMARIGUANI [28040070] |   9.93008 |   -73.9549 |        80 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Bosconia    | 1963-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      71 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28040070 | PALMARIGUANI [28040070] |   9.93008 |   -73.9549 |        80 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Bosconia    | 1963-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28040070_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040070_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040070_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040070_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28040400 (358 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1984-06-01 00:00:00 |         28040400 | PALMASOLA [28040400] |   9.97742 |   -73.8893 |        50 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Bosconia    | 1984-06-15 00:00:00 | 2019-02-07 11:42:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    86.2 |       4 |           nan |               900 |
| 1984-07-01 00:00:00 |         28040400 | PALMASOLA [28040400] |   9.97742 |   -73.8893 |        50 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Bosconia    | 1984-06-15 00:00:00 | 2019-02-07 11:42:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |   121   |      50 |           nan |               900 |
| 1984-08-01 00:00:00 |         28040400 | PALMASOLA [28040400] |   9.97742 |   -73.8893 |        50 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Bosconia    | 1984-06-15 00:00:00 | 2019-02-07 11:42:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    11.3 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28040400_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040400_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040400_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040400_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28020600 (468 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio       | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1981-12-01 00:00:00 |         28020600 | RETORNO EL [28020600] |   9.85472 |   -73.3572 |       150 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1979-02-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      56 |       4 |           nan |               900 |
| 1982-01-01 00:00:00 |         28020600 | RETORNO EL [28020600] |   9.85472 |   -73.3572 |       150 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1979-02-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      15 |      50 |           nan |               900 |
| 1982-02-01 00:00:00 |         28020600 | RETORNO EL [28020600] |   9.85472 |   -73.3572 |       150 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1979-02-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      14 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28020600_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020600_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020600_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020600_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28020440 (492 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                   |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio       | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28020440 | SANTA TERESA HACIENDA [28020440] |   9.91703 |   -73.2861 |        80 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1959-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28020440 | SANTA TERESA HACIENDA [28020440] |   9.91703 |   -73.2861 |        80 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1959-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      46 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28020440 | SANTA TERESA HACIENDA [28020440] |   9.91703 |   -73.2861 |        80 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1959-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       6 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28020440_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020440_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020440_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020440_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28020310 (281 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio       | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28020310 | BOGOTANA LA [28020310] |      10.1 |     -73.15 |       200 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1968-09-15 00:00:00 | 2004-08-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       2 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28020310 | BOGOTANA LA [28020310] |      10.1 |     -73.15 |       200 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1968-09-15 00:00:00 | 2004-08-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      62 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28020310 | BOGOTANA LA [28020310] |      10.1 |     -73.15 |       200 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1968-09-15 00:00:00 | 2004-08-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      36 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28020310_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020310_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020310_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020310_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28030190 (504 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28030190 | CARACOLI [28030190] |   10.0887 |   -73.7317 |       220 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1972-07-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      14 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28030190 | CARACOLI [28030190] |   10.0887 |   -73.7317 |       220 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1972-07-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28030190 | CARACOLI [28030190] |   10.0887 |   -73.7317 |       220 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1972-07-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28030190_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28030190_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28030190_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28030190_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28040200 (187 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040200 | CHIMILAIMA [28040200] |   10.0667 |   -73.7667 |       120 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Bosconia    | 1962-08-15 00:00:00 | 1996-12-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28040200 | CHIMILAIMA [28040200] |   10.0667 |   -73.7667 |       120 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Bosconia    | 1962-08-15 00:00:00 | 1996-12-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      17 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28040200 | CHIMILAIMA [28040200] |   10.0667 |   -73.7667 |       120 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Bosconia    | 1962-08-15 00:00:00 | 1996-12-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28040200_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040200_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040200_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040200_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28020590 (448 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28020590 | LETICIA [28020590] |   10.1524 |   -73.2217 |       140 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1979-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      15 |       4 |           nan |               900 |
| 1980-02-01 00:00:00 |         28020590 | LETICIA [28020590] |   10.1524 |   -73.2217 |       140 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1979-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      58 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28020590 | LETICIA [28020590] |   10.1524 |   -73.2217 |       140 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1979-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      10 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28020590_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020590_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020590_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020590_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28010370 (501 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28010370 | PARIS DE FRANCIA [28010370] |   10.3071 |   -73.3254 |       180 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1971-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |       4 |           nan |               900 |
| 1980-02-01 00:00:00 |         28010370 | PARIS DE FRANCIA [28010370] |   10.3071 |   -73.3254 |       180 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1971-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      74 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28010370 | PARIS DE FRANCIA [28010370] |   10.3071 |   -73.3254 |       180 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1971-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       4 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28010370_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010370_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010370_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010370_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28040060 (140 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040060 | PAVAS LAS [28040060] |   10.0667 |   -73.8833 |       150 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Bosconia    | 1963-01-15 00:00:00 | 1992-07-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      55 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28040060 | PAVAS LAS [28040060] |   10.0667 |   -73.8833 |       150 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Bosconia    | 1963-01-15 00:00:00 | 1992-07-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      60 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28040060 | PAVAS LAS [28040060] |   10.0667 |   -73.8833 |       150 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Bosconia    | 1963-01-15 00:00:00 | 1992-07-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      15 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28040060_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040060_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040060_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040060_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28025020 (494 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28025020 | RINCON EL [28025020] |   10.2714 |   -73.1314 |       350 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1964-02-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     9.6 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28025020 | RINCON EL [28025020] |   10.2714 |   -73.1314 |       350 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1964-02-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    49.1 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28025020 | RINCON EL [28025020] |   10.2714 |   -73.1314 |       350 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1964-02-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    14.2 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28025020_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025020_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025020_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025020_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28020410 (457 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28020410 | SAN BENITO [28020410] |   10.1842 |    -73.317 |       150 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1972-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28020410 | SAN BENITO [28020410] |   10.1842 |    -73.317 |       150 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1972-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      25 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28020410 | SAN BENITO [28020410] |   10.1842 |    -73.317 |       150 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1972-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28020410_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020410_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020410_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28020410_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28010070 (432 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1986-01-01 00:00:00 |         28010070 | VILLA MARLENE [28010070] |   10.1855 |   -73.4671 |       120 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1987-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |       4 |           nan |               900 |
| 1986-02-01 00:00:00 |         28010070 | VILLA MARLENE [28010070] |   10.1855 |   -73.4671 |       120 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1987-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       2 |      50 |           nan |               900 |
| 1986-03-01 00:00:00 |         28010070 | VILLA MARLENE [28010070] |   10.1855 |   -73.4671 |       120 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1987-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      33 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28010070_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010070_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010070_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010070_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28035010 (462 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28035010 | VILLA ROSA [28035010] |   10.1907 |   -73.5474 |        70 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     0   |       4 |           nan |               900 |
| 1980-02-01 00:00:00 |         28035010 | VILLA ROSA [28035010] |   10.1907 |   -73.5474 |        70 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    10.9 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28035010 | VILLA ROSA [28035010] |   10.1907 |   -73.5474 |        70 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     7.9 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28035010_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28035010_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28035010_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28035010_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28010360 (470 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28010360 | ATANQUEZ [28010360] |   10.6973 |   -73.3531 |       800 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1959-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28010360 | ATANQUEZ [28010360] |   10.6973 |   -73.3531 |       800 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1959-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      79 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28010360 | ATANQUEZ [28010360] |   10.6973 |   -73.3531 |       800 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1959-04-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28010360_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010360_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010360_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010360_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28035020 (474 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28035020 | CALLAO EL [28035020] |   10.3631 |   -73.3194 |       110 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     0   |       4 |           nan |               900 |
| 1980-02-01 00:00:00 |         28035020 | CALLAO EL [28035020] |   10.3631 |   -73.3194 |       110 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    18.9 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28035020 | CALLAO EL [28035020] |   10.3631 |   -73.3194 |       110 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-03-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     2.4 |       4 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28035020_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28035020_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28035020_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28035020_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28040170 (106 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio    | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040170 | CUEVAS LAS [28040170] |   10.4667 |   -73.5667 |      1260 | Pluviográfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pueblo Bello | 1963-06-15 00:00:00 | 1996-02-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      63 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28040170 | CUEVAS LAS [28040170] |   10.4667 |   -73.5667 |      1260 | Pluviográfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pueblo Bello | 1963-06-15 00:00:00 | 1996-02-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      21 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28040170 | CUEVAS LAS [28040170] |   10.4667 |   -73.5667 |      1260 | Pluviográfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pueblo Bello | 1963-06-15 00:00:00 | 1996-02-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       8 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28040170_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040170_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040170_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040170_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28010020 (359 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1986-01-01 00:00:00 |         28010020 | DESCANSO EL [28010020] |   10.4801 |   -73.2372 |       160 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1986-04-15 00:00:00 | 2019-02-07 11:41:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |       4 |           nan |               900 |
| 1986-02-01 00:00:00 |         28010020 | DESCANSO EL [28010020] |   10.4801 |   -73.2372 |       160 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1986-04-15 00:00:00 | 2019-02-07 11:41:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1986-03-01 00:00:00 |         28010020 | DESCANSO EL [28010020] |   10.4801 |   -73.2372 |       160 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1986-04-15 00:00:00 | 2019-02-07 11:41:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28010020_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010020_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010020_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010020_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28010040 (498 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio                | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28010040 | MANAURE [28010040] |   10.3914 |   -73.0253 |       740 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Manaure Balcón Del Cesar | 1975-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       7 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28010040 | MANAURE [28010040] |   10.3914 |   -73.0253 |       740 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Manaure Balcón Del Cesar | 1975-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     114 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28010040 | MANAURE [28010040] |   10.3914 |   -73.0253 |       740 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Manaure Balcón Del Cesar | 1975-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       6 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28010040_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010040_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010040_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010040_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28040010 (504 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio    | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040010 | PUEBLO BELLO [28040010] |   10.4146 |    -73.585 |        10 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pueblo Bello | 1963-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28040010 | PUEBLO BELLO [28040010] |   10.4146 |    -73.585 |        10 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pueblo Bello | 1963-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      27 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28040010 | PUEBLO BELLO [28040010] |   10.4146 |    -73.585 |        10 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pueblo Bello | 1963-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28040010_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040010_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040010_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040010_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28030220 (401 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1983-07-01 00:00:00 |         28030220 | SAN ANGEL [28030220] |   10.3471 |   -73.4441 |       244 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1983-06-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      79 |       4 |           nan |               900 |
| 1983-08-01 00:00:00 |         28030220 | SAN ANGEL [28030220] |   10.3471 |   -73.4441 |       244 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1983-06-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     154 |      50 |           nan |               900 |
| 1983-09-01 00:00:00 |         28030220 | SAN ANGEL [28030220] |   10.3471 |   -73.4441 |       244 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1983-06-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     249 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28030220_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28030220_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28030220_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28030220_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28025040 (171 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28025040 | SAN JOSE D ORIENTE [28025040] |     10.35 |     -73.05 |       850 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | La Paz      | 1975-08-15 00:00:00 | 1998-05-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     3.7 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28025040 | SAN JOSE D ORIENTE [28025040] |     10.35 |     -73.05 |       850 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | La Paz      | 1975-08-15 00:00:00 | 1998-05-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    56.9 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28025040 | SAN JOSE D ORIENTE [28025040] |     10.35 |     -73.05 |       850 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | La Paz      | 1975-08-15 00:00:00 | 1998-05-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     7.3 |       4 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28025040_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025040_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025040_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28025040_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 29060090 (501 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio    | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29060090 | SAN SEBASTIAN DE [29060090] |   10.5633 |   -73.6038 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pueblo Bello | 1968-05-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      11 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29060090 | SAN SEBASTIAN DE [29060090] |   10.5633 |   -73.6038 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pueblo Bello | 1968-05-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      26 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29060090 | SAN SEBASTIAN DE [29060090] |   10.5633 |   -73.6038 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pueblo Bello | 1968-05-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_29060090_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060090_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060090_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_29060090_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28010140 (255 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion             |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28010140 | VILLA CARMELITA [28010140] |   10.5333 |      -73.3 |       450 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-09-15 00:00:00 | 2004-08-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     3   |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28010140 | VILLA CARMELITA [28010140] |   10.5333 |      -73.3 |       450 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-09-15 00:00:00 | 2004-08-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    17.2 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28010140 | VILLA CARMELITA [28010140] |   10.5333 |      -73.3 |       450 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-09-15 00:00:00 | 2004-08-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    50.3 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28010140_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010140_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010140_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010140_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28010090 (474 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28010090 | PATILLAL [28010090] |   10.7039 |   -73.2116 |       450 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1962-12-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28010090 | PATILLAL [28010090] |   10.7039 |   -73.2116 |       450 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1962-12-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      51 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28010090 | PATILLAL [28010090] |   10.7039 |   -73.2116 |       450 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1962-12-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28010090_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010090_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010090_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010090_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28045010 (228 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                          | AreaOperativa                               | Departamento   | Municipio    | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:--------------------|:---------------------------------|:--------------------------------------------|:---------------|:-------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28045010 | PUEBLO BELLO  [28045010] |     10.37 |     -73.63 |      1000 | Climática Ordinaria | FEDERACION NACIONAL DE CAFETEROS | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pueblo Bello | 1954-02-15 00:00:00 | 2020-10-21 17:13:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    47.7 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28045010 | PUEBLO BELLO  [28045010] |     10.37 |     -73.63 |      1000 | Climática Ordinaria | FEDERACION NACIONAL DE CAFETEROS | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pueblo Bello | 1954-02-15 00:00:00 | 2020-10-21 17:13:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    38.3 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28045010 | PUEBLO BELLO  [28045010] |     10.37 |     -73.63 |      1000 | Climática Ordinaria | FEDERACION NACIONAL DE CAFETEROS | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pueblo Bello | 1954-02-15 00:00:00 | 2020-10-21 17:13:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    10.5 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28045010_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28045010_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28045010_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28045010_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28010130 (122 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28010130 | SARACHUI [28010130] |   10.7833 |      -73.4 |      1560 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-04-15 00:00:00 | 1990-05-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      27 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28010130 | SARACHUI [28010130] |   10.7833 |      -73.4 |      1560 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-04-15 00:00:00 | 1990-05-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      44 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28010130 | SARACHUI [28010130] |   10.7833 |      -73.4 |      1560 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-04-15 00:00:00 | 1990-05-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28010130_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010130_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010130_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010130_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 15060080 (503 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio          | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         15060080 | CANAVERALES [15060080] |   10.7578 |   -72.8452 |       230 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | San Juan Del Cesar | 1963-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         15060080 | CANAVERALES [15060080] |   10.7578 |   -72.8452 |       230 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | San Juan Del Cesar | 1963-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      23 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         15060080 | CANAVERALES [15060080] |   10.7578 |   -72.8452 |       230 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | San Juan Del Cesar | 1963-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_15060080_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060080_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060080_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060080_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 15060150 (504 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         15060150 | CONEJO EL [15060150] |   10.7779 |   -72.7982 |       350 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 1975-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         15060150 | CONEJO EL [15060150] |   10.7779 |   -72.7982 |       350 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 1975-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      23 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         15060150 | CONEJO EL [15060150] |   10.7779 |   -72.7982 |       350 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 1975-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       4 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_15060150_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060150_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060150_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060150_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28010200 (471 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio          | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28010200 | HATICO D LOS INDIO [28010200] |   10.8602 |   -73.1142 |       594 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | San Juan Del Cesar | 1970-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28010200 | HATICO D LOS INDIO [28010200] |   10.8602 |   -73.1142 |       594 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | San Juan Del Cesar | 1970-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28010200 | HATICO D LOS INDIO [28010200] |   10.8602 |   -73.1142 |       594 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | San Juan Del Cesar | 1970-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28010200_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010200_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010200_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010200_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 15060070 (387 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         15060070 | JUGUETE EL [15060070] |    10.786 |   -72.7684 |       390 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 1971-05-15 00:00:00 | 2014-08-28 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         15060070 | JUGUETE EL [15060070] |    10.786 |   -72.7684 |       390 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 1971-05-15 00:00:00 | 2014-08-28 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     133 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         15060070 | JUGUETE EL [15060070] |    10.786 |   -72.7684 |       390 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 1971-05-15 00:00:00 | 2014-08-28 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_15060070_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060070_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060070_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060070_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 15065040 (243 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-04-01 00:00:00 |         15065040 | LA PAULINA - AUT [15065040] |   10.8981 |   -72.8285 |       170 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 1966-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    72.3 |       4 |           nan |               900 |
| 1980-05-01 00:00:00 |         15065040 | LA PAULINA - AUT [15065040] |   10.8981 |   -72.8285 |       170 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 1966-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    45.2 |      50 |           nan |               900 |
| 1980-07-01 00:00:00 |         15065040 | LA PAULINA - AUT [15065040] |   10.8981 |   -72.8285 |       170 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 1966-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    87.6 |       4 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_15065040_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15065040_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15065040_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15065040_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28010280 (15 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio          | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------------|:--------------------|:--------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28010280 | PAMPLONA [28010280] |     10.65 |     -72.85 |       690 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | San Juan Del Cesar | 1971-05-15 00:00:00 | 1993-11-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       2 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28010280 | PAMPLONA [28010280] |     10.65 |     -72.85 |       690 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | San Juan Del Cesar | 1971-05-15 00:00:00 | 1993-11-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       6 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28010280 | PAMPLONA [28010280] |     10.65 |     -72.85 |       690 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | San Juan Del Cesar | 1971-05-15 00:00:00 | 1993-11-15 00:00:00 | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       8 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28010280_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010280_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010280_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010280_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 15060050 (487 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         15060050 | SABANAS DE MANUELA [15060050] |    10.953 |    -73.048 |       420 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Distracción | 1963-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         15060050 | SABANAS DE MANUELA [15060050] |    10.953 |    -73.048 |       420 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Distracción | 1963-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      27 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         15060050 | SABANAS DE MANUELA [15060050] |    10.953 |    -73.048 |       420 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Distracción | 1963-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_15060050_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060050_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060050_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_15060050_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28015070 (499 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28015070 | URUMITA [28015070] |   10.5664 |   -73.0164 |       255 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Urumita     | 1975-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     0   |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28015070 | URUMITA [28015070] |   10.5664 |   -73.0164 |       255 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Urumita     | 1975-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    28.6 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28015070 | URUMITA [28015070] |   10.5664 |   -73.0164 |       255 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Urumita     | 1975-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     0   |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28015070_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28015070_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28015070_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28015070_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28010340 (492 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28010340 | VILLANUEVA [28010340] |   10.6158 |   -72.9819 |       340 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Villanueva  | 1970-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28010340 | VILLANUEVA [28010340] |   10.6158 |   -72.9819 |       340 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Villanueva  | 1970-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      24 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28010340 | VILLANUEVA [28010340] |   10.6158 |   -72.9819 |       340 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Villanueva  | 1970-08-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28010340_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010340_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010340_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28010340_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25025090 (466 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                   |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25025090 | AEROPUERTO LAS FLORES [25025090] |   9.04633 |   -73.9708 |        34 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Banco    | 1952-02-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    70   |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25025090 | AEROPUERTO LAS FLORES [25025090] |   9.04633 |   -73.9708 |        34 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Banco    | 1952-02-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    39.6 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25025090 | AEROPUERTO LAS FLORES [25025090] |   9.04633 |   -73.9708 |        34 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Banco    | 1952-02-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     0   |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25025090_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025090_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025090_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025090_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28040320 (487 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040320 | BRILLANTE EL [28040320] |   9.70275 |   -73.9591 |       135 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Santa Ana   | 1972-07-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       7 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28040320 | BRILLANTE EL [28040320] |   9.70275 |   -73.9591 |       135 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Santa Ana   | 1972-07-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      51 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28040320 | BRILLANTE EL [28040320] |   9.70275 |   -73.9591 |       135 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Santa Ana   | 1972-07-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28040320_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040320_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040320_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040320_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25021620 (468 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion   |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1982-07-01 00:00:00 |         25021620 | IRAN [25021620]  |   9.68378 |   -74.3222 |        80 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Nueva Granada | 1982-06-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      63 |       4 |           nan |               900 |
| 1982-08-01 00:00:00 |         25021620 | IRAN [25021620]  |   9.68378 |   -74.3222 |        80 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Nueva Granada | 1982-06-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      69 |      50 |           nan |               900 |
| 1982-09-01 00:00:00 |         25021620 | IRAN [25021620]  |   9.68378 |   -74.3222 |        80 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Nueva Granada | 1982-06-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     102 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25021620_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021620_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021620_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021620_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25021040 (503 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25021040 | MENCHIQUEJO [25021040] |   9.18806 |   -74.0442 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Banco    | 1974-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25021040 | MENCHIQUEJO [25021040] |   9.18806 |   -74.0442 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Banco    | 1974-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      47 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25021040 | MENCHIQUEJO [25021040] |   9.18806 |   -74.0442 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Banco    | 1974-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       6 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25021040_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021040_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021040_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021040_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25021200 (484 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25021200 | NEGRITOS LOS [25021200] |   9.02667 |   -74.0794 |        26 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena      | El Banco    | 1976-07-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      21 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25021200 | NEGRITOS LOS [25021200] |   9.02667 |   -74.0794 |        26 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena      | El Banco    | 1976-07-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      10 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25021200 | NEGRITOS LOS [25021200] |   9.02667 |   -74.0794 |        26 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena      | El Banco    | 1976-07-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25021200_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021200_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021200_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021200_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25021500 (492 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25021500 | PUEBLITO EL [25021500] |   9.58117 |   -74.3522 |        35 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Santa Ana   | 1976-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       4 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25021500 | PUEBLITO EL [25021500] |   9.58117 |   -74.3522 |        35 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Santa Ana   | 1976-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       5 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25021500 | PUEBLITO EL [25021500] |   9.58117 |   -74.3522 |        35 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Santa Ana   | 1976-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      13 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25021500_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021500_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021500_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021500_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25021380 (477 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion               |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-06-01 00:00:00 |         25021380 | SAN ROQUE ALERTAS [25021380] |      9.07 |     -74.15 |        24 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena      | El Banco    | 1980-05-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     231 |      50 |           nan |               900 |
| 1980-07-01 00:00:00 |         25021380 | SAN ROQUE ALERTAS [25021380] |      9.07 |     -74.15 |        24 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena      | El Banco    | 1980-05-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     194 |      50 |           nan |               900 |
| 1980-08-01 00:00:00 |         25021380 | SAN ROQUE ALERTAS [25021380] |      9.07 |     -74.15 |        24 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena      | El Banco    | 1980-05-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     257 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25021380_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021380_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021380_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021380_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25020900 (492 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio                   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020900 | SAN SEBASTIAN [25020900] |   9.23389 |   -74.3558 |        65 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena      | San Sebastián De Buenavista | 1974-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25020900 | SAN SEBASTIAN [25020900] |   9.23389 |   -74.3558 |        65 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena      | San Sebastián De Buenavista | 1974-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25020900 | SAN SEBASTIAN [25020900] |   9.23389 |   -74.3558 |        65 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena      | San Sebastián De Buenavista | 1974-01-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25020900_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020900_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020900_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020900_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25025300 (470 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio                   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25025300 | SEIS EL [25025300] |   9.68367 |   -74.3223 |        50 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | San Sebastián De Buenavista | 1984-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25025300 | SEIS EL [25025300] |   9.68367 |   -74.3223 |        50 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | San Sebastián De Buenavista | 1984-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      67 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25025300 | SEIS EL [25025300] |   9.68367 |   -74.3223 |        50 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | San Sebastián De Buenavista | 1984-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       5 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25025300_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025300_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025300_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25025300_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 28040300 (480 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio             | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28040300 | VILLA CONCEPCION [28040300] |   9.70631 |   -73.8594 |       120 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ariguaní (El Dificil) | 1972-07-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28040300 | VILLA CONCEPCION [28040300] |   9.70631 |   -73.8594 |       120 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ariguaní (El Dificil) | 1972-07-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28040300 | VILLA CONCEPCION [28040300] |   9.70631 |   -73.8594 |       120 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ariguaní (El Dificil) | 1972-07-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_28040300_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040300_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040300_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_28040300_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25021540 (490 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio          | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25021540 | AGUADAS LAS ALERTA [25021540] |      8.95 |     -74.05 |        30 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Martín De Loba | 1978-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25021540 | AGUADAS LAS ALERTA [25021540] |      8.95 |     -74.05 |        30 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Martín De Loba | 1978-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      60 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25021540 | AGUADAS LAS ALERTA [25021540] |      8.95 |     -74.05 |        30 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Martín De Loba | 1978-11-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25021540_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021540_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021540_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021540_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25020880 (490 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio        | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-----------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020880 | BARRANCO DE LOBA [25020880] |   8.94667 |   -74.1106 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Barranco De Loba | 1974-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |       4 |           nan |               900 |
| 1980-02-01 00:00:00 |         25020880 | BARRANCO DE LOBA [25020880] |   8.94667 |   -74.1106 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Barranco De Loba | 1974-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      10 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25020880 | BARRANCO DE LOBA [25020880] |   8.94667 |   -74.1106 |        25 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Barranco De Loba | 1974-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25020880_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020880_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020880_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020880_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25020890 (483 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020890 | CHILLOA [25020890] |   9.11939 |   -74.2219 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Margarita   | 1974-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      15 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25020890 | CHILLOA [25020890] |   9.11939 |   -74.2219 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Margarita   | 1974-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      24 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25020890 | CHILLOA [25020890] |   9.11939 |   -74.2219 |        20 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Margarita   | 1974-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       5 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25020890_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020890_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020890_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020890_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25021320 (491 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio              | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-----------------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25021320 | SUDAN EL [25021320] |   8.64333 |   -74.2122 |        23 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Tiquisio (Puerto Rico) | 1976-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    20.9 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25021320 | SUDAN EL [25021320] |   8.64333 |   -74.2122 |        23 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Tiquisio (Puerto Rico) | 1976-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    33.7 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25021320 | SUDAN EL [25021320] |   8.64333 |   -74.2122 |        23 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Tiquisio (Puerto Rico) | 1976-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |    56.2 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25021320_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021320_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021320_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021320_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25020870 (497 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio          | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25020870 | PLAYITAS [25020870] |   8.82278 |   -73.9658 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Martín De Loba | 1974-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      12 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25020870 | PLAYITAS [25020870] |   8.82278 |   -73.9658 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Martín De Loba | 1974-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |     125 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25020870 | PLAYITAS [25020870] |   8.82278 |   -73.9658 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Martín De Loba | 1974-09-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25020870_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020870_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020870_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25020870_DensityKDE.png)

<div align="center">



**PTPM_TT_M - Station: 25021090 (475 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria     | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio    | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie            | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------|:--------------------|:------------------|:--------------|:-----------|:----------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25021090 | SANTA ROSA [25021090] |   9.09333 |   -74.3139 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Fernando | 1974-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       5 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25021090 | SANTA ROSA [25021090] |   9.09333 |   -74.3139 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Fernando | 1974-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |      16 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25021090 | SANTA ROSA [25021090] |   9.09333 |   -74.3139 |        40 | Pluviométrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Fernando | 1974-10-15 00:00:00 | NaT               | PRECIPITACION | PTPM_TT_M  | Precipitación total mensual | Mensual      |       0 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_PTPM_TT_M_25021090_TimeSerie.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021090_Boxplot.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021090_Histogram.png)
![R.LTWB](Graph/Plot_PTPM_TT_M_25021090_DensityKDE.png)


### Analysis from 1980 to 2021 for Etiqueta == "TMX_CON": 185849 (36.09%)

Pivot table: [Pivot_TMX_CON.csv](Pivot_TMX_CON.csv)
![R.LTWB](Graph/Plot_TMX_CON_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 28045020 (1050 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1983-01-01 00:00:00 |         28045020 | ALGARROBO [28045020] |     10.15 |   -74.0667 |        60 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Copey    | 1964-02-15 00:00:00 | 1987-04-15 00:00:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    36   |      50 |           nan |              1200 |
| 1983-01-02 00:00:00 |         28045020 | ALGARROBO [28045020] |     10.15 |   -74.0667 |        60 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Copey    | 1964-02-15 00:00:00 | 1987-04-15 00:00:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    36.2 |      50 |           nan |              1200 |
| 1983-01-03 00:00:00 |         28045020 | ALGARROBO [28045020] |     10.15 |   -74.0667 |        60 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Copey    | 1964-02-15 00:00:00 | 1987-04-15 00:00:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    35.8 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_28045020_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28045020_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28045020_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28045020_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 28025090 (12953 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                 |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio       | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1981-01-03 00:00:00 |         28025090 | CENTENARIO HACIENDA [28025090] |   9.85025 |   -73.2655 |       100 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1976-12-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    32.6 |      50 |           nan |              1200 |
| 1981-01-04 00:00:00 |         28025090 | CENTENARIO HACIENDA [28025090] |   9.85025 |   -73.2655 |       100 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1976-12-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    34   |      50 |           nan |              1200 |
| 1981-01-05 00:00:00 |         28025090 | CENTENARIO HACIENDA [28025090] |   9.85025 |   -73.2655 |       100 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1976-12-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    34.4 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_28025090_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28025090_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28025090_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28025090_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 25025250 (11758 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1981-04-01 00:00:00 |         25025250 | CHIRIGUANA [25025250] |   9.36103 |   -73.5934 |        40 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chiriguaná  | 1973-06-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    37.6 |      50 |           nan |              1200 |
| 1981-04-02 00:00:00 |         25025250 | CHIRIGUANA [25025250] |   9.36103 |   -73.5934 |        40 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chiriguaná  | 1973-06-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    36.2 |      50 |           nan |              1200 |
| 1981-04-03 00:00:00 |         25025250 | CHIRIGUANA [25025250] |   9.36103 |   -73.5934 |        40 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chiriguaná  | 1973-06-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    36.2 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_25025250_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_25025250_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_25025250_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_25025250_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 25025330 (7606 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                                  |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1990-03-27 00:00:00 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    34.2 |      50 |           nan |              1200 |
| 1990-03-28 00:00:00 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    37.4 |      50 |           nan |              1200 |
| 1990-03-29 00:00:00 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    35.2 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_25025330_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_25025330_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_25025330_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_25025330_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 28045040 (784 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1987-09-10 00:00:00 |         28045040 | GUAIRA LA HACIENDA [28045040] |   9.61667 |      -73.8 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    32.4 |      50 |           nan |              1200 |
| 1987-09-11 00:00:00 |         28045040 | GUAIRA LA HACIENDA [28045040] |   9.61667 |      -73.8 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    34.4 |      50 |           nan |              1200 |
| 1987-09-12 00:00:00 |         28045040 | GUAIRA LA HACIENDA [28045040] |   9.61667 |      -73.8 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    35.8 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_28045040_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28045040_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28045040_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28045040_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 28035040 (9424 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1981-06-01 00:00:00 |         28035040 | GUAYMARAL [28035040] |   9.90492 |   -73.6475 |        50 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1972-08-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    35.2 |      50 |           nan |              1200 |
| 1981-06-02 00:00:00 |         28035040 | GUAYMARAL [28035040] |   9.90492 |   -73.6475 |        50 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1972-08-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    32.4 |      50 |           nan |              1200 |
| 1981-06-03 00:00:00 |         28035040 | GUAYMARAL [28035040] |   9.90492 |   -73.6475 |        50 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1972-08-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    32   |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_28035040_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28035040_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28035040_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28035040_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 23215060 (960 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                          | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:---------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1983-09-17 00:00:00 |         23215060 | LA GLORIA [23215060] |   8.61528 |   -73.8006 |        35 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Cesar          | La Gloria   | 1995-05-15 00:00:00 | 2018-06-19 10:35:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |      33 |      50 |           nan |              1200 |
| 1983-09-18 00:00:00 |         23215060 | LA GLORIA [23215060] |   8.61528 |   -73.8006 |        35 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Cesar          | La Gloria   | 1995-05-15 00:00:00 | 2018-06-19 10:35:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |      32 |      50 |           nan |              1200 |
| 1983-09-19 00:00:00 |         23215060 | LA GLORIA [23215060] |   8.61528 |   -73.8006 |        35 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Cesar          | La Gloria   | 1995-05-15 00:00:00 | 2018-06-19 10:35:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |      33 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_23215060_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_23215060_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_23215060_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_23215060_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 28025070 (13398 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion               |   Latitud |   Longitud |   Altitud | Categoria         | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio       | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------------|----------:|-----------:|----------:|:------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28025070 | MOTILONIA CODAZZI [28025070] |   10.0018 |   -73.2494 |       180 | Agrometeorológica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1956-01-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    34.8 |      50 |           nan |              1200 |
| 1980-01-02 00:00:00 |         28025070 | MOTILONIA CODAZZI [28025070] |   10.0018 |   -73.2494 |       180 | Agrometeorológica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1956-01-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    34   |      50 |           nan |              1200 |
| 1980-01-04 00:00:00 |         28025070 | MOTILONIA CODAZZI [28025070] |   10.0018 |   -73.2494 |       180 | Agrometeorológica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1956-01-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    36.1 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_28025070_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28025070_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28025070_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28025070_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 28025080 (7076 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-03 00:00:00 |         28025080 | SOCOMBA [28025080] |   9.68667 |   -73.2406 |       170 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Becerrill   | 1976-12-15 00:00:00 | 2019-02-07 11:41:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    35   |      50 |           nan |              1200 |
| 1980-01-04 00:00:00 |         28025080 | SOCOMBA [28025080] |   9.68667 |   -73.2406 |       170 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Becerrill   | 1976-12-15 00:00:00 | 2019-02-07 11:41:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    34.4 |      50 |           nan |              1200 |
| 1980-01-05 00:00:00 |         28025080 | SOCOMBA [28025080] |   9.68667 |   -73.2406 |       170 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Becerrill   | 1976-12-15 00:00:00 | 2019-02-07 11:41:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    35   |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_28025080_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28025080_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28025080_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28025080_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 28035010 (8442 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-11 00:00:00 |         28035010 | VILLA ROSA [28035010] |   10.1907 |   -73.5474 |        70 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-03-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    35.2 |      50 |           nan |              1200 |
| 1980-01-14 00:00:00 |         28035010 | VILLA ROSA [28035010] |   10.1907 |   -73.5474 |        70 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-03-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    36.2 |      50 |           nan |              1200 |
| 1980-01-15 00:00:00 |         28035010 | VILLA ROSA [28035010] |   10.1907 |   -73.5474 |        70 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-03-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    35.2 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_28035010_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28035010_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28035010_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28035010_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 28025502 (11456 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                        |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1983-04-02 00:00:00 |         28025502 | AEROPUERTO ALFONSO LOPEZ - [28025502] |   10.4362 |   -73.2477 |       138 | Sinóptica Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 2016-01-07 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    39.2 |      50 |           nan |              1200 |
| 1983-04-04 00:00:00 |         28025502 | AEROPUERTO ALFONSO LOPEZ - [28025502] |   10.4362 |   -73.2477 |       138 | Sinóptica Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 2016-01-07 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    37.4 |      50 |           nan |              1200 |
| 1983-04-06 00:00:00 |         28025502 | AEROPUERTO ALFONSO LOPEZ - [28025502] |   10.4362 |   -73.2477 |       138 | Sinóptica Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 2016-01-07 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    37.4 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_28025502_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28025502_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28025502_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28025502_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 28035020 (12136 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28035020 | CALLAO EL [28035020] |   10.3631 |   -73.3194 |       110 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-03-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    34.6 |      50 |           nan |              1200 |
| 1980-01-02 00:00:00 |         28035020 | CALLAO EL [28035020] |   10.3631 |   -73.3194 |       110 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-03-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    30.8 |      50 |           nan |              1200 |
| 1980-01-03 00:00:00 |         28035020 | CALLAO EL [28035020] |   10.3631 |   -73.3194 |       110 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-03-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    34.4 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_28035020_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28035020_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28035020_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28035020_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 28015030 (1127 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-03 00:00:00 |         28015030 | CICOLAC [28015030] |   10.4833 |   -73.2667 |       180 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1964-01-15 00:00:00 | 1988-05-15 00:00:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    34.3 |      50 |           nan |              1200 |
| 1980-01-04 00:00:00 |         28015030 | CICOLAC [28015030] |   10.4833 |   -73.2667 |       180 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1964-01-15 00:00:00 | 1988-05-15 00:00:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    34.9 |      50 |           nan |              1200 |
| 1980-01-07 00:00:00 |         28015030 | CICOLAC [28015030] |   10.4833 |   -73.2667 |       180 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1964-01-15 00:00:00 | 1988-05-15 00:00:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    33.8 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_28015030_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28015030_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28015030_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28015030_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 28035070 (42 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion             |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 2012-12-01 00:00:00 |         28035070 | GUATAPURI - AUT [28035070] |   10.7321 |   -73.3924 |      1315 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 2006-02-26 00:00:00 | 2018-06-11 10:25:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    35.8 |      50 |           nan |              1200 |
| 2012-12-02 00:00:00 |         28035070 | GUATAPURI - AUT [28035070] |   10.7321 |   -73.3924 |      1315 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 2006-02-26 00:00:00 | 2018-06-11 10:25:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    34.6 |      50 |           nan |              1200 |
| 2012-12-03 00:00:00 |         28035070 | GUATAPURI - AUT [28035070] |   10.7321 |   -73.3924 |      1315 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 2006-02-26 00:00:00 | 2018-06-11 10:25:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    34   |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_28035070_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28035070_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28035070_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28035070_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 28025020 (12966 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-02-01 00:00:00 |         28025020 | RINCON EL [28025020] |   10.2714 |   -73.1314 |       350 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1964-02-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    32.3 |      50 |           nan |              1200 |
| 1980-02-03 00:00:00 |         28025020 | RINCON EL [28025020] |   10.2714 |   -73.1314 |       350 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1964-02-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    33.3 |      50 |           nan |              1200 |
| 1980-02-04 00:00:00 |         28025020 | RINCON EL [28025020] |   10.2714 |   -73.1314 |       350 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1964-02-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    32.3 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_28025020_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28025020_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28025020_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28025020_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 28025040 (2613 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-02 00:00:00 |         28025040 | SAN JOSE D ORIENTE [28025040] |     10.35 |     -73.05 |       850 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | La Paz      | 1975-08-15 00:00:00 | 1998-05-15 00:00:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    29.8 |      50 |           nan |              1200 |
| 1980-01-03 00:00:00 |         28025040 | SAN JOSE D ORIENTE [28025040] |     10.35 |     -73.05 |       850 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | La Paz      | 1975-08-15 00:00:00 | 1998-05-15 00:00:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    30   |      50 |           nan |              1200 |
| 1980-01-04 00:00:00 |         28025040 | SAN JOSE D ORIENTE [28025040] |     10.35 |     -73.05 |       850 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | La Paz      | 1975-08-15 00:00:00 | 1998-05-15 00:00:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    29.8 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_28025040_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28025040_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28025040_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28025040_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 15065040 (3465 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-04-01 00:00:00 |         15065040 | LA PAULINA - AUT [15065040] |   10.8981 |   -72.8285 |       170 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 1966-09-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    35.2 |      50 |           nan |              1200 |
| 1980-04-02 00:00:00 |         15065040 | LA PAULINA - AUT [15065040] |   10.8981 |   -72.8285 |       170 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 1966-09-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    37.2 |      50 |           nan |              1200 |
| 1980-04-03 00:00:00 |         15065040 | LA PAULINA - AUT [15065040] |   10.8981 |   -72.8285 |       170 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 1966-09-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    36.4 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_15065040_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_15065040_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_15065040_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_15065040_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 28015070 (12645 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28015070 | URUMITA [28015070] |   10.5664 |   -73.0164 |       255 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Urumita     | 1975-08-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    32.4 |      50 |           nan |              1200 |
| 1980-01-02 00:00:00 |         28015070 | URUMITA [28015070] |   10.5664 |   -73.0164 |       255 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Urumita     | 1975-08-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    29.8 |      50 |           nan |              1200 |
| 1980-01-03 00:00:00 |         28015070 | URUMITA [28015070] |   10.5664 |   -73.0164 |       255 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Urumita     | 1975-08-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    32.4 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_28015070_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_28015070_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_28015070_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_28015070_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 25025090 (8486 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                   |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25025090 | AEROPUERTO LAS FLORES [25025090] |   9.04633 |   -73.9708 |        34 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Banco    | 1952-02-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    33.6 |      50 |           nan |              1200 |
| 1980-01-02 00:00:00 |         25025090 | AEROPUERTO LAS FLORES [25025090] |   9.04633 |   -73.9708 |        34 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Banco    | 1952-02-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    33.4 |      50 |           nan |              1200 |
| 1980-01-03 00:00:00 |         25025090 | AEROPUERTO LAS FLORES [25025090] |   9.04633 |   -73.9708 |        34 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Banco    | 1952-02-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    33.8 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_25025090_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_25025090_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_25025090_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_25025090_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 25025002 (7701 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio                   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1985-01-06 00:00:00 |         25025002 | LOS ALAMOS - AUT [25025002] |   9.30406 |   -74.2736 |        25 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | San Sebastián De Buenavista | 2013-05-05 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    32.4 |      50 |           nan |              1200 |
| 1985-01-07 00:00:00 |         25025002 | LOS ALAMOS - AUT [25025002] |   9.30406 |   -74.2736 |        25 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | San Sebastián De Buenavista | 2013-05-05 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    33.4 |      50 |           nan |              1200 |
| 1985-01-08 00:00:00 |         25025002 | LOS ALAMOS - AUT [25025002] |   9.30406 |   -74.2736 |        25 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | San Sebastián De Buenavista | 2013-05-05 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    33.6 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_25025002_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_25025002_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_25025002_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_25025002_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 29065020 (9406 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-03-01 00:00:00 |         29065020 | PADELMA [29065020] |   10.7211 |   -74.1997 |        20 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-08-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    33.2 |      50 |           nan |              1200 |
| 1980-03-02 00:00:00 |         29065020 | PADELMA [29065020] |   10.7211 |   -74.1997 |        20 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-08-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    35   |      50 |           nan |              1200 |
| 1980-03-03 00:00:00 |         29065020 | PADELMA [29065020] |   10.7211 |   -74.1997 |        20 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-08-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    33.2 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_29065020_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_29065020_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_29065020_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_29065020_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 29065030 (10537 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29065030 | PRADO SEVILLA [29065030] |   10.7642 |   -74.1547 |        18 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1970-07-15 00:00:00 | 2019-02-07 11:32:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    33.2 |      50 |           nan |              1200 |
| 1980-01-02 00:00:00 |         29065030 | PRADO SEVILLA [29065030] |   10.7642 |   -74.1547 |        18 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1970-07-15 00:00:00 | 2019-02-07 11:32:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    32.8 |      50 |           nan |              1200 |
| 1980-01-03 00:00:00 |         29065030 | PRADO SEVILLA [29065030] |   10.7642 |   -74.1547 |        18 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1970-07-15 00:00:00 | 2019-02-07 11:32:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    33.4 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_29065030_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_29065030_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_29065030_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_29065030_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 25025300 (10066 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio                   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1985-05-01 00:00:00 |         25025300 | SEIS EL [25025300] |   9.68367 |   -74.3223 |        50 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | San Sebastián De Buenavista | 1984-11-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    35.2 |      50 |           nan |              1200 |
| 1985-05-02 00:00:00 |         25025300 | SEIS EL [25025300] |   9.68367 |   -74.3223 |        50 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | San Sebastián De Buenavista | 1984-11-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    35.2 |      50 |           nan |              1200 |
| 1985-05-03 00:00:00 |         25025300 | SEIS EL [25025300] |   9.68367 |   -74.3223 |        50 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | San Sebastián De Buenavista | 1984-11-15 00:00:00 | NaT               | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    35.2 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_25025300_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_25025300_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_25025300_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_25025300_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 15015020 (8859 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion   |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         15015020 | YE LA [15015020] |   10.9924 |   -74.2111 |        20 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1967-07-15 00:00:00 | 2019-02-07 11:34:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    32.2 |      50 |           nan |              1200 |
| 1980-01-02 00:00:00 |         15015020 | YE LA [15015020] |   10.9924 |   -74.2111 |        20 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1967-07-15 00:00:00 | 2019-02-07 11:34:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    32.6 |      50 |           nan |              1200 |
| 1980-01-03 00:00:00 |         15015020 | YE LA [15015020] |   10.9924 |   -74.2111 |        20 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1967-07-15 00:00:00 | 2019-02-07 11:34:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    33   |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_15015020_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_15015020_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_15015020_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_15015020_DensityKDE.png)

<div align="center">



**TMX_CON - Station: 29065010 (893 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion    |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1981-01-01 00:00:00 |         29065010 | ZACAPA [29065010] |   10.5833 |     -74.25 |        30 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1967-07-15 00:00:00 | 1990-04-15 00:00:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    33.6 |      50 |           nan |              1200 |
| 1981-01-02 00:00:00 |         29065010 | ZACAPA [29065010] |   10.5833 |     -74.25 |        30 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1967-07-15 00:00:00 | 1990-04-15 00:00:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    32.4 |      50 |           nan |              1200 |
| 1981-01-03 00:00:00 |         29065010 | ZACAPA [29065010] |   10.5833 |     -74.25 |        30 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1967-07-15 00:00:00 | 1990-04-15 00:00:00 | TEMPERATURA   | TMX_CON    | Temperatura máxima diaria | Diaria       |    31.4 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMX_CON_29065010_TimeSerie.png)
![R.LTWB](Graph/Plot_TMX_CON_29065010_Boxplot.png)
![R.LTWB](Graph/Plot_TMX_CON_29065010_Histogram.png)
![R.LTWB](Graph/Plot_TMX_CON_29065010_DensityKDE.png)


### Analysis from 1980 to 2021 for Etiqueta == "TMN_CON": 209823 (40.75%)

Pivot table: [Pivot_TMN_CON.csv](Pivot_TMN_CON.csv)
![R.LTWB](Graph/Plot_TMN_CON_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 28025502 (12238 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                        |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-02 00:00:00 |         28025502 | AEROPUERTO ALFONSO LOPEZ - [28025502] |   10.4362 |   -73.2477 |       138 | Sinóptica Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 2016-01-07 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    24   |      50 |           nan |              1200 |
| 1980-01-04 00:00:00 |         28025502 | AEROPUERTO ALFONSO LOPEZ - [28025502] |   10.4362 |   -73.2477 |       138 | Sinóptica Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 2016-01-07 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    22.2 |      50 |           nan |              1200 |
| 1980-01-05 00:00:00 |         28025502 | AEROPUERTO ALFONSO LOPEZ - [28025502] |   10.4362 |   -73.2477 |       138 | Sinóptica Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 2016-01-07 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    22.8 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_28025502_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28025502_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28025502_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28025502_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 28025090 (11867 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                 |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio       | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1981-01-03 00:00:00 |         28025090 | CENTENARIO HACIENDA [28025090] |   9.85025 |   -73.2655 |       100 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1976-12-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    22.2 |      50 |           nan |              1200 |
| 1981-01-04 00:00:00 |         28025090 | CENTENARIO HACIENDA [28025090] |   9.85025 |   -73.2655 |       100 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1976-12-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    22.4 |      50 |           nan |              1200 |
| 1981-01-06 00:00:00 |         28025090 | CENTENARIO HACIENDA [28025090] |   9.85025 |   -73.2655 |       100 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1976-12-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    22.6 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_28025090_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28025090_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28025090_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28025090_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 25025250 (12340 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1981-04-01 00:00:00 |         25025250 | CHIRIGUANA [25025250] |   9.36103 |   -73.5934 |        40 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chiriguaná  | 1973-06-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    22.2 |      50 |           nan |              1200 |
| 1981-04-02 00:00:00 |         25025250 | CHIRIGUANA [25025250] |   9.36103 |   -73.5934 |        40 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chiriguaná  | 1973-06-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    24   |      50 |           nan |              1200 |
| 1981-04-04 00:00:00 |         25025250 | CHIRIGUANA [25025250] |   9.36103 |   -73.5934 |        40 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chiriguaná  | 1973-06-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    23.2 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_25025250_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_25025250_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_25025250_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_25025250_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 28015030 (1404 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-02 00:00:00 |         28015030 | CICOLAC [28015030] |   10.4833 |   -73.2667 |       180 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1964-01-15 00:00:00 | 1988-05-15 00:00:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    23.3 |      50 |           nan |              1200 |
| 1980-01-03 00:00:00 |         28015030 | CICOLAC [28015030] |   10.4833 |   -73.2667 |       180 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1964-01-15 00:00:00 | 1988-05-15 00:00:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    24   |      50 |           nan |              1200 |
| 1980-01-04 00:00:00 |         28015030 | CICOLAC [28015030] |   10.4833 |   -73.2667 |       180 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1964-01-15 00:00:00 | 1988-05-15 00:00:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    22   |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_28015030_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28015030_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28015030_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28015030_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 25025330 (9275 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                                  |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1987-09-14 00:00:00 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    23   |      50 |           nan |              1200 |
| 1987-09-15 00:00:00 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    22.2 |      50 |           nan |              1200 |
| 1987-09-16 00:00:00 |         25025330 | COLEGIO AGROPECUARIO PAILITAS  - AUT [25025330] |   8.95422 |   -73.6301 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pailitas    | 1987-09-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    25   |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_25025330_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_25025330_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_25025330_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_25025330_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 23215060 (1248 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                          | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:---------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1983-10-27 00:00:00 |         23215060 | LA GLORIA [23215060] |   8.61528 |   -73.8006 |        35 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Cesar          | La Gloria   | 1995-05-15 00:00:00 | 2018-06-19 10:35:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    20.2 |      50 |           nan |              1200 |
| 1983-10-28 00:00:00 |         23215060 | LA GLORIA [23215060] |   8.61528 |   -73.8006 |        35 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Cesar          | La Gloria   | 1995-05-15 00:00:00 | 2018-06-19 10:35:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    24.6 |      50 |           nan |              1200 |
| 1983-10-29 00:00:00 |         23215060 | LA GLORIA [23215060] |   8.61528 |   -73.8006 |        35 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Cesar          | La Gloria   | 1995-05-15 00:00:00 | 2018-06-19 10:35:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    24.6 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_23215060_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_23215060_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_23215060_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_23215060_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 28025070 (13818 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion               |   Latitud |   Longitud |   Altitud | Categoria         | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio       | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------------|----------:|-----------:|----------:|:------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28025070 | MOTILONIA CODAZZI [28025070] |   10.0018 |   -73.2494 |       180 | Agrometeorológica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1956-01-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    22.8 |      50 |           nan |              1200 |
| 1980-01-02 00:00:00 |         28025070 | MOTILONIA CODAZZI [28025070] |   10.0018 |   -73.2494 |       180 | Agrometeorológica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1956-01-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    23.4 |      50 |           nan |              1200 |
| 1980-01-03 00:00:00 |         28025070 | MOTILONIA CODAZZI [28025070] |   10.0018 |   -73.2494 |       180 | Agrometeorológica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Agustín Codazzi | 1956-01-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    23.4 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_28025070_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28025070_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28025070_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28025070_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 28025020 (13452 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-02-02 00:00:00 |         28025020 | RINCON EL [28025020] |   10.2714 |   -73.1314 |       350 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1964-02-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    18.8 |      50 |           nan |              1200 |
| 1980-02-03 00:00:00 |         28025020 | RINCON EL [28025020] |   10.2714 |   -73.1314 |       350 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1964-02-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    20.6 |      50 |           nan |              1200 |
| 1980-02-04 00:00:00 |         28025020 | RINCON EL [28025020] |   10.2714 |   -73.1314 |       350 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1964-02-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    21.2 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_28025020_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28025020_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28025020_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28025020_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 28025040 (3231 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28025040 | SAN JOSE D ORIENTE [28025040] |     10.35 |     -73.05 |       850 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | La Paz      | 1975-08-15 00:00:00 | 1998-05-15 00:00:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    20.2 |      50 |           nan |              1200 |
| 1980-01-02 00:00:00 |         28025040 | SAN JOSE D ORIENTE [28025040] |     10.35 |     -73.05 |       850 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | La Paz      | 1975-08-15 00:00:00 | 1998-05-15 00:00:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    21   |      50 |           nan |              1200 |
| 1980-01-03 00:00:00 |         28025040 | SAN JOSE D ORIENTE [28025040] |     10.35 |     -73.05 |       850 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | La Paz      | 1975-08-15 00:00:00 | 1998-05-15 00:00:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    19.8 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_28025040_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28025040_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28025040_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28025040_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 28025080 (7636 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28025080 | SOCOMBA [28025080] |   9.68667 |   -73.2406 |       170 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Becerrill   | 1976-12-15 00:00:00 | 2019-02-07 11:41:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    21.8 |      50 |           nan |              1200 |
| 1980-01-02 00:00:00 |         28025080 | SOCOMBA [28025080] |   9.68667 |   -73.2406 |       170 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Becerrill   | 1976-12-15 00:00:00 | 2019-02-07 11:41:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    21.6 |      50 |           nan |              1200 |
| 1980-01-03 00:00:00 |         28025080 | SOCOMBA [28025080] |   9.68667 |   -73.2406 |       170 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Becerrill   | 1976-12-15 00:00:00 | 2019-02-07 11:41:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    21.4 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_28025080_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28025080_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28025080_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28025080_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 28045020 (1052 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1983-01-02 00:00:00 |         28045020 | ALGARROBO [28045020] |     10.15 |   -74.0667 |        60 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Copey    | 1964-02-15 00:00:00 | 1987-04-15 00:00:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    17.6 |      50 |           nan |              1200 |
| 1983-01-03 00:00:00 |         28045020 | ALGARROBO [28045020] |     10.15 |   -74.0667 |        60 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Copey    | 1964-02-15 00:00:00 | 1987-04-15 00:00:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    18.4 |      50 |           nan |              1200 |
| 1983-01-05 00:00:00 |         28045020 | ALGARROBO [28045020] |     10.15 |   -74.0667 |        60 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Copey    | 1964-02-15 00:00:00 | 1987-04-15 00:00:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    18   |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_28045020_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28045020_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28045020_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28045020_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 28035020 (11824 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28035020 | CALLAO EL [28035020] |   10.3631 |   -73.3194 |       110 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-03-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    19.4 |      50 |           nan |              1200 |
| 1980-01-02 00:00:00 |         28035020 | CALLAO EL [28035020] |   10.3631 |   -73.3194 |       110 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-03-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    19.6 |      50 |           nan |              1200 |
| 1980-01-03 00:00:00 |         28035020 | CALLAO EL [28035020] |   10.3631 |   -73.3194 |       110 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-03-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    19   |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_28035020_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28035020_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28035020_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28035020_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 28045040 (1274 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1987-09-11 00:00:00 |         28045040 | GUAIRA LA HACIENDA [28045040] |   9.61667 |      -73.8 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |      23 |      50 |           nan |              1200 |
| 1987-09-13 00:00:00 |         28045040 | GUAIRA LA HACIENDA [28045040] |   9.61667 |      -73.8 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |      25 |      50 |           nan |              1200 |
| 1987-09-14 00:00:00 |         28045040 | GUAIRA LA HACIENDA [28045040] |   9.61667 |      -73.8 |        50 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1987-09-15 00:00:00 | 1994-07-15 00:00:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |      19 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_28045040_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28045040_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28045040_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28045040_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 28035070 (42 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion             |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 2012-12-01 00:00:00 |         28035070 | GUATAPURI - AUT [28035070] |   10.7321 |   -73.3924 |      1315 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 2006-02-26 00:00:00 | 2018-06-11 10:25:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    21.8 |      50 |           nan |              1200 |
| 2012-12-02 00:00:00 |         28035070 | GUATAPURI - AUT [28035070] |   10.7321 |   -73.3924 |      1315 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 2006-02-26 00:00:00 | 2018-06-11 10:25:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    23.8 |      50 |           nan |              1200 |
| 2012-12-03 00:00:00 |         28035070 | GUATAPURI - AUT [28035070] |   10.7321 |   -73.3924 |      1315 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 2006-02-26 00:00:00 | 2018-06-11 10:25:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    21.2 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_28035070_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28035070_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28035070_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28035070_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 28035040 (13405 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1981-06-01 00:00:00 |         28035040 | GUAYMARAL [28035040] |   9.90492 |   -73.6475 |        50 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1972-08-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    24.2 |      50 |           nan |              1200 |
| 1981-06-02 00:00:00 |         28035040 | GUAYMARAL [28035040] |   9.90492 |   -73.6475 |        50 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1972-08-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    24   |      50 |           nan |              1200 |
| 1981-06-03 00:00:00 |         28035040 | GUAYMARAL [28035040] |   9.90492 |   -73.6475 |        50 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1972-08-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    23.2 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_28035040_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28035040_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28035040_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28035040_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 28035010 (10557 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-03 00:00:00 |         28035010 | VILLA ROSA [28035010] |   10.1907 |   -73.5474 |        70 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-03-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    22.4 |      50 |           nan |              1200 |
| 1980-01-04 00:00:00 |         28035010 | VILLA ROSA [28035010] |   10.1907 |   -73.5474 |        70 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-03-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    23.6 |      50 |           nan |              1200 |
| 1980-01-05 00:00:00 |         28035010 | VILLA ROSA [28035010] |   10.1907 |   -73.5474 |        70 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1968-03-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    22.2 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_28035010_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28035010_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28035010_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28035010_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 15065040 (4949 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-09-05 00:00:00 |         15065040 | LA PAULINA - AUT [15065040] |   10.8981 |   -72.8285 |       170 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 1966-09-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    22   |      50 |           nan |              1200 |
| 1980-09-06 00:00:00 |         15065040 | LA PAULINA - AUT [15065040] |   10.8981 |   -72.8285 |       170 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 1966-09-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    23.6 |      50 |           nan |              1200 |
| 1980-09-12 00:00:00 |         15065040 | LA PAULINA - AUT [15065040] |   10.8981 |   -72.8285 |       170 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 1966-09-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    24.4 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_15065040_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_15065040_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_15065040_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_15065040_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 28015070 (12475 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28015070 | URUMITA [28015070] |   10.5664 |   -73.0164 |       255 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Urumita     | 1975-08-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    23   |      50 |           nan |              1200 |
| 1980-01-02 00:00:00 |         28015070 | URUMITA [28015070] |   10.5664 |   -73.0164 |       255 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Urumita     | 1975-08-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    23.5 |      50 |           nan |              1200 |
| 1980-01-04 00:00:00 |         28015070 | URUMITA [28015070] |   10.5664 |   -73.0164 |       255 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Urumita     | 1975-08-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    22   |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_28015070_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_28015070_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_28015070_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_28015070_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 25025002 (10733 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio                   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1985-01-06 00:00:00 |         25025002 | LOS ALAMOS - AUT [25025002] |   9.30406 |   -74.2736 |        25 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | San Sebastián De Buenavista | 2013-05-05 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    23.4 |      50 |           nan |              1200 |
| 1985-01-07 00:00:00 |         25025002 | LOS ALAMOS - AUT [25025002] |   9.30406 |   -74.2736 |        25 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | San Sebastián De Buenavista | 2013-05-05 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    19.6 |      50 |           nan |              1200 |
| 1985-01-08 00:00:00 |         25025002 | LOS ALAMOS - AUT [25025002] |   9.30406 |   -74.2736 |        25 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | San Sebastián De Buenavista | 2013-05-05 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    19   |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_25025002_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_25025002_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_25025002_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_25025002_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 15015020 (9964 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion   |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         15015020 | YE LA [15015020] |   10.9924 |   -74.2111 |        20 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1967-07-15 00:00:00 | 2019-02-07 11:34:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    23.2 |      50 |           nan |              1200 |
| 1980-01-02 00:00:00 |         15015020 | YE LA [15015020] |   10.9924 |   -74.2111 |        20 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1967-07-15 00:00:00 | 2019-02-07 11:34:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    22.4 |      50 |           nan |              1200 |
| 1980-01-03 00:00:00 |         15015020 | YE LA [15015020] |   10.9924 |   -74.2111 |        20 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1967-07-15 00:00:00 | 2019-02-07 11:34:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    20.8 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_15015020_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_15015020_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_15015020_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_15015020_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 25025090 (9774 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                   |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25025090 | AEROPUERTO LAS FLORES [25025090] |   9.04633 |   -73.9708 |        34 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Banco    | 1952-02-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    24.2 |      50 |           nan |              1200 |
| 1980-01-02 00:00:00 |         25025090 | AEROPUERTO LAS FLORES [25025090] |   9.04633 |   -73.9708 |        34 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Banco    | 1952-02-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    24.2 |      50 |           nan |              1200 |
| 1980-01-03 00:00:00 |         25025090 | AEROPUERTO LAS FLORES [25025090] |   9.04633 |   -73.9708 |        34 | Climática Principal | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Banco    | 1952-02-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    24.6 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_25025090_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_25025090_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_25025090_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_25025090_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 29065020 (12983 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-03-01 00:00:00 |         29065020 | PADELMA [29065020] |   10.7211 |   -74.1997 |        20 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-08-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    21.8 |      50 |           nan |              1200 |
| 1980-03-02 00:00:00 |         29065020 | PADELMA [29065020] |   10.7211 |   -74.1997 |        20 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-08-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    21.4 |      50 |           nan |              1200 |
| 1980-03-04 00:00:00 |         29065020 | PADELMA [29065020] |   10.7211 |   -74.1997 |        20 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1967-08-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    22.2 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_29065020_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_29065020_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_29065020_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_29065020_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 29065030 (11526 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29065030 | PRADO SEVILLA [29065030] |   10.7642 |   -74.1547 |        18 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1970-07-15 00:00:00 | 2019-02-07 11:32:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    21.4 |      50 |           nan |              1200 |
| 1980-01-02 00:00:00 |         29065030 | PRADO SEVILLA [29065030] |   10.7642 |   -74.1547 |        18 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1970-07-15 00:00:00 | 2019-02-07 11:32:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    21.8 |      50 |           nan |              1200 |
| 1980-01-04 00:00:00 |         29065030 | PRADO SEVILLA [29065030] |   10.7642 |   -74.1547 |        18 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1970-07-15 00:00:00 | 2019-02-07 11:32:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    20.8 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_29065030_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_29065030_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_29065030_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_29065030_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 25025300 (11693 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio                   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------------------|:--------------------|:------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1985-05-01 00:00:00 |         25025300 | SEIS EL [25025300] |   9.68367 |   -74.3223 |        50 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | San Sebastián De Buenavista | 1984-11-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    20.4 |      50 |           nan |              1200 |
| 1985-05-02 00:00:00 |         25025300 | SEIS EL [25025300] |   9.68367 |   -74.3223 |        50 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | San Sebastián De Buenavista | 1984-11-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    20.6 |      50 |           nan |              1200 |
| 1985-05-03 00:00:00 |         25025300 | SEIS EL [25025300] |   9.68367 |   -74.3223 |        50 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | San Sebastián De Buenavista | 1984-11-15 00:00:00 | NaT               | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    20.8 |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_25025300_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_25025300_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_25025300_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_25025300_DensityKDE.png)

<div align="center">



**TMN_CON - Station: 29065010 (1063 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion    |   Latitud |   Longitud |   Altitud | Categoria           | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie          | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------|----------:|-----------:|----------:|:--------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:--------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29065010 | ZACAPA [29065010] |   10.5833 |     -74.25 |        30 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1967-07-15 00:00:00 | 1990-04-15 00:00:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    21.4 |      50 |           nan |              1200 |
| 1980-01-04 00:00:00 |         29065010 | ZACAPA [29065010] |   10.5833 |     -74.25 |        30 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1967-07-15 00:00:00 | 1990-04-15 00:00:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    23   |      50 |           nan |              1200 |
| 1980-01-05 00:00:00 |         29065010 | ZACAPA [29065010] |   10.5833 |     -74.25 |        30 | Climática Ordinaria | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | El Retén    | 1967-07-15 00:00:00 | 1990-04-15 00:00:00 | TEMPERATURA   | TMN_CON    | Temperatura mínima diaria | Diaria       |    20   |      50 |           nan |              1200 |

![R.LTWB](Graph/Plot_TMN_CON_29065010_TimeSerie.png)
![R.LTWB](Graph/Plot_TMN_CON_29065010_Boxplot.png)
![R.LTWB](Graph/Plot_TMN_CON_29065010_Histogram.png)
![R.LTWB](Graph/Plot_TMN_CON_29065010_DensityKDE.png)


### Analysis from 1980 to 2021 for Etiqueta == "EV_TT_D": 4821 (0.94%)

Pivot table: [Pivot_EV_TT_D.csv](Pivot_EV_TT_D.csv)
![R.LTWB](Graph/Plot_EV_TT_D_TimeSerie.png)
![R.LTWB](Graph/Plot_EV_TT_D_DensityKDE.png)

<div align="center">



**EV_TT_D - Station: 29065130 (4821 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion               |   Latitud |   Longitud |   Altitud | Categoria         | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie         | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------------|----------:|-----------:|----------:|:------------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:------------------|:--------------|:-----------|:-------------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 2008-10-20 00:00:00 |         29065130 | LA GRAN VIA - AUT [29065130] |     10.85 |   -74.1333 |        30 | Agrometeorológica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 2008-01-10 00:00:00 | NaT               | EVAPORACION   | EV_TT_D    | Evaporación total diaria | Diaria       |       0 |      50 |           nan |               900 |
| 2008-10-21 00:00:00 |         29065130 | LA GRAN VIA - AUT [29065130] |     10.85 |   -74.1333 |        30 | Agrometeorológica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 2008-01-10 00:00:00 | NaT               | EVAPORACION   | EV_TT_D    | Evaporación total diaria | Diaria       |       0 |      -1 |           nan |               900 |
| 2008-10-22 00:00:00 |         29065130 | LA GRAN VIA - AUT [29065130] |     10.85 |   -74.1333 |        30 | Agrometeorológica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 2008-01-10 00:00:00 | NaT               | EVAPORACION   | EV_TT_D    | Evaporación total diaria | Diaria       |       0 |      -1 |           nan |               900 |

![R.LTWB](Graph/Plot_EV_TT_D_29065130_TimeSerie.png)
![R.LTWB](Graph/Plot_EV_TT_D_29065130_Boxplot.png)
![R.LTWB](Graph/Plot_EV_TT_D_29065130_Histogram.png)
![R.LTWB](Graph/Plot_EV_TT_D_29065130_DensityKDE.png)


### Analysis from 1980 to 2021 for Etiqueta == "Q_MEDIA_M": 21126 (4.1%)

Pivot table: [Pivot_Q_MEDIA_M.csv](Pivot_Q_MEDIA_M.csv)
![R.LTWB](Graph/Plot_Q_MEDIA_M_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 25027400 (489 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio         | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado | Calificador        |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|:-------------------|------------------:|
| 1980-01-01 00:00:00 |         25027400 | ALTO DEL ROSARIO [25027400] |   8.79444 |   -74.1603 |        24 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Altos Del Rosario | 1973-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |  128.4  |      50 | nan                |               900 |
| 1980-02-01 00:00:00 |         25027400 | ALTO DEL ROSARIO [25027400] |   8.79444 |   -74.1603 |        24 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Altos Del Rosario | 1973-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   95.48 |      50 | nan                |               900 |
| 1980-03-01 00:00:00 |         25027400 | ALTO DEL ROSARIO [25027400] |   8.79444 |   -74.1603 |        24 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Altos Del Rosario | 1973-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   49.44 |       4 | EST. INTERPOLACION |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027400_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027400_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027400_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027400_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 25027360 (462 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25027360 | ARMENIA [25027360] |   8.89833 |     -74.39 |        22 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Pinillos    | 1973-03-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    2350 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25027360 | ARMENIA [25027360] |   8.89833 |     -74.39 |        22 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Pinillos    | 1973-03-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    2090 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25027360 | ARMENIA [25027360] |   8.89833 |     -74.39 |        22 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Pinillos    | 1973-03-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    1723 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027360_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027360_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027360_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027360_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 25027620 (415 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado | Calificador    |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|:---------------|------------------:|
| 1980-01-01 00:00:00 |         25027620 | CHAPETONA LA [25027620] |    8.8875 |   -73.9692 |        30 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | El Peñón    | 1974-09-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |  34.14  |       4 | EST. REGRESION |               900 |
| 1980-02-01 00:00:00 |         25027620 | CHAPETONA LA [25027620] |    8.8875 |   -73.9692 |        30 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | El Peñón    | 1974-09-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |  22.07  |       4 | EST. REGRESION |               900 |
| 1980-03-01 00:00:00 |         25027620 | CHAPETONA LA [25027620] |    8.8875 |   -73.9692 |        30 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | El Peñón    | 1974-09-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   3.943 |       4 | EST. REGRESION |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027620_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027620_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027620_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027620_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 25027490 (504 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio          | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25027490 | LAS AGUADAS [25027490] |      8.95 |     -74.05 |        27 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Martín De Loba | 1973-03-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    2761 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25027490 | LAS AGUADAS [25027490] |      8.95 |     -74.05 |        27 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Martín De Loba | 1973-03-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    2394 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25027490 | LAS AGUADAS [25027490] |      8.95 |     -74.05 |        27 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | San Martín De Loba | 1973-03-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    1843 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027490_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027490_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027490_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027490_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 25027390 (456 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio         | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25027390 | PALOMAS LAS [25027390] |   8.83056 |   -74.1706 |        24 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Altos Del Rosario | 1973-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    2550 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25027390 | PALOMAS LAS [25027390] |   8.83056 |   -74.1706 |        24 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Altos Del Rosario | 1973-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    2179 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25027390 | PALOMAS LAS [25027390] |   8.83056 |   -74.1706 |        24 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Altos Del Rosario | 1973-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    1674 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027390_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027390_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027390_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027390_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 25027330 (484 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado | Calificador        |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|:-------------------|------------------:|
| 1980-01-01 00:00:00 |         25027330 | PENONCITO [25027330] |   8.98972 |   -73.9472 |        28 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | El Peñón    | 1972-09-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    2902 |      50 | nan                |               900 |
| 1980-02-01 00:00:00 |         25027330 | PENONCITO [25027330] |   8.98972 |   -73.9472 |        28 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | El Peñón    | 1972-09-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    2421 |       4 | EST. INTERPOLACION |               900 |
| 1980-03-01 00:00:00 |         25027330 | PENONCITO [25027330] |   8.98972 |   -73.9472 |        28 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | El Peñón    | 1972-09-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    2001 |      50 | nan                |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027330_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027330_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027330_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027330_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 25027410 (423 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                          | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:---------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25027410 | REGIDOR [25027410] |   8.66633 |   -73.8208 |        35 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Bolivar        | Regidor     | 1973-04-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    2200 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25027410 | REGIDOR [25027410] |   8.66633 |   -73.8208 |        35 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Bolivar        | Regidor     | 1973-04-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    2118 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25027410 | REGIDOR [25027410] |   8.66633 |   -73.8208 |        35 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Bolivar        | Regidor     | 1973-04-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    1546 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027410_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027410_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027410_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027410_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 25027320 (473 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25027320 | SAN ROQUE [25027320] |      9.07 |     -74.16 |        24 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Margarita   | 1972-09-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |  219.5  |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25027320 | SAN ROQUE [25027320] |      9.07 |     -74.16 |        24 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Margarita   | 1972-09-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |  118.8  |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25027320 | SAN ROQUE [25027320] |      9.07 |     -74.16 |        24 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Margarita   | 1972-09-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   35.15 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027320_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027320_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027320_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027320_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 25027420 (482 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion         |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25027420 | VICTORIA LA [25027420] |     8.965 |   -74.2208 |        24 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Margarita   | 1973-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      | 198     |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25027420 | VICTORIA LA [25027420] |     8.965 |   -74.2208 |        24 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Margarita   | 1973-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      | 118.6   |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25027420 | VICTORIA LA [25027420] |     8.965 |   -74.2208 |        24 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Margarita   | 1973-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   4.306 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027420_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027420_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027420_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027420_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 25027630 (461 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio        | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado | Calificador        |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-----------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|:-------------------|------------------:|
| 1980-01-01 00:00:00 |         25027630 | RIO NUEVO [25027630] |   8.80972 |   -74.2544 |        23 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Barranco De Loba | 1971-08-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    2480 |       4 | EST. REGRESION     |               900 |
| 1980-02-01 00:00:00 |         25027630 | RIO NUEVO [25027630] |   8.80972 |   -74.2544 |        23 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Barranco De Loba | 1971-08-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    2177 |       4 | EST. INTERPOLACION |               900 |
| 1980-03-01 00:00:00 |         25027630 | RIO NUEVO [25027630] |   8.80972 |   -74.2544 |        23 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Bolivar        | Barranco De Loba | 1971-08-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    1863 |       4 | EST. REGRESION     |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027630_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027630_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027630_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027630_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 28017120 (230 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                     |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado | Calificador    |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|:---------------|------------------:|
| 1982-01-01 00:00:00 |         28017120 | ARIGUANI HACIENDA - AUT [28017120] |   10.5742 |    -73.397 |       550 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1980-12-15 00:00:00 | 2010-09-29 00:00:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   6.809 |       4 | EST. REGRESION |               900 |
| 1982-02-01 00:00:00 |         28017120 | ARIGUANI HACIENDA - AUT [28017120] |   10.5742 |    -73.397 |       550 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1980-12-15 00:00:00 | 2010-09-29 00:00:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   6.162 |       4 | EST. REGRESION |               900 |
| 1982-03-01 00:00:00 |         28017120 | ARIGUANI HACIENDA - AUT [28017120] |   10.5742 |    -73.397 |       550 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1980-12-15 00:00:00 | 2010-09-29 00:00:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   5.396 |      50 | nan            |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_28017120_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017120_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017120_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017120_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 25027590 (339 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25027590 | CAIMANCITO [25027590] |   9.57114 |   -73.7947 |        40 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Astrea      | 1974-07-15 00:00:00 | 2019-02-07 11:40:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   54.68 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25027590 | CAIMANCITO [25027590] |   9.57114 |   -73.7947 |        40 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Astrea      | 1974-07-15 00:00:00 | 2019-02-07 11:40:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   25.86 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25027590 | CAIMANCITO [25027590] |   9.57114 |   -73.7947 |        40 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Astrea      | 1974-07-15 00:00:00 | 2019-02-07 11:40:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   12.85 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027590_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027590_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027590_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027590_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 28017150 (52 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 2017-06-01 00:00:00 |         28017150 | CHEMESQUEMENA [28017150] |   10.7122 |   -73.4022 |      1160 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 2014-01-10 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      | 7.90542 |       4 |           nan |               900 |
| 2017-07-01 00:00:00 |         28017150 | CHEMESQUEMENA [28017150] |   10.7122 |   -73.4022 |      1160 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 2014-01-10 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      | 5.59158 |       4 |           nan |               900 |
| 2017-08-01 00:00:00 |         28017150 | CHEMESQUEMENA [28017150] |   10.7122 |   -73.4022 |      1160 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 2014-01-10 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      | 7.43764 |       4 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_28017150_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017150_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017150_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017150_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 28027030 (439 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28027030 | FLORES LAS [28027030] |   10.0965 |   -73.2435 |       112 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | La Paz      | 1962-10-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   2.045 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28027030 | FLORES LAS [28027030] |   10.0965 |   -73.2435 |       112 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | La Paz      | 1962-10-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   1.289 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28027030 | FLORES LAS [28027030] |   10.0965 |   -73.2435 |       112 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | La Paz      | 1962-10-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.617 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_28027030_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027030_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027030_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027030_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 25027080 (449 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                     |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25027080 | GRACIAS A DIOS HACIENDA [25027080] |   9.19447 |   -73.5765 |        46 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Curumaní    | 1963-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   2.381 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25027080 | GRACIAS A DIOS HACIENDA [25027080] |   9.19447 |   -73.5765 |        46 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Curumaní    | 1963-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   1.961 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25027080 | GRACIAS A DIOS HACIENDA [25027080] |   9.19447 |   -73.5765 |        46 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Curumaní    | 1963-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   1.481 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027080_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027080_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027080_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027080_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 28027020 (399 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28027020 | MATILDE LA [28027020] |   10.1656 |   -73.2583 |       114 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1962-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   1.363 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28027020 | MATILDE LA [28027020] |   10.1656 |   -73.2583 |       114 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1962-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   1.7   |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28027020 | MATILDE LA [28027020] |   10.1656 |   -73.2583 |       114 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | San Diego   | 1962-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.833 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_28027020_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027020_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027020_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027020_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 28017110 (465 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion     |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28017110 | MINA LA [28017110] |   10.6867 |   -73.2698 |       429 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1969-12-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   3.582 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28017110 | MINA LA [28017110] |   10.6867 |   -73.2698 |       429 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1969-12-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   2.843 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28017110 | MINA LA [28017110] |   10.6867 |   -73.2698 |       429 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1969-12-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   2.695 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_28017110_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017110_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017110_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017110_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 25027890 (424 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25027890 | PUENTE CARRETERA [25027890] |   9.34233 |   -73.4909 |       120 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chiriguaná  | 1978-09-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   1.176 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25027890 | PUENTE CARRETERA [25027890] |   9.34233 |   -73.4909 |       120 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chiriguaná  | 1978-09-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.707 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25027890 | PUENTE CARRETERA [25027890] |   9.34233 |   -73.4909 |       120 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Chiriguaná  | 1978-09-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.201 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027890_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027890_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027890_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027890_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 28017050 (263 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado | Calificador    |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|:---------------|------------------:|
| 1980-01-01 00:00:00 |         28017050 | REPOSO EL [28017050] |   10.5272 |   -73.3364 |       350 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1958-03-15 00:00:00 | 2019-02-07 11:41:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   9.391 |      50 | nan            |               900 |
| 1980-02-01 00:00:00 |         28017050 | REPOSO EL [28017050] |   10.5272 |   -73.3364 |       350 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1958-03-15 00:00:00 | 2019-02-07 11:41:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   4.655 |       4 | EST. REGRESION |               900 |
| 1980-03-01 00:00:00 |         28017050 | REPOSO EL [28017050] |   10.5272 |   -73.3364 |       350 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1958-03-15 00:00:00 | 2019-02-07 11:41:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   5.295 |       4 | EST. REGRESION |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_28017050_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017050_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017050_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017050_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 28027040 (412 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28027040 | SANTA TERESA [28027040] |   9.91594 |   -73.2837 |        80 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Becerrill   | 1962-11-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.944 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28027040 | SANTA TERESA [28027040] |   9.91594 |   -73.2837 |        80 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Becerrill   | 1962-11-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.519 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28027040 | SANTA TERESA [28027040] |   9.91594 |   -73.2837 |        80 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Becerrill   | 1962-11-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.377 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_28027040_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027040_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027040_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027040_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 28027050 (349 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado | Calificador    |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|:---------------|------------------:|
| 1980-01-01 00:00:00 |         28027050 | BECERRIL [28027050] |   9.68661 |   -73.2792 |       106 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Becerrill   | 1963-06-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    1.28 |       4 | EST. REGRESION |               900 |
| 1980-02-01 00:00:00 |         28027050 | BECERRIL [28027050] |   9.68661 |   -73.2792 |       106 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Becerrill   | 1963-06-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    1.6  |       4 | EST. REGRESION |               900 |
| 1980-03-01 00:00:00 |         28027050 | BECERRIL [28027050] |   9.68661 |   -73.2792 |       106 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Becerrill   | 1963-06-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    0.9  |       4 | EST. REGRESION |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_28027050_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027050_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027050_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027050_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 28037060 (482 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28037060 | CANTACLARO [28037060] |   10.0885 |   -73.7328 |       120 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1963-03-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.531 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28037060 | CANTACLARO [28037060] |   10.0885 |   -73.7328 |       120 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1963-03-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.464 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28037060 | CANTACLARO [28037060] |   10.0885 |   -73.7328 |       120 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1963-03-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.373 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_28037060_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037060_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037060_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037060_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 28037020 (362 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                 |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28037020 | CONVENCION HACIENDA [28037020] |   10.2678 |   -73.4171 |       104 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1962-12-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   2.411 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28037020 | CONVENCION HACIENDA [28037020] |   10.2678 |   -73.4171 |       104 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1962-12-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   2.078 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28037020 | CONVENCION HACIENDA [28037020] |   10.2678 |   -73.4171 |       104 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1962-12-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.438 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_28037020_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037020_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037020_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037020_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 28027160 (372 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28027160 | ISLANDIA [28027160] |   9.63253 |   -73.6357 |        45 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1974-11-15 00:00:00 | 2019-02-07 11:40:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   3.109 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28027160 | ISLANDIA [28027160] |   9.63253 |   -73.6357 |        45 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1974-11-15 00:00:00 | 2019-02-07 11:40:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   3.2   |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28027160 | ISLANDIA [28027160] |   9.63253 |   -73.6357 |        45 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1974-11-15 00:00:00 | 2019-02-07 11:40:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   1.236 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_28027160_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027160_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027160_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28027160_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 28037040 (474 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28037040 | MARIANGOLA [28037040] |   10.1874 |   -73.5852 |        90 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1963-01-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.564 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28037040 | MARIANGOLA [28037040] |   10.1874 |   -73.5852 |        90 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1963-01-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.212 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28037040 | MARIANGOLA [28037040] |   10.1874 |   -73.5852 |        90 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1963-01-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.196 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_28037040_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037040_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037040_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037040_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 28047020 (474 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio    | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28047020 | PUEBLO BELLO [28047020] |   10.4198 |   -73.5888 |      1125 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pueblo Bello | 1963-01-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   1.224 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28047020 | PUEBLO BELLO [28047020] |   10.4198 |   -73.5888 |      1125 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pueblo Bello | 1963-01-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   1.284 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28047020 | PUEBLO BELLO [28047020] |   10.4198 |   -73.5888 |      1125 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Pueblo Bello | 1963-01-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.594 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_28047020_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047020_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047020_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047020_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 28037010 (437 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28037010 | PUENTE CALLAO [28037010] |   10.3629 |   -73.3174 |       120 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1962-12-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.424 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28037010 | PUENTE CALLAO [28037010] |   10.3629 |   -73.3174 |       120 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1962-12-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.127 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28037010 | PUENTE CALLAO [28037010] |   10.3629 |   -73.3174 |       120 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1962-12-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.098 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_28037010_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037010_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037010_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037010_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 28037090 (410 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                  |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28037090 | PUENTE CANOAS  - AUT [28037090] |   9.64633 |   -73.6518 |        45 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1965-04-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |  30.47  |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28037090 | PUENTE CANOAS  - AUT [28037090] |   9.64633 |   -73.6518 |        45 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1965-04-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |  21.78  |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28037090 | PUENTE CANOAS  - AUT [28037090] |   9.64633 |   -73.6518 |        45 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Paso     | 1965-04-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   5.548 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_28037090_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037090_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037090_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037090_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 28037130 (422 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28037130 | PUENTE CARRETERA [28037130] |   10.1575 |   -73.6248 |        80 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1972-10-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.899 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28037130 | PUENTE CARRETERA [28037130] |   10.1575 |   -73.6248 |        80 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1972-10-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.523 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28037130 | PUENTE CARRETERA [28037130] |   10.1575 |   -73.6248 |        80 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1972-10-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.443 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_28037130_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037130_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037130_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037130_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 28037030 (474 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                    |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28037030 | PUENTE SALGUERO  - AUT [28037030] |   10.3841 |   -73.2325 |       113 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1962-12-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |  16.16  |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28037030 | PUENTE SALGUERO  - AUT [28037030] |   10.3841 |   -73.2325 |       113 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1962-12-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |  10.05  |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28037030 | PUENTE SALGUERO  - AUT [28037030] |   10.3841 |   -73.2325 |       113 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | Valledupar  | 1962-12-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   6.077 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_28037030_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037030_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037030_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28037030_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 28047080 (96 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado | Calificador    |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|:---------------|------------------:|
| 1982-01-01 00:00:00 |         28047080 | BELLEZA LA [28047080] |   10.3333 |     -73.95 |       250 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Copey    | 1982-06-15 00:00:00 | 1992-09-15 00:00:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    13.8 |       4 | EST. REGRESION |               900 |
| 1982-02-01 00:00:00 |         28047080 | BELLEZA LA [28047080] |   10.3333 |     -73.95 |       250 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Copey    | 1982-06-15 00:00:00 | 1992-09-15 00:00:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    15.2 |       4 | EST. REGRESION |               900 |
| 1982-03-01 00:00:00 |         28047080 | BELLEZA LA [28047080] |   10.3333 |     -73.95 |       250 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Copey    | 1982-06-15 00:00:00 | 1992-09-15 00:00:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    10.8 |       4 | EST. REGRESION |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_28047080_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047080_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047080_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047080_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 28047040 (247 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28047040 | PUENTE CARRETERA [28047040] |    10.271 |   -73.9727 |       151 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Copey    | 1963-02-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   1.46  |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28047040 | PUENTE CARRETERA [28047040] |    10.271 |   -73.9727 |       151 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Copey    | 1963-02-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.998 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28047040 | PUENTE CARRETERA [28047040] |    10.271 |   -73.9727 |       151 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Cesar          | El Copey    | 1963-02-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.747 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_28047040_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047040_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047040_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047040_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 15067210 (28 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion            |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio          | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 2012-04-01 00:00:00 |         15067210 | CARACOLI - AUT [15067210] |   10.9501 |    -73.051 |       460 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | San Juan Del Cesar | 2011-01-12 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   8.695 |      50 |           nan |               900 |
| 2012-05-01 00:00:00 |         15067210 | CARACOLI - AUT [15067210] |   10.9501 |    -73.051 |       460 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | San Juan Del Cesar | 2011-01-12 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |  13.27  |      50 |           nan |               900 |
| 2012-06-01 00:00:00 |         15067210 | CARACOLI - AUT [15067210] |   10.9501 |    -73.051 |       460 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | San Juan Del Cesar | 2011-01-12 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   7.892 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_15067210_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067210_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067210_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067210_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 15067020 (328 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         15067020 | CERCADO EL-AUTOMAT [15067020] |   10.9075 |   -73.0083 |       335 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 2004-04-09 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   6.81  |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         15067020 | CERCADO EL-AUTOMAT [15067020] |   10.9075 |   -73.0083 |       335 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 2004-04-09 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   5.829 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         15067020 | CERCADO EL-AUTOMAT [15067020] |   10.9075 |   -73.0083 |       335 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 2004-04-09 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   3.833 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_15067020_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067020_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067020_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067020_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 28017080 (465 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion              |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio          | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28017080 | CORRAL DE PIEDRA [28017080] |   10.8189 |   -73.0551 |       275 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | San Juan Del Cesar | 1970-03-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.865 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28017080 | CORRAL DE PIEDRA [28017080] |   10.8189 |   -73.0551 |       275 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | San Juan Del Cesar | 1970-03-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.751 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28017080 | CORRAL DE PIEDRA [28017080] |   10.8189 |   -73.0551 |       275 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | San Juan Del Cesar | 1970-03-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.655 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_28017080_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017080_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017080_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017080_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 15067200 (115 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion               |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 2010-06-01 00:00:00 |         15067200 | EL SILENCIO - AUT [15067200] |   10.9171 |   -72.9153 |       255 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 2010-06-25 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   6.725 |      50 |           nan |               900 |
| 2010-07-01 00:00:00 |         15067200 | EL SILENCIO - AUT [15067200] |   10.9171 |   -72.9153 |       255 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 2010-06-25 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   8.645 |      50 |           nan |               900 |
| 2010-08-01 00:00:00 |         15067200 | EL SILENCIO - AUT [15067200] |   10.9171 |   -72.9153 |       255 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Fonseca     | 2010-06-25 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   5.524 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_15067200_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067200_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067200_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067200_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 15067080 (291 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-07-01 00:00:00 |         15067080 | MAGUEYES LOS [15067080] |   10.9467 |   -72.7723 |       140 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Barrancas   | 1980-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.544 |      50 |           nan |               900 |
| 1980-08-01 00:00:00 |         15067080 | MAGUEYES LOS [15067080] |   10.9467 |   -72.7723 |       140 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Barrancas   | 1980-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.78  |      50 |           nan |               900 |
| 1980-09-01 00:00:00 |         15067080 | MAGUEYES LOS [15067080] |   10.9467 |   -72.7723 |       140 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Barrancas   | 1980-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.88  |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_15067080_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067080_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067080_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067080_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 15067130 (388 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado | Calificador        |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|:-------------------|------------------:|
| 1987-08-01 00:00:00 |         15067130 | POZO HONDO [15067130] |   10.9986 |   -72.8196 |       210 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Barrancas   | 1987-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.12  |      50 | nan                |               900 |
| 1987-09-01 00:00:00 |         15067130 | POZO HONDO [15067130] |   10.9986 |   -72.8196 |       210 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Barrancas   | 1987-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.271 |       4 | EST. OTROS METODOS |               900 |
| 1987-10-01 00:00:00 |         15067130 | POZO HONDO [15067130] |   10.9986 |   -72.8196 |       210 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Barrancas   | 1987-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.499 |      50 | nan                |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_15067130_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067130_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067130_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067130_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 15067150 (148 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                  |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 2008-11-01 00:00:00 |         15067150 | PUENTE GUAJIRO - AUT [15067150] |   10.9264 |   -72.8044 |       485 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Barrancas   | 2008-07-22 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |  25     |       4 |           nan |               900 |
| 2008-12-01 00:00:00 |         15067150 | PUENTE GUAJIRO - AUT [15067150] |   10.9264 |   -72.8044 |       485 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Barrancas   | 2008-07-22 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |  11.57  |       4 |           nan |               900 |
| 2009-04-01 00:00:00 |         15067150 | PUENTE GUAJIRO - AUT [15067150] |   10.9264 |   -72.8044 |       485 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Barrancas   | 2008-07-22 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   1.934 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_15067150_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067150_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067150_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067150_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 15067170 (156 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado | Calificador        |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|:-------------------|------------------:|
| 2008-12-01 00:00:00 |         15067170 | SAN FRANCISCO [15067170] |   10.9912 |   -72.7561 |       450 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Barrancas   | 2008-07-22 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |  10.19  |       4 | nan                |               900 |
| 2009-01-01 00:00:00 |         15067170 | SAN FRANCISCO [15067170] |   10.9912 |   -72.7561 |       450 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Barrancas   | 2008-07-22 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   4.381 |       4 | EST. OTROS METODOS |               900 |
| 2009-02-01 00:00:00 |         15067170 | SAN FRANCISCO [15067170] |   10.9912 |   -72.7561 |       450 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | Barrancas   | 2008-07-22 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   7.026 |       4 | EST. OTROS METODOS |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_15067170_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067170_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067170_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_15067170_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 28017140 (41 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                     |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio          | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado | Calificador        |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:-------------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|:-------------------|------------------:|
| 2010-01-01 00:00:00 |         28017140 | CORRAL DE PIEDRA  - AUT [28017140] |     10.83 |     -73.07 |       275 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | San Juan Del Cesar | 2004-09-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   76114 |      50 | nan                |               900 |
| 2010-04-01 00:00:00 |         28017140 | CORRAL DE PIEDRA  - AUT [28017140] |     10.83 |     -73.07 |       275 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | San Juan Del Cesar | 2004-09-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   50138 |       4 | EST. OTROS METODOS |               900 |
| 2010-06-01 00:00:00 |         28017140 | CORRAL DE PIEDRA  - AUT [28017140] |     10.83 |     -73.07 |       275 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | La Guajira     | San Juan Del Cesar | 2004-09-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   43005 |      50 | nan                |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_28017140_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017140_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017140_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28017140_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 28047010 (412 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28047010 | AURORA LA [28047010] |   10.2769 |   -73.9778 |       150 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Fundación   | 1961-05-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |  16.83  |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28047010 | AURORA LA [28047010] |   10.2769 |   -73.9778 |       150 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Fundación   | 1961-05-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |  11.81  |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28047010 | AURORA LA [28047010] |   10.2769 |   -73.9778 |       150 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Fundación   | 1961-05-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   9.395 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_28047010_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047010_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047010_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047010_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 29067050 (393 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29067050 | CANAL FLORIDA [29067050] |   10.7589 |   -74.1066 |        60 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1965-05-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   7.816 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29067050 | CANAL FLORIDA [29067050] |   10.7589 |   -74.1066 |        60 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1965-05-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   4.224 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29067050 | CANAL FLORIDA [29067050] |   10.7589 |   -74.1066 |        60 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1965-05-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   4.774 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067050_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067050_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067050_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067050_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 25027020 (504 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion            |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         25027020 | EL BANCO - AUT [25027020] |   8.99253 |   -73.9694 |        29 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena      | El Banco    | 1934-01-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    3231 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         25027020 | EL BANCO - AUT [25027020] |   8.99253 |   -73.9694 |        29 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena      | El Banco    | 1934-01-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    2680 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         25027020 | EL BANCO - AUT [25027020] |   8.99253 |   -73.9694 |        29 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 02 - Atlántico-Bolivar-Sucre | Magdalena      | El Banco    | 1934-01-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    2004 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_25027020_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027020_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027020_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_25027020_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 29067120 (444 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29067120 | FUNDACION [29067120] |   10.5233 |   -74.1828 |        55 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Fundación   | 1958-04-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   21.44 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29067120 | FUNDACION [29067120] |   10.5233 |   -74.1828 |        55 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Fundación   | 1958-04-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   14.8  |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29067120 | FUNDACION [29067120] |   10.5233 |   -74.1828 |        55 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Fundación   | 1958-04-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   11.41 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067120_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067120_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067120_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067120_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 28047050 (451 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                 |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio             | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:----------------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         28047050 | PALMARIGUANI  - AUT [28047050] |   9.93097 |   -73.9588 |        80 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ariguaní (El Dificil) | 1978-10-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |  10.28  |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         28047050 | PALMARIGUANI  - AUT [28047050] |   9.93097 |   -73.9588 |        80 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ariguaní (El Dificil) | 1978-10-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   6.622 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         28047050 | PALMARIGUANI  - AUT [28047050] |   9.93097 |   -73.9588 |        80 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ariguaní (El Dificil) | 1978-10-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   3.342 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_28047050_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047050_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047050_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_28047050_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 29067060 (257 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                         |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29067060 | PUERTO RICO HACIENDA  - AUT [29067060] |      10.5 |   -74.1333 |        55 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Aracataca   | 1967-06-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |  17.88  |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29067060 | PUERTO RICO HACIENDA  - AUT [29067060] |      10.5 |   -74.1333 |        55 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Aracataca   | 1967-06-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |  12.67  |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29067060 | PUERTO RICO HACIENDA  - AUT [29067060] |      10.5 |   -74.1333 |        55 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Aracataca   | 1967-06-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   9.948 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067060_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067060_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067060_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067060_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 29067070 (426 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29067070 | RIO FRIO [29067070] |   10.9054 |   -74.1541 |        30 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1978-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   7.213 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29067070 | RIO FRIO [29067070] |   10.9054 |   -74.1541 |        30 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1978-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   5.03  |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29067070 | RIO FRIO [29067070] |   10.9054 |   -74.1541 |        30 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1978-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   3.847 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067070_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067070_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067070_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067070_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 29067040 (446 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion           |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio     | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:--------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29067040 | SANTA ROSALIA [29067040] |   10.8308 |   -74.1206 |        55 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1965-05-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.514 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29067040 | SANTA ROSALIA [29067040] |   10.8308 |   -74.1206 |        55 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1965-05-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.482 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29067040 | SANTA ROSALIA [29067040] |   10.8308 |   -74.1206 |        55 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Zona Bananera | 1965-05-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   0.312 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067040_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067040_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067040_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067040_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 29067010 (448 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion       |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado | Calificador    |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|:---------------|------------------:|
| 1980-01-01 00:00:00 |         29067010 | TREBOL EL [29067010] |   10.6359 |   -74.1463 |        60 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1958-03-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   7.281 |       4 | EST. REGRESION |               900 |
| 1980-02-01 00:00:00 |         29067010 | TREBOL EL [29067010] |   10.6359 |   -74.1463 |        60 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1958-03-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   5.391 |       4 | EST. REGRESION |               900 |
| 1980-03-01 00:00:00 |         29067010 | TREBOL EL [29067010] |   10.6359 |   -74.1463 |        60 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1958-03-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   2.966 |       4 | EST. REGRESION |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067010_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067010_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067010_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067010_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 29067150 (481 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                     |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:-----------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29067150 | GANADERIA CARIBE  - AUT [29067150] |   10.5749 |   -74.1267 |        67 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Aracataca   | 1965-05-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   11.91 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29067150 | GANADERIA CARIBE  - AUT [29067150] |   10.5749 |   -74.1267 |        67 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Aracataca   | 1965-05-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    7.24 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29067150 | GANADERIA CARIBE  - AUT [29067150] |   10.5749 |   -74.1267 |        67 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Aracataca   | 1965-05-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |    4.87 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067150_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067150_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067150_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067150_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 29067130 (476 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         29067130 | PUENTE FERROCARRIL [29067130] |   10.5858 |   -74.1921 |        37 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Aracataca   | 1965-05-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   7.851 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         29067130 | PUENTE FERROCARRIL [29067130] |   10.5858 |   -74.1921 |        37 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Aracataca   | 1965-05-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   4.309 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         29067130 | PUENTE FERROCARRIL [29067130] |   10.5858 |   -74.1921 |        37 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Aracataca   | 1965-05-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   2.634 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067130_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067130_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067130_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067130_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 29067160 (397 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                   |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                               | Departamento   | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado | Calificador    |   NivelAprobacion |
|:--------------------|-----------------:|:---------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:--------------------------------------------|:---------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|:---------------|------------------:|
| 1982-01-01 00:00:00 |         29067160 | PUENTE SEVILLA  - AUT [29067160] |   10.7988 |   -74.0286 |        10 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1982-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   3.595 |       4 | EST. REGRESION |               900 |
| 1982-02-01 00:00:00 |         29067160 | PUENTE SEVILLA  - AUT [29067160] |   10.7988 |   -74.0286 |        10 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1982-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   2.123 |       4 | EST. REGRESION |               900 |
| 1982-03-01 00:00:00 |         29067160 | PUENTE SEVILLA  - AUT [29067160] |   10.7988 |   -74.0286 |        10 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 05 - Magdalena-Cesar-Guajira | Magdalena      | Ciénaga     | 1982-07-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   3.027 |       4 | EST. REGRESION |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_29067160_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067160_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067160_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_29067160_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 16067020 (244 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion      |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                          | Departamento       | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:---------------------------------------|:-------------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         16067020 | CABLE EL [16067020] |   8.67639 |   -72.9497 |       110 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | El Tarra    | 1976-08-15 00:00:00 | 2001-04-20 00:00:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   68.34 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         16067020 | CABLE EL [16067020] |   8.67639 |   -72.9497 |       110 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | El Tarra    | 1976-08-15 00:00:00 | 2001-04-20 00:00:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   54.4  |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         16067020 | CABLE EL [16067020] |   8.67639 |   -72.9497 |       110 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | El Tarra    | 1976-08-15 00:00:00 | 2001-04-20 00:00:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   41.71 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_16067020_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16067020_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16067020_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16067020_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 16037040 (387 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion        |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                          | Departamento       | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado | Calificador        |   NivelAprobacion |
|:--------------------|-----------------:|:----------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:---------------------------------------|:-------------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|:-------------------|------------------:|
| 1980-01-01 00:00:00 |         16037040 | CAMPO SEIS [16037040] |   8.60111 |   -72.8086 |        70 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Tibú        | 1973-04-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   9.241 |       4 | EST. INTERPOLACION |               900 |
| 1980-02-01 00:00:00 |         16037040 | CAMPO SEIS [16037040] |   8.60111 |   -72.8086 |        70 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Tibú        | 1973-04-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   5.077 |      50 | nan                |               900 |
| 1980-03-01 00:00:00 |         16037040 | CAMPO SEIS [16037040] |   8.60111 |   -72.8086 |        70 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Tibú        | 1973-04-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   4.551 |       4 | EST. OTROS METODOS |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_16037040_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16037040_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16037040_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16037040_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 16047020 (283 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion          |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                          | Departamento       | Municipio   | FechaInstalacion    | FechaSuspension     | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:---------------------------------------|:-------------------|:------------|:--------------------|:--------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         16047020 | PUENTE TARRA [16047020] |   8.58861 |   -73.0811 |       140 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | El Tarra    | 1971-11-15 00:00:00 | 2014-06-18 00:00:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   32.22 |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         16047020 | PUENTE TARRA [16047020] |   8.58861 |   -73.0811 |       140 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | El Tarra    | 1971-11-15 00:00:00 | 2014-06-18 00:00:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   27.17 |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         16047020 | PUENTE TARRA [16047020] |   8.58861 |   -73.0811 |       140 | Limnimétrica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | El Tarra    | 1971-11-15 00:00:00 | 2014-06-18 00:00:00 | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   18.51 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_16047020_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16047020_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16047020_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16047020_DensityKDE.png)

<div align="center">



**Q_MEDIA_M - Station: 16067010 (397 rec.)**

</div>


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


Station records head sample

| Fecha               |   CodigoEstacion | NombreEstacion                        |   Latitud |   Longitud |   Altitud | Categoria    | Entidad                                                     | AreaOperativa                          | Departamento       | Municipio   | FechaInstalacion    | FechaSuspension   | IdParametro   | Etiqueta   | DescripcionSerie     | Frecuencia   |   Valor |   Grado |   Calificador |   NivelAprobacion |
|:--------------------|-----------------:|:--------------------------------------|----------:|-----------:|----------:|:-------------|:------------------------------------------------------------|:---------------------------------------|:-------------------|:------------|:--------------------|:------------------|:--------------|:-----------|:---------------------|:-------------|--------:|--------:|--------------:|------------------:|
| 1980-01-01 00:00:00 |         16067010 | PUERTO BARCO-GABARRA - AUT [16067010] |   9.00361 |      -72.9 |        19 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Tibú        | 1969-08-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |  149.3  |      50 |           nan |               900 |
| 1980-02-01 00:00:00 |         16067010 | PUERTO BARCO-GABARRA - AUT [16067010] |   9.00361 |      -72.9 |        19 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Tibú        | 1969-08-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   87.4  |      50 |           nan |               900 |
| 1980-03-01 00:00:00 |         16067010 | PUERTO BARCO-GABARRA - AUT [16067010] |   9.00361 |      -72.9 |        19 | Limnigráfica | INSTITUTO DE HIDROLOGIA METEOROLOGIA Y ESTUDIOS AMBIENTALES | Area Operativa 08 - Santanderes-Arauca | Norte De Santander | Tibú        | 1969-08-15 00:00:00 | NaT               | CAUDAL        | Q_MEDIA_M  | Caudal medio mensual | Mensual      |   52.39 |      50 |           nan |               900 |

![R.LTWB](Graph/Plot_Q_MEDIA_M_16067010_TimeSerie.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16067010_Boxplot.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16067010_Histogram.png)
![R.LTWB](Graph/Plot_Q_MEDIA_M_16067010_DensityKDE.png)
