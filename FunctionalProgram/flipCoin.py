import random

n = 0


def flipCoin():
    heads = 0  # track heads amount
    tails = 0  # track tails amount
    headspercent = 0  # heads percentage
    tailspercent = 0  # tails percentage
    n = int(input("How many times DO you want to Flip Coin?"))
    if n >= 0:
        for i in range(n):  # run the experiment n times
            coin = random.randint(0, 1)  # assign a value to coin, either 0 or 1

            if coin == 0:  # if coin value is assigned as 0
                heads += 1  # increase heads count by 1
            else:  # if coin value is assigned something other than 1
                tails += 1  # increase tails count by 1

            headspercent = ((heads / (heads + tails)) * 100)  # since we're rolling n times this will give percentage
            tailspercent = ((tails / (heads + tails)) * 100)  # since we're rolling n times this will give percentage

        print("Heads percent: " + str(headspercent))  # printing the values on screen
        print("Tails percent: " + str(tailspercent))  # converting numbers to string by str()
    else:
        print("Enter the positive Number:")

# Driver code

flipCoin()
