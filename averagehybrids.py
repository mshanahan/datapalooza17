import csv
PlantLengthList = []
GrainYieldList = []
oldExperiment = 'u'



hybrids = open('g2f_2015_hybrid_data_no_outliersMMclean2.csv','r')
hybridReader = csv.reader(hybrids)
sortedReader = sorted(hybridReader, key=lambda row: row[1], reverse=False)

for row in sortedReader:
     experiment = row[1]
     if experiment != oldExperiment and oldExperiment != 'u':
         PlantLengthListAvg = []
         GrainYieldListAvg = []
         try:
             PlantLengthListAvg = sum(PlantLengthList) / len(PlantLengthList)
         except (TypeError,ZeroDivisionError):
             print("TYPE ERROR PLANTLENGTHLIST")
             print(PlantLengthList)   
         try:
             GrainYieldListAvg = sum(GrainYieldList) / len(GrainYieldList)
         except (TypeError,ZeroDivisionError):
             print("TYPE ERROR GRAINYIELDLIST")
             print (GrainYieldList)
         
         NewHybrids = open('NewHybrids.csv','a+')
         NewHybridWriter = csv.writer(NewHybrids)
         WriteList = []
         WriteList.append(oldExperiment)
         WriteList.append(PlantLengthListAvg)
         WriteList.append(GrainYieldListAvg)
         NewHybridWriter.writerow(WriteList)
         NewHybrids.close()
            
         PlantLengthList = []
         GrainYieldList = []
         oldExperiment = 'u'
     if experiment == oldExperiment or oldExperiment == 'u':
        # print(TempList)
         if row[20] != '' and row[20] != 'Plant height [cm]':
             PlantLengthList.append(float(row[20]))
         elif row[20] == 'Plant height [cm]':
              continue
         if row[27] != '' and row[27] != 'Grain yield [bu/acre]':
             GrainYieldList.append(float(row[27]))
         elif row[27] == 'Grain yield [bu/acre]':
              continue
     oldExperiment = row[1]
hybrids.close()
