## Impute missing values in time series through statistical methods

* Processed file: [D:/R.LTWB/.datasets/IDEAM_Outlier/Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv](../IDEAM_EDA/Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv)
* Execution date: 2022-11-10 16:25:19.862565
* Python version: 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)]
* Python path: ['D:\\R.LTWB\\.src', 'D:\\R.LTWB', 'D:\\R.HydroTools.wiki', 'D:\\R.TeachingResearchGuide', 'D:\\R.HydroTools']
* matplotlib version: 3.6.0
* pandas version: 1.4.3
* numpy version: 1.23.2
* Stations exclude: ['28010090', '28025040']
* Print table sample: True
* Instructions & script: https://github.com/rcfdtools/R.LTWB/tree/main/Section03/Impute
* License: https://github.com/rcfdtools/R.LTWB/blob/main/LICENSE.md
* Credits: r.cfdtools@gmail.com


### General dataframe information with 504 IDEAM records for 2 stations

Dataframe records head sample

| Fecha               |   28010090 |   28025040 |
|:--------------------|-----------:|-----------:|
| 1980-01-01 00:00:00 |          0 |        3.7 |
| 1980-02-01 00:00:00 |         51 |       56.9 |
| 1980-03-01 00:00:00 |          0 |        7.3 |

Dataframe records tail sample

| Fecha               |   28010090 |   28025040 |
|:--------------------|-----------:|-----------:|
| 2021-10-01 00:00:00 |      133.5 |        nan |
| 2021-11-01 00:00:00 |       56.8 |        nan |
| 2021-12-01 00:00:00 |        1.6 |        nan |

Datatypes for station and nulls values in the initial file
|       | 28010090   | 28025040   |
|:------|:-----------|:-----------|
| Dtype | float64    | float64    |
| Nulls | 30         | 333        |

![R.LTWB](Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv.png)

<div align="center">

General statistics table - Initial file

</div>


<div align="center">

|          |   count |    mean |     std |   min |   25% |   50% |   75% |     max |
|---------:|--------:|--------:|--------:|------:|------:|------:|------:|--------:|
| 28010090 |     474 | 92.4008 | 93.9715 |     0 |  10   |  71.5 | 138   | 520.861 |
| 28025040 |     171 | 96.6094 | 90.3915 |     0 |  26.1 |  68.8 | 143.5 | 360.6   |

</div>



### Method 1 - Imputing with mean values

![R.LTWB](Impute_Mean_Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv.png)

<div align="center">

|          |   count |    mean |     std |   min |     25% |     50% |      75% |     max |
|---------:|--------:|--------:|--------:|------:|--------:|--------:|---------:|--------:|
| 28010090 |     504 | 92.4008 | 91.126  |     0 | 12      | 81.25   | 134.925  | 520.861 |
| 28025040 |     504 | 96.6094 | 52.5494 |     0 | 96.6094 | 96.6094 |  96.6094 | 360.6   |

</div>



### Method 2 - Imputing with median values

![R.LTWB](Impute_Median_Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv.png)

<div align="center">

|          |   count |    mean |     std |   min |   25% |   50% |     75% |     max |
|---------:|--------:|--------:|--------:|------:|------:|------:|--------:|--------:|
| 28010090 |     504 | 91.1567 | 91.2604 |     0 |  12   |  71.5 | 134.925 | 520.861 |
| 28025040 |     504 | 78.2353 | 54.177  |     0 |  68.8 |  68.8 |  68.8   | 360.6   |

</div>



### Method 3 - Imputing with Last Observation Carried Forward (LOCF) values

![R.LTWB](Impute_LOCF_Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv.png)

<div align="center">

|          |   count |    mean |     std |   min |    25% |   50% |   75% |     max |
|---------:|--------:|--------:|--------:|------:|-------:|------:|------:|--------:|
| 28010090 |     504 | 88.0559 | 93.1409 |     0 |  5     | 65    |   135 | 520.861 |
| 28025040 |     216 | 92.362  | 83.1571 |     0 | 31.475 | 75.45 |   123 | 360.6   |

</div>



### Method 4 - Imputing with Next Observation Carried Backward (NOCB) values

![R.LTWB](Impute_NOCB_Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv.png)

<div align="center">

|          |   count |    mean |     std |   min |   25% |   50% |     75% |     max |
|---------:|--------:|--------:|--------:|------:|------:|------:|--------:|--------:|
| 28010090 |     504 | 92.3848 | 92.2593 |     0 |    10 |    74 | 134.925 | 520.861 |
| 28025040 |     504 | 34.7726 | 70.756  |     0 |     0 |     0 |  32.7   | 360.6   |

</div>



### Method 5 - Impute missing values with Linear Interpolation values

![R.LTWB](Impute_InterpolateLinear_Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv.png)

<div align="center">

|          |   count |    mean |     std |   min |   25% |   50% |     75% |     max |
|---------:|--------:|--------:|--------:|------:|------:|------:|--------:|--------:|
| 28010090 |     504 | 90.2204 | 91.9677 |     0 |    10 |    70 | 134.925 | 520.861 |
| 28025040 |     504 | 37.1782 | 69.795  |     0 |     0 |     0 |  43.95  | 360.6   |

</div>



### Method 6 - Impute missing values with Exponential (Weighted) Moving Average - EWM

![R.LTWB](Impute_MeanEWM_Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv.png)

<div align="center">

|          |   count |    mean |     std |   min |     25% |     50% |      75% |     max |
|---------:|--------:|--------:|--------:|------:|--------:|--------:|---------:|--------:|
| 28010090 |     504 | 90.5269 | 91.4604 |     0 | 12      | 65.2881 | 134.925  | 520.861 |
| 28025040 |     504 | 81.2528 | 54.3381 |     0 | 74.4529 | 74.4529 |  74.4529 | 360.6   |

</div>

