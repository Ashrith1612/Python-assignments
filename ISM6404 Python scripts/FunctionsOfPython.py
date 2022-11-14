# Functions in Python
# In python, functions are defined using the def keyword
def sum_of_two_nums(first_num, second_num):
    return (first_num + second_num)
def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
def sum_of_all_elements(some_list):
    the_sum = 0
    for i in some_list:
        the_sum += i
    return the_sum
def avg_of_all_elements(some_list):
    the_sum = 0
    num_of_elements = 0
    for i in some_list:
        the_sum += i
        num_of_elements += 1
    average = the_sum/num_of_elements
    return average
    
    
'''
print (sum_of_two_nums(40,50))
f_num = int(input("Please type the first number: "))
s_num = int(input("Please type the second number: "))
print("The sum of the two numbers you typed is: ", sum_of_two_nums(f_num, s_num))
YourScore = int(input("Please type your score: "))
print ("The grade for your score is:", grade(YourScore))
'''
lst_of_some_numbers = [10,20,30,40,50,60]
print ("the sum of all the elements of my list 
=",sum_of_all_elements(lst_of_some_numbers))
print ("the average of all the elements of my list =", 
avg_of_all_elements(lst_of_some_numbers))
