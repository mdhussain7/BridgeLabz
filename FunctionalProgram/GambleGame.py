import random
import string


# Gambling logic
def gamble(stake, goal):
    win = 0
    loss = 0
    totalGambles = 0
    while not ((stake == 0) or (stake == goal)):
        Gamble = random.randint(0, 2)  # Taking the random input
        #print(Gamble)
        totalGambles += 1  # Checking the Count of Gambling
        if Gamble == 0:  # Checking the Gambling number
            stake += 1  # Incrementing the Stake value
            print(" ---Yeh you won!--- and --- now You have --- ", stake, ".   --- goal ---:", goal)
            win += 1
        else:
            stake -= 1
            print(" ---Bad luck!You lost!--- and --- now You have --- ", stake, ".  --- goal --- :", goal)
            loss += 1
    print(" You won ", win, " times ")
    print(" You Lost ", loss, " times ")
    print(" Your Total Gamble Played ", totalGambles, " times")
    win_p = float((win / totalGambles) * 100)  # Getting the Percentage of Winning
    print(" Win Percent%", win_p)
    loss_p = float((loss / totalGambles) * 100)  # Getting the Percentage of Loosing
    print(" Loss Percent%", loss_p)


# Driver Code
if __name__ == "__main__":
    print("Want to Play?(y/n)")
    choice = input("Enter the character: \n")  # Checking for
    while (choice == "y") or (choice == "Y"):
        stake = int(input("Enter the Stake:"))
        while stake < 1:
            print("\nHey you can't start empty handed!")
            print("\nPlease enter an amount greater than 0")
            stake = int(input("Enter the Stake:"))
            print("\nEnter your goal!")
            goal = int(input())  # Taking the  goal estimation
            while goal < stake:
                print("\nDear to be millionaire, your here to win! So enter an amount greater than your stake!")
                goal = int(input("Enter your goal: "))  # Taking the minimum stake
            gamble(stake, goal)  # Function Call
        goal = int(input("\nEnter your goal!"))  # Goal to gain Profit
        gamble(stake, goal)  # Function Call
