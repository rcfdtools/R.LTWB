# -*- coding: UTF-8 -*-
# Name: AGG.py
# Description: statistical aggregations for hydro climatological series
# Requirements: Python 3+, pandas, tabulate, numpy
# SEAS: season, YR: year, TOTAL: average temperature, ANOM: anomaly value.


# Libraries
from datetime import datetime
from datetime import date
import requests
import os.path
import sys
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# General variables
station_file = 'Impute_MICE_Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv'  # Current IDEAM records file
station_path = 'D:/R.LTWB/.datasets/IDEAM_Impute/'  # Current IDEAM records path, use ../.datasets/IDEAM_Impute/ for relative path
ENSOONI_file = 'ONI_Eval_Consecutive.csv'
ENSOONI_path = 'D:/R.LTWB/.datasets/ENSOONI/'
path = 'D:/R.LTWB/.datasets/IDEAM_AGG/'  # Your local output files path, use ../.datasets/IDEAM_AGG/ for relative path
file_log_name = path + 'AGG.md'
file_log = open(file_log_name, 'w+')   # w+ create the file if it doesn't exist
date_record_name = 'Fecha'  # IDEAM date field name for the record values
plot_colormap = 'autumn'  # Color theme for plot graphics, https://matplotlib.org/stable/tutorials/colors/colormaps.html
sample_records = 3  # Records to show in the sample table head and tail
fig_size = 5  # Height size for figures plot
fig_alpha = 0.75  # Alpha transparency color in plots
show_plot = True
monthly_to_year_agg = 'sum'  # Aggregation function, E.G. sum for total monthly rain values, mean for average monthly flow values.


# Function for plot series
def plot_df(df, title='No assignment title', ylabel='Value', kind='line'):
    match kind:
        case 'line':
            ax = df.plot(colormap=plot_colormap, legend=False, alpha=1, figsize=(fig_size*2, fig_size+1), linewidth=0.5)
        case 'bar':
            ax = df.plot.bar(color='silver', legend=False, figsize=(fig_size*3, fig_size*1.75), width=0.8)
            plt.xticks(rotation=90, size=8)
    plt.title(title)
    ax.set_ylabel(ylabel)
    if show_plot: plt.show()
    plt.close('all')

# Function for monthly to year aggregations
def monthly_to_year_agg_func(df1):
    match monthly_to_year_agg:
        case 'sum':  # Typical for total monthly rain
            df_yearly_agg = df1.groupby(df1[date_record_name].dt.year).sum()
        case 'mean':  # Typical for average monthly flow
            df_yearly_agg = df1.groupby(df1[date_record_name].dt.year).mean()
    return df_yearly_agg


# Open the IDEAM station pivot dataframe and show general information
df = pd.read_csv(station_path + station_file, low_memory=False, parse_dates=[date_record_name])
#df = pd.read_csv(station_path + station_file, low_memory=False, parse_dates=[date_record_name], index_col=date_record_name)
ideam_regs = df.shape[0]
#df.reset_index(drop=True, inplace=True)
print('Records in stations file: %d' % ideam_regs)
#print(df)

# Composite aggregations for total monthly values
#print(df[date_record_name].dt.year)
#print(df.groupby(df[date_record_name].dt.year).agg(['sum', 'mean', 'max']).to_markdown())
print('\n## Composite - Yearly values per station from total monthly values (%s)\n' % monthly_to_year_agg)
df_yearly_agg = monthly_to_year_agg_func(df)
df_yearly_agg.index.name = 'Year'
print(df_yearly_agg.to_markdown())
plot_df(df_yearly_agg, 'Composite - Yearly values per station from total monthly values (%s)\n%s' % (monthly_to_year_agg, station_file), 'Values', kind='line')
print('\n### Composite - Aggregation value per station from yearly aggregations (mean)\n')
df_agg = df_yearly_agg.mean()
df_agg.index.name = 'Station'
df_agg.name = 'AggComposite'
print(df_agg.to_markdown())
plot_df(df_agg, 'Composite - Aggregation value per station from yearly aggregations (mean)\n%s' % station_file, 'Values', kind='bar')
print('\n### Composite - Monthly values per station from total monthly values (mean)\n')
df_monthly_sum = df.groupby(df[date_record_name].dt.month).mean()
df_monthly_sum.index.name = 'Month'
print(df_monthly_sum.to_markdown())
plot_df(df_monthly_sum, ' Composite - Monthly values per station from total monthly values (mean)\n%s' % station_file, 'Values', kind='line')
'''
print('\n### Composite - Aggregation value per station from monthly aggregations (sum)\n')
df_agg = df_monthly_sum.sum()
df_agg.index.name = 'Station'
df_agg.name = 'Agg'
print(df_agg.to_markdown())
plot_df(df_agg, 'Composite - Aggregation value per station from monthly aggregations (sum)\n%s' % station_file, 'Values', kind='bar')
'''


# Open the ENSO-ONI year classifier
print('\n## ENSO-ONI Events - Yearly values per station from total monthly values (%s)\n' % monthly_to_year_agg)
df_ensooni = pd.read_csv(ENSOONI_path + ENSOONI_file, low_memory=False, encoding='latin-1', index_col=False)
df_ensooni.index.name = 'Id'
enso_oni_regs = df_ensooni.shape[0]
#print(df_ensooni.to_markdown())
print('* Records in ENSO-ONI file: %d' % enso_oni_regs)
event_mark_unique = df_ensooni['EventMark'].unique()
print('* ENSO-ONI eventMark unique values: ' + str(event_mark_unique))
# Filter for Niña
for i in event_mark_unique:
    match int(i):
        case -1:
            df_ensooni_nina = df_ensooni[df_ensooni['EventMark'] == -1]
            print('\n### Niña events table (%d years)\n' % df_ensooni_nina.shape[0])
            print(df_ensooni_nina.to_markdown())
            df_ensooni_nina_unique = df_ensooni_nina['YR'].unique()
            df_yearly_agg = monthly_to_year_agg_func(df[df['Fecha'].dt.year.isin(df_ensooni_nina_unique)])
            df_yearly_agg.index.name = 'Year'
            print('\n Table aggregations (%s)\n' % monthly_to_year_agg)
            print(df_yearly_agg.to_markdown())
            plot_df(df_yearly_agg, 'Niña - Yearly values per station from total monthly values (%s)\n%s' % (monthly_to_year_agg, station_file), 'Values', kind='line')
            print('\nAggregation value per station from yearly aggregations (mean)\n')
            df_agg = df_yearly_agg.mean()
            df_agg.index.name = 'Station'
            df_agg.name = 'AggNina'
            print(df_agg.to_markdown())
        case 0:
            df_ensooni_neutral = df_ensooni[df_ensooni['EventMark'] == 0]
            print('\n### Neutral events table (%d years)\n' % df_ensooni_neutral.shape[0])
            print(df_ensooni_nina.to_markdown())
            df_ensooni_neutral_unique = df_ensooni_neutral['YR'].unique()
            df_yearly_agg = monthly_to_year_agg_func(df[df['Fecha'].dt.year.isin(df_ensooni_neutral_unique)])
            df_yearly_agg.index.name = 'Year'
            print('\n Table aggregations (%s)\n' % monthly_to_year_agg)
            print(df_yearly_agg.to_markdown())
            plot_df(df_yearly_agg, 'Neutral - Yearly values per station from total monthly values (%s)\n%s' % (monthly_to_year_agg, station_file), 'Values', kind='line')
            print('\nAggregation value per station from yearly aggregations (mean)\n')
            df_agg = df_yearly_agg.mean()
            df_agg.index.name = 'Station'
            df_agg.name = 'AggNeutral'
            print(df_agg.to_markdown())
        case 1:
            df_ensooni_nino = df_ensooni[df_ensooni['EventMark'] == 1]
            print('\n### Niño events table (%d years)\n' % df_ensooni_nino.shape[0])
            print(df_ensooni_nino.to_markdown())
            df_ensooni_nino_unique = df_ensooni_nino['YR'].unique()
            df_yearly_agg = monthly_to_year_agg_func(df[df['Fecha'].dt.year.isin(df_ensooni_nino_unique)])
            df_yearly_agg.index.name = 'Year'
            print('\n Table aggregations (%s)\n' % monthly_to_year_agg)
            print(df_yearly_agg.to_markdown())
            plot_df(df_yearly_agg, 'Niño - Yearly values per station from total monthly values (%s)\n%s' % (monthly_to_year_agg, station_file), 'Values', kind='line')
            print('\nAggregation value per station from yearly aggregations (mean)\n')
            df_agg = df_yearly_agg.mean()
            df_agg.index.name = 'Station'
            df_agg.name = 'AggNino'
            print(df_agg.to_markdown())





