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
    disc = b * b - 4 * a * c
    rhs = math.sqrt(abs(disc))/(2*a)
    print(lhs)
    print(rhs)

    if disc > 0:
        print("Two Real Roots: " , lhs , " +/- " , rhs)
    elif disc == 0:
        print("One Real Root: ", lhs)
    elif disc < 0:
        print("Two Complex Roots: " , lhs , " +/- " , rhs , "i")    


############################################################################

while True:
    choice = input("Enter Operation: \n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide \n 5.Quadratic \n Choice:")
    if choice in ('1', '2', '3', '4'):
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
            a = float(input("Enter first coefficient: "))
            b = float(input("Enter second coefficient: "))
            c = float(input("Enter third coefficient: "))

            print("Quadratic: ", a , "x^2 + ", b, "x +", c)
            quadratic(a,b,c)

            if a == 0:
                print("A must not equal 0")
                break
        except Error:
            print("Input Error")
            continue

        repeat = input("Do you want to make another calculation? (y,n)")
        if repeat == "n":
            print("Have a good day :>")
            break
        else:
            print("Input Error")