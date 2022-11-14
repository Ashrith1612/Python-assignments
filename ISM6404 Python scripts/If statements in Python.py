#If statements in Python

YourScore = int(input("Please type your score: "))

if YourScore > 90:
    print(" your score is outstanding")
else:
    print("your score is not outstanding")
    
print("Outside the if strcture")

if YourScore > 90:
    print(" your score is outstanding")
elif YourScore > 80:
    print("Your score is not outstanding, but still very good")
else:
    print("Your score is not very good")


print("outside the second if strcture")

grade = ""
if YourScore >=90:
    grade = 'A'
elif YourScore >=80:
    grade = 'B'
elif YourScore >=70:
    grade = 'C'
elif YourScore >=60:
    grade = 'D'
else: 
    grade = 'F' 
'''  
    print (sum_of_two_nums(40,50))
        
    f_num = input("Please type the first number: "))
    s_num = input("Please type the second number: "))
        
print("The sum of the two numbers you typed is: ", sum_of_two_nums(f_num, s_num))
'''
YourScore = int(input("Please type your score:"))  
print ("Your grade for your score is: ",grade(YourScore))

