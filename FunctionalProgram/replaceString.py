import string

str1 = "Hi, \n"  # Variable to store the string "Hi"
str2 = "Good Morning"  # Variable to Store the String "Good Morning"
str3 = "Fellow"  # Variable to Store the String "Fellow"
print("The Statement is ")
print("'", str1, str3, str2, "'") # Printing the String
rep = input("\nEnter the Replacing String for 'Fellow': ")
if len(rep) >= 3: # Checking the Condition for string length with min length of 3
    print("\nString can be Replaced")
    print("\nStatement Before Replacing")
    print(str1, str3, str2)
    print("\nStatement After Replacing")
    # print(str.replace(str3,str3,rep))
    repl = str.replace(str3, str3, rep)  # Replacing Logic for the String
    print("'", str1, repl, str2, "'")
else:
    print("!!! String cannot be Replaced !!!")
