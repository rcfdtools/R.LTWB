## Completado y extendido de series - Imputación
Keywords: `Outlier` `matplotlib` `pandas` `tabulate` `numpy` `missingo` `sklearn` `dtypes` `isnull` `describe` `Impute` 

<div align="center"><img alt="R.LTWB" src="Graph/Impute.png" width="95%"></div> 

Este procedimiento de completado se realiza a partir de la generación de datos sintéticos utilizando diferentes métodos estadísticos y su propósito general es la conformación de series homogéneas y continuas para las diferentes variables en estudio.

Para el desarrollo de esta actividad se utilizarán los siguientes métodos:

| Método                                                 | Descripción imputación valores nulos o vacíos                                                                          | Alcance                                                                                                      |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| 1. Media                                               | Con la media de cada estación.                                                                                         | Toda la serie es completada.                                                                                 |
| 2. Mediana                                             | Con la mediana de cada estación.                                                                                       | Toda la serie es completada.                                                                                 |
| 3. Última observación anterior - LOCF                  | Es cada segmento faltante, la serie es rellenada con el valor inmediatamente anterior y hacia abajo.                   | Se completa desde los faltantes hasta el final de la serie. Valores faltantes al inicio se mantienen vacíos. |
| 4. Última observación siguiente - NOCB                 | Es cada segmento faltante, la serie es rellenada con el valor inmediatamente siguiente y hacia arriba.                 | Se completa desde los faltantes hasta el inicio de la serie. Valores faltantes al final se mantienen vacíos. |
| 5. Interpolación lineal                                | Es cada segmento faltante, la serie es rellenada con los valores de interpolación lineal próximos.                     | Se completa desde los faltantes hasta el final de la serie. Valores faltantes al inicio se mantienen vacíos. |
| 6. Media móvil - EWM                                   | Es cada segmento faltante, la serie es rellenada con los valores de la media móvil N y hacia abajo.                    | Se completa desde los faltantes hasta el final de la serie. Valores faltantes al inicio se mantienen vacíos. |
| 7. Vecino natural - KNN                                | Completado con n vecinos naturales definidos, pesos uniformes y distancias euclidianas.                                | Toda la serie es completada.                                                                                 |
| 8. Multivariante con ecuación de encadenamiento - MICE | Completado con n vecinos naturales definidos, estrategia inicial a partir de valores medios y modelo lineal Bayesiano. | Toda la serie es completada.                                                                                 |


### Objetivos

* Para cada parámetros hidroclimatológico, imputar los valores faltantes en series de datos a partir de diferentes métodos estadísticos.
* Visualizar gráficamente los datos faltantes en las diferentes estaciones asociadas a cada parámetro hidroclimatológico.
* Obtener y comparar los estadísticos característicos de los datos iniciales y completados.
* Graficar las series de datos de estación para visualizar los datos iniciales y completados en cada método. 


### Requerimientos

* [Python 3+](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/docs/index.html) para Python
* [Tabulate](https://pypi.org/project/tabulate/) para Python, requerido para impresión de tablas en formato Markdown desde pandas.
* [numpy](https://numpy.org/) para python.
* [missingno](https://github.com/ResidentMario/missingno) para Python
* [scikit-learn](https://scikit-learn.org) para Python
* [Notepad++](https://notepad-plus-plus.org/), editor de texto y código.
* Tablas dinámicas (pivot tables) con series de datos discretos con outliers identificados y ajustados de estaciones terrestres  del IDEAM por parámetro hidroclimatológico. [:mortar_board:Aprender.](../Outlier)


### Procedimiento general

<div align="center">
<br><img alt="R.LTWB" src="Graph/Impute.svg" width="100%"><br>
<sub>Convenciones generales en diagramas: clases de entidad en azul, dataset en gris oscuro, grillas en color verde, geo-procesos en rojo, procesos automáticos o semiautomáticos en guiones rojos y procesos manuales en amarillo. Líneas conectoras con guiones corresponden a procedimientos opcionales.</sub><br><br>
</div>

1. Para realizar la identificación y procesamiento de datos atípicos, descargue el script [Impute.py](../../.src/Outlier.py) y guárdelo en la carpeta local `D:\R.LTWB\.src` de su equipo.

**Funcionalidades del script**

* Completado y extendido de series por 8 métodos estadísticos.
* Permite definir la tabla dinámica (pivot table original o con valores atípicos identificados, eliminados y/o ajustados) del parámetro hidroclimatológico a evaluar.
* El usuario puede excluir estaciones del análisis a través de la variable `station_exclude` o definir las estaciones a utilizar a través de las variables `station_include` y `only_included`.
* Análisis masivo de estaciones por parámetro hidroclimatológico con estadísticos, parámetros de evaluación y gráficas generales y detalladas por estación con representación de datos completados y/o extendidos.
* Generación de reportes detallados Markdown y reporte complementario gráfico por estación para cada parámetro hidroclimatológico evaluado. [IDEAM_Impute](../../.datasets/IDEAM_Impute).
* Para cada método y cada parámetro hidroclimatológico analizado, crea tablas en formato de texto separado por comas .csv.

> Para el ejemplo, se han excluido diferentes estaciones con registros de caudal sobre el Río Magdalena y otros ríos con caudales altos.

Contenido del script

```
# -*- coding: UTF-8 -*-
# Name: Impute.py
# Description: impute missing values in time series through statistical methods
# Requirements: Python 3+, pandas, tabulate, numpy, missingno, sklearn
# Attention: do not convert the .csv file into an Excel file because you would need process more than 1048576 records.


# Libraries
import sys
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import missingno as msno
import sklearn
from sklearn.impute import KNNImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn import linear_model
import tabulate  # required for print tables in Markdown using pandas
from datetime import datetime


# General variables
pivot_table_name = 'Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv'  # <<<<< Pivot table name to process
path_input = 'D:/R.LTWB/.datasets/IDEAM_Outlier/'  # Current location from pivot tables
station_file = path_input + pivot_table_name  # Current pivot IDEAM records file for a specified parameter
path = 'D:/R.LTWB/.datasets/IDEAM_Impute/'  # Your local output path, use ../.datasets/IDEAM_Impute/ for relative path
file_log_name = path + 'Impute_' + pivot_table_name + '.md'  # Markdown file log
file_log = open(file_log_name, 'w+')   # w+ create the file if it doesn't exist
station_file_log_name = path + 'Impute_Station_' + pivot_table_name + '.md'  # Markdown file log
date_record_name = 'Fecha'  # IDEAM date field name for the record values
plot_colormap = 'autumn'  # Color theme for plot graphics, https://matplotlib.org/stable/tutorials/colors/colormaps.html
sample_records = 3  # Records to show in the sample table head and tail
fig_size = 5  # Height size for figures plot
fig_alpha = 0.75  # Alpha transparency color in plots
print_table_sample = True
show_plot = False
plot_stations = True  # True: plot individual graphs for each station and update the complementary report
min_value = 0  # Minimum value for impute with Multivariate Imputation by Chained Equation - MICE from Scikit Learn. E.g.: 0 for rain, -inf for temperature.
n_neighbors = 5  # Number of natural neighbors for Natural Neigborns - KNN & Multivariate Imputation by Chained Equation - MICE
only_included = False  # True: let the user run this script only for the stations included in the station_include array. False: process all the stations but not the ones in the station_exclude array.
station_exclude = ['28017140', '25027020', '25027410', '25027490', '25027330', '25027390', '25027630', '25027360', '25027320', '16067010', '25027420']  # Use ['station1', 'station2', '...',]
station_include = ['15015020', '15060050', '15060070', '15060080', '15060150']  # Use ['station1', 'station2', '...',]


# Function for print and show results in a file
def print_log(txt_print, on_screen=True, center_div=False):
    if on_screen:
        print(txt_print)
    if center_div:
        file_log.write('\n<div align="center">\n' + '\n')
    file_log.write(txt_print + '\n')
    if center_div:
        file_log.write('\n</div>\n' + '\n')

# Function for plot original and imputed series
def plot_impute(df_org, df_imputed, method, file_name):
    ax1 = df_imputed.plot(color='black', legend=False, alpha=1, figsize=(fig_size*2, fig_size+1), linewidth=0.5)
    df_org.plot(ax=ax1, colormap=plot_colormap, alpha=fig_alpha, legend=False, figsize=(fig_size*2, fig_size+1), linewidth=0.85)
    plt.title('Impute with %s values for %d stations (%d missing & %d imputed)' % (method, df.shape[1], total_nulls, total_imputed))
    ax1.set_ylabel('Values in %s (%d recs.)' % (pivot_table_name, ideam_regs))
    plt.savefig(path + file_name + '.png')
    print_log('\n![R.LTWB](%s)' % (file_name + '.png'), center_div=False)
    if show_plot: plt.show()
    plt.close('all')
    # Missingno plot
    # msno.matrix(df_impute, fontsize=20, figsize=(fig_size * 4, fig_size * 2.5))
    msno.matrix(df_imputed, figsize=(fig_size * 3, fig_size * 2.5))
    plt.title('Missing values diagram for %d stations (%d missing values & %d imputed with %s)' % (df.shape[1], total_nulls, total_imputed, method))
    plt.savefig(path + 'Missingno_' + file_name + '.png')
    print_log('\n![R.LTWB](%s)' % ('Missingno_' + file_name + '.png'), center_div=False)
    if show_plot: plt.show()
    plt.close('all')
    # Plot individual graphs for station
    column_headers = df.columns.values.tolist()
    if plot_stations:
        for station in column_headers:
            ax2 = df_imputed[station].plot(color='black', legend=True, alpha=1, figsize=(fig_size, fig_size), linewidth=0.5)
            df_org[station].plot(ax=ax2, colormap=plot_colormap, alpha=1, legend=True, figsize=(fig_size, fig_size), linewidth=0.85)
            ax2.legend(['Imputed', 'Value']);
            plt.title('%s - Station %s' % (method, station))
            ax2.set_ylabel('Values in %s (%d recs.)' % (pivot_table_name, ideam_regs))
            plt.savefig(path + 'Graph/' + station + '_' + file_name + '.png')
            plt.close('all')


# Header
print_log('# Impute missing values in time series through statistical methods')
print_log('\n* Processed file: [%s](%s)' % (str(station_file), '../IDEAM_Outlier/' + pivot_table_name) +
          '\n* Execution date: ' + str(datetime.now()) +
          '\n* Python version: ' + str(sys.version) +
          '\n* Python path: ' + str(sys.path[0:5]) +
          '\n* matplotlib version: ' + str(matplotlib.__version__) +
          '\n* pandas version: ' + str(pd.__version__) +
          '\n* numpy version: ' + str(np.__version__) +
          '\n* missingno version: ' + str(msno.__version__) +
          '\n* sklearn version: ' + str(sklearn.__version__) +
          '\n* Stations exclude: ' + str(station_exclude) +
          '\n* Stations include: ' + str(station_include) +
          '\n* Print table sample: ' + str(print_table_sample) +
          '\n* Instructions & script: https://github.com/rcfdtools/R.LTWB/tree/main/Section03/Impute'
          '\n* License: https://github.com/rcfdtools/R.LTWB/blob/main/LICENSE.md'
          '\n* Credits: r.cfdtools@gmail.com')


# Open the IDEAM station pivot dataframe and show general information
df = pd.read_csv(station_file, low_memory=False, parse_dates=[date_record_name], index_col=date_record_name)
if only_included:
    df = df.loc[:, df.columns.isin(station_include)]
else:
    df = df.loc[:, ~df.columns.isin(station_exclude)]
ideam_regs = df.shape[0]
print_log('\n\n## General dataframe information with %d IDEAM records for %d stations' % (ideam_regs, df.shape[1]))
print(df.info())
if print_table_sample:
    print_log('\nDataframe records head sample\n')
    print_log(df.head(sample_records).to_markdown())
    print_log('\nDataframe records tail sample\n')
    print_log(df.tail(sample_records).to_markdown())
print_log('\nDatatypes for station and nulls values in the initial file', center_div=False)
df_dtypes = pd.DataFrame(df.dtypes, columns=['Dtype'])
df_isnull = pd.DataFrame(df.isnull().sum(), columns=['Nulls'])
df_concat = pd.concat([df_dtypes, df_isnull], axis='columns').T  # .T for transpose
print_log(df_concat.to_markdown(), center_div=False)
total_nulls = df_concat.T['Nulls'].sum()
#print_log('\nTotal nulls values founded in the dataset: %d\n' % total_nulls, center_div=False)
#nul_data = pd.DataFrame(df.isnull())
#print_log(nul_data.to_markdown())
ax = df.plot(colormap=plot_colormap, legend=False, alpha=fig_alpha, figsize=(fig_size*2, fig_size+1), linewidth=0.85)  # colormap can be replaced by color='lightblue'
plt.title('Original serie with %d stations (%d missing values)' % (df.shape[1], total_nulls))
ax.set_ylabel('Values in %s (%d recs.)' % (pivot_table_name, ideam_regs))
plt.savefig(path + pivot_table_name + '.png')
print_log('\n![R.LTWB](%s)' % (pivot_table_name + '.png'), center_div=False)
if show_plot: plt.show()
plt.close('all')
# Missingno plot
msno.matrix(df, fontsize=16, figsize=(fig_size*3, fig_size*2.5))
plt.title('Missing values diagram for %d stations (%d missing values)' % (df.shape[1], total_nulls))
ax.set_ylabel('Records')
plt.savefig(path + 'Missingno_' + pivot_table_name + '.png')
print_log('\n![R.LTWB](%s)' % ('Missingno_' + pivot_table_name + '.png'), center_div=False)
if show_plot: plt.show()
plt.close('all')
# General stats
print_log('General statistics table - Initial file', center_div=True)
print_log(df.describe().T.to_markdown(), center_div=True)  # .T for transpose


# Method 1 - Impute missing values with mean values
df_impute = df.fillna(df.mean())
df_isnull = pd.DataFrame(df_impute.isnull().sum(), columns=['Nulls'])
total_imputed = total_nulls - df_isnull['Nulls'].sum()
impute_file = 'Impute_Mean_' + pivot_table_name
df_impute.to_csv(path + impute_file)
print_log('\n\n## Method 1 - Imputing with mean values' +
          '\nAccording to this technique, the missing values are imputed using the mean value in each feature and the serie has been completed filled.' +
          '\n\nImputed file: [%s](%s)' % (impute_file, impute_file))
plot_impute(df, df_impute, 'MEAN', impute_file)
print_log('General statistics table - Imputed file', center_div=True)
print_log(df_impute.describe().T.to_markdown(), center_div=True)  # .T for transpose

# Method 2 - Impute missing values with median values
df_impute = df.fillna(df.median())
df_isnull = pd.DataFrame(df_impute.isnull().sum(), columns=['Nulls'])
total_imputed = total_nulls - df_isnull['Nulls'].sum()
imputed_file = 'Impute_Median_' + pivot_table_name
df_impute.to_csv(path + imputed_file)
print_log('\n\n## Method 2 - Imputing with median values' +
          '\nAccording to this technique, the missing values are imputed using the median value in each feature and the serie has been completed filled.' +
          '\n\nImputed file: [%s](%s)' % (imputed_file, imputed_file))
plot_impute(df, df_impute, 'MEDIAN', imputed_file)
print_log('General statistics table - Imputed file', center_div=True)
print_log(df_impute.describe().T.to_markdown(), center_div=True)  # .T for transpose

# Method 3 - Impute missing values with Last Observation Carried Forward (LOCF)
df_impute = df.fillna(method='ffill')
df_isnull = pd.DataFrame(df_impute.isnull().sum(), columns=['Nulls'])
total_imputed = total_nulls - df_isnull['Nulls'].sum()
imputed_file = 'Impute_LOCF_' + pivot_table_name
df_impute.to_csv(path + imputed_file)
print_log('\n\n## Method 3 - Imputing with Last Observation Carried Forward (LOCF) values' +
          '\nAccording to this technique, the missing values are imputed using the immediate values before it in the time series and the missing values at the start are not filled but the series are completed fillet to the end.' +
          '\n\nImputed file: [%s](%s)' % (imputed_file, imputed_file))
plot_impute(df, df_impute, 'LOCF', imputed_file)
print_log('General statistics table - Imputed file', center_div=True)
print_log(df_impute.describe().T.to_markdown(), center_div=True)  # .T for transpose

# Method 4 - Impute missing values with Next Observation Carried Backward (NOCB)
df_impute = df.fillna(method='bfill')
df_isnull = pd.DataFrame(df_impute.isnull().sum(), columns=['Nulls'])
total_imputed = total_nulls - df_isnull['Nulls'].sum()
imputed_file = 'Impute_NOCB_' + pivot_table_name
df_impute.to_csv(path + imputed_file)
print_log('\n\n## Method 4 - Imputing with Next Observation Carried Backward (NOCB) values' +
          '\nAccording to this technique, the missing values are imputed using the immediate values after it in the time series and the missing values at the end are not filled but the series are completed fillet to the start.' +
          '\n\nImputed file: [%s](%s)' % (imputed_file, imputed_file))
plot_impute(df, df_impute, 'NOCB', imputed_file)
print_log('General statistics table - Imputed file', center_div=True)
print_log(df_impute.describe().T.to_markdown(), center_div=True)  # .T for transpose

# Method 5 - Impute missing values with Linear Interpolation
df_impute = df.interpolate(method='linear')  # limit=1, limit_direction="forward"
df_isnull = pd.DataFrame(df_impute.isnull().sum(), columns=['Nulls'])
total_imputed = total_nulls - df_isnull['Nulls'].sum()
imputed_file = 'Impute_InterpolateLinear_' + pivot_table_name
df_impute.to_csv(path + imputed_file)
print_log('\n\n## Method 5 - Impute missing values with Linear Interpolation values' +
          '\nAccording to this technique, the missing values are imputed using the linear interpolation between knowing pair values in the time series and the missing values at the start are not filled but the series are completed fillet to the end.' +
          '\n\nImputed file: [%s](%s)' % (imputed_file, imputed_file))
plot_impute(df, df_impute, 'Linear Interpolation', imputed_file)
print_log('General statistics table - Imputed file', center_div=True)
print_log(df_impute.describe().T.to_markdown(), center_div=True)  # .T for transpose

# Method 6 - Impute missing values with Exponential (Weighted) Moving Average - EWM
halflife = 3
df_impute = df.fillna(df.ewm(halflife=halflife).mean())
df_isnull = pd.DataFrame(df_impute.isnull().sum(), columns=['Nulls'])
total_imputed = total_nulls - df_isnull['Nulls'].sum()
imputed_file = 'Impute_MeanEWM_' + pivot_table_name
df_impute.to_csv(path + imputed_file)
print_log('\n\n## Method 6 - Impute missing values with Exponential (Weighted) Moving Average - EWM = %d' % halflife +
          '\nAccording to this technique, the missing values are imputed using the moving average values in the time series and the missing values at the start are not filled but the series are completed fillet to the end.' +
          '\n\nImputed file: [%s](%s)' % (imputed_file, imputed_file))
plot_impute(df, df_impute, 'Exponential Weighted Moving - EWM', imputed_file)
print_log('General statistics table - Imputed file', center_div=True)
print_log(df_impute.describe().T.to_markdown(), center_div=True)  # .T for transpose

# Method 7 - Impute missing values with Natural Neigborns - KNN Imputer from Scikit Learn
#imputer = KNNImputer(n_neighbors=n_neighbors)
imputer = KNNImputer(n_neighbors=n_neighbors, weights='uniform', metric='nan_euclidean')
column_headers = df.columns.values.tolist()
index_list = list(df.index.values)
df_impute = imputer.fit_transform(df)
df_impute = pd.DataFrame(df_impute, columns=column_headers, index=index_list) # Convert numpy array to a pandas dataframe
df_isnull = pd.DataFrame(df_impute.isnull().sum(), columns=['Nulls'])
total_imputed = total_nulls - df_isnull['Nulls'].sum()
imputed_file = 'Impute_KNN_' + pivot_table_name
df_impute.to_csv(path + imputed_file)
print_log('\n\n## Method 7 - Impute missing values with Natural Neigborns - KNN = %d Imputer from Scikit Learn' % n_neighbors +
          '\nAccording to this technique, the missing values are imputed using the natural neighbors values and the serie has been completed filled. More information in https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html' +
          '\n\nImputer = KNNImputer(n_neighbors=n_neighbors, weights=uniform, metric=nan_euclidean)' +
          '\n\nImputed file: [%s](%s)' % (imputed_file, imputed_file))
plot_impute(df, df_impute, 'KNN Imputer', imputed_file)
print_log('General statistics table - Imputed file', center_div=True)
print_log(df_impute.describe().T.to_markdown(), center_div=True)  # .T for transpose

# Method 8 - Impute missing values with Multivariate Imputation by Chained Equation - MICE from Scikit Learn
imputer = IterativeImputer(estimator=linear_model.BayesianRidge(), n_nearest_features=n_neighbors, initial_strategy='mean', min_value=min_value, imputation_order='ascending')
column_headers = df.columns.values.tolist()
index_list = list(df.index.values)
df_impute = imputer.fit_transform(df)
df_impute = pd.DataFrame(df_impute, columns=column_headers, index=index_list) # Convert numpy array to a pandas dataframe
df_isnull = pd.DataFrame(df_impute.isnull().sum(), columns=['Nulls'])
total_imputed = total_nulls - df_isnull['Nulls'].sum()
imputed_file = 'Impute_MICE_' + pivot_table_name
df_impute.to_csv(path + imputed_file)
print_log('\n\n## Method 8 - Impute missing values with Multivariate Imputation by Chained Equation - MICE from Scikit Learn' +
          '\nAccording to this technique, the missing values are imputed using MICE values and the serie has been completed filled. More information in https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html' +
          '\n\nImputer = %s' % str(imputer) +
          '\n\nImputed file: [%s](%s)' % (imputed_file, imputed_file))
plot_impute(df, df_impute, 'MICE Imputer', imputed_file)
print_log('General statistics table - Imputed file', center_div=True)
print_log(df_impute.describe().T.to_markdown(), center_div=True)  # .T for transpose
detailed_report = 'Impute_Station_' + pivot_table_name + '.md'
print_log('\nComplementary report with individual graphs for stations in [%s](%s)' % (detailed_report, detailed_report))

# Create a Markdown report with individual graphs for station
column_headers = df.columns.values.tolist()
if plot_stations:
    station_file_log = open(station_file_log_name, 'w+')  # w+ create the file if it doesn't exist
    station_file_log.write('# Impute missing values in time series through statistical methods - Complementary report' +
                           '\n* Processed file: [%s](%s)' % (
                           str(station_file), '../IDEAM_Outlier/' + pivot_table_name) +
                           '\n* Execution date: ' + str(datetime.now()) +
                           '\n* Instructions & script: https://github.com/rcfdtools/R.LTWB/tree/main/Section03/Impute'
                           '\n* License: https://github.com/rcfdtools/R.LTWB/blob/main/LICENSE.md'
                           '\n* Credits: r.cfdtools@gmail.com')
    for station in column_headers:
        station_file_log.write('\n\n## Station: ' + station + '\n\n![R.LTWB](Graph/' + station + '_Impute_Mean_' + pivot_table_name + '.png)' +
                               '![R.LTWB](Graph/' + station + '_Impute_Median_' + pivot_table_name + '.png)' +
                               '![R.LTWB](Graph/' + station + '_Impute_LOCF_' + pivot_table_name + '.png)' +
                               '![R.LTWB](Graph/' + station + '_Impute_NOCB_' + pivot_table_name + '.png)' +
                               '![R.LTWB](Graph/' + station + '_Impute_InterpolateLinear_' + pivot_table_name + '.png)' +
                               '![R.LTWB](Graph/' + station + '_Impute_MeanEWM_' + pivot_table_name + '.png)' +
                               '![R.LTWB](Graph/' + station + '_Impute_KNN_' + pivot_table_name + '.png)' +
                               '![R.LTWB](Graph/' + station + '_Impute_MICE_' + pivot_table_name + '.png)')

# Comments
print_log('\n> As you notice, some of the techniques showed above can`t fill complete the missing values at the start or at the end, however, you can first choice a method and then apply another complementary method for get full filled the missin values.')
```

2. Cree una nueva carpeta en blanco con el nombre `IDEAM_Impute` en su directorio de proyecto local `D:\R.LTWB\.datasets` y dentro de ella la carpeta `Graph`. Verifique que las carpetas locales `D:\R.LTWB\.datasets\IDEAM_EDA` y/o  `D:\R.LTWB\.datasets\IDEAM_Outlier`, contengan los archivos de las tablas dinámicas de cada parámetro hicroclimatológico [IDEAM_EDA](../../.datasets/IDEAM_EDA) o [IDEAM_Outlier](../../.datasets/IDEAM_Outlier) que fueron obtenidas en las actividades denominadas [EDA](../EDA) y [Outlier](../Outlier).

> Para la identificación de valores atípicos no son requeridas las tablas de datos de correlaciones identificadas con nombre terminado en _correlation.csv.
> 
> Dependiendo del tipo de parámetro y de los análisis previamente realizados en actividades anteriores, para el desarrollo de esta actividad de completado de datos, podrá utilizar las series de datos iniciales o la series con identificación y ajuste de valores atípicos.

3. Desde el editor de texto [Notepad++](https://notepad-plus-plus.org/), abra el archivo [D:\R.LTWB\.src\Impute.py](../../.src/Impute.py), y defina las siguientes variables:

* `pivot_table_name = 'Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv'`: corresponde a la tabla dinámica (pivot table) a procesar, p.ej., Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv corresponde a datos de precipitación mensual total, Outlier_IQR_Cap_Pivot_EV_TT_D.csv corresponde a datos de evaporación diaria total, Outlier_IQR_Cap_Pivot_Q_MEDIA_M.csv corresponde a datos de caudal medio mensual, Outlier_IQR_Cap_Pivot_TMN_CON.csv corresponde a datos de temperatura mínima diaria y Outlier_IQR_Cap_Pivot_TMX_CON.csv corresponde a datos de temperatura máxima diaria, todos con identificación y ajuste de valores atípicos a partir del método de rango intercuartílico - IQR y reemplazo Cap con $\mu$ +- K * $\sigma$.
* `min_value = 0`: corresponde al valor mínimo a imputar en el Método 8 - MICE, p.ej, para lluvia, evaporación y caudal, el valor mínimo es cero, pero dependiendo de la zona geográfica y para temperatura mínima y máxima, este valor puede ser negativo y puede ser establecido como menos infinito `-inf`. Para los datos del caso de estudio utilizaremos cero debido a que no existen estaciones con registros de temperatura negativos.
* `n_neighbors = 5`: número de vecinos naturales a utilizar en el Método 7 - KNN y en el Método 8 - MICE. Este valor depende del número de estaciones disponibles en cada parámetro. 

> Debido a que en evaporación solo disponemos de una estación, no se realizarán procesos de imputación de datos faltantes para este parámetro.
> 
> Tenga en cuenta que los resultados del Método 8 - MICE pueden variar de ejecución a ejecución del script debido al tipo de imputador utilizado.

![R.LTWB](Screenshot/NotepadPlusImputepy.png)

4. En Microsoft Windows, ejecute el _Command Prompt_ o _CMD_, ingrese `D:` y de <kbd>Enter</kbd> para cambiar a la unidad D:\ donde se encuentra el repositorio R.LTWB. Utilizando el comando  `CD D:\R.LTWB\.datasets\IDEAM_Impute` ubíquese dentro de la carpeta IDEAM_Impute.

![R.LTWB](Screenshot/Windows11CMDCD.png)

5. En él `CMD`, ejecute la instrucción `C:\Python3.10.5\python.exe "D:\R.LTWB\.src\Impute.py"` que realizará el procesamiento de imputación de datos faltantes. Durante la ejecución, podrá observar que en la consola se presenta el detalle de los procesos ejecutados para cada método, además de la previsualización de diferentes tablas en formato Markdown.

> Para visualizar durante la ejecución las gráficas generales de análisis, establezca la variable `show_plot = True`.

![R.LTWB](Screenshot/Windows11CMDImpute1.png)
![R.LTWB](Screenshot/Windows11CMDImpute2.png)
![R.LTWB](Screenshot/Windows11CMDImpute3.png)
![R.LTWB](Screenshot/Windows11CMDImpute4.png)
![R.LTWB](Screenshot/Windows11CMDImpute5.png)
![R.LTWB](Screenshot/Windows11CMDImpute6.png)
![R.LTWB](Screenshot/Windows11CMDImpute7.png)
![R.LTWB](Screenshot/Windows11CMDImpute8.png)
![R.LTWB](Screenshot/Windows11CMDImpute9.png)
![R.LTWB](Screenshot/Windows11CMDImpute10.png)
![R.LTWB](Screenshot/Windows11CMDImpute11.png)
![R.LTWB](Screenshot/Windows11CMDImpute12.png)
![R.LTWB](Screenshot/Windows11CMDImpute13.png)
![R.LTWB](Screenshot/Windows11CMDImpute14.png)
![R.LTWB](Screenshot/Windows11CMDImpute15.png)
![R.LTWB](Screenshot/Windows11CMDImpute16.png)
![R.LTWB](Screenshot/Windows11CMDImpute17.png)
![R.LTWB](Screenshot/Windows11CMDImpute18.png)
![R.LTWB](Screenshot/Windows11CMDImpute19.png)
![R.LTWB](Screenshot/Windows11CMDImpute20.png)
![R.LTWB](Screenshot/Windows11CMDImpute21.png)
![R.LTWB](Screenshot/Windows11CMDImpute22.png)
![R.LTWB](Screenshot/Windows11CMDImpute23.png)
![R.LTWB](Screenshot/Windows11CMDImpute24.png)
![R.LTWB](Screenshot/Windows11CMDImpute25.png)
![R.LTWB](Screenshot/Windows11CMDImpute26.png)

Luego de la ejecución, podrá observar que en la carpeta local `D:\R.LTWB\.datasets\IDEAM_Impute` se han generado diferentes archivos de resultados por cada método para la tabla de datos de precipitación mensual total Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv.

![R.LTWB](Screenshot/Windows11CMDImpute27.png)

De igual manera, en la carpeta local  `D:\R.LTWB\.datasets\IDEAM_Impute\Graph` se ha generado para cada estación, 8 gráficas de comparación de las series iniciales y las imputadas. Para las 130 estaciones, se han generado 1040 gráficas.

![R.LTWB](Screenshot/Windows11CMDImpute28.png)

Una vez finalizado el proceso de ejecución, podrá sincronizar en la nube los resultados en su repositorio de proyectos de GitHub y podrá observar el reporte detallado en formato Markdown [Impute_Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv.md](../../.datasets/IDEAM_Impute/Impute_Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv.md) y el reporte complementario de gráficos por estación [Impute_Station_Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv.md](../../.datasets/IDEAM_Impute/Impute_Station_Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv.md).

![R.LTWB](Screenshot/Windows11CMDImpute29.png)
![R.LTWB](Screenshot/Windows11CMDImpute30.png)
![R.LTWB](Screenshot/Windows11CMDImpute31.png)
![R.LTWB](Screenshot/Windows11CMDImpute32.png)
![R.LTWB](Screenshot/Windows11CMDImpute33.png)
![R.LTWB](Screenshot/Windows11CMDImpute34.png)
![R.LTWB](Screenshot/Windows11CMDImpute35.png)
![R.LTWB](Screenshot/Windows11CMDImpute36.png)
![R.LTWB](Screenshot/Windows11CMDImpute37.png)
![R.LTWB](Screenshot/Windows11CMDImpute38.png)

6. Repita el procedimiento anterior para los datos de caudal, temperatura mínima y máxima.


### Tablas de resultados y análisis generales

Durante el proceso de ejecución del script, se generan automáticamente para cada parámetro hidroclimatológico, un reporte integrado de resultados en formato Markdown (.md), gráficas de análisis y diferentes tablas en formato .csv.

| Reporte                                                                                                                                                                                                                                                                     | Descripción                      | Estaciones | Registros | Faltantes |   M1   |   M2   |   M3   |   M4   |   M5   |   M6   |   M7   |   M8   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|:----------:|:---------:|:---------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
| [Impute_Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv.md](../../.datasets/IDEAM_Impute/Impute_Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv.md)<br>[Impute_Station_Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv.md](../../.datasets/IDEAM_Impute/Impute_Station_Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv.md)  | Precipitación mensual total, mm. |    130     |    504    |   10157   | 10157  | 10157  |  8947  |  3143  |  8947  |  8947  | 10157  | 10157  |
| [Impute_Outlier_IQR_Cap_Pivot_Q_MEDIA_M.csv.md](../../.datasets/IDEAM_Impute/Impute_Outlier_IQR_Cap_Pivot_Q_MEDIA_M.csv.md)<br>[Impute_Station_Outlier_IQR_Cap_Pivot_Q_MEDIA_M.csv.md](../../.datasets/IDEAM_Impute/Impute_Station_Outlier_IQR_Cap_Pivot_Q_MEDIA_M.csv.md)  | Caudal medio mensual, m³/s.      |     46     |    504    |   6745    |  6745  |  6745  |  4682  |  4523  |  4682  |  4682  |  6745  |  6745  |
| [Impute_Outlier_IQR_Cap_Pivot_TMN_CON.csv.md](../../.datasets/IDEAM_Impute/Impute_Outlier_IQR_Cap_Pivot_TMN_CON.csv.md)<br>[Impute_Station_Outlier_IQR_Cap_Pivot_TMN_CON.csv.md](../../.datasets/IDEAM_Impute/Impute_Station_Outlier_IQR_Cap_Pivot_TMN_CON.csv.md)          | Temperatura diaria mínima, °C.   |     25     |   15341   |  173702   | 173702 | 173702 | 148100 | 86276  | 148100 | 148100 | 173702 | 173702 |
| [Impute_Outlier_IQR_Cap_Pivot_TMX_CON.csv.md](../../.datasets/IDEAM_Impute/Impute_Outlier_IQR_Cap_Pivot_TMX_CON.csv.md)<br>[Impute_Station_Outlier_IQR_Cap_Pivot_TMX_CON.csv.md](../../.datasets/IDEAM_Impute/Impute_Station_Outlier_IQR_Cap_Pivot_TMX_CON.csv.md)          | Temperatura diaria máxima, °C.   |     25     |   15341   |  197676   | 197676 | 197676 | 169785 | 108658 | 169785 | 169785 | 197676 | 197676 |

> En la tabla anterior, las columnas M1 a M8 contienen el número de datos imputados por cada método utilizado.
>
> Para todos los parámetros se han utilizado 5 vecinos naturales para la generación de datos sintéticos por los métodos KNN y MICE.
> 
> Dentro de cada reporte independiente por parámetro, se encuentran los enlaces a los archivos .csv generados por cada método.

Al revisar los estadísticos característicos, p. ej. de la estación 15015020, correspondiente a datos de precipitación total mensual en mmm, podrá observar los siguientes valores de media y desviación estándar:

<div align='center'>

| Método                                                                                                   | $\mu$, media | $\sigma$, std |
|:---------------------------------------------------------------------------------------------------------|:-------------|:--------------|
| Serie original                                                                                           | 59.7829      | 74.2829       |
| Serie con atípicos identificados con rango intercuartílico - IQR.<br>Reemplazo con $\mu$ +- K * $\sigma$ | 59.718       | 73.9846       |
| M1. Imputación con media, $\mu$                                                                          | 59.718       | 60.6479       |
| M2. Imputación con mediana                                                                               | 50.0217      | 62.2231       |
| M3. Imputación LOCF                                                                                      | 54.6675      | 68.6241       |
| M4. Imputación NOCB                                                                                      | 70.1873      | 73.8053       |
| M5. Imputación pir interpolación lineal                                                                  | 55.7429      | 70.1337       |
| M6. Media móvil - EWM                                                                                    | 64.0103      | 61.0386       |
| M7. Vecino natural - KNN                                                                                 | 56.6695      | 68.2329       |
| M8. Multivariante con ecuación de encadenamiento - MICE                                                  | 59.5799      | 71.8106       |

</div>

> Evalúe los datos sintéticos de precipitación generados en las estaciones 28010280 (489 meses faltantes de 504 definidos en la ventana de tiempo), 28040170 y 28010130.

Al revisar los estadísticos característicos, p. ej. de la estación 15067080, correspondiente a datos de caudal medio mensual en m³/s, podrá observar los siguientes valores de media y desviación estándar:

![R.LTWB](Screenshot/Windows11CMDImpute39.png)

<div align='center'>

| Método                                                                                                   | $\mu$, media | $\sigma$, std |
|:---------------------------------------------------------------------------------------------------------|:-------------|:--------------|
| Serie original                                                                                           | 2.17867      | 3.43166       |
| Serie con atípicos identificados con rango intercuartílico - IQR.<br>Reemplazo con $\mu$ +- K * $\sigma$ | 2.10051      | 2.89856       |
| M1. Imputación con media, $\mu$                                                                          | 2.10051      | 2.20089       |
| M2. Imputación con mediana                                                                               | 1.62587      | 2.26987       |
| M3. Imputación LOCF                                                                                      | 1.63324      | 2.55661       |
| M4. Imputación NOCB                                                                                      | 2.10959      | 2.85675       |
| M5. Imputación pir interpolación lineal                                                                  | 1.88085      | 2.52606       |
| M6. Media móvil - EWM                                                                                    | 1.93414      | 2.39007       |
| M7. Vecino natural - KNN                                                                                 | 2.1734       | 2.59388       |
| M8. Multivariante con ecuación de encadenamiento - MICE                                                  | 2.14873      | 2.50686       |

</div>

> Evalúe los datos sintéticos de caudal generados en las estaciones 15067210 (476 meses faltantes de 504 definidos en la ventana de tiempo), 28017150 y 28047080.

Al revisar los estadísticos característicos, p. ej. de la estación 15015020, correspondiente a datos de temperatura mínima diaria en °C, podrá observar los siguientes valores de media y desviación estándar:

![R.LTWB](Screenshot/Windows11CMDImpute40.png)

<div align='center'>

| Método                                                                                                   | $\mu$, media | $\sigma$, std |
|:---------------------------------------------------------------------------------------------------------|:-------------|:--------------|
| Serie original                                                                                           | 22.1888      | 1.60856       |
| Serie con atípicos identificados con rango intercuartílico - IQR.<br>Reemplazo con $\mu$ +- K * $\sigma$ | 22.1889      | 1.60836       |
| M1. Imputación con media, $\mu$                                                                          | 22.1889      | 1.29618       |
| M2. Imputación con mediana                                                                               | 22.2629      | 1.30009       |
| M3. Imputación LOCF                                                                                      | 21.8967      | 1.49166       |
| M4. Imputación NOCB                                                                                      | 22.4437      | 1.60576       |
| M5. Imputación pir interpolación lineal                                                                  | 22.1279      | 1.37931       |
| M6. Media móvil - EWM                                                                                    | 21.9331      | 1.50143       |
| M7. Vecino natural - KNN                                                                                 | 22.4928      | 1.50449       |
| M8. Multivariante con ecuación de encadenamiento - MICE                                                  | 22.3708      | 1.43403       |

</div>

> Evalúe los datos sintéticos de temperatura mínima generados en las estaciones 28035070 (15299 dias faltantes de 15341 definidos en la ventana de tiempo), 28045020 y 29065010.

Al revisar los estadísticos característicos, p. ej. de la estación 15015020, correspondiente a datos de temperatura máxima diaria en °C, podrá observar los siguientes valores de media y desviación estándar:

![R.LTWB](Screenshot/Windows11CMDImpute41.png)

<div align='center'>

| Método                                                                                                   | $\mu$, media | $\sigma$, std |
|:---------------------------------------------------------------------------------------------------------|:-------------|:--------------|
| Serie original                                                                                           | 33.0729      | 1.48932       |
| Serie con atípicos identificados con rango intercuartílico - IQR.<br>Reemplazo con $\mu$ +- K * $\sigma$ | 33.0737      | 1.48617       |
| M1. Imputación con media, $\mu$                                                                          | 33.0737      | 1.12933       |
| M2. Imputación con mediana                                                                               | 33.1271      | 1.13106       |
| M3. Imputación LOCF                                                                                      | 32.8218      | 1.43228       |
| M4. Imputación NOCB                                                                                      | 31.9541      | 2.32025       |
| M5. Imputación pir interpolación lineal                                                                  | 32.316       | 1.62844       |
| M6. Media móvil - EWM                                                                                    | 32.6945      | 1.36275       |
| M7. Vecino natural - KNN                                                                                 | 33.1279      | 1.30787       |
| M8. Multivariante con ecuación de encadenamiento - MICE                                                  | 33.2334      | 1.28619       |

</div>

> Evalúe los datos sintéticos de temperatura máxima generados en las estaciones 28035070 (15299 dias faltantes de 15341 definidos en la ventana de tiempo), 28045040 y 29065010.

**Conclusión general**

Existen diferentes metodologías estadísticas para el completado y extendido de series, su aplicación en hidrología depende del tipo de parámetro hidroclimatológico a estudiar, del número de datos faltantes, del número de estaciones simultáneas evaluadas y de la ventana de tiempo definida para los análisis. Si bien existen metodologías geo-estadísticas en las que se evalúan las relaciones espaciales (basadas en distancia y/o proximidad, bandas de elevación y correlación con otros parámetros) entre las estaciones utilizadas, con los métodos estadísticos vecino natural - KNN o multivariante - MICE, se pueden obtener datos sintéticos que mantienen la tendencia general de la zona estudiada a partir de las estaciones definidas. Para el desarrollo de las actividades posteriores de este curso, usaremos las series de datos completadas y extendidas por el Método 8 - Multivariante con ecuación de encadenamiento - MICE, debido a que permite mantener la tendencia general de los datos zonales y valores similares de media y desviación estándar. 

En este momento, dispone de reportes detallados de completado y extendido de datos por cada parámetro hidroclimatológico y diferentes tablas en formato de texto separado por comas `.csv` para los diferentes métodos implementados.


### Actividades complementarias:pencil2:

En la siguiente tabla se listan las actividades complementarias que deben ser desarrolladas y documentadas por el estudiante en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (mostrar nombre completo, código y enlace a su cuenta de GitHub), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.

| Actividad | Alcance                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|:---------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1     | A partir del script [Impute.py](../../.src/Impute.py), realice el completado y extendido de los parámetros climatológicos definidos como actividad complementaria en [descarga de datos hidroclimatológicos](../CNEStationDatasetDownload); correspondientes a brillo solar, radiación solar, humedad del aire cerca al suelo y parámetros relacionados con viento y nubosidad.                                                                                               |
|     2     | Para todas los parámetros climatológicos y a partir de las gráficas y tablas de análisis generadas mediante el script [Impute.py](../../.src/Impute.py), presente un análisis cualitativo e identifique en que estaciones no se han obtenido datos sintéticos consistentes para los métodos implementados.                                                                                                                                                                    | 
|     3     | A partir de los datos de precipitación media mensual, identifique una estación que contenga una serie continua cercana a 41 años, analice los estadísticos de 10 años consecutivos de datos, elimínelos de la serie y genere datos sintéticos por el método KNN y MICE. Luego, grafique la serie original y la serie sintética, obtenga los estadísticos y realice una análisis cualitativo de similitud y correlación, explicando que tan similares son los datos generados. |

### Referencias

* https://www.projectpro.io/recipes/deal-with-missing-values-in-timeseries-in-python
* https://towardsdatascience.com/8-methods-for-handling-missing-values-with-python-pandas-842544cdf891
* https://towardsdatascience.com/4-techniques-to-handle-missing-values-in-time-series-data-c3568589b5a8
* https://www.section.io/engineering-education/missing-values-in-time-series/
* https://www.kaggle.com/code/parulpandey/a-guide-to-handling-missing-values-in-python
* https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.interpolate.html
* https://github.com/ResidentMario/missingno
* https://towardsdatascience.com/imputing-missing-data-with-simple-and-advanced-techniques-f5c7b157fb87#:~:text=Time%20Series%20Imputation&text=One%20way%20to%20impute%20missing,with%20the%20previously%20observed%20value
* https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html
* https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html


### Control de versiones

| Versión    | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Autor                                       | Horas |
|------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|:-----:|
| 2022.11.16 | Complementación documentación general con análisis descriptivos por parámetro. Ilustración cabecera y diagrama de procesos.                                                                                                                                                                                                                                                                                                                                                                               | [rcfdtools](https://github.com/rcfdtools)   |   4   |
| 2022.11.14 | Inicio documentación general.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | [rcfdtools](https://github.com/rcfdtools)   |   3   |
| 2022.11.12 | Generador de 8 gráficas individuales de series por estación. Reporte complementario para visualización de gráficas por estación. Exportación de imputaciones a archivos .csv para cada método.                                                                                                                                                                                                                                                                                                            | [rcfdtools](https://github.com/rcfdtools)   |   4   |
| 2022.11.11 | Method 7 - Impute missing values with Natural Neigborns - KNN = 5 Imputer from Scikit Learn. Method 8 - Impute missing values with Multivariate Imputation by Chained Equation - MICE from Scikit Learn.                                                                                                                                                                                                                                                                                                  | [rcfdtools](https://github.com/rcfdtools)   |   3   |
| 2022.11.10 | Script versión inicial. Method 1 - Imputing with mean values. Method 2 - Imputing with median values. Method 3 - Imputing with Last Observation Carried Forward (LOCF) values. Method 4 - Imputing with Next Observation Carried Backward (NOCB) values. Method 5 - Impute missing values with Linear Interpolation values. Method 6 - Impute missing values with Exponential (Weighted) Moving Average - EWM. Métodos con generación de reporte y gráficas sin exportación de datasets imputados a .csv. | [rcfdtools](https://github.com/rcfdtools)   |   5   |


_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Actividad anterior](../Outlier) | [Inicio](../../Readme.md) | [:beginner: Ayuda](https://github.com/rcfdtools/R.LTWB/discussions/25) | [Actividad siguiente]() |
|----------------------------------|---------------------------|------------------------------------------------------------------------|-------------------------|

