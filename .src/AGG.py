# -*- coding: UTF-8 -*-
# Name: AGG.py
# Description: statistical aggregations for hydro-climatological series
# Requirements: Python 3+, pandas, tabulate, numpy
# SEAS: season, YR: year, TOTAL: average temperature, ANOM: anomaly value.


# Libraries
from datetime import datetime
from datetime import date
import os.path
import sys
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import tabulate  # required for print tables in Markdown using pandas


# General variables
station_file = 'Impute_MICE_Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv'  # Current IDEAM records file
station_path = 'D:/R.LTWB/.datasets/IDEAM_Impute/'  # Current IDEAM records path, use ../.datasets/IDEAM_Impute/ for relative path
ENSOONI_file = 'ONI_Eval_Consecutive.csv'
ENSOONI_path = 'D:/R.LTWB/.datasets/ENSOONI/'
path = 'D:/R.LTWB/.datasets/IDEAM_AGG/'  # Your local output files path, use ../.datasets/IDEAM_AGG/ for relative path
file_log_name = path + 'AGG_' + station_file + '.md'
file_log = open(file_log_name, 'w+')   # w+ create the file if it doesn't exist
date_record_name = 'Fecha'  # IDEAM date field name for the record values
plot_colormap = 'Spectral'  # Color theme for plot graphics (E.g. autumn), https://matplotlib.org/stable/tutorials/colors/colormaps.html
fig_size = 5  # Height size for figures plot
fig_alpha = 0.75  # Alpha transparency color in plots
show_plot = False
df_agg_full = pd.DataFrame(columns=['Station'])  # Integrated dataframe aggregations
df_agg_zonal = pd.DataFrame(columns=['Month'])  # Integrated dataframe zonal aggregations
daily_serie = True  # The stations series contain daily values
monthly_to_year_agg = 'Sum'  # Aggregation function, E.G. Sum for total monthly rain values, Mean for average monthly flow values.


# Function for print and show results in a file
def print_log(txt_print, on_screen=True, center_div=False):
    if on_screen:
        print(txt_print)
    if center_div:
        file_log.write('\n<div align="center">\n' + '\n')
    file_log.write(txt_print + '\n')
    if center_div:
        file_log.write('\n</div>\n' + '\n')

# Function for plot series
def plot_df(df, title='No assignment title', ylabel='Value', kind='line', plt_save_name='xxxxx', legend=False):
    match kind:
        case 'line':
            ax = df.plot(colormap=plot_colormap, legend=legend, alpha=1, figsize=(fig_size*2, fig_size+1), linewidth=0.5)
        case 'bar':
            ax = df.plot.bar(colormap=plot_colormap, legend=legend, stacked=True, figsize=(fig_size*3, fig_size*1.75), width=0.8)
            plt.xticks(rotation=90, size=8)
    plt.title(title)
    ax.set_ylabel(ylabel + '\n' + station_file + '\n' + ENSOONI_file)
    if show_plot: plt.show()
    plt_name = plt_save_name + '_' + station_file + '.png'
    plt.savefig(path + 'Graph/' + plt_name, dpi=150)
    print_log('\n![R.LTWB](%s)' % ('Graph/' + plt_name), center_div=False)
    plt.close('all')

# Function for monthly to year aggregations
def monthly_to_year_agg_func(df1):
    match monthly_to_year_agg:
        case 'Sum':  # Typical for total monthly rain
            df_yearly_agg = df1.groupby(df1[date_record_name].dt.year).sum()
        case 'Mean':  # Typical for average monthly flow
            df_yearly_agg = df1.groupby(df1[date_record_name].dt.year).mean()
    return df_yearly_agg


# Open the IDEAM station pivot dataframe and show general information
df = pd.read_csv(station_path + station_file, low_memory=False, parse_dates=[date_record_name])
ideam_regs = df.shape[0]


# Header
print_log('# Statistical aggregations for hydro-climatological composite series and yearly events Niño, Niña and Neutral')
print_log('\nFor further information about the NOAA - Oceanic Niño Index (ONI) classifier for climatological yearly events Niño, Niña and Neutral, check this activitie https://github.com/rcfdtools/R.LTWB/tree/main/Section03/ENSOONI')
print_log('\n* Station records file: [%s](%s)' % (str(station_file), '../IDEAM_Impute/' + station_file) +
          '\n* ENSO-ONI year file: [%s](%s)' % (str(ENSOONI_file), '../ENSOONI/' + ENSOONI_file) +
          '\n* Records in station file: %d' % ideam_regs +
          '\n* Daily serie: %s' % daily_serie +
          '\n* Aggregation function: %s' % monthly_to_year_agg +
          '\n* Execution date: ' + str(datetime.now()) +
          '\n* Python version: ' + str(sys.version) +
          '\n* Python path: ' + str(sys.path[0:5]) +
          '\n* matplotlib version: ' + str(matplotlib.__version__) +
          '\n* pandas version: ' + str(pd.__version__) +
          '\n* Instructions & script: https://github.com/rcfdtools/R.LTWB/tree/main/Section03/AGG'
          '\n* License: https://github.com/rcfdtools/R.LTWB/blob/main/LICENSE.md'
          '\n* Credits: r.cfdtools@gmail.com')


# Aggregations from daily to monthly values
if daily_serie:
    #print_log('\n\n## Daily values to monthly aggregation (%s)\n' % monthly_to_year_agg)
    match monthly_to_year_agg:
        case 'Sum':  # Typical for total daily rain
            df = df.groupby([df[date_record_name].dt.year, df[date_record_name].dt.month]).sum()
        case 'Mean':  # Typical for average daily flow, daily temperature
            df = df.groupby([df[date_record_name].dt.year, df[date_record_name].dt.month]).mean()
    df.index.name = 'Group'
    df['Aux'] = df.index
    df[date_record_name] = df.Aux.str[0].astype(str) + '-' + df.Aux.str[1].astype(str) + '-01'
    df[date_record_name] = df[date_record_name].astype('datetime64[ns]')
    df = df.drop(['Aux'], axis=1)
    df = df.reset_index(drop=True)
    df.index.name = 'Id'
    df.insert(0, date_record_name, df.pop(date_record_name))
    #print_log(df.to_markdown())


# Composite aggregations for monthly values
#print_log(df[date_record_name].dt.year)
#print_log(df.groupby(df[date_record_name].dt.year).agg(['sum', 'mean', 'max']).to_markdown())
print_log('\n## Composite - Yearly values per station from monthly values (%s)\n' % monthly_to_year_agg)
df_yearly_agg = monthly_to_year_agg_func(df)
df_yearly_agg.index.name = 'Year'
print_log(df_yearly_agg.to_markdown())
plot_df(df_yearly_agg, 'Composite - Yearly values per station from monthly values (%s)\n' % monthly_to_year_agg, 'Values', kind='line', plt_save_name='AggComposite_Yearly_%s' % monthly_to_year_agg)
print_log('\nComposite - Aggregation value per station from yearly aggregations (mean)\n')
df_agg = df_yearly_agg.mean()  # Results as list
df_agg.index.name = 'Station'
df_agg.name = 'AggComposite'
df_agg = df_agg.to_frame()  # List to frame
print_log(df_agg.T.to_markdown())
plot_df(df_agg, 'Composite - Aggregation value per station from yearly aggregations (mean)\n', 'Values', kind='bar', plt_save_name='AggComposite_Yearly_Mean')
print_log('\nComposite - Monthly values per station (mean)\n')
df_monthly_val = df.groupby(df[date_record_name].dt.month).mean()
df_monthly_val.index.name = 'Month'
print_log(df_monthly_val.to_markdown())
plot_df(df_monthly_val, 'Composite - Monthly values per station (mean)\n', 'Values', kind='line', plt_save_name='AggComposite_Monthly_Mean')
print_log('\nComposite - Zonal monthly values (mean)\n', center_div=True)
df_monthly_zonal = df_monthly_val.mean(axis=1)
df_monthly_zonal.name = 'AggCompositeZonal'
df_monthly_zonal = df_monthly_zonal.to_frame()
print_log(df_monthly_zonal.to_markdown(), center_div=True)
df_agg_full = df_agg
df_agg_zonal = df_monthly_zonal
#print_log('\n### Composite - Aggregation value per station from monthly aggregations (sum)\n')
#df_agg = df_monthly_val.sum()
#df_agg.index.name = 'Station'
#df_agg.name = 'Agg'
#print_log(df_agg.to_markdown())
#plot_df(df_agg, 'Composite - Aggregation value per station from monthly aggregations (sum)\n', 'Values', kind='bar')



# Aggregation values with the ENSO-ONI year classifier
print_log('\n## ENSO-ONI Events - Yearly values per station from monthly values (%s)\n' % monthly_to_year_agg)
df_ensooni = pd.read_csv(ENSOONI_path + ENSOONI_file, low_memory=False, encoding='latin-1', index_col=False)
df_ensooni.index.name = 'Id'
enso_oni_regs = df_ensooni.shape[0]
#print_log(df_ensooni.to_markdown())
print_log('* Records in ENSO-ONI file: %d' % enso_oni_regs)
event_mark_unique = df_ensooni['EventMark'].unique()
print_log('* ENSO-ONI eventMark unique values: ' + str(event_mark_unique))
#for i in event_mark_unique:
for i in (-1, 1, 0):
    match int(i):
        case -1:
            ensooni_tag = 'Niña'
            agg_name = 'AggNina'
        case 0:
            ensooni_tag = 'Neutral'
            agg_name = 'AggNeutral'
        case 1:
            ensooni_tag = 'Niño'
            agg_name = 'AggNino'
    df_ensooni_eval = df_ensooni[df_ensooni['EventMark'] == i]
    print_log('\n### %s events analysis (%d years identified)\n' % (ensooni_tag, df_ensooni_eval.shape[0]))
    print_log(df_ensooni_eval.to_markdown(), center_div=True)
    df_ensooni_unique = df_ensooni_eval['YR'].unique()
    df_yearly_agg = monthly_to_year_agg_func(df[df[date_record_name].dt.year.isin(df_ensooni_unique)])
    df_yearly_agg.index.name = 'Year'
    print_log('\n%s - Table aggregations (%s)\n' % (ensooni_tag, monthly_to_year_agg))
    print_log(df_yearly_agg.to_markdown())
    plot_df(df_yearly_agg, '%s - Yearly values per station from monthly values (%s)\n' % (ensooni_tag, monthly_to_year_agg), 'Values', kind='line', plt_save_name='%s_Yearly_%s' % (agg_name,monthly_to_year_agg))
    print_log('\n%s - Aggregation value per station from yearly aggregations (mean)\n' % ensooni_tag)
    df_agg = df_yearly_agg.mean()  # Results as list
    df_agg.index.name = 'Station'
    df_agg.name = agg_name
    df_agg = df_agg.to_frame()  # List to frame
    print_log(df_agg.T.to_markdown())
    plot_df(df_agg, '%s - Aggregation value per station from yearly aggregations (mean)\n' % ensooni_tag, 'Values', kind='bar', plt_save_name='%s_Yearly_Mean' % agg_name)
    print_log('\n%s - Monthly values per station (mean)\n' % ensooni_tag)
    df_monthly_filter = df[df[date_record_name].dt.year.isin(df_ensooni_unique)]
    df_monthly_val = df.groupby(df_monthly_filter[date_record_name].dt.month).mean()
    df_monthly_val.index.name = 'Month'
    print_log(df_monthly_val.to_markdown())
    plot_df(df_monthly_val,'%s - Monthly values per station (mean)\n' % ensooni_tag, 'Values', kind='line', plt_save_name='%s_Monthly_Mean' % agg_name)
    df_agg_full = pd.concat([df_agg_full, df_agg], axis=1)
    print_log('\n%s - Zonal monthly values (mean)\n' % ensooni_tag, center_div=True)
    df_monthly_zonal = df_monthly_val.mean(axis=1)
    df_monthly_zonal.name = agg_name + 'Zonal'
    df_monthly_zonal = df_monthly_zonal.to_frame()
    print_log(df_monthly_zonal.to_markdown(), center_div=True)
    df_agg_zonal = pd.concat([df_agg_zonal, df_monthly_zonal], axis=1)


# Yearly aggregation matrix
print_log('\n\n## Yearly aggregation matrix values per station from yearly values (mean) and zonal monthly values (mean)\n')
print_log('\nYearly matrix values per station (required for spatial interpolations) \n', center_div=True)
print_log(df_agg_full.to_markdown(), center_div=True)
plot_df(df_agg_full, 'Aggregation value matrix stacked per station from yearly aggregations (mean)\n', 'Values', kind='bar', plt_save_name='AggMatrix_Yearly_Mean', legend=True)
print_log('\nMonthly zonal values\n', center_div=True)
print_log(df_agg_zonal.to_markdown(), center_div=True)
plot_df(df_agg_zonal, 'Zonal aggregation values per month (mean)\n', 'Values', kind='line', plt_save_name='AggZonal_Monthly_Mean', legend=True)
