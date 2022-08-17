# -*- coding: UTF-8 -*-
import glob
from zipfile import ZipFile
import os
import pandas as pd
# All files and directories ending with .txt and that don't begin with a dot:
zip_files = glob.glob('../.datasets/IDEAM/*.zip')
for i in zip_files:
    print('Uncompressing %s' %i)
    ZipFile(i).extractall('../.datasets/IDEAM/')
    os.rename('../.datasets/IDEAM/excel.csv.csv', i+'.csv')
csv_files = glob.glob('../.datasets/IDEAM/*.csv')
df = pd.concat(map(pd.read_csv, csv_files), ignore_index=True)
print(df)
df.to_csv('../.datasets/IDEAM/IDEAM.csv', encoding='utf-8', index=False)



'''
# -*- coding: UTF-8 -*-
# Parameters
thermal_level_caldas = False  # True for Caldas classification, False for conventional classification range
thermal_level_ref_conv = [[1000,'Cálido, 24°C+, <= 1000 meters'],
                          [2000,'Templado, 18°C+, <= 2000 meters'],
                          [3000,'Frío, 12°C+, <= 3000 meters'],
                          [4000,'Páramo, 0°C, <= 4000 meters'],
                          [99999,'Glacial, 0°C-, > 4000 meters']] # Elevation value in meters
thermal_level_ref_caldas = [[800,'Cálido, T>=24°C, <=800meter'],
                            [1800,'Templado, 24°C>T>18°C, <=1800meter'],
                            [2800,'Frío, 18°C>T>12°C, <=2800meter'],
                            [3700,'Muy Frío, 12°C>T>6°C, <=3700meter'],
                            [4700,'Extremadamente Frio, 6°C>T>0°C, <=4700meter'],
                            [99999,'Nival, T<0°C, >4700meter']] # Elevation value in meters

# Thermal level system
if thermal_level_caldas == True:
    thermal_level_ref = thermal_level_ref_caldas
else:
    thermal_level_ref = thermal_level_ref_conv

def thermal_level_f(elevation):
    for i in thermal_level_ref[:]:
        if elevation <= i[0]:
            return i[0],i[1]

elevation_value = 1825
print('The elevation value %d correspond to the Thermic level value: %s ' %(elevation_value, thermal_level_f(elevation_value)[1]))



from datetime import datetime
installation_date = '14/09/1972'
#installation_date = ''
#suspension_date = '02/07/2019'
suspension_date = ''
tw_end_date = '31/12/2021' # Time window end
def len_years_serie(installation_date, suspension_date):
    if not installation_date:
        installation_date = tw_end_date
        suspension_date = tw_end_date
    if not suspension_date:
        suspension_date = tw_end_date
    diff_date = datetime.strptime(suspension_date, '%d/%m/%Y') - datetime.strptime(installation_date, '%d/%m/%Y')
    return float(diff_date.days)/365

print(len_years_serie(installation_date, suspension_date))

# Basic date difference sample over Python 3
installation_date = datetime.strptime('14/09/1972', '%d/%m/%Y')
#installation_date = ''
suspension_date = datetime.strptime('02/07/2019', '%d/%m/%Y')
#suspension_date = ''
tw_end_date = datetime.strptime('31/12/2021', '%d/%m/%Y') # Time window end
is_python3 = True # Insert False for Python 2
def len_years_serie(installation_date, suspension_date):
    if not installation_date:
        installation_date = tw_end_date
    if not suspension_date:
        suspension_date = tw_end_date
    if is_python3:
        diff_date = suspension_date - installation_date
    else:
        diff_date = datetime.strptime(suspension_date, '%d/%m/%Y') - datetime.strptime(installation_date, '%d/%m/%Y')
    print('diff_date: %s\n' %(diff_date)+
          'Type: %s' %(type(diff_date)))
    return float(diff_date.days)/365
print('len_years_serie: %f' %(len_years_serie(installation_date, suspension_date)))


# Basic date difference sample
#import dateutil.utils
installation_date = '1972-09-14'
suspension_date = '2019-07-02'
diff_date = datetime.strptime(suspension_date, '%Y-%m-%d') - datetime.strptime(installation_date, '%Y-%m-%d')
print('Basic date difference sample\n'
      'Installation date: %s\n' %(installation_date)+
      'Suspension date: %s\n' %(suspension_date)+
      'Serie length, years: %f' %(diff_date.days/365))


# Basic date difference sample with only date end time window cut
installation_date = '1972-09-14'
suspension_date = '' # Use '' for not suspension date
tw_end_date = '2021-12-31' # Time window end
def len_years_serie(installation_date, suspension_date):
    if suspension_date:
        diff_date = datetime.strptime(suspension_date, '%Y-%m-%d') - datetime.strptime(installation_date, '%Y-%m-%d')
    else:
        diff_date = datetime.strptime(tw_end_date, '%Y-%m-%d') - datetime.strptime(installation_date, '%Y-%m-%d')
    return float(diff_date.days)/365
print('\nBasic date difference sample with only date end time window cut\n'
      'Installation date: %s\n' %(installation_date)+
      'Suspension date: %s\n' %(suspension_date)+
      'Time-window end date: %s\n' %(tw_end_date)+
      'Serie length, years: %f' %len_years_serie(installation_date,suspension_date))


# Basic date difference sample with full date end time window cut
# The function don't check leap year and divide the dates difference between 365
# Date values format must be like YYYY-mm-dd
installation_date = '1972-09-14' # 1972-09-14
suspension_date = '' # Use '' for not suspension date
tw_start_date = '' # Time-window start. Use '' for set 1900-01-01
tw_end_date = '2021-12-31' # Time-window end. Use '' for use the current date and prevent over-time wrong suspension dates
if not tw_start_date: tw_start_date = '1900-01-01'
if not tw_end_date: tw_end_date = str(datetime.today().date())
def len_years_serie(installation_date, suspension_date):
    if installation_date:
        if datetime.strptime(installation_date, '%Y-%m-%d') <= datetime.strptime(tw_start_date, '%Y-%m-%d'):
            tw_installation_date = tw_start_date
        else:
            tw_installation_date = installation_date
        if suspension_date:
            if datetime.strptime(suspension_date, '%Y-%m-%d') >= datetime.strptime(tw_end_date, '%Y-%m-%d'):
                tw_suspension_date = tw_end_date
            else:
                tw_suspension_date = suspension_date
            diff_date = datetime.strptime(suspension_date, '%Y-%m-%d') - datetime.strptime(installation_date, '%Y-%m-%d')
            tw_diff_date = datetime.strptime(tw_suspension_date, '%Y-%m-%d') - datetime.strptime(tw_installation_date, '%Y-%m-%d')
        else:
            diff_date = datetime.strptime(tw_end_date, '%Y-%m-%d') - datetime.strptime(installation_date, '%Y-%m-%d')
            tw_diff_date = datetime.strptime(tw_end_date, '%Y-%m-%d') - datetime.strptime(tw_installation_date, '%Y-%m-%d')
        diff_date = float(diff_date.days)/365
        tw_diff_date = float(tw_diff_date.days)/365
        if diff_date < 0: diff_date = 0
        if tw_diff_date < 0: tw_diff_date = 0
    else:
        diff_date = 0
        tw_diff_date = 0
    return diff_date, tw_diff_date # First value is complete length. Second value is time window length
print('\nBasic date difference sample with full date end time window cut\n'
      'Installation date: %s\n' %(installation_date)+
      'Suspension date: %s\n' %(suspension_date)+
      'Time-window start date: %s\n' %(tw_start_date)+
      'Time-window end date: %s\n' %(tw_end_date)+
      'Serie full length, years: %f\n' %len_years_serie(installation_date,suspension_date)[0]+
      'Serie time-window length, years: %f' %len_years_serie(installation_date,suspension_date)[1])
'''

