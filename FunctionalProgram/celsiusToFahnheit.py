def c_2_f(c):
    c = [c * (9 / 5) + 32]  # Applying the formula (c = c*9/5+32)
    return c


def f_2_c(f):
    f = (f - 32) * (5 / 9)  # Applying the formula (f = (f-32)*(5/9)))
    return f


def main():
    value = int(input("Enter the value:"))  # Taking the User input
    op = int(input("Press 1 for  celsius conversion \n 2 for Fahrenheit Conversion\n"))  # Restricting the user by
    # using the option
    if op == 1:
        print(value, " is converted to Celsius : ", f_2_c(value))
    elif op == 2:
        print(value, " is converted to Fahrenheit : ", c_2_f(value))
    else:
        print("Invalid Input")


# Driver Code

main()
