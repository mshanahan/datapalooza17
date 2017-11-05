import csv

#changes to make:
  #INH1 INI1 -> INH1
  #KSH1 KSI1 -> KSH1
  #MNI1 -> DELETE
  #MOH1  MOI1  MOH2  MOI2 -> WRITE ONCE AS MOH1, WRITE AGAIN AS MOH2
  #NEH1 NEH4 -> DELETE
  #NYH1 NYI1 -> DELETE
  #NYH3 NYI2 -> NYH3
  #WIH1 WII1 -> WIH1
  
weather = open('NewWeather.csv','r')
rWeather = open('RearrangedWeather.csv','w')
weatherReader = csv.reader(weather)
rWeatherWriter = csv.writer(rWeather)
for row in weatherReader:
  if(len(row) == 0):
    continue
  if row[0] == 'INH1  INI1':
    row[0] = 'INH1'
    rWeatherWriter.writerow(row)
  elif row[0] == 'KSH1  KSI1':
    row[0] = 'KSH1'
    rWeatherWriter.writerow(row)
  elif row[0] == 'MNI1':
    continue
  elif row[0] == 'MOH1  MOI1  MOH2  MOI2':
    row[0] = 'MOH1'
    rWeatherWriter.writerow(row)
    row[0] = 'MOH2'
    rWeatherWriter.writerow(row)
  elif row[0] == 'NEH1  NEH4':
    continue
  elif row[0] == 'NYH1  NYI1':
    continue
  elif row[0] == 'NYH3  NYI2':
    row[0] = 'NYH3'
    rWeatherWriter.writerow(row)
  elif row[0] == 'WIH1  WII1':
    row[0] = 'WIH1'
    rWeatherWriter.writerow(row)
  else:
    rWeatherWriter.writerow(row)
rWeather.close()
weather.close()
