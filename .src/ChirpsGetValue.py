# -*- coding: UTF-8 -*-
# Name: ChirpsGetValue.py
# Description: this script downloads the Chirps monthly rain geogrids and identify the specific values in the IDEAM - Colombia monthly stations series for calculate their correlations.
# Repository: https://github.com/rcfdtools/R.LTWB/tree/main/Section03/xxxxx
# License: https://github.com/rcfdtools/R.LTWB/wiki/License
# Requirements: Python 3+, pandas, rasterio, requests
# Attention: do not convert the .csv file into an Excel file because you would need process more than 1048576 records.

# Libraries
import os.path
import requests
import rasterio
from rasterio.plot import show
import pandas as pd
import gzip
import shutil
import glob
import matplotlib.pyplot as plt

# Function for get the raster value in a specific coordinate
def chirps_value(raster_file, longitude, latitude):
    raster = rasterio.open(path + raster_file)
    row, col = raster.index(longitude, latitude)
    return raster.read(1)[row, col]

# General variables
station_file = 'D:/R.LTWB/.datasets/IDEAM/IDEAMJoined.csv' # Current IDEAM records file
station_file_chirps = 'IDEAMJoinedChirps.csv' # Output IDEAM records with the Chirps values
path = 'D:/R.LTWB/.datasets/CHIRPS/' # Your local .zip files path, use ../.datasets/CHIRPS/ for relative path
url_server = 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_monthly/tifs/'
plot_raster = False # Plot every geogrid
remove_temp_file_comp = True # Remove all the compressed Chirps files downloaded after processing
remove_temp_file_geogrid = True # Remove all the Chirps geogrid files after processing
remove_temp_file_csv = False # Remove all .csv sliced files after processing
date_install = 'FechaInstalacion' # IDEAM installation date field name
date_suspend = 'FechaSuspension' # IDEAM suspension date field name
date_record = 'Fecha' # IDEAM date field name for the record values
parameter_name = 'Etiqueta == "PTPM_TT_M"' # IDEAM field name and specific monthly rain tag
latitude_name = 'Latitud' # IDEAM latitude name
longitude_name = 'Longitud' # IDEAM longitude name
value_name = 'Valor' # IDEAM value field name
geogrid_extension = '.tif'
compress_format = '.gz'
year_start = 1981 # Chirps values starts at 1981
year_end = 2021 # This value have to correspond with the end of the IDEAM series

# Open the IDEAM station dataframe and show general information
# Learn more about the IDEAM file in https://github.com/rcfdtools/R.LTWB/tree/main/Section03/CNEStationDatasetDownload
station_df = pd.read_csv(station_file, low_memory=False, parse_dates=[date_install, date_suspend, date_record])
print('\nGeneral dataframe information ')
print(station_df.info())
print('\nStation records sample')
print(station_df)
station_df = station_df.query(parameter_name) # Filter for the monthly rain values
print('\nFiltered records for %s: %s' %(parameter_name, str(station_df.shape[0])))

# Processing Chirps values per year and month
print('\nProcessing Chrips values per year and month')
cols = ['datetime', 'Year', 'Month', 'Pearson', 'Kendall', 'Spearman']
correlation_df = pd.DataFrame(columns = cols)
for year in range(year_start, year_end+1, 1):
    for month in range (12):
        year_month = str(year).zfill(4) + '-' + str(month+1).zfill(2)
        date = year_month + '-01'
        chirps_file = 'chirps-v2.0.' + str(year).zfill(4) + '.' + str(month+1).zfill(2)
        url_file = url_server + chirps_file + geogrid_extension + compress_format
        compress_file = path + chirps_file + geogrid_extension + compress_format
        print('\nProcessing geogrid %s from %s' %(year_month, url_file))
        # Request the compress geogrid Chirps file if the processed sliced .csv doesn't exist
        if os.path.isfile(compress_file) == False and os.path.isfile(path + chirps_file + '.csv') == False:
            print('Saving compressed file as %s' %compress_file)
            file_request = requests.get(url_file)
            if file_request:
                open(compress_file, 'wb').write(file_request.content)
        else:
            print('Compressed file %s is already in the directory.' %compress_file)
        # Uncompress the Chirps file if the geodrid and the processed sliced .csv doesn't exist
        if os.path.isfile(path + chirps_file + geogrid_extension) == False and os.path.isfile(path + chirps_file + '.csv') == False:
            with gzip.open(compress_file, 'rb') as f_in:
                with open(path + chirps_file + geogrid_extension, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
                    print('Uncompressing geogrid as %s' %(path + chirps_file + geogrid_extension))
        else:
            print('Geogrid %s is already in the directory.' %(path + chirps_file + geogrid_extension))
        # Plot raster in screen if the geogrid file still
        if plot_raster and remove_temp_file_geogrid == False:
            raster = rasterio.open(path + chirps_file + geogrid_extension)
            #print(raster.crs) # Print coordinate reference system - CRS
            #print(raster.count) # Print number of bands
            show(raster) # Plot the raster file
        # Slice the IDEAM file per year and month and get the Chirps values
        if os.path.isfile(path + chirps_file + '.csv') == False:
            station_df_filter = station_df[station_df['Fecha'].dt.strftime('%Y-%m') == year_month]
            stations = station_df_filter.shape[0]
            print('Slicing .csv serie for %s with %d records' %(year_month, stations))
            station_df_filter['SatValue'] = chirps_value(chirps_file + geogrid_extension, station_df_filter[longitude_name], station_df_filter[latitude_name])
            station_df_filter['SatDesc'] = chirps_file + geogrid_extension
            station_df_filter.to_csv(path + chirps_file + '.csv')
        else:
            print('Sliced .csv serie %s with Chirps values is already in the directory.' % (path + chirps_file + '.csv'))
        # Correlation analysis
        print('Correlation analysis')
        df = pd.read_csv(path + chirps_file + '.csv', low_memory=False)
        correlation_pearson = df[value_name].corr(df['SatValue'], method='pearson')
        print('[Pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient): %f' %correlation_pearson)
        correlation_kendall = df[value_name].corr(df['SatValue'], method='kendall')
        print('[Kendall rank correlation coefficient](https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient): %f' %correlation_kendall)
        correlation_spearman = df[value_name].corr(df['SatValue'], method='spearman')
        print('[Spearman’s rank correlation coefficient](https://en.wikipedia.org/wiki/Spearman%%27s_rank_correlation_coefficient): %f' %correlation_spearman)
        df2 = pd.DataFrame([[pd.to_datetime(date, format=('%Y/%m/%d')), year, month + 1, correlation_pearson, correlation_kendall, correlation_spearman]], columns = cols)
        #correlation_df = pd.concat([correlation_df, df2], ignore_index = True)
        correlation_df = pd.concat([correlation_df, df2])
# Join .csv files and plot
csv_files = glob.glob(path + 'chirps-v2.0.*.csv')
df = pd.concat(map(pd.read_csv, csv_files), ignore_index=True)
df.to_csv(path + station_file_chirps, encoding='utf-8', index=False)
df = pd.read_csv(path + station_file_chirps, low_memory=False)
fig = df.plot.scatter(x=value_name, y='SatValue', alpha=0.5, figsize=(6, 6))
plt.title('IDEAM vs. CHIRPS - Scatter plot')
fig.figure.savefig(path + 'PlotScatterIdeamChirps.png')
plt.show()
fig = df.boxplot(column=[value_name, 'SatValue'], figsize=(6, 6), grid=False)
plt.title('IDEAM & CHIRPS - Boxplot')
fig.figure.savefig(path + 'PlotIdeamChirpsBoxplot.png')
plt.show()
# Correlation plot
correlation_df.set_index('datetime', inplace = True)
print('\nCorrelation values time series')
print(correlation_df.info())
print(correlation_df)
print('\nAverage correlation values per method')
print(correlation_df.iloc[:, [2, 3, 4]].mean(axis=0)) # iloc for get only the required attributes
fig = correlation_df.iloc[:, [2, 3, 4]].plot(figsize=(10, 6), rot=90)
plt.title('IDEAM vs. CHIRPS - Monthly correlations')
fig.figure.savefig(path + 'PlotMonthlyCorrelationTimeSerie.png')
correlation_df.iloc[:, [2, 3, 4]].plot.box(figsize=(6, 6))
fig = plt.title('IDEAM vs. CHIRPS - Correlations boxplot')
fig.figure.savefig(path + 'PlotMonthlyCorrelationBoxplot.png')
plt.show()
# Remove temporal files
if remove_temp_file_comp:
    chirps_files = glob.glob(path + 'chirps-v2.0.*.gz')
    for chirps_file in chirps_files:
        os.remove(chirps_file)
if remove_temp_file_geogrid:
    geogrid_files = glob.glob(path + 'chirps-v2.0.*.tif')
    for geogrid_file in geogrid_files:
        os.remove(geogrid_file)
if remove_temp_file_csv: # csv glob.glob created before
    for csv_file in csv_files:
        os.remove(csv_file)
print('\nProcess accomplished, check the results file: %s' %(path + station_file_chirps))
