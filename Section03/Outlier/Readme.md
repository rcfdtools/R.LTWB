## Identificación y procesamiento de datos atípicos - Outliers
Keywords: `Outlier` `matplotlib` `pandas` `tabulate` `numpy` `dtypes` `isnull` `describe` `Drop` `Capped` `Impute` `Interquartile-range` `Empirical-rule` `Z-score`

<div align="center"><img alt="R.LTWB" src="Graph/Outlier.png" width="95%"></div> 

En esta actividad se obtienen los parámetros estadísticos de cada parámetro hidroclimatológico en cada estación y se identifican, excluyen y completan los datos atípicos a través de métodos estadísticos.

Para el desarrollo de esta actividad se utilizarán los siguientes métodos:

* Método 1 - Rango intercuartílico - IQR[^1]: aplica para datos que no siguen una distribución normal y permite identificar valores atípicos a partir de valores que se encuentran por fuera del rango intercuartílico Q1 a Q3. El valor del primer cuartil puede corresponder al percentil 25 y el valor del tercer cuartil puede corresponder al percentil 75 del conjunto de datos, por lo que el rango intercuartílico se calcula como Q3-Q1.  
* Método 2 - Regla empírica - ER[^2]: este método, también denominado regla 3-sigma o regla 68-5-99.7 correspondientes a una distribución normal, permiten identificar valores atípicos cuyas observaciones se encuentran fuera de la banda $\mu$ +- K * $\sigma$. 
* Método 3 - núcleo estándar Z-score[^3]: este método, similar o idéntico al método 2, permite calificar cada observación a partir del valor Z = ( x - $\mu$ ) / $\sigma$. Valores fuera de un valor establecido, p.ej. Z-score=3, son identificados como atípicos.


### Objetivos

* Obtener estadísticas generales de cada estación para cada parámetro hidroclimatológico.
* Identificar valores atípicos a través de diferentes métodos estadísticos (Rango intercuartílico - IQR, regla empírica - ER y núcleo estándar Z-score).
* Representar gráficamente las series de cada parámetro visualizando también los datos atípicos identificados.
* Excluir valores atípicos de la matriz de estaciones para cada parámetro.
* Reemplazar valores atípicos por valores límite definidos a partir de un rango de confianza ( $\mu$ +- K * $\sigma$ ).
* Imputar valores atípicos con el valor de la media de cada estación.


### Requerimientos

* [Python 3+](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/docs/index.html) para Python
* [Tabulate](https://pypi.org/project/tabulate/) para Python, requerido para impresión de tablas en formato Markdown desde pandas.
* [numpy](https://numpy.org/) para python.
* [Notepad++](https://notepad-plus-plus.org/), editor de texto y código.
* Tablas dinámicas (pivot tables) con series de datos discretos de estaciones terrestres del IDEAM por parámetro hidroclimatológico. [:mortar_board:Aprender.](../EDA)


### Procedimiento general

<div align="center">
<br><img alt="R.LTWB" src="Graph/Outlier.svg" width="100%"><br>
<sub>Convenciones generales en diagramas: clases de entidad en azul, dataset en gris oscuro, grillas en color verde, geo-procesos en rojo, procesos automáticos o semiautomáticos en guiones rojos y procesos manuales en amarillo. Líneas conectoras con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>

1. Para realizar la identificación y procesamiento de datos atípicos, descargue el script [Outlier.py](../../.src/Outlier.py) y guárdelo en la carpeta local `D:\R.LTWB\.src` de su equipo.

**Funcionalidades del script**

* Identificación de atípicos por 3 métodos estadísticos (Método 1 - Rango intercuartílico - IQR, Método 2 - Regla empírica - ER y Método 3 - núcleo estándar Z-score).
* Permite definir la tabla dinámica (pivot table) del parámetro hidroclimatológico a evaluar.
* El usuario puede excluir estaciones del análisis a través de la variable `station_exclude`.
* Definición del cuartil inferior `q1_val` y superior `q3_val` que define el rango de exclusión en el método de rango intercuartílico - IQR.
* Definición manual del multiplicador `cap_multiplier` o K-sigma que permite definir los valores de reemplazo ( $\mu$ +- K * $\sigma$ ).  
* Definición manual del límite de exclusión `zscore_threshold` en el método de exclusión por núcleo estándar.
* Análisis masivo de estaciones por parámetro hidroclimatológico con estadísticos, parámetros de evaluación y gráficas con marcado de atípicos.
* Generación de reportes detallados Markdown por cada parámetro hidroclimatológico evaluado. [IDEAM_Outlier](../../.datasets/IDEAM_Outlier).
* Para cada método y cada parámetro hidroclimatológico analizado, crea las siguientes tablas: datos atípicos identificados, datos de entrada sin datos atípicos (drop), datos de entrada con datos atípicos reemplazados (cap) y datos de entrada con datos atípicos imputados (impute). 

> En el Método 3 o núcleo estándar Z-score, se genera una tabla adicional para cada parámetro hidroclimatológico que contiene los puntajes a partir de los cuales se realiza la identificación de valores atípicos.   
> 
> Para el ejemplo, se han excluido diferentes estaciones con registros de caudal sobre el Río Magdalena y otros ríos con caudales altos.

Contenido del script

```
# -*- coding: UTF-8 -*-
# Name: Outlier.py
# Description: outliers detection and processing through statistical methods
# Requirements: Python 3+, pandas, tabulate
# Attention: do not convert the .csv file into an Excel file because you would need process more than 1048576 records.


# Libraries
import sys
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import tabulate  # required for print tables in Markdown using pandas
from datetime import datetime


# Function for print and show results in a file
def print_log(txt_print, on_screen=True, center_div=False):
    if on_screen:
        print(txt_print)
    if center_div:
        file_log.write('\n<div align="center">\n' + '\n')
    file_log.write(txt_print + '\n')
    if center_div:
        file_log.write('\n</div>\n' + '\n')

# Function to find or drop outliers using interquartile range - IQR
# Ref: https://careerfoundry.com/en/blog/data-analytics/how-to-find-outliers/
def find_drop_outliers_IQR(df, drop=True):
    # drop: True for only drop values, False for only find values.
    q1 = df.quantile(q1_val)
    q3 = df.quantile(q3_val)
    IQR = q3-q1
    if drop:
        outliers = df[~((df < (q1 - 1.5 * IQR)) | (df > (q3 + 1.5 * IQR)))]
    else:
        outliers = df[((df < (q1-1.5*IQR)) | (df > (q3+1.5*IQR)))]
    return outliers

# Function for Cap IQR outliers with specified limits (mean() - cap_multiplier * std())
def cap_outliers_IQR(df):
    column_headers = df.columns.values.tolist()
    index_list = list(df.index.values)
    q1 = df.quantile(q1_val)
    q3 = df.quantile(q3_val)
    IQR = q3-q1
    upper = df[~(df > (q3+1.5*IQR))].max()
    lower = df[~(df < (q1-1.5*IQR))].min()
    lower_cap = df.mean() - cap_multiplier * df.std()
    upper_cap = df.mean() + cap_multiplier * df.std()
    df = np.where(df > upper,
       upper_cap,
       np.where(
           df < lower,
           lower_cap,
           df
           )
       )
    df = pd.DataFrame(df, columns=column_headers, index=index_list) # Convert numpy array to a pandas dataframe
    return df

# Function for impute IQR outliers with the mean values
def impute_outliers_IQR(df):
    column_headers = df.columns.values.tolist()
    index_list = list(df.index.values)
    q1 = df.quantile(q1_val)
    q3 = df.quantile(q3_val)
    IQR = q3-q1
    upper = df[~(df > (q3+1.5*IQR))].max()
    lower = df[~(df < (q1-1.5*IQR))].min()
    df = np.where(df > upper,
       df.mean(),
       np.where(
           df < lower,
           df.mean(),
           df
           )
       )
    df = pd.DataFrame(df, columns=column_headers, index=index_list) # Convert numpy array to a pandas dataframe
    return df

# Function to find or drop outliers using empirical rules - ER
def find_drop_outliers_ER(df, drop=True):
    # drop: True for only drop values, False for only find values.
    lower_cap = df.mean() - cap_multiplier * df.std()
    upper_cap = df.mean() + cap_multiplier * df.std()
    if drop:
        outliers = df[~((df < lower_cap) | (df > upper_cap))]
    else:
        outliers = df[((df < lower_cap) | (df > upper_cap))]
    return outliers

# Function for Cap ER or Z-score outliers with specified limits (mean() +- k * std())
def cap_outliers_ER_zscore(df, kz=3):
    #kz: K-sigma or Z-score value.
    column_headers = df.columns.values.tolist()
    index_list = list(df.index.values)
    lower_cap = df.mean() - kz * df.std()
    upper_cap = df.mean() + kz * df.std()
    df = np.where(df > upper_cap,
       upper_cap,
       np.where(
           df < lower_cap,
           lower_cap,
           df
           )
       )
    df = pd.DataFrame(df, columns=column_headers, index=index_list) # Convert numpy array to a pandas dataframe
    return df

# Function for impute ER or Z-score outliers with mean values
def impute_outliers_ER_zscore(df, kz=3):
    column_headers = df.columns.values.tolist()
    index_list = list(df.index.values)
    lower_cap = df.mean() - kz * df.std()
    upper_cap = df.mean() + kz * df.std()
    df = np.where(df > upper_cap,
       df.mean(),
       np.where(
           df < lower_cap,
           df.mean(),
           df
           )
       )
    df = pd.DataFrame(df, columns=column_headers, index=index_list) # Convert numpy array to a pandas dataframe
    return df

# Function to find or drop outliers using the Z-score or standard score
def find_drop_outliers_zscore(df, drop=True):
    # drop: True for only drop values, False for only find values.
    z = (df - df.mean()) / df.std()
    if drop:
        outliers = df[~(abs(z) >= zscore_threshold)]
    else:
        outliers = df[(abs(z) >= zscore_threshold)]
    return outliers


# General variables
pivot_table_name = 'Pivot_Q_MEDIA_M.csv'  # <<<<< Pivot table name to process
path_input = 'D:/R.LTWB/.datasets/IDEAM_EDA/'  # Current location from pivot tables
station_file = path_input + pivot_table_name  # Current pivot IDEAM records file for a specified parameter
path = 'D:/R.LTWB/.datasets/IDEAM_Outlier/'  # Your local output path, use ../.datasets/IDEAM_Outlier/ for relative path
file_log_name = path + 'Outlier_IQR_' + pivot_table_name + '.md'  # Markdown file log
file_log = open(file_log_name, 'w+')   # w+ create the file if it doesn't exist
date_record_name = 'Fecha'  # IDEAM date field name for the record values
plot_colormap = 'autumn'  # Color theme for plot graphics, https://matplotlib.org/stable/tutorials/colors/colormaps.html
sample_records = 3  # Records to show in the sample table head and tail
fig_size = 5  # Height size for figures plot
print_table_sample = True
show_plot = True
station_exclude = ['28017140', '25027020', '25027410', '25027490', '25027330', '25027390', '25027630', '25027360', '25027320', '16067010', '25027420']  # Use ['station1', 'station2', '...',]
q1_val = 0.1  # Default is 0.25. Method 1.
q3_val = 0.9  # Default is 0.75. Method 1.
cap_multiplier = 3.85  # Replacement cap outlier value multiplier or k value, default is 3. e.j, mean() +- cap_multiplier * std(). k over empirical rules. . Method 1 & 2.
zscore_threshold = 3.85  # Z-score threshold, default is 3. Method 3. If the threshold is equal to the cap_multiplier, the results are the same as Method 2.


# Header
print_log('## Outliers detection and processing through statistical methods')
print_log('\n* Processed file: [%s](%s)' % (str(station_file), '../IDEAM_EDA/' + pivot_table_name) +
          '\n* Execution date: ' + str(datetime.now()) +
          '\n* Python version: ' + str(sys.version) +
          '\n* Python path: ' + str(sys.path[0:5]) +
          '\n* matplotlib version: ' + str(matplotlib.__version__) +
          '\n* pandas version: ' + str(pd.__version__) +
          '\n* numpy version: ' + str(np.__version__) +
          '\n* Stations exclude: ' + str(station_exclude) +
          '\n* Print table sample: ' + str(print_table_sample) +
          '\n* Instructions & script: https://github.com/rcfdtools/R.LTWB/tree/main/Section03/Outlier'
          '\n* License: https://github.com/rcfdtools/R.LTWB/blob/main/LICENSE.md'
          '\n* Credits: r.cfdtools@gmail.com')


# Open the IDEAM station pivot dataframe and show general information
df = pd.read_csv(station_file, low_memory=False, parse_dates=[date_record_name], index_col=date_record_name)
df = df.loc[:, ~df.columns.isin(station_exclude)]
ideam_regs = df.shape[0]
print_log('\n\n### General dataframe information with %d IDEAM records for %d stations' % (ideam_regs, df.shape[1]))
print(df.info())
if print_table_sample:
    print_log('\nDataframe records head sample\n')
    print_log(df.head(sample_records).to_markdown())
    print_log('\nDataframe records tail sample\n')
    print_log(df.tail(sample_records).to_markdown())
print_log('\nDatatypes for station and nulls values in the initial file', center_div=False)
df_dtypes = pd.DataFrame(df.dtypes, columns=['Dtype'])
df_isnull = pd.DataFrame(df.isnull().sum(), columns=['Nulls'])
df_concat = pd.concat([df_dtypes, df_isnull], axis='columns').T # .T for transpose
print_log(df_concat.to_markdown(), center_div=True)
print_log('General statistics table - Initial file', center_div=True)
print_log(df.describe().T.to_markdown(), center_div=True) # .T for transpose


# Method 1 - Outliers processing through interquartile range IQR
print_log('### Method 1 - Outliers processing using the interquartile range IQR (q1 = %s, q3 = %s)' % (str(q1_val), str(q3_val)))
print_log('\nSince the data doesn`t follow a normal distribution, we will calculate the outlier data points using the statistical method called interquartile range (IQR) instead of using Z-score. Using the IQR, the outlier data points are the ones falling below Q1 - 1.5 IQR or above Q3 + 1.5 IQR. The Q1 could be the 25th percentile and Q3 could be the 75th percentile of the dataset, and IQR represents the interquartile range calculated by Q3 minus Q1 (Q3-Q1). [^1]')
outliers = find_drop_outliers_IQR(df, drop=False)
outlier_file = 'Outlier_IQR_' + pivot_table_name
outliers.to_csv(path + outlier_file)
print_log('\nOutliers parameters:'
          '\n* mean: mean value'
          '\n* std: standard deviation value'              
          '\n* q1: quartile %s' % str(q1_val) +
          '\n* q3: quartile %s' % str(q3_val) +
          '\n* IQR: interquartile range (q3-q1)' +
          '\n* OlLowerLim: outlier bottom limit (q1-1.5*IQR)'
          '\n* OlUpperLim: outlier top limit (q3+1.5*IQR)'
          '\n* OlMinVal: minimum outlier value founded'
          '\n* OlMaxVal: maximum outlier value founded'
          '\n* OlCount: # outliers founded'
          '\n* CapLowerLim: capped lower limit for outliers replacement ( $\mu$ - %s * $\sigma$ )' % str(cap_multiplier) +
          '\n* CapUpperLim: capped upper limit for outliers replacement ( $\mu$ + %s * $\sigma$ )\n' % str(cap_multiplier)
          )
# Assemble the parameters table
df_mean = df.mean().to_frame()
df_mean.columns = ['mean']
df_std = df.std().to_frame()
df_std.columns = ['std']
df_q1 = df.quantile(q1_val).to_frame()
df_q1.columns = ['q1']
df_q3 = df.quantile(q3_val).to_frame()
df_q3.columns = ['q3']
df_IQR = (df_q3['q3'] - df_q1['q1']).to_frame()
df_IQR.columns = ['IQR']
df_lower_lim = (df_q1['q1'] + 1.5 * df_IQR['IQR']).to_frame()
df_lower_lim.columns = ['OlLowerLim']
df_upper_lim = (df_q3['q3'] + 1.5 * df_IQR['IQR']).to_frame()
df_upper_lim.columns = ['OlUpperLim']
df_min = pd.DataFrame(outliers.min(), columns=['OlMinVal'])
df_max = pd.DataFrame(outliers.max(), columns=['OlMaxVal'])
df_count = pd.DataFrame(outliers.count(), columns=['OlCount'])
df_lower_cap = pd.DataFrame(df.mean()-cap_multiplier*df.std(), columns=['CapLowerLim'])
df_upper_cap = pd.DataFrame(df.mean()+cap_multiplier*df.std(), columns=['CapUpperLim'])
df_concat = pd.concat([df_mean, df_std, df_q1, df_q3, df_IQR, df_lower_lim, df_upper_lim, df_min, df_max, df_count, df_lower_cap, df_upper_cap], axis='columns')
print_log(df_concat.to_markdown(), center_div=True)
# Plot values and outliers
df_outlier = pd.read_csv(path + outlier_file, low_memory=False, parse_dates=[date_record_name], index_col=date_record_name)
ax = df.plot(colormap=plot_colormap, legend=False, alpha=0.1, figsize=(12, 6))  # colormap can be replaced by color='lightblue'
df_outlier.plot(ax=ax, color='black', legend=False, figsize=(fig_size*2, fig_size+1))
plt.title('Method 1 - IQR outliers (q1 = %s, q3 = %s) for %d stations (%d outliers)' % (str(q1_val), str(q3_val), df.shape[1], df_concat['OlCount'].sum()))
ax.set_ylabel('Values for %s (%d recs.)' % (pivot_table_name, ideam_regs))
plt.savefig(path + outlier_file + '.png')
print_log('\n![R.LTWB](%s)' % (outlier_file + '.png'), center_div=False)
if show_plot: plt.show()
plt.close('all')
# Drop outliers values
not_outliers = find_drop_outliers_IQR(df, drop=True)
outlier_file_drop = 'Outlier_IQR_Drop_' + pivot_table_name
not_outliers.to_csv(path + outlier_file_drop)
# Capped outliers values
df_capped = cap_outliers_IQR(df)
outlier_file_cap = 'Outlier_IQR_Cap_' + pivot_table_name
df_capped.to_csv(path + outlier_file_cap, index_label=date_record_name)
# Impute outliers with mean values
df_impute = impute_outliers_IQR(df)
outlier_file_impute = 'Outlier_IQR_Impute_' + pivot_table_name
df_impute.to_csv(path + outlier_file_impute, index_label=date_record_name)
# Print results
print_log('\n#### Identified and cleaning tables for %d IQR outliers founded' % df_concat['OlCount'].sum() +
          '\n* Outliers identified file: [%s](../../.datasets/IDEAM_Outlier/%s)' % (outlier_file, outlier_file) +
          '\n* Outliers dropped file: [%s](../../.datasets/IDEAM_Outlier/%s)' % (outlier_file_drop, outlier_file_drop) +
          '\n* Outliers capped file: [%s](../../.datasets/IDEAM_Outlier/%s)' % (outlier_file_cap, outlier_file_cap) +
          '\n* Outliers imputed file: [%s](../../.datasets/IDEAM_Outlier/%s)' % (outlier_file_impute, outlier_file_impute))
print_log('\n\n#### Statistical values for the capped and imputed file', center_div=False)
print_log('IQR - General statistics table - Capped file', center_div=True)
print_log(df_capped.describe().T.to_markdown(), center_div=True) # .T for transpose
print_log('IQR - General statistics table - Imputed file', center_div=True)
print_log(df_impute.describe().T.to_markdown(), center_div=True) # .T for transpose


# Method 2 - Outliers processing through empirical rule - ER or k-sigma (mean() - cap_multiplier * std())
print_log('\n\n### Method 2 - Outliers processing through empirical rule - ER or _k-sigma_ ( $\mu$ - _k_ * $\sigma$ ) with _k_ = %s' % str(cap_multiplier))
print_log('\n\nThe empirical rule, also referred to as the three-sigma rule or 68-95-99.7 rule, is a statistical rule which states that for a normal distribution, almost all observed data will fall within three standard deviations (denoted by $\sigma$) of the mean or average (denoted by $\mu$). In particular, the empirical rule predicts that 68% of observations falls within the first standard deviation ( $\mu$ ± $\sigma$ ), 95% within the first two standard deviations ( $\mu$ ± 2 $\sigma$ ), and 99.7% within the first three standard deviations ( $\mu$ ± 3 $\sigma$ ).[^2]')
outliers = find_drop_outliers_ER(df, drop=False)
outlier_file = 'Outlier_ER_' + pivot_table_name
outliers.to_csv(path + outlier_file)
print_log('\nOutliers parameters:'
          '\n* mean: mean value'
          '\n* std: standard deviation value'          
          '\n* OlMinVal: minimum outlier value founded'
          '\n* OlMaxVal: maximum outlier value founded'
          '\n* OlCount: # outliers founded'
          '\n* CapLowerLim: capped lower limit for outliers replacement ( $\mu$ - %s * $\sigma$ )' % str(cap_multiplier) +
          '\n* CapUpperLim: capped upper limit for outliers replacement ( $\mu$ + %s * $\sigma$ )\n' % str(cap_multiplier)
          )
# Assemble the parameters table
df_mean = df.mean().to_frame()
df_mean.columns = ['mean']
df_std = df.std().to_frame()
df_std.columns = ['std']
df_min = pd.DataFrame(outliers.min(), columns=['OlMinVal'])
df_max = pd.DataFrame(outliers.max(), columns=['OlMaxVal'])
df_count = pd.DataFrame(outliers.count(), columns=['OlCount'])
df_concat = pd.concat([df_mean, df_std, df_min, df_max, df_count, df_lower_cap, df_upper_cap], axis='columns')
print_log(df_concat.to_markdown(), center_div=True)
# Plot values and outliers
df_outlier = pd.read_csv(path + outlier_file, low_memory=False, parse_dates=[date_record_name], index_col=date_record_name)
ax = df.plot(colormap=plot_colormap, legend=False, alpha=0.1, figsize=(12, 6))  # colormap can be replaced by color='lightblue'
df_outlier.plot(ax=ax, color='black', legend=False, figsize=(fig_size*2, fig_size+1))
plt.title('Method 2 - ER or k-sigma outliers (k = %s) for %d stations (%d outliers)' % (str(cap_multiplier), df.shape[1], df_concat['OlCount'].sum()))
ax.set_ylabel('Values for %s (%d recs.)' % (pivot_table_name, ideam_regs))
plt.savefig(path + outlier_file + '.png')
print_log('\n![R.LTWB](%s)' % (outlier_file + '.png'), center_div=False)
if show_plot: plt.show()
plt.close('all')
# Drop outliers values
not_outliers = find_drop_outliers_ER(df, drop=True)
outlier_file_drop = 'Outlier_ER_Drop_' + pivot_table_name
not_outliers.to_csv(path + outlier_file_drop)
# Capped outliers values
df_capped = cap_outliers_ER_zscore(df, kz=cap_multiplier)
outlier_file_cap = 'Outlier_ER_Cap_' + pivot_table_name
df_capped.to_csv(path + outlier_file_cap, index_label=date_record_name)
# Impute outliers with mean values
df_impute = impute_outliers_ER_zscore(df, kz=cap_multiplier)
outlier_file_impute = 'Outlier_ER_Impute_' + pivot_table_name
df_impute.to_csv(path + outlier_file_impute, index_label=date_record_name)
# Print results
print_log('\n#### Identified and cleaning tables for %d ER or k-sigma outliers founded' % df_concat['OlCount'].sum() +
          '\n* Outliers identified file: [%s](../../.datasets/IDEAM_Outlier/%s)' % (outlier_file, outlier_file) +
          '\n* Outliers dropped file: [%s](../../.datasets/IDEAM_Outlier/%s)' % (outlier_file_drop, outlier_file_drop) +
          '\n* Outliers capped file: [%s](../../.datasets/IDEAM_Outlier/%s)' % (outlier_file_cap, outlier_file_cap) +
          '\n* Outliers imputed file: [%s](../../.datasets/IDEAM_Outlier/%s)' % (outlier_file_impute, outlier_file_impute))
print_log('\n\n#### Statistical values for the capped and imputed file', center_div=False)
print_log('ER - General statistics table - Capped file', center_div=True)
print_log(df_capped.describe().T.to_markdown(), center_div=True) # .T for transpose
print_log('ER - General statistics table - Imputed file', center_div=True)
print_log(df_impute.describe().T.to_markdown(), center_div=True) # .T for transpose


# Method 3 - Outliers processing through Z-score or standard core
print_log('\n\n### Method 3 - Outliers processing through Z-score >= %s or standard core' % str(zscore_threshold))
print_log('\n\nZ score is an important concept in statistics. Z score is also called standard score. This score helps to understand if each data value is greater or smaller than mean and how far away it is from the mean. More specifically, Z score tells how many standard deviations away a data point is from the mean. Z = ( x - $\mu$ ) / $\sigma$.[^3]')
print_log('\n\n> Altought with this method, the identified outliers are the same obtained in Method 2 that uses the empirical rule when the Z-score threshold is the same _k-sigma_ value, the Method 3 creates the Z-score table values. Use this method to compare the identified outliers with differents _k-sigma_ values.')
outliers = find_drop_outliers_zscore(df, drop=False)
outlier_file = 'Outlier_ZScore_' + pivot_table_name
outliers.to_csv(path + outlier_file)
zscore = (df - df.mean()) / df.std()
zscore_file = 'Outlier_ZScore_Value_' + pivot_table_name
zscore.to_csv(path + zscore_file)
print_log('\nOutliers parameters:'
          '\n* mean: mean value'
          '\n* std: standard deviation value'
          '\n* OlMinVal: minimum outlier value founded'
          '\n* OlMaxVal: maximum outlier value founded'
          '\n* OlCount: # outliers founded'
          '\n* CapLowerLim: capped lower limit for outliers replacement ( $\mu$ - %s * $\sigma$ )' % str(cap_multiplier) +
          '\n* CapUpperLim: capped upper limit for outliers replacement ( $\mu$ + %s * $\sigma$ )\n' % str(cap_multiplier)
          )
# Assemble the parameters table
df_mean = df.mean().to_frame()
df_mean.columns = ['mean']
df_std = df.std().to_frame()
df_std.columns = ['std']
df_min = pd.DataFrame(outliers.min(), columns=['OlMinVal'])
df_max = pd.DataFrame(outliers.max(), columns=['OlMaxVal'])
df_count = pd.DataFrame(outliers.count(), columns=['OlCount'])
df_concat = pd.concat([df_mean, df_std, df_min, df_max, df_count, df_lower_cap, df_upper_cap], axis='columns')
print_log(df_concat.to_markdown(), center_div=True)
# Plot values and outliers
df_outlier = pd.read_csv(path + outlier_file, low_memory=False, parse_dates=[date_record_name], index_col=date_record_name)
ax = df.plot(colormap=plot_colormap, legend=False, alpha=0.1, figsize=(12, 6))  # colormap can be replaced by color='lightblue'
df_outlier.plot(ax=ax, color='black', legend=False, figsize=(fig_size*2, fig_size+1))
plt.title('Method 3 - Z-score or standard core >= %s for %d stations (%d outliers)' % (str(zscore_threshold), df.shape[1], df_concat['OlCount'].sum()))
ax.set_ylabel('Values for %s (%d recs.)' % (pivot_table_name, ideam_regs))
plt.savefig(path + outlier_file + '.png')
print_log('\n![R.LTWB](%s)' % (outlier_file + '.png'), center_div=False)
if show_plot: plt.show()
plt.close('all')
# Drop outliers values
not_outliers = find_drop_outliers_zscore(df, drop=True)
outlier_file_drop = 'Outlier_ZScore_Drop_' + pivot_table_name
not_outliers.to_csv(path + outlier_file_drop)
# Capped outliers values
df_capped = cap_outliers_ER_zscore(df, kz=zscore_threshold)
outlier_file_cap = 'Outlier_ZScore_Cap_' + pivot_table_name
df_capped.to_csv(path + outlier_file_cap, index_label=date_record_name)
# Impute outliers with mean values
df_impute = impute_outliers_ER_zscore(df, kz=zscore_threshold)
outlier_file_impute = 'Outlier_ZScore_Impute_' + pivot_table_name
df_impute.to_csv(path + outlier_file_impute, index_label=date_record_name)
# Print results
print_log('\n#### Identified and cleaning tables for %d Z-score or standard core outliers founded' % df_concat['OlCount'].sum() +
          '\n* Outliers Z-score values file: [%s](../../.datasets/IDEAM_Outlier/%s)' % (zscore_file, zscore_file) +
          '\n* Outliers identified file: [%s](../../.datasets/IDEAM_Outlier/%s)' % (outlier_file, outlier_file) +
          '\n* Outliers dropped file: [%s](../../.datasets/IDEAM_Outlier/%s)' % (outlier_file_drop, outlier_file_drop) +
          '\n* Outliers capped file: [%s](../../.datasets/IDEAM_Outlier/%s)' % (outlier_file_cap, outlier_file_cap) +
          '\n* Outliers imputed file: [%s](../../.datasets/IDEAM_Outlier/%s)' % (outlier_file_impute, outlier_file_impute))
print_log('\n\n#### Statistical values for the capped and imputed file', center_div=False)
print_log('Z-score - General statistics table - Capped file', center_div=True)
print_log(df_capped.describe().T.to_markdown(), center_div=True) # .T for transpose
print_log('Z-score - General statistics table - Imputed file', center_div=True)
print_log(df_impute.describe().T.to_markdown(), center_div=True) # .T for transpose
print_log('\n\n> The _drop files_ contains the database values without the outliers identified.'
          '\n>'
          '\n> The _capped files_ contains the database values and the outliers has been replaced with the lower or upper capped value calculated. Lower outliers could be replaced with negative values because the limit is defined with (mean() - cap_multiplier * std()). In some cases like _temperature analysis_, the upper outliers values could be replaced with values over the original values and you can try to fix this issue changing the parameter _cap_multiplier_ that defines the stripe values range.'
          '\n>'
          '\n> The imputation method replace each outlier value with the mean value that contains the original outliers values.'
          )
print_log('\n\n[^1]: Adapted from: https://careerfoundry.com/en/blog/data-analytics/how-to-find-outliers/' +
          '\n[^2]: https://www.investopedia.com/terms/e/empirical-rule.asp'+
          '\n[^3]: Adapted from: https://www.geeksforgeeks.org/z-score-for-outlier-detection-python/')
```

2. Cree una nueva carpeta en blanco con el nombre `IDEAM_Outlier` en su directorio de proyecto local `D:\R.LTWB\.datasets` y dentro de ella la carpeta `Graph`. Verifique que la carpeta `D:\R.LTWB\.datasets\IDEAM_EDA`, contenga los archivos de las tablas dinámicas de cada parámetro hicroclimatológico [IDEAM_EDA](../../.datasets/IDEAM_EDA) que fueron obtenidas en la actividad denominada [EDA](../EDA).

> Para la identificación de valores atípicos no son requeridas las tablas de datos de correlaciones identificadas con nombre terminado en _correlation.csv.

3. Desde el editor de texto [Notepad++](https://notepad-plus-plus.org/), abra el archivo [D:\R.LTWB\.src\Outlier.py](../../.src/Outlier.py), y defina las siguientes variables:

* `pivot_table_name = 'Pivot_PTPM_TT_M.csv'`: corresponde a la tabla dinámica (pivot table) a procesar, p.ej., Pivot_PTPM_TT_M.csv corresponde a datos de precipitación mensual total, Pivot_EV_TT_D.csv corresponde a datos de evaporación diaria total, Pivot_Q_MEDIA_M.csv corresponde a datos de caudal medio mensual, Pivot_TMN_CON.csv corresponde a datos de temperatura mínima diaria y Pivot_TMX_CON.csv corresponde a datos de temperatura máxima diaria.
* `q1_val = 0.1`: cuartil inferior, el valor por defecto es 0.25 en el Método 1 de rango intercuartílico. Para este ejemplo utilizaremos 0.1 para excluir precipitaciones totales altas atípicas.
* `q3_val = 0.9`: cuartil inferior, el valor por defecto es 0.75 en el Método 1 de rango intercuartílico. Para este ejemplo utilizaremos 0.9 para excluir precipitaciones totales bajas atípicas.
* `cap_multiplier = 4.5`: multiplicado K-sigma, el valor por defecto es 3. En el método 1 este valor es usado para definir el límite de reemplazo de valores y en el método 2 para identificación de valores atípicos.
* `zscore_threshold = 4.5`: límite de exclusión en Z-score del método 3, el valor por defecto es 3.  

> Para los datos ejemplo de precipitación mensual total, la identificación de valores atípicos en el rango intercuartílico 0.1 a 0.9 es similar a la obtenida en los métodos 2 y 3 definiendo K-sigma y el Z-score en 4.5.
> 
> Los métodos 2 y 3 permiten identificar los mismos valores atípicos cuando el valor de K-sigma y Z-score es idéntico. Utilice estos métodos para comparar gráficamente exclusión de valores atípicos con diferentes posiciones en la distribución normal.

![R.LTWB](Screenshot/NotepadPlusOutlierpy.png)

4. En Microsoft Windows, ejecute el _Command Prompt_ o _CMD_, ingrese `D:` y de <kbd>Enter</kbd> para cambiar a la unidad D:\ donde se encuentra el repositorio R.LTWB. Utilizando el comando  `CD D:\R.LTWB\.datasets\IDEAM_Outlier` ubíquese dentro de la carpeta IDEAM_Outlier.

![R.LTWB](Screenshot/Windows11CMDCD.png)

5. En él `CMD`, ejecute la instrucción `C:\Python3.10.5\python.exe "D:\R.LTWB\.src\Outlier.py"` que realizará el procesamiento y análisis de los datos. Durante la ejecución, podrá observar que en la consola se presenta el detalle de los procesos ejecutados para cada método, además de la previsualización de diferentes tablas en formato Markdown y gráficas.

![R.LTWB](Screenshot/Windows11CMDOutlier1.png)
![R.LTWB](Screenshot/Windows11CMDOutlier2.png)
![R.LTWB](Screenshot/Windows11CMDOutlier3.png)
![R.LTWB](Screenshot/Windows11CMDOutlier4.png)
![R.LTWB](Screenshot/Windows11CMDOutlier5.png)
![R.LTWB](Screenshot/Windows11CMDOutlier6.png)
![R.LTWB](Screenshot/Windows11CMDOutlier7.png)
![R.LTWB](Screenshot/Windows11CMDOutlier8.png)

Luego de la ejecución, podrá observar que en la carpeta local `D:\R.LTWB\.datasets\IDEAM_Outlier` se han generado diferentes archivos de resultados por cada método para la tabla de datos de precipitación mensual total Pivot_PTPM_TT_M.csv.

![R.LTWB](Screenshot/Windows11CMDOutlier9.png)

Una vez finalizado el proceso de ejecución, podrá sincronizar en la nube los resultados en su repositorio de proyectos de GitHub y podrá observar el reporte detallado en formato Markdown [Outlier_IQR_Pivot_PTPM_TT_M.csv.md](../../.datasets/IDEAM_Outlier/Outlier_IQR_Pivot_PTPM_TT_M.csv.md).

![R.LTWB](Screenshot/Windows11CMDOutlier10.png)
![R.LTWB](Screenshot/Windows11CMDOutlier11.png)
![R.LTWB](Screenshot/Windows11CMDOutlier12.png)
![R.LTWB](Screenshot/Windows11CMDOutlier13.png)
![R.LTWB](Screenshot/Windows11CMDOutlier14.png)
![R.LTWB](Screenshot/Windows11CMDOutlier15.png)
![R.LTWB](Screenshot/Windows11CMDOutlier16.png)
![R.LTWB](Screenshot/Windows11CMDOutlier17.png)
![R.LTWB](Screenshot/Windows11CMDOutlier18.png)
![R.LTWB](Screenshot/Windows11CMDOutlier19.png)

6. Repita el procedimiento anterior para los datos de evaporación, caudal, temperatura mínima y máxima.


### Tablas de resultados y análisis generales

Durante el proceso de ejecución del script, se generan automáticamente para cada parámetro hidroclimatológico, un reporte integrado de resultados en formato Markdown (.md), gráficas de análisis y diferentes tablas en formato .csv.

| Reporte                                                                                                | Descripción                                                                 | Estaciones | Registros | 1.IQR | 1.ER | 3.Z-Score | 
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|:----------:|:---------:|:-----:|:----:|:---------:|
| [Outlier_IQR_Pivot_PTPM_TT_M.csv.md](../../.datasets/IDEAM_Outlier/Outlier_IQR_Pivot_PTPM_TT_M.csv.md) | Precipitación mensual total, mm. q1=0.1, q3=0.9, k-sigma=4.5, Z-score=4.5   |    130     |    504    |  94   |  92  |    92     |
| [Outlier_IQR_Pivot_EV_TT_D.csv.md](../../.datasets/IDEAM_Outlier/Outlier_IQR_Pivot_EV_TT_D.csv.md)     | Evaporación diaria total, mm. q1=0.25, q3=0.75, k-sigma=0.45, Z-score=0.45  |     1      |   4821    |  781  | 706  |    706    |
| [Outlier_IQR_Pivot_Q_MEDIA_M.csv.md](../../.datasets/IDEAM_Outlier/Outlier_IQR_Pivot_Q_MEDIA_M.csv.md) | Caudal medio mensual, m³/s. q1=0.1, q3=0.9, k-sigma=3.85, Z-score=3.85      |     46     |    504    |  126  | 123  |    123    |
| [Outlier_IQR_Pivot_TMN_CON.csv.md](../../.datasets/IDEAM_Outlier/Outlier_IQR_Pivot_TMN_CON.csv.md)     | Temperatura diaria mínima, °C. q1=0.175, q3=0.825, k-sigma=3.5, Z-score=3.5 |     25     |   15341   |  403  | 410  |    410    |
| [Outlier_IQR_Pivot_TMX_CON.csv.md](../../.datasets/IDEAM_Outlier/Outlier_IQR_Pivot_TMX_CON.csv.md)     | Temperatura diaria máxima, °C. q1=0.175, q3=0.825, k-sigma=3.6, Z-score=3.6 |     25     |   15341   |  225  | 216  |    216    |

> En la tabla, 1.IQR: número de valores atípicos identificados en Método 1 - Rango intercuartílico, 2.ER: número de valores atípicos identificados en Método 2 - Regla empírica y 3.Z-score: número de valores atípicos identificados en Método 3 - Z-score. La columna _registros_ corresponde al número de registros de cada estación, incluidos los valores faltantes y/o nulos.
>
> Nótese que para datos de temperatura mínima, se han identificado por los 3 métodos, valores atípicos en la zona inferior de las gráficas. En el caso de la temperatura máxima se han identificado valores atípicos en la zona superior e inferior de las gráficas.
> 
> Dentro de cada reporte independiente por parámetro, se encuentran los enlaces a los archivos .csv imputados por cada método.

Al revisar los estadísticos característicos, p. ej. de la estación 15015020, correspondiente a datos de precipitación total mensual, podrá observar los siguientes valores similares de media y desviación estándar:

<div align='center'>

| Método                                                              | $\mu$, media | $\sigma$, std |
|:--------------------------------------------------------------------|:-------------|:--------------|
| Serie original                                                      | 59.7829      | 74.2829       |
| 1. Rango intercuartílico - IQR. Reemplazo con $\mu$ +- K * $\sigma$ | 59.718       | 73.9846       |
| 1. Rango intercuartílico - IQR. Imputación con $\mu$                | 57.7459      | 69.3425       |
| 2. Regla empírica - ER. Reemplazo con $\mu$ +- K * $\sigma$         | 59.718       | 73.9846       |
| 2. Regla empírica - ER. Imputación con $\mu$                        | 57.7459      | 69.3425       |
| 3. Z-score o núcleo estándar. Reemplazo con $\mu$ +- K * $\sigma$   | 59.718       | 73.9846       |
| 3. Z-score o núcleo estándar. Imputación con $\mu$                  | 57.7459      | 69.3425       |

</div>

**Conclusión general**

De acuerdo a los valores atípicos identificados para cada variable hidroclimatológica y evaluando las gráficas compuestas donde se representan todas las series de las estaciones objeto de estudio, se puede evidenciar y concluir que no existen en los conjuntos de datos, valores que deban ser necesariamente excluidos, reemplazados o imputados por métodos estadísticos. Para el desarrollo de las actividades posteriores, podrá trabajar con los datos originales o con las tablas de datos con valores atípicos limpiados y/o ajustados, toda vez que se mantienen similares los estadísticos característicos.  

En este momento, dispone de reportes detallados de análisis por cada parámetro hidroclimatológico y diferentes tablas con el procesamiento de datos atípicos.


### Actividades complementarias:pencil2:

En la siguiente tabla se listan las actividades complementarias que deben ser desarrolladas y documentadas por el estudiante en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (mostrar nombre completo, código y enlace a su cuenta de GitHub), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.

| Actividad | Alcance                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|:---------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1     | A partir del script [Outlier.py](../../.src/Outlier.py), realice el análisis de valores atípicos de los parámetros climatológicos definidos como actividad complementaria en [descarga de datos hidroclimatológicos](../CNEStationDatasetDownload); correspondientes a brillo solar, radiación solar, humedad del aire cerca al suelo y parámetros relacionados con viento y nubosidad.                                                                                       |
|     2     | Para todas los parámetros climatológicos y a partir de las gráficas y tablas de análisis generadas mediante el script [Outlier.py](../../.src/Outlier.py), presente un análisis cuantitativo definiendo diferentes cuartiles q1 y q3, obtenga el valor K-sigma y Z-score que permita identificar un número similar de valores atípicos.                                                                                                                                       | 


### Referencias

* https://careerfoundry.com/en/blog/data-analytics/how-to-find-outliers/
* https://datasciencesphere.com/analytics/5-easy-ways-to-detect-outliers-in-python/
* https://realpython.com/pandas-merge-join-and-concat/
* https://www.geeksforgeeks.org/pandas-plot-multiple-time-series-dataframe-into-a-single-plot/
* https://www.tutorialspoint.com/plotting-multiple-dataframes-using-pandas-functionality
* https://sparkbyexamples.com/pandas/pandas-get-column-names
* https://www.statology.org/pandas-index-to-list/
* https://www.statology.org/pandas-exclude-column/
* https://www.investopedia.com/terms/e/empirical-rule.asp
* https://latex-tutorial.com/symbols/greek-alphabet/


### Control de versiones

| Versión    | Descripción                                                                                                                                                                                                                                                                                                    | Autor                                      | Horas |
|------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|:-----:|
| 2022.11.07 | Documentación general. Ejecución para precipitación, evaporación, caudal, temperatura mínima y temperatura máxima. Ajuste de valores de exclusión en método 3 a partir del valor absoluto Z-score obtenido para cada dato. Ilustración cabecera y diagrama de procesos.                                        | [rcfdtools](https://github.com/rcfdtools)  |  7.5  |
| 2022.11.05 | Método 2: funciones para identificación, eliminación, reemplazo e imputación. Generador documento detallado análisis Markdown. Método 3: Z-Score. Idéntico al método 2 con la diferencia que se crea la tabla de puntajes. Al utilizar el k-sigma igual al Z-score threshold, se obtienen los mismos outliers. | [rcfdtools](https://github.com/rcfdtools)  |   5   |
| 2022.11.04 | Método 1: inclusión de reemplazo de outliers usando rango definido  (mean() +- cap_multiplier * std()).                                                                                                                                                                                                        | [rcfdtools](https://github.com/rcfdtools)  |   4   |
| 2022.11.03 | Método 1: inclusión de límites de reemplazo en tabla de parámetros IQR. Ajuste de datos descartando outliers identificados (drop). Método 2, borrador:  identificación de outliers y reemplaza con valores cap con  (mean() +- cap_multiplier * std())                                                         | [rcfdtools](https://github.com/rcfdtools)  |  4.5  |
| 2022.11.02 | Método 1: Rango intercuartílico definido por usuario. Tabla de marcación. Tabla de análisis. Gráfico de análisis.                                                                                                                                                                                              | [rcfdtools](https://github.com/rcfdtools)  |   8   |

_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Actividad anterior](../EDA) | [Inicio](../../Readme.md) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/24) | [Actividad siguiente](../Impute) |
|------------------------------|---------------------------|------------------------------------------------------------------------|----------------------------------|

[^1]: Adapted from: https://careerfoundry.com/en/blog/data-analytics/how-to-find-outliers/
[^2]: https://www.investopedia.com/terms/e/empirical-rule.asp
[^3]: Adapted from: https://www.geeksforgeeks.org/z-score-for-outlier-detection-python/
