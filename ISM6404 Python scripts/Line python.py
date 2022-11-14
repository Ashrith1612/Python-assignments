# Reading a text file

'''
When we have to read data from some data file, we first 
have to open the file in read mode
So, how to open a file in read mode?

'''

myFile = open('myDataFile.txt','r')

# now that we have opened the file in read mode, we will read it

contentsOfMyFile = myFile.read()

print(contentsOfMyFile)

myFile.close()

#what if we want to read one line at a time?
myFile = open('myDataFile.txt','r')
firstLine = myFile.readline()
print(firstLine)

secondLine = myFile.readline()
print(secondLine)

thirdLine = myFile.readline()
print(thirdLine)

fourthLine = myFile.readline()
print(fourthLine)

myFile.close()

#What if we want to read few characters at a time?
myFile = open('myDataFile.txt','r')
firstTenCharacters = myFile.read(10)
secondTenCharacters = myFile.read(10)
print(firstTenCharacters)
print(secondTenCharacters)
myFile.close()

#How to append to a data file
myFile = open('myDataFile.txt','a')  #this time we are opening the file in append mode
myFile.write("\nThis new sentence will be appended")
myFile.close()

myFile = open('myDataFile.txt','r')
contentsOfMyFile = myFile.read()
print (contentsOfMyFile)

myFile.close()
