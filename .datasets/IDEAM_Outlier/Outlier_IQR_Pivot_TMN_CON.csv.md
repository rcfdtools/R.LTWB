## Outliers detection and processing through statistical methods

* Processed file: [D:/R.LTWB/.datasets/IDEAM_EDA/Pivot_TMN_CON.csv](../IDEAM_EDA/Pivot_TMN_CON.csv)
* Execution date: 2022-11-07 13:48:36.815571
* Python version: 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)]
* Python path: ['D:\\R.LTWB\\.src', 'D:\\R.LTWB', 'D:\\R.GISPython', 'D:\\R.HydroTools', 'D:\\R.GISPython.wiki']
* matplotlib version: 3.6.0
* pandas version: 1.4.3
* numpy version: 1.23.2
* Stations exclude: ['28017140', '25027020', '25027410', '25027490', '25027330', '25027390', '25027630', '25027360', '25027320', '16067010', '25027420']
* Print table sample: True
* Instructions & script: https://github.com/rcfdtools/R.LTWB/tree/main/Section03/Outlier
* License: https://github.com/rcfdtools/R.LTWB/blob/main/LICENSE.md
* Credits: r.cfdtools@gmail.com


### General dataframe information with 15341 IDEAM records for 25 stations

Dataframe records head sample

| Fecha               |   15015020 |   15065040 |   23215060 |   25025002 |   25025090 |   25025250 |   25025300 |   25025330 |   28015030 |   28015070 |   28025020 |   28025040 |   28025070 |   28025080 |   28025090 |   28025502 |   28035010 |   28035020 |   28035040 |   28035070 |   28045020 |   28045040 |   29065010 |   29065020 |   29065030 |
|:--------------------|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|
| 1980-01-01 00:00:00 |       23.2 |        nan |        nan |        nan |       24.2 |        nan |        nan |        nan |      nan   |       23   |        nan |       20.2 |       22.8 |       21.8 |        nan |        nan |      nan   |       19.4 |        nan |        nan |        nan |        nan |       21.4 |        nan |       21.4 |
| 1980-01-02 00:00:00 |       22.4 |        nan |        nan |        nan |       24.2 |        nan |        nan |        nan |       23.3 |       23.5 |        nan |       21   |       23.4 |       21.6 |        nan |         24 |      nan   |       19.6 |        nan |        nan |        nan |        nan |      nan   |        nan |       21.8 |
| 1980-01-03 00:00:00 |       20.8 |        nan |        nan |        nan |       24.6 |        nan |        nan |        nan |       24   |      nan   |        nan |       19.8 |       23.4 |       21.4 |        nan |        nan |       22.4 |       19   |        nan |        nan |        nan |        nan |      nan   |        nan |      nan   |

Dataframe records tail sample

| Fecha               |   15015020 |   15065040 |   23215060 |   25025002 |   25025090 |   25025250 |   25025300 |   25025330 |   28015030 |   28015070 |   28025020 |   28025040 |   28025070 |   28025080 |   28025090 |   28025502 |   28035010 |   28035020 |   28035040 |   28035070 |   28045020 |   28045040 |   29065010 |   29065020 |   29065030 |
|:--------------------|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|
| 2021-12-29 00:00:00 |        nan |        nan |        nan |       21.8 |       23   |       24.8 |       23.2 |         23 |        nan |       21.8 |       18.8 |        nan |       23   |        nan |       21.2 |        nan |       22.6 |       22.8 |       25.4 |        nan |        nan |        nan |        nan |       25   |        nan |
| 2021-12-30 00:00:00 |        nan |        nan |        nan |       22.4 |       24   |       24.4 |       22.6 |         24 |        nan |       21   |       18.2 |        nan |       22.8 |        nan |       20   |        nan |       20.8 |       22.4 |       24.4 |        nan |        nan |        nan |        nan |       24.8 |        nan |
| 2021-12-31 00:00:00 |        nan |        nan |        nan |       20.4 |       21.4 |       24.2 |       22   |        nan |        nan |       20.2 |       20.2 |        nan |       22   |        nan |       21.2 |        nan |       20.8 |       22   |       24   |        nan |        nan |        nan |        nan |       25.4 |        nan |

Datatypes for station and nulls values in the initial file

<div align="center">

|       | 15015020   | 15065040   | 23215060   | 25025002   | 25025090   | 25025250   | 25025300   | 25025330   | 28015030   | 28015070   | 28025020   | 28025040   | 28025070   | 28025080   | 28025090   | 28025502   | 28035010   | 28035020   | 28035040   | 28035070   | 28045020   | 28045040   | 29065010   | 29065020   | 29065030   |
|:------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| Dtype | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    | float64    |
| Nulls | 5377       | 10392      | 14093      | 4608       | 5567       | 3001       | 3648       | 6066       | 13937      | 2866       | 1889       | 12110      | 1523       | 7705       | 3474       | 3103       | 4784       | 3517       | 1936       | 15299      | 14289      | 14067      | 14278      | 2358       | 3815       |

</div>


<div align="center">

General statistics table - Initial file

</div>


<div align="center">

|          |   count |    mean |     std |   min |   25% |   50% |   75% |   max |
|---------:|--------:|--------:|--------:|------:|------:|------:|------:|------:|
| 15015020 |    9964 | 22.1888 | 1.60856 |  16   |  21.2 |  22.4 |  23.2 |  26.8 |
| 15065040 |    4949 | 22.9664 | 1.75384 |  12.4 |  22.2 |  23.2 |  24.2 |  27.8 |
| 23215060 |    1248 | 23.6837 | 1.20744 |  16.6 |  23   |  23.8 |  24.6 |  26.8 |
| 25025002 |   10733 | 22.9428 | 1.56303 |  16.8 |  22   |  23   |  24   |  27.2 |
| 25025090 |    9774 | 23.5651 | 1.53376 |  17   |  22.6 |  23.6 |  24.8 |  28   |
| 25025250 |   12340 | 22.3963 | 1.63717 |  17   |  21.2 |  22.4 |  23.8 |  27.1 |
| 25025300 |   11693 | 22.9902 | 1.75271 |  15.4 |  22   |  23.2 |  24.2 |  27.8 |
| 25025330 |    9275 | 22.7791 | 1.6933  |  13.1 |  21.8 |  23   |  24   |  28.6 |
| 28015030 |    1404 | 22.9291 | 1.32774 |  10   |  22.2 |  23   |  23.8 |  26.8 |
| 28015070 |   12475 | 22.34   | 1.33165 |  15.4 |  21.5 |  22.5 |  23.2 |  26.2 |
| 28025020 |   13452 | 20.547  | 1.73534 |  12   |  19.6 |  20.8 |  21.8 |  26   |
| 28025040 |    3231 | 18.674  | 2.11514 |   8.4 |  18   |  19.2 |  20   |  27.4 |
| 28025070 |   13818 | 23.7666 | 1.54724 |  17.4 |  22.8 |  23.8 |  25   |  28.6 |
| 28025080 |    7636 | 21.7751 | 1.87894 |  15.2 |  20.4 |  22.2 |  23.2 |  27   |
| 28025090 |   11867 | 22.4272 | 1.67337 |  15   |  21.6 |  22.8 |  23.6 |  27.4 |
| 28025502 |   12238 | 23.8861 | 1.27915 |  18.4 |  23   |  23.8 |  24.8 |  28.6 |
| 28035010 |   10557 | 23.3278 | 1.49337 |  13.4 |  22.6 |  23.4 |  24.2 |  28.8 |
| 28035020 |   11824 | 22.8005 | 1.82844 |  15.8 |  21.8 |  23   |  24   |  28.6 |
| 28035040 |   13405 | 24.269  | 1.23846 |  17.2 |  23.4 |  24.2 |  25   |  28.6 |
| 28035070 |      42 | 22.0286 | 1.01844 |  20.6 |  21.4 |  21.8 |  22.6 |  25.6 |
| 28045020 |    1052 | 21.2974 | 1.79272 |  14.6 |  20.2 |  21.6 |  22.6 |  26.4 |
| 28045040 |    1274 | 23.128  | 1.26701 |  14.6 |  22.4 |  23.2 |  24   |  26.6 |
| 29065010 |    1063 | 21.3162 | 1.60256 |  15.2 |  20.4 |  21.4 |  22.4 |  25.2 |
| 29065020 |   12983 | 22.327  | 1.85521 |  14.2 |  21.2 |  22.6 |  23.6 |  27.4 |
| 29065030 |   11526 | 21.8104 | 1.55983 |  14   |  20.8 |  22   |  23   |  27   |

</div>

### Method 1 - Outliers processing using the interquartile range IQR (q1 = 0.175, q3 = 0.825)

Since the data doesn`t follow a normal distribution, we will calculate the outlier data points using the statistical method called interquartile range (IQR) instead of using Z-score. Using the IQR, the outlier data points are the ones falling below Q1 - 1.5 IQR or above Q3 + 1.5 IQR. The Q1 could be the 25th percentile and Q3 could be the 75th percentile of the dataset, and IQR represents the interquartile range calculated by Q3 minus Q1 (Q3-Q1). [^1]

Outliers parameters:
* mean: mean value
* std: standard deviation value
* q1: quartile 0.175
* q3: quartile 0.825
* IQR: interquartile range (q3-q1)
* OlLowerLim: outlier bottom limit (q1-1.5*IQR)
* OlUpperLim: outlier top limit (q3+1.5*IQR)
* OlMinVal: minimum outlier value founded
* OlMaxVal: maximum outlier value founded
* OlCount: # outliers founded
* CapLowerLim: capped lower limit for outliers replacement ( $\mu$ - 3.5 * $\sigma$ )
* CapUpperLim: capped upper limit for outliers replacement ( $\mu$ + 3.5 * $\sigma$ )


<div align="center">

|          |    mean |     std |    q1 |   q3 |   IQR |   OlLowerLim |   OlUpperLim |   OlMinVal |   OlMaxVal |   OlCount |   CapLowerLim |   CapUpperLim |
|---------:|--------:|--------:|------:|-----:|------:|-------------:|-------------:|-----------:|-----------:|----------:|--------------:|--------------:|
| 15015020 | 22.1888 | 1.60856 | 20.6  | 23.6 |  3    |       25.1   |       28.1   |       16   |       16   |         1 |       16.5588 |       27.8188 |
| 15065040 | 22.9664 | 1.75384 | 21.6  | 24.6 |  3    |       26.1   |       29.1   |       12.4 |       17   |        25 |       16.828  |       29.1049 |
| 23215060 | 23.6837 | 1.20744 | 22.6  | 24.8 |  2.2  |       25.9   |       28.1   |       16.6 |       19.2 |         8 |       19.4576 |       27.9097 |
| 25025002 | 22.9428 | 1.56303 | 21.6  | 24.4 |  2.8  |       25.8   |       28.6   |       16.8 |       17.4 |        13 |       17.4722 |       28.4134 |
| 25025090 | 23.5651 | 1.53376 | 22.2  | 25   |  2.8  |       26.4   |       29.2   |       17   |       17.6 |         8 |       18.197  |       28.9333 |
| 25025250 | 22.3963 | 1.63717 | 20.8  | 24.2 |  3.4  |       25.9   |       29.3   |      nan   |      nan   |         0 |       16.6662 |       28.1264 |
| 25025300 | 22.9902 | 1.75271 | 21.4  | 24.6 |  3.2  |       26.2   |       29.4   |       15.4 |       16.4 |        11 |       16.8557 |       29.1247 |
| 25025330 | 22.7791 | 1.6933  | 21.3  | 24.2 |  2.9  |       25.65  |       28.55  |       13.1 |       28.6 |        44 |       16.8526 |       28.7057 |
| 28015030 | 22.9291 | 1.32774 | 21.8  | 24   |  2.2  |       25.1   |       27.3   |       10   |       18.3 |         7 |       18.282  |       27.5762 |
| 28015070 | 22.34   | 1.33165 | 21    | 23.6 |  2.6  |       24.9   |       27.5   |       15.4 |       17   |        21 |       17.6792 |       27.0007 |
| 28025020 | 20.547  | 1.73534 | 19    | 22.2 |  3.2  |       23.8   |       27     |       12   |       14.2 |        21 |       14.4733 |       26.6207 |
| 28025040 | 18.674  | 2.11514 | 17    | 20.2 |  3.2  |       21.8   |       25     |        8.4 |       27.4 |        48 |       11.271  |       26.077  |
| 28025070 | 23.7666 | 1.54724 | 22.4  | 25.2 |  2.8  |       26.6   |       29.4   |       17.4 |       18   |        14 |       18.3513 |       29.182  |
| 28025080 | 21.7751 | 1.87894 | 20    | 23.4 |  3.4  |       25.1   |       28.5   |      nan   |      nan   |         0 |       15.1988 |       28.3514 |
| 28025090 | 22.4272 | 1.67337 | 21    | 23.8 |  2.8  |       25.2   |       28     |       15   |       16.6 |        36 |       16.5704 |       28.284  |
| 28025502 | 23.8861 | 1.27915 | 22.7  | 25.1 |  2.4  |       26.3   |       28.7   |       18.4 |       19   |         5 |       19.4091 |       28.3631 |
| 28035010 | 23.3278 | 1.49337 | 22.2  | 24.6 |  2.4  |       25.8   |       28.2   |       13.4 |       28.8 |        62 |       18.101  |       28.5546 |
| 28035020 | 22.8005 | 1.82844 | 21.2  | 24.4 |  3.2  |       26     |       29.2   |       15.8 |       16.2 |         6 |       16.4009 |       29.2    |
| 28035040 | 24.269  | 1.23846 | 23.2  | 25.4 |  2.2  |       26.5   |       28.7   |       17.2 |       19.8 |        28 |       19.9343 |       28.6036 |
| 28035070 | 22.0286 | 1.01844 | 21.2  | 22.6 |  1.4  |       23.3   |       24.7   |       25.6 |       25.6 |         1 |       18.464  |       25.5931 |
| 28045020 | 21.2974 | 1.79272 | 19.6  | 22.8 |  3.2  |       24.4   |       27.6   |       14.6 |       14.8 |         2 |       15.0229 |       27.5719 |
| 28045040 | 23.128  | 1.26701 | 22.2  | 24.2 |  2    |       25.2   |       27.2   |       14.6 |       19   |         9 |       18.6935 |       27.5625 |
| 29065010 | 21.3162 | 1.60256 | 19.97 | 22.8 |  2.83 |       24.215 |       27.045 |       15.2 |       15.4 |         2 |       15.7072 |       26.9251 |
| 29065020 | 22.327  | 1.85521 | 20.6  | 24   |  3.4  |       25.7   |       29.1   |       14.2 |       15.4 |        27 |       15.8338 |       28.8203 |
| 29065030 | 21.8104 | 1.55983 | 20.2  | 23.2 |  3    |       24.7   |       27.7   |       14   |       15.4 |         4 |       16.351  |       27.2698 |

</div>


![R.LTWB](Outlier_IQR_Pivot_TMN_CON.csv.png)

#### Identified and cleaning tables for 403 IQR outliers founded
* Outliers identified file: [Outlier_IQR_Pivot_TMN_CON.csv](../../.datasets/IDEAM_Outlier/Outlier_IQR_Pivot_TMN_CON.csv)
* Outliers dropped file: [Outlier_IQR_Drop_Pivot_TMN_CON.csv](../../.datasets/IDEAM_Outlier/Outlier_IQR_Drop_Pivot_TMN_CON.csv)
* Outliers capped file: [Outlier_IQR_Cap_Pivot_TMN_CON.csv](../../.datasets/IDEAM_Outlier/Outlier_IQR_Cap_Pivot_TMN_CON.csv)
* Outliers imputed file: [Outlier_IQR_Impute_Pivot_TMN_CON.csv](../../.datasets/IDEAM_Outlier/Outlier_IQR_Impute_Pivot_TMN_CON.csv)


#### Statistical values for the capped and imputed file

<div align="center">

IQR - General statistics table - Capped file

</div>


<div align="center">

|          |   count |    mean |     std |     min |   25% |   50% |   75% |     max |
|---------:|--------:|--------:|--------:|--------:|------:|------:|------:|--------:|
| 15015020 |    9964 | 22.1889 | 1.60836 | 16.4    |  21.2 |  22.4 |  23.2 | 26.8    |
| 15065040 |    4949 | 22.9699 | 1.73975 | 16.828  |  22.2 |  23.2 |  24.2 | 27.8    |
| 23215060 |    1248 | 23.6922 | 1.17043 | 19.4576 |  23   |  23.8 |  24.6 | 26.8    |
| 25025002 |   10733 | 22.9432 | 1.56162 | 17.4722 |  22   |  23   |  24   | 27.2    |
| 25025090 |    9774 | 23.5659 | 1.53079 | 18      |  22.6 |  23.6 |  24.8 | 28      |
| 25025250 |   12340 | 22.3963 | 1.63717 | 17      |  21.2 |  22.4 |  23.8 | 27.1    |
| 25025300 |   11693 | 22.991  | 1.7495  | 16.6    |  22   |  23.2 |  24.2 | 27.8    |
| 25025330 |    9275 | 22.784  | 1.67325 | 16.8526 |  21.8 |  23   |  24   | 28.7057 |
| 28015030 |    1404 | 22.9361 | 1.28381 | 18.282  |  22.2 |  23   |  23.8 | 26.8    |
| 28015070 |   12475 | 22.342  | 1.32337 | 17.2    |  21.5 |  22.5 |  23.2 | 26.2    |
| 28025020 |   13452 | 20.5484 | 1.72989 | 14.4    |  19.6 |  20.8 |  21.8 | 26      |
| 28025040 |    3231 | 18.6727 | 2.11411 | 11.271  |  18   |  19.2 |  20   | 26.077  |
| 28025070 |   13818 | 23.7672 | 1.54528 | 18.2    |  22.8 |  23.8 |  25   | 28.6    |
| 28025080 |    7636 | 21.7751 | 1.87894 | 15.2    |  20.4 |  22.2 |  23.2 | 27      |
| 28025090 |   11867 | 22.4284 | 1.66885 | 16.5704 |  21.6 |  22.8 |  23.6 | 27.4    |
| 28025502 |   12238 | 23.8863 | 1.2782  | 19.1    |  23   |  23.8 |  24.8 | 28.6    |
| 28035010 |   10557 | 23.3291 | 1.48753 | 18.101  |  22.6 |  23.4 |  24.2 | 28.5546 |
| 28035020 |   11824 | 22.8007 | 1.82776 | 16.4    |  21.8 |  23   |  24   | 28.6    |
| 28035040 |   13405 | 24.2706 | 1.23193 | 19.9343 |  23.4 |  24.2 |  25   | 28.6    |
| 28035070 |      42 | 22.0284 | 1.01785 | 20.6    |  21.4 |  21.8 |  22.6 | 25.5931 |
| 28045020 |    1052 | 21.298  | 1.7905  | 15      |  20.2 |  21.6 |  22.6 | 26.4    |
| 28045040 |    1274 | 23.1351 | 1.2346  | 18.6935 |  22.4 |  23.2 |  24   | 26.6    |
| 29065010 |    1063 | 21.3169 | 1.59977 | 15.7072 |  20.4 |  21.4 |  22.4 | 25.2    |
| 29065020 |   12983 | 22.3291 | 1.84749 | 15.6    |  21.2 |  22.6 |  23.6 | 27.4    |
| 29065030 |   11526 | 21.8109 | 1.55779 | 16      |  20.8 |  22   |  23   | 27      |

</div>


<div align="center">

IQR - General statistics table - Imputed file

</div>


<div align="center">

|          |   count |    mean |      std |   min |   25% |   50% |   75% |   max |
|---------:|--------:|--------:|---------:|------:|------:|------:|------:|------:|
| 15015020 |    9964 | 22.1894 | 1.60737  |  16.4 |  21.2 |  22.4 | 23.2  |  26.8 |
| 15065040 |    4949 | 23.0009 | 1.6838   |  17.1 |  22.2 |  23.2 | 24.2  |  27.8 |
| 23215060 |    1248 | 23.7193 | 1.11988  |  19.8 |  23   |  23.8 | 24.6  |  26.8 |
| 25025002 |   10733 | 22.9498 | 1.54996  |  17.6 |  22   |  23   | 24    |  27.2 |
| 25025090 |    9774 | 23.5703 | 1.52306  |  18   |  22.6 |  23.6 | 24.8  |  28   |
| 25025250 |   12340 | 22.3963 | 1.63717  |  17   |  21.2 |  22.4 | 23.8  |  27.1 |
| 25025300 |   11693 | 22.9968 | 1.73934  |  16.6 |  22   |  23.2 | 24.2  |  27.8 |
| 25025330 |    9275 | 22.8109 | 1.62239  |  17   |  21.8 |  23   | 24    |  28   |
| 28015030 |    1404 | 22.9593 | 1.24079  |  18.5 |  22.2 |  23   | 23.8  |  26.8 |
| 28015070 |   12475 | 22.3499 | 1.30945  |  17.2 |  21.5 |  22.5 | 23.2  |  26.2 |
| 28025020 |   13452 | 20.5579 | 1.71313  |  14.4 |  19.6 |  20.8 | 21.8  |  26   |
| 28025040 |    3231 | 18.7781 | 1.90898  |  12.3 |  18   |  19.2 | 20    |  24   |
| 28025070 |   13818 | 23.7727 | 1.53563  |  18.2 |  22.8 |  23.8 | 25    |  28.6 |
| 28025080 |    7636 | 21.7751 | 1.87894  |  15.2 |  20.4 |  22.2 | 23.2  |  27   |
| 28025090 |   11867 | 22.4462 | 1.63726  |  16.8 |  21.6 |  22.8 | 23.6  |  27.4 |
| 28025502 |   12238 | 23.8882 | 1.275    |  19.1 |  23   |  23.8 | 24.8  |  28.6 |
| 28035010 |   10557 | 23.3568 | 1.43229  |  18.6 |  22.6 |  23.4 | 24.2  |  28.2 |
| 28035020 |   11824 | 22.8039 | 1.82207  |  16.4 |  21.8 |  23   | 24    |  28.6 |
| 28035040 |   13405 | 24.2796 | 1.21585  |  20   |  23.4 |  24.2 | 25    |  28.6 |
| 28035070 |      42 | 21.9435 | 0.847765 |  20.6 |  21.4 |  21.8 | 22.55 |  24   |
| 28045020 |    1052 | 21.31   | 1.76942  |  15   |  20.2 |  21.6 | 22.6  |  26.4 |
| 28045040 |    1274 | 23.1664 | 1.17635  |  19.2 |  22.4 |  23.2 | 24    |  26.6 |
| 29065010 |    1063 | 21.3275 | 1.5811   |  16   |  20.4 |  21.4 | 22.4  |  25.2 |
| 29065020 |   12983 | 22.3426 | 1.82354  |  15.6 |  21.2 |  22.6 | 23.6  |  27.4 |
| 29065030 |   11526 | 21.8128 | 1.55447  |  16   |  20.8 |  22   | 23    |  27   |

</div>



### Method 2 - Outliers processing through empirical rule - ER or _k-sigma_ ( $\mu$ - _k_ * $\sigma$ ) with _k_ = 3.5


The empirical rule, also referred to as the three-sigma rule or 68-95-99.7 rule, is a statistical rule which states that for a normal distribution, almost all observed data will fall within three standard deviations (denoted by $\sigma$) of the mean or average (denoted by $\mu$). In particular, the empirical rule predicts that 68% of observations falls within the first standard deviation ( $\mu$ � $\sigma$ ), 95% within the first two standard deviations ( $\mu$ � 2 $\sigma$ ), and 99.7% within the first three standard deviations ( $\mu$ � 3 $\sigma$ ).[^2]

Outliers parameters:
* mean: mean value
* std: standard deviation value
* OlMinVal: minimum outlier value founded
* OlMaxVal: maximum outlier value founded
* OlCount: # outliers founded
* CapLowerLim: capped lower limit for outliers replacement ( $\mu$ - 3.5 * $\sigma$ )
* CapUpperLim: capped upper limit for outliers replacement ( $\mu$ + 3.5 * $\sigma$ )


<div align="center">

|          |    mean |     std |   OlMinVal |   OlMaxVal |   OlCount |   CapLowerLim |   CapUpperLim |
|---------:|--------:|--------:|-----------:|-----------:|----------:|--------------:|--------------:|
| 15015020 | 22.1888 | 1.60856 |       16   |       16.4 |         2 |       16.5588 |       27.8188 |
| 15065040 | 22.9664 | 1.75384 |       12.4 |       16.6 |        21 |       16.828  |       29.1049 |
| 23215060 | 23.6837 | 1.20744 |       16.6 |       19.2 |         8 |       19.4576 |       27.9097 |
| 25025002 | 22.9428 | 1.56303 |       16.8 |       17.4 |        13 |       17.4722 |       28.4134 |
| 25025090 | 23.5651 | 1.53376 |       17   |       18   |        18 |       18.197  |       28.9333 |
| 25025250 | 22.3963 | 1.63717 |      nan   |      nan   |         0 |       16.6662 |       28.1264 |
| 25025300 | 22.9902 | 1.75271 |       15.4 |       16.8 |        16 |       16.8557 |       29.1247 |
| 25025330 | 22.7791 | 1.6933  |       13.1 |       16.8 |        42 |       16.8526 |       28.7057 |
| 28015030 | 22.9291 | 1.32774 |       10   |       18   |         6 |       18.282  |       27.5762 |
| 28015070 | 22.34   | 1.33165 |       15.4 |       17.6 |        36 |       17.6792 |       27.0007 |
| 28025020 | 20.547  | 1.73534 |       12   |       14.4 |        30 |       14.4733 |       26.6207 |
| 28025040 | 18.674  | 2.11514 |        8.4 |       27.4 |        22 |       11.271  |       26.077  |
| 28025070 | 23.7666 | 1.54724 |       17.4 |       18.2 |        18 |       18.3513 |       29.182  |
| 28025080 | 21.7751 | 1.87894 |      nan   |      nan   |         0 |       15.1988 |       28.3514 |
| 28025090 | 22.4272 | 1.67337 |       15   |       16.4 |        32 |       16.5704 |       28.284  |
| 28025502 | 23.8861 | 1.27915 |       18.4 |       28.6 |        12 |       19.4091 |       28.3631 |
| 28035010 | 23.3278 | 1.49337 |       13.4 |       28.8 |        26 |       18.101  |       28.5546 |
| 28035020 | 22.8005 | 1.82844 |       15.8 |       16.4 |        10 |       16.4009 |       29.2    |
| 28035040 | 24.269  | 1.23846 |       17.2 |       19.8 |        28 |       19.9343 |       28.6036 |
| 28035070 | 22.0286 | 1.01844 |       25.6 |       25.6 |         1 |       18.464  |       25.5931 |
| 28045020 | 21.2974 | 1.79272 |       14.6 |       15   |         4 |       15.0229 |       27.5719 |
| 28045040 | 23.128  | 1.26701 |       14.6 |       18.4 |         8 |       18.6935 |       27.5625 |
| 29065010 | 21.3162 | 1.60256 |       15.2 |       15.4 |         2 |       15.7072 |       26.9251 |
| 29065020 | 22.327  | 1.85521 |       14.2 |       15.8 |        45 |       15.8338 |       28.8203 |
| 29065030 | 21.8104 | 1.55983 |       14   |       16.2 |        10 |       16.351  |       27.2698 |

</div>


![R.LTWB](Outlier_ER_Pivot_TMN_CON.csv.png)

#### Identified and cleaning tables for 410 ER or k-sigma outliers founded
* Outliers identified file: [Outlier_ER_Pivot_TMN_CON.csv](../../.datasets/IDEAM_Outlier/Outlier_ER_Pivot_TMN_CON.csv)
* Outliers dropped file: [Outlier_ER_Drop_Pivot_TMN_CON.csv](../../.datasets/IDEAM_Outlier/Outlier_ER_Drop_Pivot_TMN_CON.csv)
* Outliers capped file: [Outlier_ER_Cap_Pivot_TMN_CON.csv](../../.datasets/IDEAM_Outlier/Outlier_ER_Cap_Pivot_TMN_CON.csv)
* Outliers imputed file: [Outlier_ER_Impute_Pivot_TMN_CON.csv](../../.datasets/IDEAM_Outlier/Outlier_ER_Impute_Pivot_TMN_CON.csv)


#### Statistical values for the capped and imputed file

<div align="center">

ER - General statistics table - Capped file

</div>


<div align="center">

|          |   count |    mean |     std |     min |   25% |   50% |   75% |     max |
|---------:|--------:|--------:|--------:|--------:|------:|------:|------:|--------:|
| 15015020 |    9964 | 22.1889 | 1.6083  | 16.5588 |  21.2 |  22.4 |  23.2 | 26.8    |
| 15065040 |    4949 | 22.9701 | 1.73927 | 16.828  |  22.2 |  23.2 |  24.2 | 27.8    |
| 23215060 |    1248 | 23.6922 | 1.17043 | 19.4576 |  23   |  23.8 |  24.6 | 26.8    |
| 25025002 |   10733 | 22.9432 | 1.56162 | 17.4722 |  22   |  23   |  24   | 27.2    |
| 25025090 |    9774 | 23.5661 | 1.53007 | 18.197  |  22.6 |  23.6 |  24.8 | 28      |
| 25025250 |   12340 | 22.3963 | 1.63717 | 17      |  21.2 |  22.4 |  23.8 | 27.1    |
| 25025300 |   11693 | 22.9911 | 1.7493  | 16.8557 |  22   |  23.2 |  24.2 | 27.8    |
| 25025330 |    9275 | 22.784  | 1.6732  | 16.8526 |  21.8 |  23   |  24   | 28.6    |
| 28015030 |    1404 | 22.9361 | 1.28376 | 18.282  |  22.2 |  23   |  23.8 | 26.8    |
| 28015070 |   12475 | 22.3423 | 1.3222  | 17.6792 |  21.5 |  22.5 |  23.2 | 26.2    |
| 28025020 |   13452 | 20.5485 | 1.72972 | 14.4733 |  19.6 |  20.8 |  21.8 | 26      |
| 28025040 |    3231 | 18.6787 | 2.09404 | 11.271  |  18   |  19.2 |  20   | 26.077  |
| 28025070 |   13818 | 23.7672 | 1.54513 | 18.3513 |  22.8 |  23.8 |  25   | 28.6    |
| 28025080 |    7636 | 21.7751 | 1.87894 | 15.2    |  20.4 |  22.2 |  23.2 | 27      |
| 28025090 |   11867 | 22.4284 | 1.66881 | 16.5704 |  21.6 |  22.8 |  23.6 | 27.4    |
| 28025502 |   12238 | 23.8864 | 1.27787 | 19.4091 |  23   |  23.8 |  24.8 | 28.3631 |
| 28035010 |   10557 | 23.3297 | 1.48523 | 18.101  |  22.6 |  23.4 |  24.2 | 28.5546 |
| 28035020 |   11824 | 22.8007 | 1.82776 | 16.4009 |  21.8 |  23   |  24   | 28.6    |
| 28035040 |   13405 | 24.2706 | 1.23193 | 19.9343 |  23.4 |  24.2 |  25   | 28.6    |
| 28035070 |      42 | 22.0284 | 1.01785 | 20.6    |  21.4 |  21.8 |  22.6 | 25.5931 |
| 28045020 |    1052 | 21.2981 | 1.79035 | 15.0229 |  20.2 |  21.6 |  22.6 | 26.4    |
| 28045040 |    1274 | 23.1354 | 1.23377 | 18.6935 |  22.4 |  23.2 |  24   | 26.6    |
| 29065010 |    1063 | 21.3169 | 1.59977 | 15.7072 |  20.4 |  21.4 |  22.4 | 25.2    |
| 29065020 |   12983 | 22.3293 | 1.84661 | 15.8338 |  21.2 |  22.6 |  23.6 | 27.4    |
| 29065030 |   11526 | 21.811  | 1.55732 | 16.351  |  20.8 |  22   |  23   | 27      |

</div>


<div align="center">

ER - General statistics table - Imputed file

</div>


<div align="center">

|          |   count |    mean |      std |   min |   25% |     50% |   75% |   max |
|---------:|--------:|--------:|---------:|------:|------:|--------:|------:|------:|
| 15015020 |    9964 | 22.19   | 1.60632  |  16.6 |  21.2 | 22.4    | 23.2  |  26.8 |
| 15065040 |    4949 | 22.9961 | 1.69241  |  17   |  22.2 | 23.2    | 24.2  |  27.8 |
| 23215060 |    1248 | 23.7193 | 1.11988  |  19.8 |  23   | 23.8    | 24.6  |  26.8 |
| 25025002 |   10733 | 22.9498 | 1.54996  |  17.6 |  22   | 23      | 24    |  27.2 |
| 25025090 |    9774 | 23.576  | 1.51259  |  18.2 |  22.6 | 23.6    | 24.8  |  28   |
| 25025250 |   12340 | 22.3963 | 1.63717  |  17   |  21.2 | 22.4    | 23.8  |  27.1 |
| 25025300 |   11693 | 22.9995 | 1.73449  |  17   |  22   | 23.2    | 24.2  |  27.8 |
| 25025330 |    9275 | 22.8109 | 1.62466  |  16.9 |  21.8 | 23      | 24    |  28.6 |
| 28015030 |    1404 | 22.956  | 1.247    |  18.3 |  22.2 | 23      | 23.8  |  26.8 |
| 28015070 |   12475 | 22.3558 | 1.29819  |  17.8 |  21.5 | 22.5    | 23.2  |  26.2 |
| 28025020 |   13452 | 20.562  | 1.7057   |  14.6 |  19.6 | 20.8    | 21.8  |  26   |
| 28025040 |    3231 | 18.7245 | 2.0023   |  11.4 |  18   | 19.2    | 20    |  24   |
| 28025070 |   13818 | 23.7743 | 1.5327   |  18.4 |  22.8 | 23.8    | 25    |  28.6 |
| 28025080 |    7636 | 21.7751 | 1.87894  |  15.2 |  20.4 | 22.2    | 23.2  |  27   |
| 28025090 |   11867 | 22.4442 | 1.64077  |  16.6 |  21.6 | 22.8    | 23.6  |  27.4 |
| 28025502 |   12238 | 23.8886 | 1.27015  |  19.5 |  23   | 23.8861 | 24.8  |  28.3 |
| 28035010 |   10557 | 23.3416 | 1.46234  |  18.2 |  22.6 | 23.4    | 24.2  |  28.4 |
| 28035020 |   11824 | 22.8061 | 1.81825  |  16.6 |  21.8 | 23      | 24    |  28.6 |
| 28035040 |   13405 | 24.2796 | 1.21585  |  20   |  23.4 | 24.2    | 25    |  28.6 |
| 28035070 |      42 | 21.9435 | 0.847765 |  20.6 |  21.4 | 21.8    | 22.55 |  24   |
| 28045020 |    1052 | 21.3219 | 1.74783  |  15.6 |  20.2 | 21.6    | 22.6  |  26.4 |
| 28045040 |    1274 | 23.1632 | 1.18212  |  19   |  22.4 | 23.2    | 24    |  26.6 |
| 29065010 |    1063 | 21.3275 | 1.5811   |  16   |  20.4 | 21.4    | 22.4  |  25.2 |
| 29065020 |   12983 | 22.3518 | 1.80643  |  16   |  21.2 | 22.6    | 23.6  |  27.4 |
| 29065030 |   11526 | 21.8158 | 1.54899  |  16.4 |  20.8 | 22      | 23    |  27   |

</div>



### Method 3 - Outliers processing through Z-score >= 3.5 or standard core


Z score is an important concept in statistics. Z score is also called standard score. This score helps to understand if each data value is greater or smaller than mean and how far away it is from the mean. More specifically, Z score tells how many standard deviations away a data point is from the mean. Z = ( x - $\mu$ ) / $\sigma$.[^3]


> Altought with this method, the identified outliers are the same obtained in Method 2 that uses the empirical rule when the Z-score threshold is the same _k-sigma_ value, the Method 3 creates the Z-score table values. Use this method to compare the identified outliers with differents _k-sigma_ values.

Outliers parameters:
* mean: mean value
* std: standard deviation value
* OlMinVal: minimum outlier value founded
* OlMaxVal: maximum outlier value founded
* OlCount: # outliers founded
* CapLowerLim: capped lower limit for outliers replacement ( $\mu$ - 3.5 * $\sigma$ )
* CapUpperLim: capped upper limit for outliers replacement ( $\mu$ + 3.5 * $\sigma$ )


<div align="center">

|          |    mean |     std |   OlMinVal |   OlMaxVal |   OlCount |   CapLowerLim |   CapUpperLim |
|---------:|--------:|--------:|-----------:|-----------:|----------:|--------------:|--------------:|
| 15015020 | 22.1888 | 1.60856 |       16   |       16.4 |         2 |       16.5588 |       27.8188 |
| 15065040 | 22.9664 | 1.75384 |       12.4 |       16.6 |        21 |       16.828  |       29.1049 |
| 23215060 | 23.6837 | 1.20744 |       16.6 |       19.2 |         8 |       19.4576 |       27.9097 |
| 25025002 | 22.9428 | 1.56303 |       16.8 |       17.4 |        13 |       17.4722 |       28.4134 |
| 25025090 | 23.5651 | 1.53376 |       17   |       18   |        18 |       18.197  |       28.9333 |
| 25025250 | 22.3963 | 1.63717 |      nan   |      nan   |         0 |       16.6662 |       28.1264 |
| 25025300 | 22.9902 | 1.75271 |       15.4 |       16.8 |        16 |       16.8557 |       29.1247 |
| 25025330 | 22.7791 | 1.6933  |       13.1 |       16.8 |        42 |       16.8526 |       28.7057 |
| 28015030 | 22.9291 | 1.32774 |       10   |       18   |         6 |       18.282  |       27.5762 |
| 28015070 | 22.34   | 1.33165 |       15.4 |       17.6 |        36 |       17.6792 |       27.0007 |
| 28025020 | 20.547  | 1.73534 |       12   |       14.4 |        30 |       14.4733 |       26.6207 |
| 28025040 | 18.674  | 2.11514 |        8.4 |       27.4 |        22 |       11.271  |       26.077  |
| 28025070 | 23.7666 | 1.54724 |       17.4 |       18.2 |        18 |       18.3513 |       29.182  |
| 28025080 | 21.7751 | 1.87894 |      nan   |      nan   |         0 |       15.1988 |       28.3514 |
| 28025090 | 22.4272 | 1.67337 |       15   |       16.4 |        32 |       16.5704 |       28.284  |
| 28025502 | 23.8861 | 1.27915 |       18.4 |       28.6 |        12 |       19.4091 |       28.3631 |
| 28035010 | 23.3278 | 1.49337 |       13.4 |       28.8 |        26 |       18.101  |       28.5546 |
| 28035020 | 22.8005 | 1.82844 |       15.8 |       16.4 |        10 |       16.4009 |       29.2    |
| 28035040 | 24.269  | 1.23846 |       17.2 |       19.8 |        28 |       19.9343 |       28.6036 |
| 28035070 | 22.0286 | 1.01844 |       25.6 |       25.6 |         1 |       18.464  |       25.5931 |
| 28045020 | 21.2974 | 1.79272 |       14.6 |       15   |         4 |       15.0229 |       27.5719 |
| 28045040 | 23.128  | 1.26701 |       14.6 |       18.4 |         8 |       18.6935 |       27.5625 |
| 29065010 | 21.3162 | 1.60256 |       15.2 |       15.4 |         2 |       15.7072 |       26.9251 |
| 29065020 | 22.327  | 1.85521 |       14.2 |       15.8 |        45 |       15.8338 |       28.8203 |
| 29065030 | 21.8104 | 1.55983 |       14   |       16.2 |        10 |       16.351  |       27.2698 |

</div>


![R.LTWB](Outlier_ZScore_Pivot_TMN_CON.csv.png)

#### Identified and cleaning tables for 410 Z-score or standard core outliers founded
* Outliers Z-score values file: [Outlier_ZScore_Value_Pivot_TMN_CON.csv](../../.datasets/IDEAM_Outlier/Outlier_ZScore_Value_Pivot_TMN_CON.csv)
* Outliers identified file: [Outlier_ZScore_Pivot_TMN_CON.csv](../../.datasets/IDEAM_Outlier/Outlier_ZScore_Pivot_TMN_CON.csv)
* Outliers dropped file: [Outlier_ZScore_Drop_Pivot_TMN_CON.csv](../../.datasets/IDEAM_Outlier/Outlier_ZScore_Drop_Pivot_TMN_CON.csv)
* Outliers capped file: [Outlier_ZScore_Cap_Pivot_TMN_CON.csv](../../.datasets/IDEAM_Outlier/Outlier_ZScore_Cap_Pivot_TMN_CON.csv)
* Outliers imputed file: [Outlier_ZScore_Impute_Pivot_TMN_CON.csv](../../.datasets/IDEAM_Outlier/Outlier_ZScore_Impute_Pivot_TMN_CON.csv)


#### Statistical values for the capped and imputed file

<div align="center">

Z-score - General statistics table - Capped file

</div>


<div align="center">

|          |   count |    mean |     std |     min |   25% |   50% |   75% |     max |
|---------:|--------:|--------:|--------:|--------:|------:|------:|------:|--------:|
| 15015020 |    9964 | 22.1889 | 1.6083  | 16.5588 |  21.2 |  22.4 |  23.2 | 26.8    |
| 15065040 |    4949 | 22.9701 | 1.73927 | 16.828  |  22.2 |  23.2 |  24.2 | 27.8    |
| 23215060 |    1248 | 23.6922 | 1.17043 | 19.4576 |  23   |  23.8 |  24.6 | 26.8    |
| 25025002 |   10733 | 22.9432 | 1.56162 | 17.4722 |  22   |  23   |  24   | 27.2    |
| 25025090 |    9774 | 23.5661 | 1.53007 | 18.197  |  22.6 |  23.6 |  24.8 | 28      |
| 25025250 |   12340 | 22.3963 | 1.63717 | 17      |  21.2 |  22.4 |  23.8 | 27.1    |
| 25025300 |   11693 | 22.9911 | 1.7493  | 16.8557 |  22   |  23.2 |  24.2 | 27.8    |
| 25025330 |    9275 | 22.784  | 1.6732  | 16.8526 |  21.8 |  23   |  24   | 28.6    |
| 28015030 |    1404 | 22.9361 | 1.28376 | 18.282  |  22.2 |  23   |  23.8 | 26.8    |
| 28015070 |   12475 | 22.3423 | 1.3222  | 17.6792 |  21.5 |  22.5 |  23.2 | 26.2    |
| 28025020 |   13452 | 20.5485 | 1.72972 | 14.4733 |  19.6 |  20.8 |  21.8 | 26      |
| 28025040 |    3231 | 18.6787 | 2.09404 | 11.271  |  18   |  19.2 |  20   | 26.077  |
| 28025070 |   13818 | 23.7672 | 1.54513 | 18.3513 |  22.8 |  23.8 |  25   | 28.6    |
| 28025080 |    7636 | 21.7751 | 1.87894 | 15.2    |  20.4 |  22.2 |  23.2 | 27      |
| 28025090 |   11867 | 22.4284 | 1.66881 | 16.5704 |  21.6 |  22.8 |  23.6 | 27.4    |
| 28025502 |   12238 | 23.8864 | 1.27787 | 19.4091 |  23   |  23.8 |  24.8 | 28.3631 |
| 28035010 |   10557 | 23.3297 | 1.48523 | 18.101  |  22.6 |  23.4 |  24.2 | 28.5546 |
| 28035020 |   11824 | 22.8007 | 1.82776 | 16.4009 |  21.8 |  23   |  24   | 28.6    |
| 28035040 |   13405 | 24.2706 | 1.23193 | 19.9343 |  23.4 |  24.2 |  25   | 28.6    |
| 28035070 |      42 | 22.0284 | 1.01785 | 20.6    |  21.4 |  21.8 |  22.6 | 25.5931 |
| 28045020 |    1052 | 21.2981 | 1.79035 | 15.0229 |  20.2 |  21.6 |  22.6 | 26.4    |
| 28045040 |    1274 | 23.1354 | 1.23377 | 18.6935 |  22.4 |  23.2 |  24   | 26.6    |
| 29065010 |    1063 | 21.3169 | 1.59977 | 15.7072 |  20.4 |  21.4 |  22.4 | 25.2    |
| 29065020 |   12983 | 22.3293 | 1.84661 | 15.8338 |  21.2 |  22.6 |  23.6 | 27.4    |
| 29065030 |   11526 | 21.811  | 1.55732 | 16.351  |  20.8 |  22   |  23   | 27      |

</div>


<div align="center">

Z-score - General statistics table - Imputed file

</div>


<div align="center">

|          |   count |    mean |      std |   min |   25% |     50% |   75% |   max |
|---------:|--------:|--------:|---------:|------:|------:|--------:|------:|------:|
| 15015020 |    9964 | 22.19   | 1.60632  |  16.6 |  21.2 | 22.4    | 23.2  |  26.8 |
| 15065040 |    4949 | 22.9961 | 1.69241  |  17   |  22.2 | 23.2    | 24.2  |  27.8 |
| 23215060 |    1248 | 23.7193 | 1.11988  |  19.8 |  23   | 23.8    | 24.6  |  26.8 |
| 25025002 |   10733 | 22.9498 | 1.54996  |  17.6 |  22   | 23      | 24    |  27.2 |
| 25025090 |    9774 | 23.576  | 1.51259  |  18.2 |  22.6 | 23.6    | 24.8  |  28   |
| 25025250 |   12340 | 22.3963 | 1.63717  |  17   |  21.2 | 22.4    | 23.8  |  27.1 |
| 25025300 |   11693 | 22.9995 | 1.73449  |  17   |  22   | 23.2    | 24.2  |  27.8 |
| 25025330 |    9275 | 22.8109 | 1.62466  |  16.9 |  21.8 | 23      | 24    |  28.6 |
| 28015030 |    1404 | 22.956  | 1.247    |  18.3 |  22.2 | 23      | 23.8  |  26.8 |
| 28015070 |   12475 | 22.3558 | 1.29819  |  17.8 |  21.5 | 22.5    | 23.2  |  26.2 |
| 28025020 |   13452 | 20.562  | 1.7057   |  14.6 |  19.6 | 20.8    | 21.8  |  26   |
| 28025040 |    3231 | 18.7245 | 2.0023   |  11.4 |  18   | 19.2    | 20    |  24   |
| 28025070 |   13818 | 23.7743 | 1.5327   |  18.4 |  22.8 | 23.8    | 25    |  28.6 |
| 28025080 |    7636 | 21.7751 | 1.87894  |  15.2 |  20.4 | 22.2    | 23.2  |  27   |
| 28025090 |   11867 | 22.4442 | 1.64077  |  16.6 |  21.6 | 22.8    | 23.6  |  27.4 |
| 28025502 |   12238 | 23.8886 | 1.27015  |  19.5 |  23   | 23.8861 | 24.8  |  28.3 |
| 28035010 |   10557 | 23.3416 | 1.46234  |  18.2 |  22.6 | 23.4    | 24.2  |  28.4 |
| 28035020 |   11824 | 22.8061 | 1.81825  |  16.6 |  21.8 | 23      | 24    |  28.6 |
| 28035040 |   13405 | 24.2796 | 1.21585  |  20   |  23.4 | 24.2    | 25    |  28.6 |
| 28035070 |      42 | 21.9435 | 0.847765 |  20.6 |  21.4 | 21.8    | 22.55 |  24   |
| 28045020 |    1052 | 21.3219 | 1.74783  |  15.6 |  20.2 | 21.6    | 22.6  |  26.4 |
| 28045040 |    1274 | 23.1632 | 1.18212  |  19   |  22.4 | 23.2    | 24    |  26.6 |
| 29065010 |    1063 | 21.3275 | 1.5811   |  16   |  20.4 | 21.4    | 22.4  |  25.2 |
| 29065020 |   12983 | 22.3518 | 1.80643  |  16   |  21.2 | 22.6    | 23.6  |  27.4 |
| 29065030 |   11526 | 21.8158 | 1.54899  |  16.4 |  20.8 | 22      | 23    |  27   |

</div>



> The _drop files_ contains the database values without the outliers identified.
>
> The _capped files_ contains the database values and the outliers has been replaced with the lower or upper capped value calculated. Lower outliers could be replaced with negative values because the limit is defined with (mean() - cap_multiplier * std()). In some cases like _temperature analysis_, the upper outliers values could be replaced with values over the original values and you can try to fix this issue changing the parameter _cap_multiplier_ that defines the stripe values range.
>
> The imputation method replace each outlier value with the mean value that contains the original outliers values.


[^1]: Adapted from: https://careerfoundry.com/en/blog/data-analytics/how-to-find-outliers/
[^2]: https://www.investopedia.com/terms/e/empirical-rule.asp
[^3]: Adapted from: https://www.geeksforgeeks.org/z-score-for-outlier-detection-python/