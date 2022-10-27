# -*- coding: UTF-8 -*-
# Name: EDA.py
# Description:
# Requirements: Python 3+, pandas, rasterio, requests, tabulate
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


# General variables
station_file = 'D:/R.LTWB/.datasets/IDEAM/IDEAMJoined.csv'  # Current IDEAM records file
path = 'D:/R.LTWB/.datasets/IDEAM_EDA/'  # Your local .zip files path, use ../.datasets/CHIRPS/ for relative path
file_log_name = path + 'EDA.md'
file_log = open(file_log_name, 'w+')   # w+ create the file if it doesn't exist
station_name = 'CodigoEstacion'  # IDEAM station code name
date_install_name = 'FechaInstalacion'  # IDEAM installation date field name
date_suspend_name = 'FechaSuspension'  # IDEAM suspension date field name
date_record_name = 'Fecha'  # IDEAM date field name for the record values
latitude_name = 'Latitud'  # IDEAM latitude name ***********
longitude_name = 'Longitud'  # IDEAM longitude name ***********
value_name = 'Valor'  # IDEAM value field name
grade_name = 'Grado' # IDEAM grade field name
approved_name = 'NivelAprobacion' # IDEAM approved level field name
tag_name = 'Etiqueta' # IDEAM record parameter frecuency tag
plot_colormap = 'magma'  # Color theme for plot graphics, https://matplotlib.org/stable/tutorials/colors/colormaps.html
sample_records = 12
histogram_binds = 12
fig_size = 10
year_start = 1980  # Chirps values starts at 1981
year_end = 2021  # This value have to correspond with the end of the IDEAM series

# Header
print_log('## Exploración y análisis de series - EDA - Representación gráfica')
print_log('\n* Archivo de resultados: ' + file_log_name +
          '\n* Fecha y hora de inicio de ejecución: ' + str(datetime.now()) +
          '\n* Python versión: ' + str(sys.version) +
          '\n* Python rutas: ' + str(sys.path[0:5]) +
          '\n* matplotlib versión: ' + str(matplotlib.__version__) +
          '\n* Encuentra este script en https://github.com/rcfdtools/R.LTWB/tree/main/Section03/EDA'
          '\n* Cláusulas y condiciones de uso en https://github.com/rcfdtools/R.LTWB/blob/main/LICENSE.md'
          '\n* Créditos: r.cfdtools@gmail.com')

# Open the IDEAM station dataframe and show general information
# Learn more about the IDEAM file in https://github.com/rcfdtools/R.LTWB/tree/main/Section03/CNEStationDatasetDownload
station_df = pd.read_csv(station_file, low_memory=False, parse_dates=[date_install_name, date_suspend_name, date_record_name], converters={station_name: str, grade_name: str, approved_name: str})
ideam_regs = station_df.shape[0]
print_log('\n\n### General dataframe information with %d IDEAM records' % ideam_regs)
print(station_df.info())
print_log('\nStation records sample for head\n')
print_log(station_df.head(sample_records).to_markdown())
print_log('\nStation records sample for tail\n')
print_log(station_df.tail(sample_records).to_markdown())

# Slice data from each parameter and station
parameter_list = station_df[tag_name].unique()
for parameter in parameter_list:
    # General information per parameter
    parameter_name = tag_name + ' == "' + parameter + '"'  # Parameter filter
    station_df1 = station_df.query(parameter_name)  # Filter for parameter
    station_df1 = station_df1[(station_df[date_record_name] >= str(year_start) + '-01-01') & (station_df[date_record_name] <= str(year_end) + '-12-31')]  # Filter per date range
    ideam_regs_query = station_df1.shape[0]
    print_log('\n\n### Analysis from %d to %d for %s: %i (%s%%)' % (year_start, year_end, parameter_name, ideam_regs_query, str(round((ideam_regs_query / ideam_regs) * 100, 2))))

    # Data analysis per station
    station_df1.set_index(date_record_name, inplace=True)
    station_list = station_df1[station_name].unique()
    for station in station_list:
        filter = station_name + ' == "' + station + '"'
        df = station_df1.query(filter)
        #df.set_index(date_record_name, inplace=True) # Already indexed in station_df1
        #print(df)
        print_log('\n\n**%s - Station: %s (%s rec.)**' %(parameter, station, df.shape[0]))
        print_log('Statistics table', center_div=True)
        print_log(df[value_name].describe().to_markdown(), center_div=True)
        fig = df.plot(y=value_name, figsize=(fig_size, fig_size/2), rot=90, colormap=plot_colormap, legend=False, alpha=1, lw=1)
        fig.set_ylabel(value_name)
        plt.title('Time serie for %s - Station %s (%d records)' % (parameter, station, df.shape[0]), fontsize = 10)
        fig_name = 'Plot_' + parameter + '_' + station + '_TimeSerie.png'
        plt.savefig(path + 'Graph/' + fig_name)
        print_log('![R.LTWB](Graph/%s)' %fig_name, center_div=True)
        plt.close('all')
        fig = df.plot.hist(column=value_name, bins=histogram_binds, alpha=0.9, figsize=(fig_size/2, fig_size/2), colormap=plot_colormap, edgecolor='white', legend=False)
        plt.title('Histogram for %s - Station %s (%d records)' % (parameter, station, df.shape[0]), fontsize = 10)
        fig_name = 'Plot_' + parameter + '_' + station + '_Histogram.png'
        plt.savefig(path + 'Graph/' + fig_name)
        print_log('![R.LTWB](Graph/%s)' %fig_name, center_div=False)
        plt.close('all')  # After the fig is saved, close the fig release memory
        fig = df[value_name].plot.kde(colormap=plot_colormap, figsize=(fig_size/2, fig_size/2))
        plt.title('KDE density for %s - Station %s (%d rec.)' % (parameter, station, df.shape[0]), fontsize = 10)
        fig_name = 'Plot_' + parameter + '_' + station + '_DensityKDE.png'
        plt.savefig(path + 'Graph/' + fig_name)
        print_log('![R.LTWB](Graph/%s)' %fig_name, center_div=False)
        plt.close('all') # After the fig is saved, close the fig release memory

    # Pivot table & plot
    pivot_table = station_df1.pivot_table(index=date_record_name, columns=station_name, values=value_name)
    #print(pivot_table)
    pivot_table.to_csv(path + 'Pivot_' + parameter + '.csv')
    fig = pivot_table.plot(figsize=(fig_size, fig_size/2), rot=90, colormap=plot_colormap, legend=False, alpha=0.5, lw=1)
    fig.set_ylabel(value_name)
    plt.title('Time series for %s with %d stations (%d rec.)' % (parameter, len(station_list), ideam_regs_query), fontsize = 10)
    plt.savefig(path + 'Graph/Plot_' + parameter + '_TimeSerie.png')
    fig = pivot_table.plot.kde(colormap=plot_colormap, figsize=(fig_size, fig_size/2), legend=False)
    plt.title('KDE density for %s with %d stations (%d rec.)' % (parameter, len(station_list), ideam_regs_query), fontsize = 10)
    plt.savefig(path + 'Graph/Plot_' + parameter + '_DensityKDE.png')

# plt.show()
plt.close('all')
