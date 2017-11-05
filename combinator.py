import csv

soil = open('NewSoil.csv','r')
weather = open('RearrangedWeather.csv','r')
hybrids = open('NewHybrids.csv','r')

soilReader = csv.reader(soil)
weatherReader = csv.reader(weather)
hybridsReader = csv.reader(hybrids)

combined = open('CombinedData.csv','w')
combinedWriter = csv.writer(combined)

titles = ['experiment','PH','OM','P','K','Temperature','Dew Point','Relative Humidity','Solar Radiation','Soil Temperature','Soil Moisture','Plant Height','Grain Yield']
combinedWriter.writerow(titles)

for soilRow in soilReader:
    weatherRow = next(weatherReader)
    hybridsRow = next(hybridsReader)
    
    if(len(weatherRow) > 0):
        weatherRow.pop(0)
    if(len(hybridsRow) > 0):
        hybridsRow.pop(0)
    soilRow.extend(weatherRow)
    soilRow.extend(hybridsRow)
    combinedWriter.writerow(soilRow)

soil.close()
weather.close()
hybrids.close()
combined.close()
