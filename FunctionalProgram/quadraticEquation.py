import math  # Importing the Math package form the python

name = input("Enter your name :\n ")  # Taking the input for the User name
print("Hi, '", name, "'.")
print(name, ", you are here for finding the real and imaginary roots")
print("\n Equation is 'Ax*x + Bx + C' ")
print("\n Please give the following details:")

try:
    a = int(input(" Enter the value of 'A' : \n "))  # Taking the input for Value of 'A'

    b = int(input(" Enter the value of 'B' : \n "))  # Taking the input for Value of 'B'

    c = int(input(" Enter the value of 'C' : \n "))  # Taking the input for Value of 'C'

    if a != 0:
        d = (b * b) - (4 * a * c)  # Calculating the determinant Value
        if d > 0:  # Checking if the value of d is '>' than '0'
            root1 = float((-b + math.sqrt(d)) / (2 * a))  # Printing the value of root1 .i.e: (-b + Square Root of d)/(
            # 2*a)
            root2 = float((-b - math.sqrt(d)) / (2 * a))  # Printing the value of root2 .i.e: (-b - Square Root of
            # d)/(2*a)
            print(" root1 = %.2f", root1, " and root2 = %.2f", root2)
        elif d == 0:  # Checking if the value of d is '=' to '0'
            root1 = root2 = -b / (2 * a)  # printing the value of root 1 and root 2 .i.e: (-b /(2*a))
            print(" root1 = root2 = ", root1)
        else:
            realPart = float(-b / (2 * a))  # printing the value of realPart .i.e: (-b/(2*a))
            imaginaryPart = float(math.sqrt(-d) / (2 * a))  # printing the value of ImaginaryPart .i.e: (-b/(2*a))
            print(" root1 = ", realPart, " + ", imaginaryPart, " i")
            print()
            print(" root2 = ", realPart, " - ", imaginaryPart, " i")
except ValueError:
    print(" Enter the Numeric value ")
except ZeroDivisionError:
    print(" Division by Zero Error ")
