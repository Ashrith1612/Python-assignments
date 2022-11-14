# Some variations of parameter lists in functions

def some_functions(a,b,c,d):
    print(a,b,c,d)
    
#default parameters
def some_function_2(a,b,c,d=10):
    print(a,b,c,d)
    
def some_function_3(a,b,c=100,d=200):
    print(a,b,c,d)
    
#variable number of parameters

def addNumber(num):
    sum = 10
    for i in num:
        sum += i
    return sum
    
some_function(10,20,30,40)

some_function_2(10,20,30)

some_function_2(10,20,30,40)

some_function_3(10,20)
some_function_3(10,20,30)
some_function_3(10,20,30,40)

