# -*- coding: UTF-8 -*-
# Name: Outlier.py
# Description: outliers detection and processing
# Requirements: Python 3+, pandas, tabulate
# Attention: do not convert the .csv file into an Excel file because you would need process more than 1048576 records.


# Libraries
import sys
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
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

# Function to find outliers using interquartile range - IQR
# Ref: https://careerfoundry.com/en/blog/data-analytics/how-to-find-outliers/
def find_outliers_IQR(df):
    q1 = df.quantile(q1_val)
    q3 = df.quantile(q3_val)
    IQR = q3-q1
    outliers = df[((df < (q1-1.5*IQR)) | (df > (q3+1.5*IQR)))]
    return outliers

# Function to drop outliers using interquartile range - IQR
# Ref: https://careerfoundry.com/en/blog/data-analytics/how-to-find-outliers/
def drop_outliers_IQR(df):
    q1 = df.quantile(q1_val)
    q3 = df.quantile(q3_val)
    IQR = q3-q1
    not_outliers = df[~((df < (q1-1.5*IQR)) | (df > (q3+1.5*IQR)))]
    return not_outliers



# General variables
pivot_table_name = 'Pivot_PTPM_TT_M.csv'  # <<<<< Pivot table name to process
path_input = 'D:/R.LTWB/.datasets/IDEAM_EDA/'  # Current location from pivot tables
station_file = path_input + pivot_table_name  # Current pivot IDEAM records file for a specified parameter
path = 'D:/R.LTWB/.datasets/IDEAM_Outlier/'  # Your local output path, use ../.datasets/IDEAM_Outlier/ for relative path
file_log_name = path + 'Outlier_IQR_' + pivot_table_name + '.md'  # First file log
file_log = open(file_log_name, 'w+')   # w+ create the file if it doesn't exist
date_record_name = 'Fecha'  # IDEAM date field name for the record values
plot_colormap = 'autumn'  # Color theme for plot graphics, https://matplotlib.org/stable/tutorials/colors/colormaps.html
sample_records = 3  # Records to show in the sample table head and tail
fig_size = 5  # Height size for figures plot
print_table_sample = True
q1_val = 0.1  # Default is 0.25
q3_val = 0.9  # Default is 0.75


# Header
print_log('## Outliers detection and processing')
print_log('\n* Processed file: [%s](%s)' % (str(station_file), '../IDEAM_EDA/' + pivot_table_name) +
          '\n* Execution date: ' + str(datetime.now()) +
          '\n* Python version: ' + str(sys.version) +
          '\n* Python path: ' + str(sys.path[0:5]) +
          '\n* matplotlib version: ' + str(matplotlib.__version__) +
          '\n* pandas version: ' + str(pd.__version__) +
          '\n* Print table sample: ' + str(print_table_sample) +
          '\n* Instructions & script: https://github.com/rcfdtools/R.LTWB/tree/main/Section03/Outlier'
          '\n* License: https://github.com/rcfdtools/R.LTWB/blob/main/LICENSE.md'
          '\n* Credits: r.cfdtools@gmail.com')


# Open the IDEAM station dataframe and show general information
df = pd.read_csv(station_file, low_memory=False, parse_dates=[date_record_name], index_col=date_record_name)
ideam_regs = df.shape[0]
print_log('\n\n### General dataframe information with %d IDEAM records for %d stations' % (ideam_regs, df.shape[1]))
print(df.info())
if print_table_sample:
    print_log('\nDataframe records head sample\n')
    print_log(df.head(sample_records).to_markdown())
    print_log('\nDataframe records tail sample\n')
    print_log(df.tail(sample_records).to_markdown())
print_log('\nDatatypes for station and nulls values in the dataset', center_div=False)
df_dtypes = pd.DataFrame(df.dtypes, columns=['Dtype'])
df_isnull = pd.DataFrame(df.isnull().sum(), columns=['Nulls'])
df_concat = pd.concat([df_dtypes, df_isnull], axis='columns').T # .T for transpose
print_log(df_concat.to_markdown(), center_div=True)
print_log('General statistics table', center_div=True)
print_log(df.describe().T.to_markdown(), center_div=True) # .T for transpose


# Method 1 - Outliers processing for interquartile range IQR
print_log('### Method 1 - Outliers processing using the interquartile range IQR (q1 = %s, q3 = %s)' % (str(q1_val), str(q3_val)))
outliers = find_outliers_IQR(df)
outlier_file = 'Outlier_IQR_' + pivot_table_name
print_log('\nOutliers table: [%s](../../.datasets/IDEAM_Outlier/%s)' % (outlier_file, outlier_file))
outliers.to_csv(path + outlier_file)
print_log('\nOutliers parameters'
          '\n* q1: quartile %s' % str(q1_val) +
          '\n* q3: quartile %s' % str(q3_val) +
          '\n* IQR: interquartile range (q3-q1)' +
          '\n* OlLowerLim: outlier bottom limit (q1-1.5*IQR)'
          '\n* OlUpperLim: outlier top limit (q3+1.5*IQR)'
          '\n* OlMinVal: minimum outlier value founded'
          '\n* OlMaxVal: maximum outlier value founded'
          '\n* OlCount: # outliers founded\n'
          )
df_q1 = df.quantile(q1_val).to_frame()
df_q1.columns = ['q1']
df_q3 = df.quantile(q3_val).to_frame()
df_q3.columns = ['q3']
df_IQR = (df_q3['q3'] - df_q1['q1']).to_frame()
df_IQR.columns = ['IQR']
df_bottom_lim = (df_q1['q1'] + 1.5 * df_IQR['IQR']).to_frame()
df_bottom_lim.columns = ['OlLowerLim']
df_top_lim = (df_q3['q3'] + 1.5 * df_IQR['IQR']).to_frame()
df_top_lim.columns = ['OlUpperLim']
df_count = pd.DataFrame(outliers.count(), columns=['OlCount'])
df_min = pd.DataFrame(outliers.min(), columns=['OlMinVal'])
df_max = pd.DataFrame(outliers.max(), columns=['OlMaxVal'])
df_concat = pd.concat([df_q1, df_q3, df_IQR, df_bottom_lim, df_top_lim, df_min, df_max, df_count], axis='columns')
print_log(df_concat.to_markdown(), center_div=True)
# Plot values and outliers
df_outlier = pd.read_csv(path + outlier_file, low_memory=False, parse_dates=[date_record_name], index_col=date_record_name)
ax = df.plot(colormap=plot_colormap, legend=False, alpha=0.1, figsize=(12, 6))  # colormap can be replaced by color='lightblue'
df_outlier.plot(ax=ax, color='black', legend=False, figsize=(fig_size*2, fig_size+1))
plt.title('Method 1 - IQR outliers (q1 = %s, q3 = %s) for %d stations (%d outliers)' % (str(q1_val), str(q3_val), df.shape[1], df_concat['OlCount'].sum()))
ax.set_ylabel('Values for %s' % pivot_table_name)
plt.savefig(path + outlier_file + '.png')
print_log('\n![R.LTWB](%s)' % (outlier_file + '.png'), center_div=False)
print_log('\nIQR outliers identified: %d' % df_concat['OlCount'].sum())
plt.show()
plt.close('all')
# Drop outliers values
not_outliers = drop_outliers_IQR(df)
outlier_file = 'Outlier_IQR_Drop_' + pivot_table_name
print_log('\nOutliers drop file: [%s](../../.datasets/IDEAM_Outlier/%s)' % (outlier_file, outlier_file))
not_outliers.to_csv(path + outlier_file)


#print(df_IQR)
#print(type(df_IQR))