import math
import datetime


class Utility:
    @staticmethod
    def checkAnagram(s1, s2):
        if sorted(s1) == sorted(s2):
            return True
        else:
            return False

    @staticmethod
    def primes_method(n):
        out = list()
        logic = [True] * (n + 1)
        for p in range(2, n + 1):
            if logic[p]:
                out.append(p)
                for i in range(p, n + 1, p):
                    logic[i] = False
        return out

    @staticmethod
    def palindromeNumbers(list_a):
        c = 0
        for i in list_a:
            t = i
            rev = 0
            while t > 0:
                rev = rev * 10 + t % 10
                t = t / 10
            if rev == i:
                print(i)
                c = c + 1
        print()
        print("Total palindrome nos. are", c)
        print()

    @staticmethod
    def compare(a, b):
        for x, y in zip(a, b):
            if x == y:
                return True
            else:
                return False

    @staticmethod
    def anagram(res):
        if res:
            return "are Anagram."
        else:
            return "are not Anagram."

    @staticmethod
    def isPalindrome(s):
        rev = ''.join(reversed(s))
        if s == rev:
            return True
        return False

    @staticmethod
    def binarySearch(arr, l, r, key):  # l = low, r = high
        if r >= l:
            mid = int(l + (r - l) / 2)
            if arr[mid] == key:
                return mid
            elif arr[mid] > key:
                return Utility.binarySearch(arr, l, mid - 1, key)
            else:
                return Utility.binarySearch(arr, mid + 1, r, key)
        else:
            return -1

    @staticmethod
    def insertionSort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
                arr[j + 1] = key
        return arr

    @staticmethod
    def bubbleSort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    @staticmethod
    def find(low, up):
        if low == up:
            print()
            print("Your number is : ", low)
            print()
            print("The Intermediary numbers is ", (low - 1), " and ", (low + 1))
            return 0
        mid = int((low + up) / 2)
        print("Press 1 : ", low, " - ", mid)
        print("Press 2 : ", (mid + 1), " - ", up)
        ch = int(input())
        if ch == 1:
            Utility.find(low, mid)
        else:
            Utility.find(mid + 1, up)

    @staticmethod
    def check(n, f):
        try:
            with open(f) as f:
                datafile = f.readlines()
            found = False  # This isn't really necessary
            for line in datafile:
                if n in line:
                    # found = True # Not necessary
                    return True
            return False  # Because you finished the search without finding
        except FileNotFoundError:
            print("Enter the Valid File Name")

    @staticmethod
    def mergeSort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2  # Finding the mid of the array
            L = arr[:mid]  # Dividing the array elements
            R = arr[mid:]  # into 2 halves
            Utility.mergeSort(L)  # Sorting the first half
            Utility.mergeSort(R)  # Sorting the second half
            i = j = k = 0
            # Copy data to temp arrays L[] and R[]
            while (i < len(L)) and (j < len(R)):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                    k += 1
            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    @staticmethod
    def printList(arr):
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()

    @staticmethod
    def vendingMachine(amount):
        notes = [1000, 500, 200, 100, 50, 10, 5, 2, 1]
        noteCounter = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        counter = 0
        print("Your Currency Count is given Below: ")
        for i, j in zip(notes, noteCounter):
            if amount >= i:
                j = amount // i
                amount = amount - j * i
                j = j + 1
                print(i, "  : ", j)

    @staticmethod
    def squareRoot(n, epsilon):
        t = n
        while abs(t - n / t) > epsilon * t:
            t = (n / t + t) / 2.0
        print()
        print("Square Root of the number:'", n, "' with Newton's Formula is '", t, "'")
        print()

    @staticmethod
    def decimalToBinary(n):
        return bin(n).replace("0b", "")

    @staticmethod
    def binaryToDecimal(binary):
        b = binary
        decimal, i, n = 0, 0, 0
        while binary != 0:
            rem = binary % 10
            decimal = decimal + rem * pow(2, i)
            binary = binary // 10
            i += 1
        return decimal

    @staticmethod
    def swapNibbles(x):
        return (x & 0x0F) << 4 | (x & 0xF0) >> 4

    @staticmethod
    def Log2(x):
        return math.log10(x) / math.log10(2)

    @staticmethod
    def isPowerOfTwo(n):
        return math.ceil(Utility.Log2(n)) == math.floor(Utility.Log2(n))

    @staticmethod
    def cel_to_fahr(c):
        c = c * 9 / 5 + 32
        return c

    @staticmethod
    def fahr_to_cel(f):
        f = (f - 32) * (5 / 9)
        return f

    @staticmethod
    def monthlyPayment(Y, P, R):
        n = 12 * Y
        r = float(R / (12 * 100))
        denominator = float(1 - (pow((1 + r), (-n))))
        numerator = float(P * r)
        payment = float(numerator / denominator)
        return payment


u = Utility()


def main():

    n = int(input(
        "Press \n 1. Anagram \n 2. Palindrome \n 3. Anagram Palindrome \n 4. Binary Search Integer \n 5. Binary "
        "Search String \n 6. Insertion Sort Integer \n 7. Insertion Sort String \n 8. Bubble Sort Integer \n 9. "
        "Bubble Sort String \n 10. To Find the number in your mind \n 11. To Find word from a file \n 12. Merge Sort "
        "String \n 13. Merge Sort Integer \n 14. Vending Machine \n 15. Square Root of a Number Using Newton's Method "
        "\n 16. Number Conversion from Binary to Decimal and vice versa \n 17. Number Conversion and performing "
        "Nibble Operations \n 18. To Find the Day of the Week \n 19. Temperature Conversion \n 20. Monthly Payment \n "
        "21. Exit \n"))
    if n == 1:
        s1 = input("Enter the String1: ")
        print()
        s2 = input("Enter the String2: ")
        print()
        res = u.checkAnagram(s1, s2)
        print(s1, " and ", s2, " ", u.anagram(res))
        print("Bye!")
    elif n == 2:
        end = int(input("Enter the number:"))
        print()
        a = u.primes_method(end)
        print("Prime Numbers are:", a)
        b = str(a)
        # print(b,type(b))
        print(u.anagram(b))
        print("Palindrome numbers are:")
        u.palindromeNumbers(a)
        print("Bye!")
    elif n == 3:
        print("You are here to check Anagram Strings are Palindrome or not")
        s1 = input("Enter the String1: ")
        print()
        s2 = input("Enter the String2: ")
        print()
        res = u.checkAnagram(s1, s2)
        print(s1, " and ", s2, " ", u.anagram(res))
        print()
        com = u.compare(s1, s2)
        # print(com)
        if com:
            pal = u.isPalindrome(s1)
            # print(pal)
            if pal:
                print(s1, " is palindrome")
            else:
                print(s1, " is Not a Palindrome")
        elif not com:
            pal1 = u.isPalindrome(s1)
            pal2 = u.isPalindrome(s2)
            # print(pal1)
            # print(pal2)
            if (pal1 == True) and (pal2 == True):
                print(s1, " and ", s2, " are 'Palindrome'")
            elif (pal1 == False) and (pal2 == False):
                print(s1, " and ", s2, " are 'Not palindrome'")
            elif (pal1 == True) and (pal2 == False):
                print(s1, " is a 'Palindrome'.\n But ", s2, " is 'Not palindrome'")
            elif (pal1 == False) and (pal2 == True):
                print(s1, " is 'Not a Palindrome'.\n But ", s2, " 'is a Palindrome'")
        else:
            print("Enter the Proper Strings")
        print("Bye!")
    elif n == 4:
        n = int(input("Enter the Number of elements you want to insert:"))
        arr = list()
        print("Enter the elements:")
        for i in range(n):
            arr.append(int(input()))
        key = int(input("Enter the Key element:"))
        result = u.binarySearch(arr, 0, len(arr) - 1, key)
        if result != -1:
            print("Element is present at index %d" % result)
        else:
            print("Element is not present in array")
        print("Bye!")
    elif n == 5:
        n = int(input("Enter the Number of elements you want to insert:"))
        arr = list()
        print("Enter the elements in ascending order: (i.e from A-Z)")
        for i in range(n):
            arr.append(input())
        key = input("Enter the Key element:")
        result = u.binarySearch(arr, 0, len(arr) - 1, key)
        # print(result)
        if result != -1:
            print("Element is present at index %d" % result)
        else:
            print("Element is not present in array")
        print("Bye!")
    elif n == 6:
        n = int(input("Enter the number of elements you want to insert:"))
        arr = list()
        print("Enter the Elements:")
        for i in range(n):
            arr.append(int(input()))
        a = u.insertionSort(arr)
        print("Sorted array is:")
        for i in range(len(a)):
            print("%d" % a[i])
        print("Bye!")
    elif n == 7:
        n = int(input("Enter the number of elements you want to insert:"))
        arr = list()
        print("Enter the Elements:")
        for i in range(n):
            arr.append(input())
        a = u.insertionSort(arr)
        print("Sorted array is:")
        for i in range(len(a)):
            print("%s" % a[i])
        print("Bye!")
    elif n == 8:
        n = int(input("Enter the Number of elements:"))
        arr = list()
        print("Enter the Elements:")
        for i in range(n):
            arr.append(int(input()))
        a = u.bubbleSort(arr)
        print("Sorted array is:")
        for i in range(len(a)):
            print("%d" % a[i])
        print("Bye!")
    elif n == 9:
        n = int(input("Enter the Number of elements:"))
        arr = list()
        print("Enter the Elements:")
        for i in range(n):
            arr.append(input())
        a = u.bubbleSort(arr)
        print("Sorted array is:")
        for i in range(len(a)):
            print("%s" % a[i])
        print("Bye!")

    elif n == 10:
        choice = int(input("Press 1 to Continue:"))
        if choice == 1:
            n = int(input("Enter the Range  (N) :"))
            u.find(0, n - 1)
        else:
            print("Please enter the valid number to Continue:")
        print("Bye!")
    elif n == 11:
        n = input("Enter the word You want to search: ")
        f = input("Enter the file name: ")
        res = u.check(n, f)
        if res:
            print("' ", n, " ' Found in the file '", f, "'")
        else:
            print("' ", n, " ' Not Found in the file '", f, "'")
            print("---------- May be File not So does the word ----------")
        print("Bye!")
    elif n == 12:
        n = int(input("Enter the number of element's that you want to insert:"))
        arr = list()
        print("Enter the elements:")
        for i in range(n):
            arr.append(input())
        print("Given array is", end="\n")
        u.printList(arr)
        u.mergeSort(arr)
        print("Sorted array is: ", end="\n")
        u.printList(arr)
        print("Bye!")
    elif n == 13:
        n = int(input("Enter the number of element's that you want to insert:"))
        arr = list()
        print("Enter the elements:")
        for i in range(n):
            arr.append(int(input()))
        print("Given elements: ", end="\n")
        u.printList(arr)
        u.mergeSort(arr)
        print("Sorted elements: ", end="\n")
        u.printList(arr)
        print("Bye!")
    elif n == 14:
        amount = int(input("Enter the amount in Rs:"))
        a = list()
        a = a.append(u.vendingMachine(amount))
        print(a)
        print("Bye!")
    elif n == 15:
        n = float(input("Enter the Number:"))
        epsilon = float(1e-15)
        u.squareRoot(n, epsilon)
        print("Bye!")
    elif n == 16:
        n = int(input("Press \n 1. Decimal To Binary \n 2. Binary To Decimal \n"))
        if n == 1:
            n = int(input("Enter the Number to convert as Binary:"))
            binary = u.decimalToBinary(n)
            print(n, " to binary is ", binary)
            print("Bye!")
        elif n == 2:
            binary = int(input("Enter the Number to convert as Binary:"))
            decimal = u.binaryToDecimal(binary)
            print(binary, " to decimal is ", decimal)
            print("Bye!")
        else:
            print("Enter the Proper Input!!")
            print("Bye!")
    elif n == 17:
        n = int(input("Enter the Number:"))
        swap = u.swapNibbles(n)
        print(n, " After Swapping to Nibbles : ", swap)
        print()
        res = u.decimalToBinary(swap)
        print(swap, " After converting to binary : ", res)
        print()
        firstHalf = res[:4]
        secondHalf = res[4:]
        print("After Dividing ", res, " to ", firstHalf, " and ", secondHalf)
        print()
        b2d = u.binaryToDecimal(int(res))
        b2d1 = u.binaryToDecimal(int(firstHalf))
        b2d2 = u.binaryToDecimal(int(secondHalf))
        print(res, "After Converted to Decimal ", b2d)
        print(firstHalf, "After Converted to Decimal ", b2d1)
        print(secondHalf, "After Converted to Decimal ", b2d2)
        print("Want to Check the number is a Power of 2 or Not:")
        print()
        print("Press \n 1. Check for ", b2d, "\n 2. Check for ", b2d1, "\n 3. Check for ", b2d2, "\n 4. Exit \n")
        print()
        check = int(input())
        if check == 1:
            if u.isPowerOfTwo(b2d1):
                print(b2d, " is Power of 2")
                print()
            else:
                print(b2d, " is Not a Power of 2")
                print()
        elif check == 2:
            if u.isPowerOfTwo(b2d1):
                print(b2d1, " is Power of 2")
                print()
            else:
                print(b2d1, " is Not a Power of 2")
                print()
        elif check == 3:
            if u.isPowerOfTwo(b2d1):
                print(b2d2, " is Power of 2")
                print()
            else:
                print(b2d2, " is Not a Power of 2")
                print()
        elif check == 4:
            exit()
            print("Bye!!")
    elif n == 18:
        week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        l = list(map(int, input(" Enter date Ex: dd/mm/yyyy \n").split('/')))
        day = datetime.date(l[2], l[1], l[0]).weekday()
        print(week_days[day])
        print("Bye!!")
    elif n == 19:
        value = int(input("Enter the value:"))
        op = int(input("Press \n 1. For Celcius conversion \n 2. For Fahrenheit Conversion\n"))
        if op == 1:
            print(value, "  is converted to Celcius : ", u.fahr_to_cel(value))
        elif op == 2:
            print(value, "  is converted to Fahrenheit : ", u.cel_to_fahr(value))
        else:
            print("Invalid Input")
    elif n == 20:
        print("Want to Know your monthly Payment Details?")
        print("Follow the below instructions:")
        Y = int(input("Enter the years:"))
        P = int(input("Enter the Principal Loan Amount:"))
        R = int(input("Enter the Monthly Cent Interest:"))
        res = u.monthlyPayment(Y, P, R)
        print("Your Monthly Payment with year: ", Y, " Principal Loan Amount: ", P, " Interest ", R, " ")
        print("Total Amount: ", res)

    elif n == 21:
        exit()


main()
