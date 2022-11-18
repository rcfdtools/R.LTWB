# -*- coding: UTF-8 -*-
# Name: ENSOONI.py
# Description: get the NOAA oni.ascii.txt and classify the climatological events Niño, Niña and Neutral.
# Requirements: Python 3+, pandas, tabulate, numpy, missingno, sklearn
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
url_file = 'https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt'
local_file = 'ONI_Ascii'
file_extension = '.txt'
path = 'D:/R.LTWB/.datasets/ENSOONI/'  # Your local output path, use ../.datasets/ENSOONI/ for relative path
analysis_file = 'ONI_Eval'  # Output analysis file name
file_log_name = path + analysis_file + '.md'  # Markdown file log
file_log = open(file_log_name, 'w+')   # w+ create the file if it doesn't exist
fig_size = 5  # Height size for figures plot
show_plot = False  # Show plots in screen
threshold = 0.5  # Temperature anomaly grader in °C
consecutive_event = 5  # Number of consecutive events


# Function for print and show results in a file
def print_log(txt_print, on_screen=True, center_div=False):
    if on_screen:
        print(txt_print)
    if center_div:
        file_log.write('\n<div align="center">\n' + '\n')
    file_log.write(txt_print + '\n')
    if center_div:
        file_log.write('\n</div>\n' + '\n')


# Function for eval the count events
def enso_oni_tag(nina_count, nino_count, neutral_count, consecutive_event):
    if nina_count >= consecutive_event:
        event = 'Niña'
        event_val = -1
        event_label = nina_count
    else:
        if nino_count >= consecutive_event:
            event = 'Niño'
            event_val = 1
            event_label = nino_count
        else:
            event = 'Neutral'
            event_val = 0
            event_label = neutral_count
    return event, event_val, event_label


# Downloading and reading the file
file_download_text = 'File downloaded and updated = No (already exist)'
current_date = date.today()
current_date_txt = str(current_date.year).zfill(4)+str(current_date.month).zfill(2)+str(current_date.day).zfill(2)
file_request = requests.get(url_file)
file_save = path + local_file + '_' + current_date_txt + file_extension
if file_request:
    if os.path.isfile(file_save) == False:
        open(file_save, 'wb').write(file_request.content)
        file_download_text = 'File downloaded and updated = Yes'
df = pd.read_csv(file_save, sep='\s+')
print(file_download_text)
records = int(df.shape[0])


# Header
print_log('# NOAA - Oceanic Niño Index (ONI) classifier for climatological year events Niño, Niña and Neutral')
print_log('\nThe following analysis are based on a threshold of +/- 0.5°C for the Oceanic Niño Index (ONI) [3 month running mean of ERSST.v5 SST anomalies in the Niño 3.4 region (5°N-5°S, 120°-170°W)], based on centered 30-year base periods updated every 5 years.\nThe ONI is one measure of the El Niño-Southern Oscillation, and other indices can confirm whether features consistent with a coupled ocean-atmosphere phenomenon accompanied these periods.[^1]')
print_log('\n* Processed file: [%s](%s)' % (str(file_save), '../ENSOONI/' + local_file + '_' + current_date_txt + file_extension) +
          '\n* Execution date: ' + str(datetime.now()) +
          '\n* Python version: ' + str(sys.version) +
          '\n* Python path: ' + str(sys.path[0:5]) +
          '\n* matplotlib version: ' + str(matplotlib.__version__) +
          '\n* pandas version: ' + str(pd.__version__) +
          '\n* numpy version: ' + str(np.__version__) +
          '\n* Instructions & script: https://github.com/rcfdtools/R.LTWB/tree/main/Section03/ENSOONI'
          '\n* License: https://github.com/rcfdtools/R.LTWB/blob/main/LICENSE.md'
          '\n* Credits: r.cfdtools@gmail.com')


# General information
print_log('\n## General ONI Ascii file information')
print_log('\n* Ascii file from: %s' % url_file +
          '\n* Records: %d' % records +
          '\n* Years: %f\n' % (records/ 12))
print_log('\nTable records', center_div=True)
print_log(df.to_markdown(), center_div=True)
# Plot historic values
ax = df.plot(x='YR', y='TOTAL',  color='black', legend=False, figsize=(fig_size*2, fig_size*1.5), kind='line', grid=False, style='.-', ms=4, mfc='black', mec='black', linewidth=0.75)
plt.title('ENSO ONI - Historic records')
ax.set_ylabel('Seasonal value °C')
plt.grid(color='silver', linestyle='-', linewidth=0.25, alpha=0.5)
plt.savefig(path + local_file + file_extension + '_Historic.png', dpi=150)
if show_plot: plt.show()
plt.close('all')
print_log('\n![R.LTWB](%s)' % (local_file + file_extension + '_Historic.png'), center_div=False)
# Plot anomaly values
ax = df.plot(x='YR', y='ANOM',  color='black', legend=False, figsize=(fig_size*2, fig_size*1.5), kind='line', grid=False, style='.-', ms=4, mfc='black', mec='black', linewidth=0.75)
plt.title('ENSO ONI - Anomaly records')
ax.set_ylabel('Seasonal value °C')
plt.grid(color='silver', linestyle='-', linewidth=0.25, alpha=0.5)
y_ticks = np.arange(-2.5, 3.5, 0.5)
plt.yticks(y_ticks)
plt.savefig(path + local_file + file_extension + '_Anomaly.png', dpi=150)
if show_plot: plt.show()
print_log('\n![R.LTWB](%s)' % (local_file + file_extension + '_Anomaly.png'), center_div=False)
plt.close('all')


# Processing n non-consecutive overlapping seasons
print_log('\n\n## ENSO ONI yearly events classification with %s non-consecutive overlapping seasons and %s°C threshold' % (consecutive_event, str(threshold)))
print_log('\nClassification file: [%s](%s)' % (analysis_file + '_NonConsecutive.csv', analysis_file + '_NonConsecutive.csv'))
columns=['YR', 'NinaCount', 'NinoCount', 'NeutralCount', 'Event', 'EventMark', 'EventLabel']
df_out = pd.DataFrame(columns=columns)
start_year = df['YR'].min()
nina_count, nino_count = 0, 0
for i in range (records):
    start_year_aux = df['YR'][i]
    if start_year == start_year_aux:
        if df['ANOM'][i] <= -threshold:
            nina_count += 1
        if df['ANOM'][i] >= threshold:
            nino_count += 1
    else:
        neutral_count = 12 - nina_count - nino_count
        event = enso_oni_tag(nina_count, nino_count, neutral_count, consecutive_event)[0]
        event_val = enso_oni_tag(nina_count, nino_count, neutral_count, consecutive_event)[1]
        event_label = enso_oni_tag(nina_count, nino_count, neutral_count, consecutive_event)[2]
        df_eval = pd.DataFrame(np.array([[start_year, nina_count, nino_count, neutral_count, event, event_val, event_label]]), columns=columns)
        df_out = pd.concat([df_out, df_eval], ignore_index=True)
        start_year = df['YR'][i]
        nina_count = 0
        nino_count = 0
        if df['ANOM'][i] <= -threshold:
            nina_count += 1
        if df['ANOM'][i] >= threshold:
            nino_count += 1
neutral_count = 12 - nina_count - nino_count
event = enso_oni_tag(nina_count, nino_count, neutral_count, consecutive_event)[0]
event_val = enso_oni_tag(nina_count, nino_count, neutral_count, consecutive_event)[1]
event_label = enso_oni_tag(nina_count, nino_count, neutral_count, consecutive_event)[2]
df_eval = pd.DataFrame(np.array([[start_year, nina_count, nino_count, neutral_count, event, event_val, event_label]]), columns=columns)
df_out = pd.concat([df_out, df_eval], ignore_index=True)
df_out = df_out.set_index('YR')
convert_dict = {'NinaCount': int,
                'NinoCount': int,
                'NeutralCount': int,
                'EventMark': int,
                'EventLabel': int
                }
df_out = df_out.astype(convert_dict)
print_log('\nTable records', center_div=True)
print_log(df_out.to_markdown(), center_div=True)
df_out.to_csv(path + analysis_file + '_NonConsecutive.csv', encoding='latin-1')
# Plot event graph
x = np.arange(0, df_out.shape[0]-1, 1)
x_label = np.arange(int(df_out.index.values.min()), int(df_out.index.values.max()), 1)
ax = df_out.plot(y='EventMark',  color='silver', legend=False, figsize=(fig_size*2.5, fig_size*1.25), kind='line', grid=True, style='.-', ms=12, mfc='silver', mec='silver', linewidth=0.75)
plt.title('ENSO ONI - Events with %s non consecutive overlapping seasons\n\n' % consecutive_event)
plt.yticks([-1, 0, 1], ['Niña\n(cold & wet)\nAnom. ≤ -%s°C' % str(threshold), 'Neutral', 'Niño\n(hot & dry)\nAnom. ≥ %s°C' % str(threshold)])
plt.xticks(x, x_label, rotation=90, size=9)
ax.set_ylabel('Event')
plt.grid(color='silver', linestyle='-', linewidth=0.1, alpha=0.25)
for index in range(df_out.shape[0]-1):
    ax.text(x[index], df_out['EventMark'][index], str(x_label[index]) + ' (' + str(df_out['EventLabel'][index]) + ')', size=9, rotation=80)
plt.savefig(path + analysis_file + '_NonConsecutive.png', dpi=150)
if show_plot: plt.show()
plt.close('all')
print_log('\n![R.LTWB](%s)' % (analysis_file + '_NonConsecutive.png'), center_div=False)


# Processing n consecutive overlapping seasons
print_log('\n\n## ENSO ONI yearly events classification with %s consecutive overlapping seasons and %s°C threshold' % (consecutive_event, str(threshold)))
print_log('\nClassification file: [%s](%s)' % (analysis_file + '_Consecutive.csv', analysis_file + '_Consecutive.csv'))
columns=['YR', 'NinaCount', 'NinoCount', 'NeutralCount', 'Event', 'EventMark', 'EventLabel']
df_out = pd.DataFrame(columns=columns)
start_year = df['YR'].min()
nina_count, nino_count, nina_max, nino_max = 0, 0, 0, 0
for i in range(records):
    start_year_aux = df['YR'][i]
    if start_year == start_year_aux:
        if df['ANOM'][i] <= -threshold and i < records - 1:
            nina_count += 1
            if nina_max < nina_count:
                nina_max = nina_count
        else:
            nina_count = 0
        if df['ANOM'][i] >= threshold and i < records - 1:
            nino_count += 1
            if nino_max < nino_count:
                nino_max = nino_count
        else:
            nino_count = 0
    else:
        neutral_count = 12 - nina_max - nino_max
        event = enso_oni_tag(nina_max, nino_max, neutral_count, consecutive_event)[0]
        event_val = enso_oni_tag(nina_max, nino_max, neutral_count, consecutive_event)[1]
        event_label = enso_oni_tag(nina_max, nino_max, neutral_count, consecutive_event)[2]
        df_eval = pd.DataFrame(np.array([[start_year, nina_max, nino_max, neutral_count, event, event_val, event_label]]), columns=columns)
        df_out = pd.concat([df_out, df_eval], ignore_index=True)
        start_year = df['YR'][i]
        #nina_max, nino_max = 0, 0
        nina_count, nino_count, nina_max, nino_max = 0, 0, 0, 0
        if df['ANOM'][i] <= -threshold and i < records - 1:
            nina_count += 1
            if nina_max < nina_count:
                nina_max = nina_count
        else:
            nina_count = 0
        if df['ANOM'][i] >= threshold and i < records - 1:
            nino_count += 1
            if nino_max < nino_count:
                nino_max = nino_count
        else:
            nino_count = 0
neutral_count = 12 - nina_max - nino_max
event = enso_oni_tag(nina_max, nino_max, neutral_count, consecutive_event)[0]
event_val = enso_oni_tag(nina_max, nino_max, neutral_count, consecutive_event)[1]
event_label = enso_oni_tag(nina_max, nino_max, neutral_count, consecutive_event)[2]
df_eval = pd.DataFrame(np.array([[start_year, nina_max, nino_max, neutral_count, event, event_val, event_label]]), columns=columns)
df_out = pd.concat([df_out, df_eval], ignore_index=True)
df_out = df_out.set_index('YR')
convert_dict = {'NinaCount': int,
                'NinoCount': int,
                'NeutralCount': int,
                'EventMark': int,
                'EventLabel': int
                }
df_out = df_out.astype(convert_dict)
print_log('\nTable records', center_div=True)
print_log(df_out.to_markdown(), center_div=True)
df_out.to_csv(path + analysis_file + '_Consecutive.csv', encoding='latin-1')
# Plot event graph
x = np.arange(0, df_out.shape[0]-1, 1)
x_label = np.arange(int(df_out.index.values.min()), int(df_out.index.values.max()), 1)
ax = df_out.plot(y='EventMark',  color='silver', legend=False, figsize=(fig_size*2.5, fig_size*1.25), kind='line', grid=True, style='.-', ms=12, mfc='silver', mec='silver', linewidth=0.75)
plt.title('ENSO ONI - Events with %s consecutive overlapping seasons\n\n' % consecutive_event)
plt.yticks([-1, 0, 1], ['Niña\n(cold & wet)\nAnom. ≤ -%s°C' % str(threshold), 'Neutral', 'Niño\n(hot & dry)\nAnom. ≥ %s°C' % str(threshold)])
plt.xticks(x, x_label, rotation=90, size=9)
ax.set_ylabel('Event')
plt.grid(color='silver', linestyle='-', linewidth=0.1, alpha=0.25)
for index in range(df_out.shape[0]-1):
    ax.text(x[index], df_out['EventMark'][index], str(x_label[index]) + ' (' + str(df_out['EventLabel'][index]) + ')', size=9, rotation=80)
plt.savefig(path + analysis_file + '_Consecutive.png', dpi=150)
if show_plot: plt.show()
plt.close('all')
print_log('\n![R.LTWB](%s)' % (analysis_file + '_NonConsecutive.png'), center_div=False)

print_log('\n[^1]: https://origin.cpc.ncep.noaa.gov/products/analysis_monitoring/ensostuff/ONI_v5.php')