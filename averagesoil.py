import csv
PHList = []
OMList = []
PList = []
KList = []
oldExperiment = 'u'

soil = open('g2f_2015_soil_dataMMclean2.csv','r')
soilReader = csv.reader(soil)
sortedReader = sorted(soilReader, key=lambda row: row[4], reverse=False)

for row in sortedReader:
     experiment = row[4]
     if experiment != oldExperiment and oldExperiment != 'u':
         PHListAvg = []
         OMListAvg = []
         PListAvg = []
         KListAvg = []
         try:
             PHListAvg = sum(PHList) / len(PHList)
         except (TypeError,ZeroDivisionError):
             print("TYPE ERROR PHLIST")
             print(PHList)   
         try:
             OMListAvg = sum(OMList) / len(OMList)
         except (TypeError,ZeroDivisionError):
             print("TYPE ERROR OMLIST")
             print (OMList)
         try:
             PListAvg = sum(PList) / len(PList)
         except (TypeError,ZeroDivisionError):
             print("TYPE ERROR PLIST")
             print(PList)
         try:
             KListAvg = sum(KList) / len(KList)
         except (TypeError,ZeroDivisionError):
             print("TYPE ERROR KLIST")
             print(KList)
         
         NewSoil = open('NewSoil.csv','a+')
         NewSoilWriter = csv.writer(NewSoil)
         WriteList = []
         WriteList.append(oldExperiment)
         WriteList.append(PHListAvg)
         WriteList.append(OMListAvg)
         WriteList.append(PListAvg)
         WriteList.append(KListAvg)
         NewSoilWriter.writerow(WriteList)
         NewSoil.close()
            
         PHList = []
         OMList = []
         PList = []
         KList = []
         oldExperiment = 'u'
         print(row)
     if experiment == oldExperiment or oldExperiment == 'u':
        # print(TempList)
         if row[6] != '' and row[6] != 'PH':
             PHList.append(float(row[6]))
         elif row[6] == 'PH':
              experiment = ''
              oldExperiment = 'u'
              continue
         if row[7] != '' and row[7] != 'OM':
             OMList.append(float(row[7]))
         elif row[7] == 'OM':
              experiment = ''
              continue
         if row[8] != '' and row[8] != 'P':
             PList.append(float(row[8]))
         elif row[8] == 'P':
              experiment = ''
              continue
         if row[9] != '' and row[9] != 'K':
             KList.append(int(row[9]))
         elif row[9] == 'K':
             experiment = ''
             continue
     oldExperiment = row[4]
soil.close()
