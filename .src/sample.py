from datetime import datetime

# Date difference sample
fecha_instalacion = '1973-11-02'
fecha_suspension = '2022-06-28'
diff_date = datetime.strptime(fecha_suspension, '%Y-%m-%d') - datetime.strptime(fecha_instalacion, '%Y-%m-%d')

print(diff_date.days/365)