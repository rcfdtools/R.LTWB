# -*- coding: UTF-8 -*-
# Name: AGG.py
# Description: statistical aggregations for hydro climatological series
# Requirements: Python 3+, pandas, tabulate, numpy
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
station_file = 'D:/R.LTWB/.datasets/IDEAM_Impute/Impute_MICE_Outlier_IQR_Cap_Pivot_PTPM_TT_M.csv'  # Current IDEAM records file
path = 'D:/R.LTWB/.datasets/IDEAM_AGG/'  # Your local output files path, use ../.datasets/IDEAM_AGG/ for relative path
file_log_name = path + 'AGG.md'
file_log = open(file_log_name, 'w+')   # w+ create the file if it doesn't exist
date_record_name = 'Fecha'  # IDEAM date field name for the record values
only_included = False  # True: let the user run this script only for the stations included in the station_include array. False: process all the stations but not the ones in the station_exclude array.
station_exclude = ['28017140', '25027020', '25027410', '25027490', '25027330', '25027390', '25027630', '25027360', '25027320', '16067010', '25027420']  # Use ['station1', 'station2', '...',]
station_include = ['15015020', '15060050', '15060070', '15060080', '15060150']  # Use ['station1', 'station2', '...',]


# Open the IDEAM station pivot dataframe and show general information
df = pd.read_csv(station_file, low_memory=False, parse_dates=[date_record_name], index_col=date_record_name)
if only_included:
    df = df.loc[:, df.columns.isin(station_include)]
else:
    df = df.loc[:, ~df.columns.isin(station_exclude)]
ideam_regs = df.shape[0]
print('Records: %d' % ideam_regs)