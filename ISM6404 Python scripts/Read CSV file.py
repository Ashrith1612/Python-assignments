# Reading a csv file

import csv

with open ('WeightHeightData.csv','r') as myCsvFile:
    csvReader = csv.reader(myCsvFile)
    for eachRow in csvReader:
        print(eachRow)
        
myCsvFile.close()

with open ('WeightHeightData.csv','r') as myCsvFile:
    csvReader = csv.reader(myCsvFile)
    for eachRow in csvReader:
        for eachCol in eachRow:
            print(eachCol)
        
myCsvFile.close()

#Another variation of reading a csv file
#If we wanted to read the data into variables

with open('WeightHeightData.csv','r') as myCsvFile:
    csvReader = csv.reader(myCsvFile)
    for eachRow in csvReader:
        userWeight = eachRow[0]
        userHeight = eachRow[1]
        
        print(userWeight, userHeight)
        
myCsvFile.close()

#Read a csv file in which the first row has field names

with open('WeightHeightAgeDataWithFieldNamesInFirstRow.csv', 'r') as myCsvFile:
    
    csvReader = csv.reader(myCsvFile)
    rowNumber = 1
    for eachRow in csvReader:
        if rowNumber ==1:
            field1 = eachRow[0]
            field2 = eachRow[1]
            field3 = eachRow[2]
            print(field1,field2,field3)
            rowNumber +=1
        else:
            userWeight = eachRow[0]
            userHeight = eachRow[1]
            userAge = eachRow[2]
            rowNumber += 1
            print(userWeight,userHeight,userAge)
            

