# -*- coding: UTF-8 -*-
# Name: Agg.py
# Description: statistical aggregations for hydro-climatological series
# Requirements: Python 3+, pandas, tabulate


# Libraries
from datetime import datetime
import sys
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import tabulate  # required for print tables in Markdown using pandas


# General variables
station_file = 'Impute_MICE_Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv'  # Current IDEAM records file
station_path = 'D:/R.LTWB/.datasets/IDEAM_Impute/'  # Current IDEAM records path, use ../.datasets/IDEAM_Impute/ for relative path
ENSOONI_file = 'ONI_Eval_Consecutive.csv'
ENSOONI_path = 'D:/R.LTWB/.datasets/ENSOONI/'
path = 'D:/R.LTWB/.datasets/IDEAM_Agg/'  # Your local output files path, use ../.datasets/IDEAM_Agg/ for relative path
file_log_name = path + 'Agg_' + station_file + '.md'
file_log = open(file_log_name, 'w+')   # w+ create the file if it doesn't exist
date_record_name = 'Fecha'  # IDEAM date field name for the record values
plot_colormap = 'Spectral'  # Color theme for plot graphics (E.g. autumn), https://matplotlib.org/stable/tutorials/colors/colormaps.html
fig_size = 5  # Height size for figures plot
show_plot = False
df_agg_full = pd.DataFrame(columns=['Station'])  # Integrated dataframe aggregations values
df_agg_std_full = pd.DataFrame(columns=['Station'])  # Integrated dataframe aggregations standard deviationss
df_agg_zonal = pd.DataFrame(columns=['Month'])  # Integrated dataframe zonal aggregations
daily_serie = False  # The stations series contain daily values
agg_func = 'Sum'  # Aggregation function, E.G. 'Sum' for total monthly rain or evaporation values, 'Mean' for average monthly flow or max and min temperature values, 'Max' for PMax24hr from total daily rain.
unit = 'Rain, mm'  # 'Rain, mm' 'Min temperature, °C' 'Max temperature, °C' 'Flow, m³/s' 'Potential evaporation, mm'

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
def plot_df(df, title='No assignment title', kind='line', plt_save_name='xxxxx', legend=False):
    match kind:
        case 'line':
            ax = df.plot(colormap=plot_colormap, legend=legend, alpha=1, figsize=(fig_size*2, fig_size+1), linewidth=0.65)
        case 'bar':
            ax = df.plot.bar(colormap=plot_colormap, legend=legend, stacked=True, figsize=(fig_size*3, fig_size*1.75), width=0.8)
            plt.xticks(rotation=90, size=8)
    plt.title(title)
    ax.set_ylabel(unit + '\n' + station_file + '\n' + ENSOONI_file)
    if show_plot: plt.show()
    plt_name = plt_save_name + '_' + station_file + '.png'
    plt.savefig(path + 'Graph/' + plt_name, dpi=150)
    print_log('\n![R.LTWB](%s)' % ('Graph/' + plt_name), center_div=False)
    plt.close('all')

# Function for monthly to year aggregations
def monthly_to_yearly_agg_func(df1):
    df2 = df1
    df2 = df2.drop(columns=['Month'])
    match agg_func:
        case 'Sum':  # Typical for total monthly rain
            df_yearly_agg = df2.groupby('Year').sum()
        case 'Mean':  # Typical for average monthly flow
            df_yearly_agg = df2.groupby('Year').mean()
        case 'Max':  # Typical for PMax24hr from total daily rain
            df_yearly_agg = df2.groupby('Year').max()
        case 'Min':  # Typical for average monthly flow
            df_yearly_agg = df2.groupby('Year').min()
    return df_yearly_agg


# Open the IDEAM station pivot dataframe and show general information
df = pd.read_csv(station_path + station_file, low_memory=False, parse_dates=[date_record_name])
df[date_record_name] = pd.to_datetime(df[date_record_name], dayfirst=True)  #, format='%d/%m/%Y'
df['Year'] = df[date_record_name].dt.year
df['Month'] = df[date_record_name].dt.month
df = df.drop(columns=[date_record_name])


# Header
print_log('# Statistical aggregations for hydro-climatological composite series and yearly events Niño, Niña and Neutral')
print_log('\nFor further information about the NOAA - Oceanic Niño Index (ONI) classifier for climatological yearly events Niño, Niña and Neutral, check this activity https://github.com/rcfdtools/R.LTWB/tree/main/Section03/ENSOONI')
print_log('\n* Station records file: [%s](%s)' % (str(station_file), '../IDEAM_Impute/' + station_file) +
          '\n* ENSO-ONI year file: [%s](%s)' % (str(ENSOONI_file), '../ENSOONI/' + ENSOONI_file) +
          '\n* Stations: %d' % (df.shape[1] - 1) +
          '\n* Records: %d' % df.shape[0] +
          '\n* Daily serie: %s' % daily_serie +
          '\n* Aggregation function: %s' % agg_func +
          '\n* Execution date: ' + str(datetime.now()) +
          '\n* Python version: ' + str(sys.version) +
          '\n* Python path: ' + str(sys.path[0:5]) +
          '\n* matplotlib version: ' + str(matplotlib.__version__) +
          '\n* pandas version: ' + str(pd.__version__) +
          '\n* Instructions & script: https://github.com/rcfdtools/R.LTWB/tree/main/Section03/Agg'
          '\n* License: https://github.com/rcfdtools/R.LTWB/blob/main/LICENSE.md'
          '\n* Credits: r.cfdtools@gmail.com')


# Aggregations from daily to monthly values
if daily_serie:
    match agg_func:
        case 'Sum':  # Typical for total daily rain
            df = df.groupby([df['Year'], df['Month']]).sum()
        case 'Mean':  # Typical for average daily flow, daily temperature
            df = df.groupby([df['Year'], df['Month']]).mean()
    df.to_csv(path + 'Agg_YM_' + station_file)  # YM means yearly and monthly
    df = pd.read_csv(path + 'Agg_YM_' + station_file, low_memory=False)

# Composite aggregations for monthly values
print_log('\n\n## Composite - Yearly values per station from monthly values (%s)\n' % agg_func)
if daily_serie:
    print_log('Daily values to year-month aggregation (%s) file: [%s](%s)\n' % (agg_func, 'Agg_YM_' + station_file, 'Agg_YM_' + station_file ))
df_yearly_agg = monthly_to_yearly_agg_func(df)
df_yearly_agg.index.name = 'Year'
print_log(df_yearly_agg.to_markdown())
plot_df(df_yearly_agg, title='Composite - Yearly values per station from monthly values (%s)\n' % agg_func, kind='line', plt_save_name='AggComposite_Yearly_%s' % agg_func)
print_log('\nComposite - Aggregation value per station from yearly aggregations (mean)\n')
df_agg = df_yearly_agg.mean()  # Results as list
df_agg.index.name = 'Station'
df_agg.name = 'AggComposite'
df_agg = df_agg.to_frame()  # List to frame
print_log(df_agg.T.to_markdown())
print_log('\nComposite - Aggregation value per station from yearly aggregations (std - standard deviation)\n')
df_agg_std = df_yearly_agg.std()  # Results as list
df_agg_std.index.name = 'Station'
df_agg_std.name = 'StdAggComposite'
df_agg_std = df_agg_std.to_frame()  # List to frame
print_log(df_agg_std.T.to_markdown())
plot_df(df_agg, title='Composite - Aggregation value per station from yearly aggregations (mean)\n', kind='bar', plt_save_name='AggComposite_Station_Mean')
print_log('\nComposite - Monthly values per station (mean)\n')
df_monthly_val = df.groupby('Month').mean()
df_monthly_val = df_monthly_val.drop(columns=['Year'])
print_log(df_monthly_val.to_markdown())
plot_df(df_monthly_val, title='Composite - Monthly values per station (mean)\n', kind='line', plt_save_name='AggComposite_Monthly_Mean')
print_log('\nComposite - Zonal monthly values (mean)\n', center_div=True)
df_monthly_zonal = df_monthly_val.mean(axis=1)
#df_monthly_zonal = df_monthly_val.mean(axis=0)
df_monthly_zonal.name = 'AggCompositeZonal'
df_monthly_zonal = df_monthly_zonal.to_frame()
print_log(df_monthly_zonal.to_markdown(), center_div=True)
df_agg_full = df_agg
df_agg_std_full = df_agg_std
df_agg_zonal = df_monthly_zonal


# Aggregation values with the ENSO-ONI year classifier
print_log('\n## ENSO-ONI Events - Yearly values per station from monthly values (%s)\n' % agg_func)
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
    df_yearly_agg = monthly_to_yearly_agg_func(df[df['Year'].isin(df_ensooni_unique)])
    df_yearly_agg.index.name = 'Year'
    print_log('\n%s - Table aggregations (%s)\n' % (ensooni_tag, agg_func))
    print_log(df_yearly_agg.to_markdown())
    plot_df(df_yearly_agg, title='%s - Yearly values per station from monthly values (%s)\n' % (ensooni_tag, agg_func), kind='line', plt_save_name='%s_Yearly_%s' % (agg_name,agg_func))
    print_log('\n%s - Aggregation value per station from yearly aggregations (mean)\n' % ensooni_tag)
    df_agg = df_yearly_agg.mean()  # Results as list
    df_agg.index.name = 'Station'
    df_agg.name = agg_name
    df_agg = df_agg.to_frame()  # List to frame
    print_log(df_agg.T.to_markdown())
    print_log('\n%s - Aggregation value per station from yearly aggregations (std - standard deviation)\n' % ensooni_tag)
    df_agg_std = df_yearly_agg.std()  # Results as list
    df_agg_std.index.name = 'Station'
    df_agg_std.name = 'Std' + agg_name
    df_agg_std = df_agg_std.to_frame()  # List to frame
    print_log(df_agg_std.T.to_markdown())
    plot_df(df_agg, title='%s - Aggregation value per station from yearly aggregations (mean)\n' % ensooni_tag, kind='bar', plt_save_name='%s_Station_Mean' % agg_name)
    print_log('\n%s - Monthly values per station (mean)\n' % ensooni_tag)
    df_monthly_filter = df[df['Year'].isin(df_ensooni_unique)]
    df_monthly_filter = df_monthly_filter.drop(columns=['Year'])
    df_monthly_val = df_monthly_filter.groupby('Month').mean()
    df_monthly_val.index.name = 'Month'
    print_log(df_monthly_val.to_markdown())
    plot_df(df_monthly_val, title='%s - Monthly values per station (mean)\n' % ensooni_tag, kind='line', plt_save_name='%s_Monthly_Mean' % agg_name)
    df_agg_full = pd.concat([df_agg_full, df_agg], axis=1)
    df_agg_std_full = pd.concat([df_agg_std_full, df_agg_std], axis=1)
    print_log('\n%s - Zonal monthly values (mean)\n' % ensooni_tag, center_div=True)
    df_monthly_zonal = df_monthly_val.mean(axis=1)
    df_monthly_zonal.name = agg_name + 'Zonal'
    df_monthly_zonal = df_monthly_zonal.to_frame()
    print_log(df_monthly_zonal.to_markdown(), center_div=True)
    df_agg_zonal = pd.concat([df_agg_zonal, df_monthly_zonal], axis=1)


# Yearly aggregation matrix
df_agg_full.to_csv(path + 'Agg_' + station_file)
df_agg_std_full.to_csv(path + 'Agg_Std_' + station_file)
print_log('\n\n## Yearly aggregation matrix values per station from yearly values (mean) and zonal monthly values (mean)\n')
print_log('\nYearly matrix values per station (required for spatial interpolations)<br>File: [%s](%s)\n' % ('Agg_' + station_file, 'Agg_' + station_file), center_div=True)
print_log(df_agg_full.to_markdown(), center_div=True)
print_log('\nYearly matrix standard deviations per station<br>File: [%s](%s)\n' % ('Agg_Std_' + station_file, 'Agg_Std_' + station_file), center_div=True)
print_log(df_agg_std_full.to_markdown(), center_div=True)
plot_df(df_agg_full, title='Aggregation value matrix stacked per station from yearly aggregations (mean)\n', kind='bar', plt_save_name='AggMatrix_Yearly_Mean', legend=True)
print_log('\nMonthly zonal values\n', center_div=True)
print_log(df_agg_zonal.to_markdown(), center_div=True)
plot_df(df_agg_zonal, title='Zonal aggregation values per month (mean)\n', kind='line', plt_save_name='AggZonal_Monthly_Mean', legend=True)
