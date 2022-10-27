## Exploración y análisis de series - EDA - Representación gráfica

* Archivo de resultados: D:/R.LTWB/.datasets/IDEAM_EDA/EDA.md
* Fecha y hora de inicio de ejecución: 2022-10-27 16:40:38.910919
* Python versión: 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)]
* Python rutas: ['D:\\R.LTWB\\.src', 'D:\\R.LTWB', 'D:\\R.GISPython.wiki', 'D:\\R.GISPython', 'D:\\R.HydroTools']
* matplotlib versión: 3.6.0
* Print table samples: True
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
