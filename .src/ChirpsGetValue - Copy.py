# -*- coding: UTF-8 -*-
# Do not convert the .csv file into an Excel file because you would be process more than 1048576 records.

# Libraries
import os.path
import requests
import rasterio
from rasterio.plot import show
import pandas as pd
import matplotlib.pyplot as plt
import gzip
import shutil
import glob

# Function for get the raster value in a specific coordinate
def chirps_value(raster_file, longitude, latitude):
    raster = rasterio.open(path + raster_file)
    row, col = raster.index(longitude, latitude)
    return raster.read(1)[row, col]

# General variables
path = 'C:/temp/ChirpsTest/' # Your local .zip files path, use ../.datasets/IDEAM/ for relative path
url_server = 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_monthly/tifs/'
plot_raster = False
latitude_name = 'Latitud'
longitude_name = 'Longitud'
grid_extension = '.tif'
compress_format = '.gz'
station_file = 'IDEAMJoined.csv'
station_file_chirps = 'IDEAMJoinedChirps.csv'
year_start = 1981
year_end = 2021

# Open the station dataframe and show general information
station_df = pd.read_csv(path+station_file, low_memory=False, parse_dates=['FechaInstalacion', 'FechaSuspension', 'Fecha'])
#station_df = pd.read_excel(path+station_file, index_col='Fecha')
print('\nGeneral dataframe information: ')
print(station_df.info())
print('\nStation records sample')
print('\n', station_df)
station_df = station_df.query('Etiqueta == "PTPM_TT_M"') # Filter for rain values
print('\nFiltered records for PTPM_TT_M: %s' %(str(station_df.shape[0])))

# Processing values per year and month
print('\nProcessing values per year and month')
for year in range(year_start, year_end+1, 1):
    for month in range (12): # 12 months
        year_month = str(year).zfill(4) + '-' + str(month+1).zfill(2)
        chirps_file = 'chirps-v2.0.' + str(year).zfill(4) + '.' + str(month+1).zfill(2)
        url_file = url_server + chirps_file + grid_extension + compress_format
        compress_file = path + chirps_file + grid_extension + compress_format
        print('Getting %s' %url_file)
        print('Saving as %s' %compress_file)
        file_request = requests.get(url_file)
        if file_request:
            if os.path.isfile(compress_file) == False:
                open(compress_file, 'wb').write(file_request.content)
        if os.path.isfile(path + chirps_file + grid_extension) == False:
            with gzip.open(compress_file, 'rb') as f_in:
                with open(path + chirps_file + grid_extension, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
        if plot_raster:
            raster = rasterio.open(path + chirps_file + grid_extension)
            #print(raster.crs) # Print coordinate reference system - CRS
            #print(raster.count) # Print number of bands
            show(raster) # Plot the raster file
        if os.path.isfile(path + chirps_file + '.csv') == False:
            station_df_filter = station_df[station_df['Fecha'].dt.strftime('%Y-%m') == year_month]
            stations = station_df_filter.shape[0]
            print('Processing: %s with %s records' %(year_month, str(stations) ))
            station_df_filter['SatValue'] = chirps_value(chirps_file + grid_extension, station_df_filter[longitude_name], station_df_filter[latitude_name])
            station_df_filter['SatDesc'] = chirps_file + grid_extension
            station_df_filter.to_csv(path + chirps_file + '.csv')
# Join .csv files
csv_files = glob.glob(path + 'chirps-v2.0.*.csv')
df = pd.concat(map(pd.read_csv, csv_files), ignore_index=True)
df.to_csv(path + station_file_chirps, encoding='utf-8', index=False)
print('\nProcess accomplished, check the file: %s' %(path + station_file_chirps))

# References
# https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_monthly/tifs/
# https://hatarilabs.com/ih-en/extract-point-value-from-a-raster-file-with-python-geopandas-and-rasterio-tutorial
# https://www.youtube.com/watch?v=6zzneGT4mkg
# https://sparkbyexamples.com/pandas/pandas-dataframe-filter/
# https://towardsdatascience.com/8-ways-to-filter-pandas-dataframes-d34ba585c1b8
# https://towardsdatascience.com/4-tricks-you-should-know-to-parse-date-columns-with-pandas-read-csv-27355bb2ad0e
# https://www.codegrepper.com/code-examples/python/how+to+extract+gz+file+python
# https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html