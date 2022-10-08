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
import tabulate # required for print tables in Markdown using pandas
from datetime import date

# Function for get the raster value in a specific coordinate
def chirps_value(raster_file, longitude, latitude):
    raster = rasterio.open(path + raster_file)
    row, col = raster.index(longitude, latitude)
    return raster.read(1)[row, col]

# Function for print and show results in a file
def print_log(txt_print, on_screen=True, center_div=False):
    if on_screen: print(txt_print)
    if center_div: file_log.write('\n<div align="center">\n' + '\n')
    file_log.write(txt_print + '\n')
    if center_div: file_log.write('\n</div>\n' + '\n')

# General variables
station_file = 'D:/R.LTWB/.datasets/IDEAM/IDEAMJoined.csv' # Current IDEAM records file
path = 'D:/R.LTWB/.datasets/CHIRPS/' # Your local .zip files path, use ../.datasets/CHIRPS/ for relative path
station_file_chirps = 'IDEAMJoinedChirps.csv' # Output IDEAM records with the Chirps values
station_file_corr_date = 'IDEAMJoinedChirpsCorrelationDate.csv' # Output IDEAM correlations with Chirps for each date
station_file_corr_date_mean = 'IDEAMJoinedChirpsCorrelationDateMean.csv' # Output IDEAM correlations with Chirps - mean
station_file_corr_year = 'IDEAMJoinedChirpsCorrelationYear.csv' # Output IDEAM correlations with Chirps for each year
station_file_corr_month = 'IDEAMJoinedChirpsCorrelationMonth.csv' # Output IDEAM correlations with Chirps for each month
file_log_name = path + 'RemoteSensingRainChirps.md'
file_log = open(file_log_name, 'w+')  # w+ create the file if it doesn't exist
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
plot_colormap = 'tab20b' # Color theme for plot graphics, https://matplotlib.org/stable/tutorials/colors/colormaps.html
year_start = 1981 # Chirps values starts at 1981
year_end = 2021 # This value have to correspond with the end of the IDEAM series

# Open the IDEAM station dataframe and show general information
# Learn more about the IDEAM file in https://github.com/rcfdtools/R.LTWB/tree/main/Section03/CNEStationDatasetDownload
station_df = pd.read_csv(station_file, low_memory=False, parse_dates=[date_install, date_suspend, date_record])
print_log('\n### General dataframe information\n')
print(station_df.info())
print('\nStation records sample\n')
print(station_df)
ideam_regs = station_df.shape[0]
print_log('* IDEAM records: %s' %(str(ideam_regs)))
station_df = station_df.query(parameter_name) # Filter for the monthly rain values
ideam_regs_query = station_df.shape[0]
print_log('* Filtered records for %s: %i (%s%%)' %(parameter_name, ideam_regs_query, str(round((ideam_regs_query/ideam_regs)*100, 2))))

# Processing Chrips values per month in each year (displayed only in Python console)
print('\n\n### Processing Chrips values per month in each year\n')
cols = ['Date', 'Year', 'Month', 'Pearson', 'Kendall', 'Spearman']
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
        df = pd.read_csv(path + chirps_file + '.csv', low_memory=False)
        correlation_pearson = df[value_name].corr(df['SatValue'], method='pearson')
        correlation_kendall = df[value_name].corr(df['SatValue'], method='kendall')
        correlation_spearman = df[value_name].corr(df['SatValue'], method='spearman')
        print('Correlation analysis. Pearson = %f, Kendall = %f, Spearman = %f' %(correlation_pearson, correlation_kendall, correlation_spearman))
        df2 = pd.DataFrame([[pd.to_datetime(date, format=('%Y/%m/%d')), year, month + 1, correlation_pearson, correlation_kendall, correlation_spearman]], columns = cols)
        #correlation_df = pd.concat([correlation_df, df2], ignore_index = True)
        correlation_df = pd.concat([correlation_df, df2])

# Join .csv files and plot
print_log('\n\n### General IDEAM vs. CHIRPS - Plots\n')
csv_files = glob.glob(path + 'chirps-v2.0.*.csv')
df = pd.concat(map(pd.read_csv, csv_files), ignore_index=True)
df.to_csv(path + station_file_chirps, encoding='utf-8', index=False)
df = pd.read_csv(path + station_file_chirps, low_memory=False)
print_log('\nProcessed .csv file [%s](%s)\n' %(station_file_chirps, station_file_chirps))
fig = df.plot.scatter(x=value_name, y='SatValue', alpha=0.25, figsize=(6, 6), c='black', cmap=None)
plt.title('IDEAM vs. CHIRPS - Scatter plot')
fig.figure.savefig(path + 'PlotDateScatterIdeamChirps.png')
plt.show()
print_log('![R.LTWB](PlotDateScatterIdeamChirps.png)', center_div=True)
fig = df.boxplot(column=[value_name, 'SatValue'], figsize=(6, 6), grid=False)
plt.title('IDEAM & CHIRPS - Boxplot')
fig.figure.savefig(path + 'PlotDateIdeamChirpsBoxplot.png')
print_log('![R.LTWB](PlotDateIdeamChirpsBoxplot.png)', center_div=True)
plt.show()

# Correlation save & plot
print_log('\n\n### Correlation Analysis\n\nThe correlation methods used for the analysis are:\n')
print_log('* [Pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)  ')
print_log('* [Kendall rank correlation coefficient](https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient)  ')
print_log('* [Spearman’s rank correlation coefficient](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient)  ')
correlation_df.to_csv(path + station_file_corr_date, encoding='utf-8', index=False)
correlation_df.set_index('Date', inplace = True)
print_log('\n\n#### Correlation values for the date records\n\nThe following table, shows the monthly average correlation values obtained from the IDEAM records and the correspondent Chirps values.\nGet the table [%s](%s) \n' %(station_file_corr_date, station_file_corr_date))
print_log(correlation_df.to_markdown(), center_div=True)
df = correlation_df.iloc[:, [2, 3, 4]].mean(axis=0)  # iloc for get only the required attributes
df.to_csv(path + station_file_corr_date_mean, encoding='utf-8', index=True)
fig = correlation_df.iloc[:, [2, 3, 4]].plot(figsize=(10, 6), rot=90, colormap=plot_colormap)
plt.title('IDEAM vs. CHIRPS - Correlations per date')
fig.figure.savefig(path + 'PlotDateCorrelationTimeSerie.png')
print_log('\n![R.LTWB](PlotDateCorrelationTimeSerie.png)')
print_log('\n\n#### Average correlations per method\n\nThe values shown below, correspond to the average correlation values in each date processed.\nGet the table [%s](%s) \n' %(station_file_corr_date_mean, station_file_corr_date_mean))
print_log(df.to_markdown(), center_div=True)
correlation_df.iloc[:, [2, 3, 4]].plot.box(figsize=(6, 6))
fig = plt.title('IDEAM vs. CHIRPS - Correlations boxplot')
fig.figure.savefig(path + 'PlotDateCorrelationBoxplot.png')
print_log('\n![R.LTWB](PlotDateCorrelationBoxplot.png)')
df = correlation_df.groupby('Year').mean()
df.to_csv(path + station_file_corr_year, encoding='utf-8', index=True)
print_log('\n\n#### Average correlation yearly and method\n\nThis table shows the average correlation values obtained for each method in every year in the record set.\nGet the table [%s](%s) \n' %(station_file_corr_year, station_file_corr_year))
print_log(df.to_markdown(), center_div=True)
fig = df.plot(figsize=(10, 6), rot=90, colormap=plot_colormap)
plt.title('IDEAM vs. CHIRPS - Correlations per year')
fig.figure.savefig(path + 'PlotYearCorrelationTimeSerie.png')
print_log('\n![R.LTWB](PlotYearCorrelationTimeSerie.png)')
df = correlation_df.groupby('Month').mean()
df.to_csv(path + station_file_corr_month, encoding='utf-8', index=True)
print_log('\n#### Average correlation monthly and method\n\nThis table shows the average correlation values obtained in every month in the record set.\nGet the table [%s](%s) \n' %(station_file_corr_month, station_file_corr_month))
print_log(df.to_markdown(), center_div=True)
fig = df.plot(figsize=(10, 6), rot=0, colormap=plot_colormap)
plt.title('IDEAM vs. CHIRPS - Correlations per month')
plt.xticks(range(1, 13, 1))
fig.figure.savefig(path + 'PlotMonthCorrelationTimeSerie.png')
print_log('\n![R.LTWB](PlotMonthCorrelationTimeSerie.png)')
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
print('\nProcess accomplished, check the results files like: %s' %(path + station_file_chirps))


