# -*- coding: UTF-8 -*-
# Name: CNEStationCSVJoin.py
# Description: this script uncompress and join multiple .zip files get manually from http://dhime.ideam.gov.co/atencionciudadano/ into a single .csv file.
# Repository: https://github.com/rcfdtools/R.LTWB/tree/main/Section03/CNEStationDatasetDownload
# License: https://github.com/rcfdtools/R.LTWB/wiki/License
# Requirements: Python 3+, Pandas

# Libraries
import glob
from zipfile import ZipFile
import os
import pandas as pd

# Procedure
path = 'D:/R.LTWB/.datasets/IDEAM/' # Your local .zip files path, use ../.datasets/IDEAM/ for relative path
join_file = 'IDEAMJoined.csv' # Joined file name
if os.path.isfile(path + join_file):
    os.remove(path + join_file)
zip_files = glob.glob(path + '*.zip')
for i in zip_files:
    print('Unzipping %s' %i)
    ZipFile(i).extractall(path)
    os.rename(path + 'excel.csv.csv', i+'.csv')
csv_files = glob.glob(path + 'datos*.csv')
df = pd.concat(map(pd.read_csv, csv_files), ignore_index=True)
df.to_csv(path + join_file, encoding='utf-8', index=False)
print(df)
for csv_file in csv_files:
    os.remove(csv_file)