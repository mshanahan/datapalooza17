import csv
TempList = []
DewList = []
RelHumList = []
SolList = []
SoilTempList = []
SoilMoistureList = []
oldExperiment = 'u'



weather = open('g2f_2015_weather_cleanMMclean2.csv','r')
weatherReader = csv.reader(weather)
sortedReader = sorted(weatherReader, key=lambda row: row[2], reverse=False)

for row in sortedReader:
     experiment = row[2]
     if experiment != oldExperiment and oldExperiment != 'u':
         TempListAvg = []
         DewListAvg = []
         RelHumListAvg = []
         SolListAvg = []
         SoilTempListAvg = []
         SoilMoistureListAvg = []
         try:
             TempListAvg = sum(TempList) / len(TempList)
         except (TypeError,ZeroDivisionError):
             print("TYPE ERROR TEMPLIST")
             print(TempList)   
         try:
             DewListAvg = sum(DewList) / len(DewList)
         except (TypeError,ZeroDivisionError):
             print("TYPE ERROR DEWLIST")
             print (DewList)
         try:
             RelHumListAvg = sum(RelHumList) / len(RelHumList)
         except (TypeError,ZeroDivisionError):
             print("TYPE ERROR RELHUMLIST")
             print(RelHumList)
         try:
             SolListAvg = sum(SolList) / len(SolList)
         except (TypeError,ZeroDivisionError):
             print("TYPE ERROR SOLLIST")
             print(SolList)
         try:
             SoilTempListAvg = sum(SoilTempList) / len(SoilTempList)
         except (TypeError,ZeroDivisionError):
             print("TYPE ERROR SOILTEMPLIST")
             print(SoilTempList)
         try:
             SoilMoistureListAvg = sum(SoilMoistureList) / len(SoilMoistureList)
         except (TypeError,ZeroDivisionError):
             print("TYPE ERROR SOILMOISTURELIST")
             print(SoilMoistureList)
         
         NewWeather = open('NewWeather.csv','a+')
         NewWeatherWriter = csv.writer(NewWeather)
         WriteList = []
         WriteList.append(oldExperiment)
         WriteList.append(TempListAvg)
         WriteList.append(DewListAvg)
         WriteList.append(RelHumListAvg)
         WriteList.append(SolListAvg)
         WriteList.append(SoilTempListAvg)
         WriteList.append(SoilMoistureListAvg)
         NewWeatherWriter.writerow(WriteList)
         NewWeather.close()
            
         TempList = []
         DewList = []
         RelHumList = []
         SolList = []
         SoilTempList = []
         SoilMoistureList = []
         oldExperiment = 'u'
     if experiment == oldExperiment or oldExperiment == 'u':
        # print(TempList)
         if row[9] != '' and row[9] != 'Temperature [C]':
             TempList.append(float(row[9]))
         elif row[9] == 'Temperature [C]':
              continue
         if row[10] != '' and row[10] != 'Dew Point [C]':
             DewList.append(float(row[10]))
         elif row[10] == 'Dew Point [C]':
              continue
         if row[11] != '' and row[11] != 'Relative Humidity [%]':
               RelHumList.append(float(row[11]))
         elif row[11] == 'Relative Humidity [%]':
              continue
         if row[12] != '' and row[12] != 'Solar Radiation [W/m2]':
             SolList.append(int(row[12]))
         elif row[12] == 'Solar Radiation [W/m2]':
              continue
         if row[17] != '' and row[17] != 'Soil Temperature [C]':
             SoilTempList.append(float(row[17]))
         elif row[17] == 'Soil Temperature [C]':
              continue
         if row[18] != '' and row[18] != 'Soil Moisture [%]':
             SoilMoistureList.append(float(row[18]))
         elif row[18] == 'Soil Moisture [%]':
              continue
     oldExperiment = row[2]
weather.close()
