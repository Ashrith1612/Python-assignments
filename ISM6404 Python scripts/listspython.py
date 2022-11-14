# We will learn about lists
# Lists are used lots in Python

#How to declare a list?
# using square brackets []

first_name = [] # here, first_name is the name of a list because we used square brackets

first_name = ["John", "Nancy", "Barb", "Kathy", "Peter", "Bob"]

#How to access the elements of a list?
#Each element has an index value
#The index value of the first element is 0

print (first_name)   #this will print the entire list
print(first_name[0])  #this will print John, because John is the first element and has an index value of 0

print(first_name[5]) #This will print Bob

print(first_name[6]) #This will give an error

#To access the last element, we can use the index value of -1

print(first_name[-1]) # this will print the last element which is Bob
print(first_name[-3]) # this will print Kathy

#How to access a partial list?

print(first_name[2:5])

#You can assign a list to another list variable

partial_first_name = first_name[0:4]

print(partial_first_name)

#How to insert an element somewhere in the middle?

#Suppose we wanted to insert Pat at 4th place (index value of 3)

first_name.insert(3,"Pat")

print(first_name)

#Second approach: using the pop function
first_name.pop(2) # this will delete since Kathy is at index value

