# -*- coding: UTF-8 -*-
# Name: Outlier.py
# Description: outliers detection and processing throught statistical methods
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

# Cap IQR outliers with specified limits (mean() - cap_multiplier * std())
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

# Impute IQR outliers with mean values
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


# General variables
pivot_table_name = 'Pivot_Q_MEDIA_M.csv'  # <<<<< Pivot table name to process
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
station_exclude = ['28017140', '25027020', '25027410', '25027490', '25027330', '25027390', '25027630', '25027360', '25027320', '16067010', '25027420']  # Use ['station1', 'station2', '...',]
q1_val = 0.1  # Default is 0.25
q3_val = 0.9  # Default is 0.75
cap_multiplier = 3 # Replacement outlier value multiplier, default is 3. e.j, mean() +- cap_multiplier * std()


# Header
print_log('## Outliers detection and processing throught statistical methods')
print_log('\n* Processed file: [%s](%s)' % (str(station_file), '../IDEAM_EDA/' + pivot_table_name) +
          '\n* Execution date: ' + str(datetime.now()) +
          '\n* Python version: ' + str(sys.version) +
          '\n* Python path: ' + str(sys.path[0:5]) +
          '\n* matplotlib version: ' + str(matplotlib.__version__) +
          '\n* pandas version: ' + str(pd.__version__) +
          '\n* numpy version: ' + str(np.__version__) +
          '\n* Print table sample: ' + str(print_table_sample) +
          '\n* Instructions & script: https://github.com/rcfdtools/R.LTWB/tree/main/Section03/Outlier'
          '\n* License: https://github.com/rcfdtools/R.LTWB/blob/main/LICENSE.md'
          '\n* Credits: r.cfdtools@gmail.com')


# Open the IDEAM station dataframe and show general information
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


# Method 1 - Outliers processing for interquartile range IQR
print_log('### Method 1 - Outliers processing using the interquartile range IQR (q1 = %s, q3 = %s)' % (str(q1_val), str(q3_val)))
outliers = find_outliers_IQR(df)
outlier_file = 'Outlier_IQR_' + pivot_table_name
outliers.to_csv(path + outlier_file)
print_log('\nOutliers parameters:'
          '\n* q1: quartile %s' % str(q1_val) +
          '\n* q3: quartile %s' % str(q3_val) +
          '\n* IQR: interquartile range (q3-q1)' +
          '\n* OlLowerLim: outlier bottom limit (q1-1.5*IQR)'
          '\n* OlUpperLim: outlier top limit (q3+1.5*IQR)'
          '\n* OlMinVal: minimum outlier value founded'
          '\n* OlMaxVal: maximum outlier value founded'
          '\n* OlCount: # outliers founded'
          '\n* CapLowerLim: capped lower limit for outliers replacement (mean() - %s * std())' % str(cap_multiplier) +
          '\n* CapUpperLim: capped upper limit for outliers replacement (mean() + %s * std())\n' % str(cap_multiplier)
          )
# Assemble the parameters table
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
df_concat = pd.concat([df_q1, df_q3, df_IQR, df_lower_lim, df_upper_lim, df_min, df_max, df_count, df_lower_cap, df_upper_cap], axis='columns')
print_log(df_concat.to_markdown(), center_div=True)
# Plot values and outliers
df_outlier = pd.read_csv(path + outlier_file, low_memory=False, parse_dates=[date_record_name], index_col=date_record_name)
ax = df.plot(colormap=plot_colormap, legend=False, alpha=0.1, figsize=(12, 6))  # colormap can be replaced by color='lightblue'
df_outlier.plot(ax=ax, color='black', legend=False, figsize=(fig_size*2, fig_size+1))
plt.title('Method 1 - IQR outliers (q1 = %s, q3 = %s) for %d stations (%d outliers)' % (str(q1_val), str(q3_val), df.shape[1], df_concat['OlCount'].sum()))
ax.set_ylabel('Values for %s' % pivot_table_name)
plt.savefig(path + outlier_file + '.png')
print_log('\n![R.LTWB](%s)' % (outlier_file + '.png'), center_div=False)
plt.show()
plt.close('all')
# Drop outliers values
not_outliers = drop_outliers_IQR(df)
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
# Print resoults
print_log('\n#### Identified and cleaning tables for %d IQR outliers founded' % df_concat['OlCount'].sum() +
          '\n* Outliers identified file: [%s](../../.datasets/IDEAM_Outlier/%s)' % (outlier_file, outlier_file) +
          '\n* Outliers dropped file: [%s](../../.datasets/IDEAM_Outlier/%s)' % (outlier_file_drop, outlier_file_drop) +
          '\n* Outliers capped file: [%s](../../.datasets/IDEAM_Outlier/%s)' % (outlier_file_cap, outlier_file_cap) +
          '\n* Outliers imputed file: [%s](../../.datasets/IDEAM_Outlier/%s)' % (outlier_file_impute, outlier_file_impute))
print_log('\n> The _drop file_ contains the database values without the outliers identified.'
          '\n>'
          '\n> The _capped file_ contains the database values and the outliers has been replaced with the lower or upper capped value calculated. Lower outliers could be replaced with negative values because the limit is defined with (mean() - cap_multiplier * std()). In some cases like _temperature analysis_, the upper outliers values could be replaced with values over the original values and you can try to fix this issue changing the parameter _cap_multiplier_ that defines the stripe values range.'
          '\n>'
          '\n> The imputation method replace each outlier value with the mean value that contains the original outliers values.'
          )
print_log('\n\n#### Statistical values for the capped and imputed file', center_div=False)
print_log('General statistics table - Capped file', center_div=True)
print_log(df_capped.describe().T.to_markdown(), center_div=True) # .T for transpose
print_log('General statistics table - Imputed file', center_div=True)
print_log(df_impute.describe().T.to_markdown(), center_div=True) # .T for transpose
'''
print('\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print(df.head(sample_records).to_markdown())
print('\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXX Index')
print(list(df.index.values))
print('\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
'''


# Method 2 - Outliers processing with a specified range (mean() - cap_multiplier * std())
'''
df_capped = df
column_headers = df_capped.columns.values.tolist()
lower_limit = df_capped.mean()-cap_multiplier*df_capped.std()
upper_limit = df_capped.mean()+cap_multiplier*df_capped.std()
df_capped = np.where(df_capped > upper_limit,
    upper_limit,
    np.where(
       df_capped < lower_limit,
       lower_limit,
       df_capped
    )
)
df_capped = pd.DataFrame(df_capped, columns=column_headers)
outlier_file_cap = 'Outlier_IQR_Cap_' + pivot_table_name
df_capped.to_csv(path + outlier_file_cap)
'''

#print(df_IQR)
#print(type(df_IQR))