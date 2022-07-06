from datetime import datetime

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

