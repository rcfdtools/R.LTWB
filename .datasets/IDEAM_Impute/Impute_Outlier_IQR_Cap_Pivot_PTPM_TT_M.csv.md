## Impute missing values in time series through statistical methods

* Processed file: [D:/R.LTWB/.datasets/IDEAM_Outlier/Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv](../IDEAM_EDA/Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv)
* Execution date: 2022-11-10 10:22:09.037573
* Python version: 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)]
* Python path: ['D:\\R.LTWB\\.src', 'D:\\R.LTWB', 'D:\\R.GISPython.wiki', 'D:\\R.HydroTools', 'D:\\R.HydroTools.wiki']
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

<div align="center">

|       | 28010090   | 28025040   |
|:------|:-----------|:-----------|
| Dtype | float64    | float64    |
| Nulls | 30         | 333        |

</div>


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


### Method 1 - Imputing with mean for 2 stations (363 missing values)

![R.LTWB](Impute_Mean_Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv.png)
