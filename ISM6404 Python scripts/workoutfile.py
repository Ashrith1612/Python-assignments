#Reading and plotting data with multiple fields

import csv

Duration = []
Pulse = []
MaxPulse = []
Calories = []

with open("WorkoutData.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    recordnum = 1
    for eachRow in csvreader:
        if recordnum == 1:
            Field1 = eachRow[0]
            Field2 = eachRow[1]
            Field3 = eachRow[2]
            Field4 = eachRow[3]
            recordnum += 1       
        else:
            Duration.append(int(eachRow[0]))
            Pulse.append(int(eachRow[1]))
            MaxPulse.append(int(eachRow[2]))
            Calories.append(float(eachRow[3]))
            recordnum += 1

csvfile.close()
print (Duration)
print (Pulse)
print (MaxPulse)
print (Calories)

import matplotlib.pyplot as plt
plt.scatter(Pulse,MaxPulse)
plt.scatter(Duration, Calories)
plt.scatter(MaxPulse,Calories)
plt.hist(Calories)


