# -*- coding: UTF-8 -*-
# Name: ENSOONI.py
# Description: get the NOOA oni.ascii.txt and classify the climatological phenomenas Niño, Niña and Neutral.
# Requirements: Python 3+, pandas, tabulate, numpy, missingno, sklearn
# SEAS: season, YR: year, TOTAL: average temperature, ANOM: anomaly value.


# Libraries
from datetime import datetime
from datetime import date
import requests
import os.path
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# General variables
url_file = 'https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt'
local_file = 'oni_ascii'
file_extension = '.txt'
path = 'D:/R.LTWB/.datasets/ENSOONI/'  # Your local output path, use ../.datasets/ENSOONI/ for relative path
analysis_File = 'oni_eval.csv'  # Output analysis file
fig_size = 5  # Height size for figures plot
show_plot = False  # Show plots in screen
threshold = 0.5  # Temperature anomaly grader in °C
consecutive_event = 5  # Number of consecutive events


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
#print(df.info())
#print(df.to_markdown())


# Processing n non-consecutive overlapping seasons
print('\n\n## ENSO ONI yearly events classification with %s non-consecutive overlapping seasons and %s°C threshold' % (consecutive_event, str(threshold)))
columns=['YR', 'NinaCount', 'NinoCount', 'NeutralCount', 'Event', 'EventMark', 'EventLabel']
df_out = pd.DataFrame(columns=columns)
start_year = df['YR'].min()
records = int(df.shape[0])
print('\n* Records: %d' % records +
      '\n* Years: %f\n' % (records/ 12))
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
print(df_out.to_markdown())
df_out.to_csv(path + 'NonConsecutive_' + analysis_File, encoding='latin-1')
# Plot event graph
x = np.arange(0, df_out.shape[0]-1, 1)
x_label = np.arange(int(df_out.index.values.min()), int(df_out.index.values.max()), 1)
ax = df_out.plot(y='EventMark',  color='skyblue', legend=False, figsize=(fig_size*2.5, fig_size*1.25), kind='line', grid=True, style='.-', ms=16, mfc='skyblue', mec='skyblue', linewidth=0.75)
plt.title('ENSO ONI - Events with %s non consecutive overlapping seasons\n\n' % consecutive_event)
plt.yticks([-1, 0, 1], ['Niña\n(cold & wet)\nAnom. ≤ -%s°C' % str(threshold), 'Neutro', 'Niño\n(hot & dry)\nAnom. ≥ %s°C' % str(threshold)])
plt.xticks(x, x_label, rotation=90, size=9)
ax.set_ylabel('Event')
plt.grid(color='silver', linestyle='-', linewidth=0.25, alpha=0.5)
for index in range(df_out.shape[0]-1):
    ax.text(x[index], df_out['EventMark'][index], str(x_label[index]) + ' (' + str(df_out['EventLabel'][index]) + ')', size=9, rotation=60)
plt.savefig(path + 'NonConsecutive_' + analysis_File + '.png')
if show_plot: plt.show()
plt.close('all')


# Processing n consecutive overlapping seasons
print('\n\n## ENSO ONI yearly events classification with %s consecutive overlapping seasons and %s°C threshold' % (consecutive_event, str(threshold)))
columns=['YR', 'NinaCount', 'NinoCount', 'NeutralCount', 'Event', 'EventMark', 'EventLabel']
df_out = pd.DataFrame(columns=columns)
start_year = df['YR'].min()
records = int(df.shape[0])
print('\n* Records: %d' % records +
      '\n* Years: %f\n' % (records/ 12))
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
print(df_out.to_markdown())
df_out.to_csv(path + 'Consecutive_' + analysis_File, encoding='latin-1')
# Plot event graph
x = np.arange(0, df_out.shape[0]-1, 1)
x_label = np.arange(int(df_out.index.values.min()), int(df_out.index.values.max()), 1)
ax = df_out.plot(y='EventMark',  color='skyblue', legend=False, figsize=(fig_size*2.5, fig_size*1.25), kind='line', grid=True, style='.-', ms=16, mfc='skyblue', mec='skyblue', linewidth=0.75)
plt.title('ENSO ONI - Events with %s consecutive overlapping seasons\n\n' % consecutive_event)
plt.yticks([-1, 0, 1], ['Niña\n(cold & wet)\nAnom. ≤ -%s°C' % str(threshold), 'Neutro', 'Niño\n(hot & dry)\nAnom. ≥ %s°C' % str(threshold)])
plt.xticks(x, x_label, rotation=90, size=9)
ax.set_ylabel('Event')
plt.grid(color='silver', linestyle='-', linewidth=0.25, alpha=0.5)
for index in range(df_out.shape[0]-1):
    ax.text(x[index], df_out['EventMark'][index], str(x_label[index]) + ' (' + str(df_out['EventLabel'][index]) + ')', size=9, rotation=60)
plt.savefig(path + 'Consecutive_' + analysis_File + '.png')
if show_plot: plt.show()
plt.close('all')