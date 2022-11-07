## Outliers detection and processing through statistical methods

* Processed file: [D:/R.LTWB/.datasets/IDEAM_EDA/Pivot_EV_TT_D.csv](../IDEAM_EDA/Pivot_EV_TT_D.csv)
* Execution date: 2022-11-07 10:58:24.937806
* Python version: 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)]
* Python path: ['D:\\R.LTWB\\.src', 'D:\\R.LTWB', 'D:\\R.TeachingResearchGuide', 'D:\\R.HydroTools', 'D:\\R.GISPython']
* matplotlib version: 3.6.0
* pandas version: 1.4.3
* numpy version: 1.23.2
* Stations exclude: ['28017140', '25027020', '25027410', '25027490', '25027330', '25027390', '25027630', '25027360', '25027320', '16067010', '25027420']
* Print table sample: True
* Instructions & script: https://github.com/rcfdtools/R.LTWB/tree/main/Section03/Outlier
* License: https://github.com/rcfdtools/R.LTWB/blob/main/LICENSE.md
* Credits: r.cfdtools@gmail.com


### General dataframe information with 4821 IDEAM records for 1 stations

Dataframe records head sample

| Fecha               |   29065130 |
|:--------------------|-----------:|
| 2008-10-20 00:00:00 |          0 |
| 2008-10-21 00:00:00 |          0 |
| 2008-10-22 00:00:00 |          0 |

Dataframe records tail sample

| Fecha               |   29065130 |
|:--------------------|-----------:|
| 2021-12-29 00:00:00 |       2013 |
| 2021-12-30 00:00:00 |       1963 |
| 2021-12-31 00:00:00 |       1847 |

Datatypes for station and nulls values in the initial file

<div align="center">

|       | 29065130   |
|:------|:-----------|
| Dtype | float64    |
| Nulls | 0          |

</div>


<div align="center">

General statistics table - Initial file

</div>


<div align="center">

|          |   count |    mean |     std |   min |   25% |   50% |   75% |   max |
|---------:|--------:|--------:|--------:|------:|------:|------:|------:|------:|
| 29065130 |    4821 | 281.089 | 625.398 |  -176 |     0 |     0 |   139 |  2529 |

</div>

### Method 1 - Outliers processing using the interquartile range IQR (q1 = 0.25, q3 = 0.75)

Since the data doesn`t follow a normal distribution, we will calculate the outlier data points using the statistical method called interquartile range (IQR) instead of using Z-score. Using the IQR, the outlier data points are the ones falling below Q1 - 1.5 IQR or above Q3 + 1.5 IQR. The Q1 could be the 25th percentile and Q3 could be the 75th percentile of the dataset, and IQR represents the interquartile range calculated by Q3 minus Q1 (Q3-Q1). [^1]

Outliers parameters:
* mean: mean value
* std: standard deviation value
* q1: quartile 0.25
* q3: quartile 0.75
* IQR: interquartile range (q3-q1)
* OlLowerLim: outlier bottom limit (q1-1.5*IQR)
* OlUpperLim: outlier top limit (q3+1.5*IQR)
* OlMinVal: minimum outlier value founded
* OlMaxVal: maximum outlier value founded
* OlCount: # outliers founded
* CapLowerLim: capped lower limit for outliers replacement ( $\mu$ - 0.45 * $\sigma$ )
* CapUpperLim: capped upper limit for outliers replacement ( $\mu$ + 0.45 * $\sigma$ )


<div align="center">

|          |    mean |     std |   q1 |   q3 |   IQR |   OlLowerLim |   OlUpperLim |   OlMinVal |   OlMaxVal |   OlCount |   CapLowerLim |   CapUpperLim |
|---------:|--------:|--------:|-----:|-----:|------:|-------------:|-------------:|-----------:|-----------:|----------:|--------------:|--------------:|
| 29065130 | 281.089 | 625.398 |    0 |  139 |   139 |        208.5 |        347.5 |        350 |       2529 |       781 |      -0.34029 |       562.518 |

</div>


![R.LTWB](Outlier_IQR_Pivot_EV_TT_D.csv.png)

#### Identified and cleaning tables for 781 IQR outliers founded
* Outliers identified file: [Outlier_IQR_Pivot_EV_TT_D.csv](../../.datasets/IDEAM_Outlier/Outlier_IQR_Pivot_EV_TT_D.csv)
* Outliers dropped file: [Outlier_IQR_Drop_Pivot_EV_TT_D.csv](../../.datasets/IDEAM_Outlier/Outlier_IQR_Drop_Pivot_EV_TT_D.csv)
* Outliers capped file: [Outlier_IQR_Cap_Pivot_EV_TT_D.csv](../../.datasets/IDEAM_Outlier/Outlier_IQR_Cap_Pivot_EV_TT_D.csv)
* Outliers imputed file: [Outlier_IQR_Impute_Pivot_EV_TT_D.csv](../../.datasets/IDEAM_Outlier/Outlier_IQR_Impute_Pivot_EV_TT_D.csv)


#### Statistical values for the capped and imputed file

<div align="center">

IQR - General statistics table - Capped file

</div>


<div align="center">

|          |   count |    mean |     std |   min |   25% |   50% |   75% |     max |
|---------:|--------:|--------:|--------:|------:|------:|------:|------:|--------:|
| 29065130 |    4821 | 119.339 | 205.785 |  -176 |     0 |     0 |   139 | 562.518 |

</div>


<div align="center">

IQR - General statistics table - Imputed file

</div>


<div align="center">

|          |   count |   mean |    std |   min |   25% |   50% |   75% |   max |
|---------:|--------:|-------:|-------:|------:|------:|------:|------:|------:|
| 29065130 |    4821 | 73.748 | 112.62 |  -176 |     0 |     0 |   139 |   347 |

</div>



### Method 2 - Outliers processing through empirical rule - ER or _k-sigma_ ( $\mu$ - _k_ * $\sigma$ ) with _k_ = 0.45


The empirical rule, also referred to as the three-sigma rule or 68-95-99.7 rule, is a statistical rule which states that for a normal distribution, almost all observed data will fall within three standard deviations (denoted by $\sigma$) of the mean or average (denoted by $\mu$). In particular, the empirical rule predicts that 68% of observations falls within the first standard deviation ( $\mu$ ± $\sigma$ ), 95% within the first two standard deviations ( $\mu$ ± 2 $\sigma$ ), and 99.7% within the first three standard deviations ( $\mu$ ± 3 $\sigma$ ).[^2]

Outliers parameters:
* mean: mean value
* std: standard deviation value
* OlMinVal: minimum outlier value founded
* OlMaxVal: maximum outlier value founded
* OlCount: # outliers founded
* CapLowerLim: capped lower limit for outliers replacement ( $\mu$ - 0.45 * $\sigma$ )
* CapUpperLim: capped upper limit for outliers replacement ( $\mu$ + 0.45 * $\sigma$ )


<div align="center">

|          |    mean |     std |   OlMinVal |   OlMaxVal |   OlCount |   CapLowerLim |   CapUpperLim |
|---------:|--------:|--------:|-----------:|-----------:|----------:|--------------:|--------------:|
| 29065130 | 281.089 | 625.398 |       -176 |       2529 |       706 |      -0.34029 |       562.518 |

</div>


![R.LTWB](Outlier_ER_Pivot_EV_TT_D.csv.png)

#### Identified and cleaning tables for 706 ER or k-sigma outliers founded
* Outliers identified file: [Outlier_ER_Pivot_EV_TT_D.csv](../../.datasets/IDEAM_Outlier/Outlier_ER_Pivot_EV_TT_D.csv)
* Outliers dropped file: [Outlier_ER_Drop_Pivot_EV_TT_D.csv](../../.datasets/IDEAM_Outlier/Outlier_ER_Drop_Pivot_EV_TT_D.csv)
* Outliers capped file: [Outlier_ER_Cap_Pivot_EV_TT_D.csv](../../.datasets/IDEAM_Outlier/Outlier_ER_Cap_Pivot_EV_TT_D.csv)
* Outliers imputed file: [Outlier_ER_Impute_Pivot_EV_TT_D.csv](../../.datasets/IDEAM_Outlier/Outlier_ER_Impute_Pivot_EV_TT_D.csv)


#### Statistical values for the capped and imputed file

<div align="center">

ER - General statistics table - Capped file

</div>


<div align="center">

|          |   count |   mean |    std |      min |   25% |   50% |   75% |     max |
|---------:|--------:|-------:|-------:|---------:|------:|------:|------:|--------:|
| 29065130 |    4821 | 116.76 | 200.93 | -0.34029 |     0 |     0 |   139 | 562.518 |

</div>


<div align="center">

ER - General statistics table - Imputed file

</div>


<div align="center">

|          |   count |    mean |    std |   min |   25% |   50% |   75% |   max |
|---------:|--------:|--------:|-------:|------:|------:|------:|------:|------:|
| 29065130 |    4821 | 76.3636 | 117.73 |     0 |     0 |     0 |   140 |   557 |

</div>



### Method 3 - Outliers processing through Z-score >= 0.25 or standard core


Z score is an important concept in statistics. Z score is also called standard score. This score helps to understand if each data value is greater or smaller than mean and how far away it is from the mean. More specifically, Z score tells how many standard deviations away a data point is from the mean. Z = ( x - $\mu$ ) / $\sigma$.[^3]


> Altought with this method, the identified outliers are the same obtained in Method 2 that uses the empirical rule when the Z-score threshold is the same _k-sigma_ value, the Method 3 creates the Z-score table values. Use this method to compare the identified outliers with differents _k-sigma_ values.

Outliers parameters:
* mean: mean value
* std: standard deviation value
* OlMinVal: minimum outlier value founded
* OlMaxVal: maximum outlier value founded
* OlCount: # outliers founded
* CapLowerLim: capped lower limit for outliers replacement ( $\mu$ - 0.45 * $\sigma$ )
* CapUpperLim: capped upper limit for outliers replacement ( $\mu$ + 0.45 * $\sigma$ )


<div align="center">

|          |    mean |     std |   OlMinVal |   OlMaxVal |   OlCount |   CapLowerLim |   CapUpperLim |
|---------:|--------:|--------:|-----------:|-----------:|----------:|--------------:|--------------:|
| 29065130 | 281.089 | 625.398 |        438 |       2529 |       714 |      -0.34029 |       562.518 |

</div>


![R.LTWB](Outlier_ZScore_Pivot_EV_TT_D.csv.png)

#### Identified and cleaning tables for 714 Z-score or standard core outliers founded
* Outliers Z-score values file: [Outlier_ZScore_Value_Pivot_EV_TT_D.csv](../../.datasets/IDEAM_Outlier/Outlier_ZScore_Value_Pivot_EV_TT_D.csv)
* Outliers identified file: [Outlier_ZScore_Pivot_EV_TT_D.csv](../../.datasets/IDEAM_Outlier/Outlier_ZScore_Pivot_EV_TT_D.csv)
* Outliers dropped file: [Outlier_ZScore_Drop_Pivot_EV_TT_D.csv](../../.datasets/IDEAM_Outlier/Outlier_ZScore_Drop_Pivot_EV_TT_D.csv)
* Outliers capped file: [Outlier_ZScore_Cap_Pivot_EV_TT_D.csv](../../.datasets/IDEAM_Outlier/Outlier_ZScore_Cap_Pivot_EV_TT_D.csv)
* Outliers imputed file: [Outlier_ZScore_Impute_Pivot_EV_TT_D.csv](../../.datasets/IDEAM_Outlier/Outlier_ZScore_Impute_Pivot_EV_TT_D.csv)


#### Statistical values for the capped and imputed file

<div align="center">

Z-score - General statistics table - Capped file

</div>


<div align="center">

|          |   count |    mean |   std |     min |     25% |     50% |   75% |     max |
|---------:|--------:|--------:|------:|--------:|--------:|--------:|------:|--------:|
| 29065130 |    4821 | 183.438 | 114.5 | 124.739 | 124.739 | 124.739 |   139 | 437.438 |

</div>


<div align="center">

Z-score - General statistics table - Imputed file

</div>


<div align="center">

|          |   count |    mean |     std |   min |     25% |     50% |     75% |   max |
|---------:|--------:|--------:|--------:|------:|--------:|--------:|--------:|------:|
| 29065130 |    4821 | 275.801 | 30.5568 |   125 | 281.089 | 281.089 | 281.089 |   437 |

</div>



> The _drop files_ contains the database values without the outliers identified.
>
> The _capped files_ contains the database values and the outliers has been replaced with the lower or upper capped value calculated. Lower outliers could be replaced with negative values because the limit is defined with (mean() - cap_multiplier * std()). In some cases like _temperature analysis_, the upper outliers values could be replaced with values over the original values and you can try to fix this issue changing the parameter _cap_multiplier_ that defines the stripe values range.
>
> The imputation method replace each outlier value with the mean value that contains the original outliers values.


[^1]: Adapted from: https://careerfoundry.com/en/blog/data-analytics/how-to-find-outliers/
[^2]: https://www.investopedia.com/terms/e/empirical-rule.asp
[^3]: Adapted from: https://www.geeksforgeeks.org/z-score-for-outlier-detection-python/
