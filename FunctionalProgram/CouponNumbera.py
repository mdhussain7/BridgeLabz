import random
from array import array


def main():
    n = int(input("Enter the number of card types:"))  # Taking the User input
    x = array('i', [1, 0])  # Array of cards with 0 and 1 fluctuation
    count = 0  # Total number of cards collected
    distinct = 0  # Number of distinct cards
    # repeatedly choose a random card and check whether it's a new one
    while distinct < n:
        value = int((random.randint(0, n)) * n-1)  # random card between 0 and n-1
        print("Random Number Generated:\t", value)
        count = count + 1  # we collected one more card
        print("Count of each random Number:\t", count)
        res = isCollected(value, n)
        y = x[res]
        # print(y)
        if not y:
            distinct = distinct + 1
            # isCollected = True
        print("The total number of cards collected =\t", count)
        # print("The distinct elements:",distinct)


#  Checking the random numbers

def isCollected(value, n):
    if value <= n:
        return 1
    else:
        return 0


# Driver Code

main()
