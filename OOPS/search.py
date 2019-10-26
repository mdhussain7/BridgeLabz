import json
from difflib import get_close_matches
try:
    data = json.load(open("CompanyShares.json"))
except FileNotFoundError:
    print(" Invalid File Name")


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if ((yn == "Y") or (yn == "y")):
            return data[get_close_matches(w, data.keys())[0]]
        elif ((yn == "N")or(yn == 'n')):
            return "The Company doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The Company doesn't exist. Please double check it."

try:
    while True:
        
        file = open("CompanyShares.json", "r+")
        item = json.load(file)
        file.close()
                
        for key in item:
            print("\n ------- ", key, " ------- \n")

            for value in item[key]:        
                print("Company:", value['Company'])
                print("Current:", value['Current'])
                print("%Gain:", value['%Gain'])
                
                llist = list()
                llist.append(value)
                
                print("\n------------------------------\n")
                f = open("Company.txt", "a+")
                f.write(str(llist)+",")
                print("Data is Written into 'Company.txt' Successfully")
                print()
                #print(llist)
                #print(value)
        word = input("Enter the Company: ")        
        output = translate(word)
        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)
except KeyboardInterrupt:
    print()
    print("Bye!!")
    print()
except ValueError:
    print()
    print("Enter the proper word to get definitions")
    print()
