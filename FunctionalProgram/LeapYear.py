year = int(input("Please Enter the Year : ")) # Taking the year input
y = year # Storing the input
Count = 0
while y > 0:
    y = y // 10
    Count = Count + 1 # Getting the Count of the input till it becomes Zero

if Count == 4:  # Checking the count is exactly 4
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):  # Logic of Leap year
        print("%d is a Leap Year" % year)
    else:
        print("%d is Not a Leap Year" % year)
else:
    print("Please Enter the 4 digit number")
