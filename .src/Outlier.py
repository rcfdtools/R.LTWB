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

# Function to find outliers using empirical rules - ER
def find_outliers_ER(df):
    lower_cap = df.mean() - cap_multiplier * df.std()
    upper_cap = df.mean() + cap_multiplier * df.std()
    outliers = df[((df < lower_cap) | (df > upper_cap))]
    return outliers

# Function to drop outliers using empirical rules - ER
def drop_outliers_ER(df):
    lower_cap = df.mean() - cap_multiplier * df.std()
    upper_cap = df.mean() + cap_multiplier * df.std()
    not_outliers = df[~((df < lower_cap) | (df > upper_cap))]
    return not_outliers

# Function for Cap ER outliers with specified limits (mean() - cap_multiplier * std())
def cap_outliers_ER(df):
    column_headers = df.columns.values.tolist()
    index_list = list(df.index.values)
    lower_cap = df.mean() - cap_multiplier * df.std()
    upper_cap = df.mean() + cap_multiplier * df.std()
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

# Function for impute ER outliers with the mean values
def impute_outliers_ER(df):
    column_headers = df.columns.values.tolist()
    index_list = list(df.index.values)
    lower_cap = df.mean() - cap_multiplier * df.std()
    upper_cap = df.mean() + cap_multiplier * df.std()
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

# Function to find outliers using the Z-score or standard score
def find_outliers_zscore(df):
    z = (df - df.mean()) / df.std()
    outliers = df[(z >= zscore_threshold)]
    return outliers

# Function to drop outliers using the Z-score or standard score
def drop_outliers_zscore(df):
    z = (df - df.mean()) / df.std()
    not_outliers = df[~(z >= zscore_threshold)]
    return not_outliers

# Function for Cap Z-score outliers with specified limits (mean() - cap_multiplier * std())
def cap_outliers_zscore(df):
    column_headers = df.columns.values.tolist()
    index_list = list(df.index.values)
    lower_cap = df.mean() - zscore_threshold * df.std()
    upper_cap = df.mean() + zscore_threshold * df.std()
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

# Function for impute ER outliers with the mean values
def impute_outliers_zscore(df):
    column_headers = df.columns.values.tolist()
    index_list = list(df.index.values)
    lower_cap = df.mean() - zscore_threshold * df.std()
    upper_cap = df.mean() + zscore_threshold * df.std()
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


# General variables
pivot_table_name = 'Pivot_TMX_CON.csv'  # <<<<< Pivot table name to process
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
q1_val = 0.175  # Default is 0.25. Method 1.
q3_val = 0.825  # Default is 0.75. Method 1.
cap_multiplier = 3.6  # Replacement cap outlier value multiplier or k value, default is 3. e.j, mean() +- cap_multiplier * std(). k over empirical rules. . Method 1 & 2.
zscore_threshold = 2.95  # Z-score threshold, default is 3. Method 3. If the threshold is equal to the cap_multiplier, the results are the same as Method 2.


# Header
print_log('## Outliers detection and processing through statistical methods for %s' % pivot_table_name)
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
outliers = find_outliers_IQR(df)
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
outliers = find_outliers_ER(df)
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
not_outliers = drop_outliers_ER(df)
outlier_file_drop = 'Outlier_ER_Drop_' + pivot_table_name
not_outliers.to_csv(path + outlier_file_drop)
# Capped outliers values
df_capped = cap_outliers_ER(df)
outlier_file_cap = 'Outlier_ER_Cap_' + pivot_table_name
df_capped.to_csv(path + outlier_file_cap, index_label=date_record_name)
# Impute outliers with mean values
df_impute = impute_outliers_ER(df)
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
outliers = find_outliers_zscore(df)
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
not_outliers = drop_outliers_zscore(df)
outlier_file_drop = 'Outlier_ZScore_Drop_' + pivot_table_name
not_outliers.to_csv(path + outlier_file_drop)
# Capped outliers values
df_capped = cap_outliers_zscore(df)
outlier_file_cap = 'Outlier_ZScore_Cap_' + pivot_table_name
df_capped.to_csv(path + outlier_file_cap, index_label=date_record_name)
# Impute outliers with mean values
df_impute = impute_outliers_zscore(df)
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