# -*- coding: UTF-8 -*-
# Name: Impute.py
# Description: impute missing values in time series through statistical methods
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

# Function for plot original and imputed series
def plot_impute(df_org, df_impute, method, file_name):
    ax = df_impute.plot(color='black', legend=False, alpha=1, figsize=(fig_size*2, fig_size+1), linewidth=0.75)
    df_org.plot(ax=ax, colormap=plot_colormap, alpha=1, legend=False, figsize=(fig_size*2, fig_size+1))
    plt.title('Impute with %s value for %d stations (%d missing & %d imputed)' % (method, df.shape[1], total_nulls, total_imputed))
    ax.set_ylabel('Values in %s (%d recs.)' % (pivot_table_name, ideam_regs))
    plt.savefig(path + file_name + '.png')
    print_log('\n![R.LTWB](%s)' % (file_name + '.png'), center_div=False)
    if show_plot: plt.show()
    plt.close('all')


# General variables
pivot_table_name = 'Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv'  # <<<<< Pivot table name to process
path_input = 'D:/R.LTWB/.datasets/IDEAM_Outlier/'  # Current location from pivot tables
station_file = path_input + pivot_table_name  # Current pivot IDEAM records file for a specified parameter
path = 'D:/R.LTWB/.datasets/IDEAM_Impute/'  # Your local output path, use ../.datasets/IDEAM_Impute/ for relative path
file_log_name = path + 'Impute_' + pivot_table_name + '.md'  # Markdown file log
file_log = open(file_log_name, 'w+')   # w+ create the file if it doesn't exist
date_record_name = 'Fecha'  # IDEAM date field name for the record values
plot_colormap = 'autumn'  # Color theme for plot graphics, https://matplotlib.org/stable/tutorials/colors/colormaps.html
sample_records = 3  # Records to show in the sample table head and tail
fig_size = 5  # Height size for figures plot
fig_alpha = 0.5  # Alpha transparency color in plots
print_table_sample = True
show_plot = False
station_exclude = ['28017140', '25027020', '25027410', '25027490', '25027330', '25027390', '25027630', '25027360', '25027320', '16067010', '25027420']  # Use ['station1', 'station2', '...',]
#station_exclude = ['28010090', '28025040']  # Use ['station1', 'station2', '...',]


# Header
print_log('## Impute missing values in time series through statistical methods')
print_log('\n* Processed file: [%s](%s)' % (str(station_file), '../IDEAM_EDA/' + pivot_table_name) +
          '\n* Execution date: ' + str(datetime.now()) +
          '\n* Python version: ' + str(sys.version) +
          '\n* Python path: ' + str(sys.path[0:5]) +
          '\n* matplotlib version: ' + str(matplotlib.__version__) +
          '\n* pandas version: ' + str(pd.__version__) +
          '\n* numpy version: ' + str(np.__version__) +
          '\n* Stations exclude: ' + str(station_exclude) +
          '\n* Print table sample: ' + str(print_table_sample) +
          '\n* Instructions & script: https://github.com/rcfdtools/R.LTWB/tree/main/Section03/Impute'
          '\n* License: https://github.com/rcfdtools/R.LTWB/blob/main/LICENSE.md'
          '\n* Credits: r.cfdtools@gmail.com')


# Open the IDEAM station pivot dataframe and show general information
df = pd.read_csv(station_file, low_memory=False, parse_dates=[date_record_name], index_col=date_record_name)
#df = df.loc[:, df.columns.isin(station_exclude)]
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
total_nulls = df_concat.T['Nulls'].sum()
#print_log('\nTotal nulls values founded in the dataset: %d\n' % total_nulls, center_div=False)
#nul_data = pd.DataFrame(df.isnull())
#print_log(nul_data.to_markdown())
ax = df.plot(colormap=plot_colormap, legend=False, alpha=fig_alpha, figsize=(fig_size*2, fig_size+1))  # colormap can be replaced by color='lightblue'
plt.title('Original serie with %d stations (%d missing values)' % (df.shape[1], total_nulls))
ax.set_ylabel('Values in %s (%d recs.)' % (pivot_table_name, ideam_regs))
plt.savefig(path + pivot_table_name + '.png')
print_log('\n![R.LTWB](%s)' % (pivot_table_name + '.png'), center_div=False)
if show_plot: plt.show()
plt.close('all')
print_log('General statistics table - Initial file', center_div=True)
print_log(df.describe().T.to_markdown(), center_div=True) # .T for transpose

# Method 1 - Impute missing values with mean values
df_impute = df.fillna(df.mean())
df_isnull = pd.DataFrame(df_impute.isnull().sum(), columns=['Nulls'])
total_imputed = total_nulls - df_isnull['Nulls'].sum()
print_log('\n### Method 1 - Imputing with mean values for %d stations (%d missing & %d imputed)' % (df.shape[1], total_nulls, total_imputed))
impute_file = 'Impute_Mean_' + pivot_table_name
plot_impute(df, df_impute, 'MEAN', impute_file)

# Method 2 - Impute missing values with median values
df_impute = df.fillna(df.median())
df_isnull = pd.DataFrame(df_impute.isnull().sum(), columns=['Nulls'])
total_imputed = total_nulls - df_isnull['Nulls'].sum()
print_log('\n### Method 2 - Imputing with median values for %d stations (%d missing & %d imputed)' % (df.shape[1], total_nulls, total_imputed))
impute_file = 'Impute_Median_' + pivot_table_name
plot_impute(df, df_impute, 'MEDIAN', impute_file)

# Method 3 - Impute missing values with Last Observation Carried Forward (LOCF)
df_impute = df.fillna(method='bfill')
df_isnull = pd.DataFrame(df_impute.isnull().sum(), columns=['Nulls'])
total_imputed = total_nulls - df_isnull['Nulls'].sum()
print_log('\n### Method 3 - Imputing with Last Observation Carried Forward (LOCF) values for %d stations (%d missing & %d imputed)' % (df.shape[1], total_nulls, total_imputed))
impute_file = 'Impute_LOCF_' + pivot_table_name
plot_impute(df, df_impute, 'LOCF', impute_file)

# Method 4 - Impute missing values with Next Observation Carried Backward (NOCB)
df_impute = df.fillna(method='ffill')
df_isnull = pd.DataFrame(df_impute.isnull().sum(), columns=['Nulls'])
total_imputed = total_nulls - df_isnull['Nulls'].sum()
print_log('\n### Method 4 - Imputing with Next Observation Carried Backward (NOCB) values for %d stations (%d missing & %d imputed)' % (df.shape[1], total_nulls, total_imputed))
impute_file = 'Impute_NOCB_' + pivot_table_name
plot_impute(df, df_impute, 'NOCB', impute_file)

# Method 5 - Impute missing values with Linear Interpolation
df_impute = df.interpolate(method='linear')
df_isnull = pd.DataFrame(df_impute.isnull().sum(), columns=['Nulls'])
total_imputed = total_nulls - df_isnull['Nulls'].sum()
print_log('\n### Method 5 - Impute missing values with Linear Interpolation values for %d stations (%d missing & %d imputed)' % (df.shape[1], total_nulls, total_imputed))
impute_file = 'Impute_InterpolateLinear_' + pivot_table_name
plot_impute(df, df_impute, 'Linear Interpolation', impute_file)

