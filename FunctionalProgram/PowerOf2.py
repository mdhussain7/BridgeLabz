n = int(input("Enter the number:"))
for i in range(pow(2, n)):
    print("2 *", i, " = ", (2 * i)) #
    if ((2 * i) % 400 == 0) or (((2 * i) % 4 == 0) and ((2 * i) % 100 != 0)): # Leap Year Condition
        print("%d is a Leap Year" % (2 * i))
    else:
        print("%d is Not a Leap Year" % (2 * i))
