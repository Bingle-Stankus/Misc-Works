# Simple Calculator in Python
# By: Ryan Pointer #a

###### IMPORTS #############################################################
import math
############################################################################

###### OPERATIONS ##########################################################

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

def quadratic(a, b, c):
    lhs = (-b)/(2*a)
    rhs = math.sqrt(abs(b * b - 4 * a *c))/(2*a)


############################################################################

while True:
    choice = input("Enter Operation: \n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide \nChoice:")
    if choice in ('1', '2', '3', '4',):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except Error:
            print("Input Error")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", addition(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtraction(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiplication(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", division(num1, num2))

    elif choice in ('5'):
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            c = float(input("Enter third number: "))
        except Error:
            print("Input Error")
            continue

        print("Coefficients: ", a , "x^2 + ", b, "X +", c)

        repeat = input("Do you want to make another calculation? (y,n)")
        if repeat == "n":
            print("Have a good day :>")
            break
        else:
            print("Input Error")