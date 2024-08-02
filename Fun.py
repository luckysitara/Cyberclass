#!/usr/bin/env python3

def greet():

    message='effect of range in  loop'
    return (message)
g = greet()
print(g)

#ASSIGNMENTS
# why do we use return in function instead of print
#write some functions for 4 other arithmetic operations
#keyword arguments
#variable lenght argument and keyword variable lenght argument
def add(first, second):
    result = first + second
    return(result)


a = int(input("Enter the first number:  "))
b = int(input("Enter the second number: "))
s = add(a,b)

print(f'the sum of {a} and {b} is: {s}')

'''
positional arguments: positional arguments that are called in respect to their position
'''
def sum(a,b=7):
    c=a+b
    return(c)
w=sum(3,6)
print(w)
