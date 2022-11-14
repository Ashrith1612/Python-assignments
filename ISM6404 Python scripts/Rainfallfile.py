#Reading data from a file

import csv

Months = []

Rainfall =[]

with open ("RainfallByMonthDataWithHeader.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    recordnum = 1
    for eachRow in csvreader:
        if recordnum == 1:
            Field1 = eachRow[0]
            Field2 = eachRow[1]
            recordnum += 1
        else:
            Months.append(eachRow[0])
            Rainfall.append(eachRow[1])
            recordnum += 1
            
csvfile.close()
print (Months)
print (Rainfall)


import matplotlib.pyplot as plt
plt.plot(Months,Rainfall)
plt.show()