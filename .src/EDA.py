# -*- coding: UTF-8 -*-
# Name: EDA.py
# Description:
# Requirements: Python 3+, pandas, rasterio, requests, tabulate
# Attention: do not convert the .csv file into an Excel file because you would need process more than 1048576 records.

# Libraries
import os.path
import sys
import pandas as pd
import shutil
import glob
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
path = 'D:/R.LTWB/Section03/EDA/'  # Your local .zip files path, use ../.datasets/CHIRPS/ for relative path
station_file_chirps = 'IDEAMJoinedChirps.csv'  # Output IDEAM records with the Chirps values
station_file_corr_date = 'IDEAMJoinedChirpsCorrelationDate.csv'  # Output IDEAM correlations with Chirps for each date
station_file_corr_date_mean = 'IDEAMJoinedChirpsCorrelationDateMean.csv'  # Output IDEAM correlations with Chirps - mean
station_file_corr_year = 'IDEAMJoinedChirpsCorrelationYear.csv'  # Output IDEAM correlations with Chirps for each year
station_file_corr_month = 'IDEAMJoinedChirpsCorrelationMonth.csv'  # Output IDEAM correlations with Chirps for each month
file_log_name = path + 'EDA.md'
file_log = open(file_log_name, 'w+')   # w+ create the file if it doesn't exist
url_server = 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_monthly/tifs/'
plot_raster = False  # Plot every geogrid
remove_temp_file_comp = True  # Remove all the compressed Chirps files downloaded after processing
remove_temp_file_geogrid = True  # Remove all the Chirps geogrid files after processing
remove_temp_file_csv = False  # Remove all .csv sliced files after processing
station_name = 'CodigoEstacion'  # IDEAM station code name
date_install_name = 'FechaInstalacion'  # IDEAM installation date field name
date_suspend_name = 'FechaSuspension'  # IDEAM suspension date field name
date_record_name = 'Fecha'  # IDEAM date field name for the record values
latitude_name = 'Latitud'  # IDEAM latitude name
longitude_name = 'Longitud'  # IDEAM longitude name
value_name = 'Valor'  # IDEAM value field name
grade_name = 'Grado' # IDEAM grade field name
approved_name = 'NivelAprobacion' # IDEAM approved level field name
tag_name = 'Etiqueta' # IDEAM record parameter frecuency tag
plot_colormap = 'tab20b'  # Color theme for plot graphics, https://matplotlib.org/stable/tutorials/colors/colormaps.html
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
          '\n* Créditos: r.cfdtools@gmail.com\n')

# Open the IDEAM station dataframe and show general information
# Learn more about the IDEAM file in https://github.com/rcfdtools/R.LTWB/tree/main/Section03/CNEStationDatasetDownload
station_df = pd.read_csv(station_file, low_memory=False, parse_dates=[date_install_name, date_suspend_name, date_record_name], converters={station_name: str, grade_name: str, approved_name: str})
print_log('\n### General dataframe information\n')
print(station_df.info())
print('\nStation records sample\n')
print(station_df)
ideam_regs = station_df.shape[0]

#print(station_df)
#df = station_df.groupby('CodigoEstacion')
#df = station_df.groupby('CodigoEstacion').mean()
#print('\n' + df.to_markdown())

# Slice data from each parameter and station
parameter_list = station_df[tag_name].unique()
print('\n\n## Processing each parameter from %d to %d for %d IDEAM records\n' %(year_start, year_end, ideam_regs))
for parameter in parameter_list:
    # General information per parameter
    parameter_name = tag_name + ' == "' + parameter + '"'  # Parameter filter
    station_df1 = station_df.query(parameter_name)  # Filter for parameter
    station_df1 = station_df1[(station_df[date_record_name] >= str(year_start) + '-01-01') & (station_df[date_record_name] <= str(year_end) + '-12-31')]  # Filter per date range
    ideam_regs_query = station_df1.shape[0]
    print_log('\n### Filtered records for %s: %i (%s%%)' % (parameter_name, ideam_regs_query, str(round((ideam_regs_query / ideam_regs) * 100, 2))))

    # Data analysis per station
    print('\n#### Processing data for each station\n')
    station_df1.set_index(date_record_name, inplace=True)
    station_list = station_df1[station_name].unique()
    for station in  station_list:
        filter = station_name + ' == "' + station + '"'
        df = station_df.query(filter)
        #print(df)
        print('Processing station: %s with %s records.' %(station, df.shape[0]))
        #print(df.describe().to_markdown())

    # Pivot table
    pivot_table = station_df1.pivot_table(index=date_record_name, columns=station_name, values=value_name)
    #print(pivot_table)
    pivot_table.to_csv(path + 'Pivot_' + parameter + '.csv')
    fig = pivot_table.plot(figsize=(10, 6), rot=90, colormap=plot_colormap, legend=False, alpha=0.25)
    plt.title('Graph series for %s with %d stations and %d records' % (parameter, len(station_list), ideam_regs_query))
    plt.savefig(path + 'Plot_' + parameter + '_TimeSerie.png')

# plt.show()
