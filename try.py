from math import pow
from exceptions import *

def result(y,x):
    try:
        pow(y,x)
    except:
        print(("Error: cant do a root to a negative number"))
    else:
        x=pow(y,x)
        print (x)

def modolo(x,y):
    try:
        x= x%y
    except ZeroDivisionError:
        print("Error: can not divide by 0")
    else:
        print (x)

def Factorial(y):
    if y < 0:
        raise NegativeInFactorial()
    if int(y) != y:
        raise FloatInFactorial()
    else:
        x = 1
        for i in range(2, y + 1):
            x *= i
        print (x)
def main():
    my_string = "This is a sample string."
    split_location = 10

    # Split the string into two parts
    first_part, second_part = my_string[:split_location], my_string[split_location:]
    print("First part:", first_part)
    print("Second part:", second_part)
main()