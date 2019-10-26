def min_to_hour(min):
    hour = min/60
    return hour

def sec_to_hour(sec):
    hour = sec/3600
    return hour

def main():
    min = int(input("Enter the minutes that you want to convert into hours: "))
    mh = min_to_hour(min)
    sec = int(input("Enter the seconds that you want to convert into hours: "))
    sh = sec_to_hour(sec)
    print("Minutes '",min,"' after converting to hours is '",mh,"'")
    print("Seconds '",sec,"' after converting to hours is '",sh,"'")

main()
