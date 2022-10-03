# Do not convert the .csv file into an Excel file because you would be process more than 1048576 records.

import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt


path = 'C:/temp/ChirpsTest/' # Your local .zip files path, use ../.datasets/IDEAM/ for relative path
'''
raster_file = 'chirps-v2.0.1981.01.tif'
raster = rasterio.open(path+raster_file)
# print(raster.crs) # Print coordinate reference system
# print(raster.count) # Print number of bands
# show(raster) # Plot the raster file

# Sample coordinate raster reading in a specific coordinate
row, col = raster.index(-74.044222,9.188056)
value = raster.read(1)[row, col]
print(value)
'''

# Processing values for each station and year
import pandas as pd
# import xlrd # Tested with 2.0.1 version. # Has to be installed with not import required.

sampleRecord = 12 # Number of records to show in the sample
latitude_name = 'Latitud'
longitude_name = 'Longitud'
station_file='IDEAMJoined.csv'
station_df = pd.read_csv(path+station_file, low_memory=False, parse_dates=['FechaInstalacion', 'FechaSuspension', 'Fecha'])
#station_df = pd.read_excel(path+station_file, index_col='Fecha')
print('\nGeneral dataframe information: ')
print(station_df.info())
print('\nStation records sample')
print('\n', station_df)
station_df = station_df.query('Etiqueta == "PTPM_TT_M"') # Filter for rain values
print('\nFiltered records for PTPM_TT_M: %s' %(str(station_df.shape[0])))

# Filter for specified year and month
year_start = 1981
year_end = 1981
for year in range(year_start, year_end+1, 1):
    for month in range (12):
        year_month = str(year).zfill(4) + '-' + str(month+1).zfill(2)
        station_df_filter = station_df[station_df['Fecha'].dt.strftime('%Y-%m') == year_month]
        print('Processing: %s with %s records' %(year_month, str(station_df_filter.shape[0]) ))
        #print('\nFiltered records for PTPM_TT_M and specified year and month: %s' %(str(station_df_filter.shape[0])))

#station_df_filter = station_df.filter(items=['CodigoEstacion', latitude_name, longitude_name, 'Fecha', 'Etiqueta','Frecuencia', 'Valor'])
#print(station_df_filter)





# References
# https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_monthly/tifs/
# https://hatarilabs.com/ih-en/extract-point-value-from-a-raster-file-with-python-geopandas-and-rasterio-tutorial
# https://www.youtube.com/watch?v=6zzneGT4mkg
# https://sparkbyexamples.com/pandas/pandas-dataframe-filter/
# https://towardsdatascience.com/8-ways-to-filter-pandas-dataframes-d34ba585c1b8
# https://towardsdatascience.com/4-tricks-you-should-know-to-parse-date-columns-with-pandas-read-csv-27355bb2ad0e