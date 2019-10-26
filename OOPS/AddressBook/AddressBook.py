import json
import sys
import re

class AddressBook:
    def __init__(self):
        self.list = []

    def create(self):
        self.list = {'data': []}
        #file = input('Enter the file wich you want to create: \n')
        with open('Address.json', 'a+') as f:
            json.dump(self.list, f, indent=2)
            f.close()
            print('File Successfully Created..')

    def open(self):
        #file = input("Enter the file which you want to open: \n")
        try:
            with open('Address.json', 'r') as f:
            #with open('Addressdata.json', 'r') as f:
                self.list = json.load(f)
        except FileNotFoundError:
            print("Invalid File Name")

    def sort(self):
        for i in range(len(self.list['data'])):
            for j in range(len(self.list['data'])):
                if self.list['data'][i]['zipcode'] < self.list['data'][j]['zipcode']:
                    (self.list['data'][i], self.list['data'][j]) = (self.list['data'][j], self.list['data'][i])
        self.display()

    def sortName(self):
        for i in range(len(self.list['data'])):
            for j in range(len(self.list['data'])):
                if self.list['data'][i]['fname'] < self.list['data'][j]['fname']:
                    self.list['data'][i], self.list['data'][j] = (self.list['data'][j], self.list['data'][i])
        self.display()

    def add(self):
        addnew = {}
        Fname = input(" Enter Your First Name : ")
        if not Fname.isalpha():

            print("Please Enter your Name in Albhatic Manner: ")
            Fname = input("Enter your Name")
            addnew['Fname'] = Fname

        elif not re.match("^[a-zA-Z]*$", Fname):
            addnew['Fname'] = Fname
        addnew['Fname'] = Fname

        Lname = input(" Enter Your Last Name : ")

        if not Lname.isalpha():

            print("Please Enter your LName in Alphabatic Manner: ")
            Lname = input(" Enter Your Last Name : ")
            addnew['Lname'] = Lname

        elif not re.match("^[a-zA-Z]*$", Lname):
            addnew['Lname'] = Lname
        addnew['Lname'] = Lname

        mob = input(" Enter Your Mobile Num:  ")

        if not mob.isnumeric():

            print("Please Enter your Mobile Number in Numeric Manner: ")
            mob = input(" Enter Your Mobile Num:  ")
            addnew['mobile'] = mob

        elif not re.match("^[0-9]*$", mob):
            addnew['mobile'] = mob
        addnew['mobile'] = mob

        area = input(" Enter Your Area : ")

        if not area.isalnum():

            print("Please Enter your Area Name in Alphabatic Manner: ")
            area = input(" Enter Your Area : ")
            addnew['area'] = area

        elif not re.match("^[a-zA-Z]*$", area):
            addnew['area'] = area
        addnew['area'] = area

        city = input(" Enter Your City :  ")

        if not city.isalpha():

            print("Please Enter your City Name in Alphabatic Manner: ")
            city = input(" Enter Your City :  ")
            addnew['city'] = city

        elif not re.match("^[a-zA-Z]*$", city):
            addnew['city'] = city
        addnew['city'] = city

        zipcode = input(" Enter Your Zipcode : ")

        if not zipcode.isnumeric():

            print("Please Enter your ZipCode in Numeric Manner: ")
            zipcode = input(" Enter Your Zipcode : ")
            addnew['zipcode'] = zipcode

        elif not re.match("^[0-9]*$", zipcode):
            addnew['zipcode'] = zipcode
        addnew['zipcode'] = zipcode

        state = input(" Enter Your State: ")

        if not state.isalpha():
            print("Please Enter your State Name in Alphabatic Manner: ")
            state = input(" Enter Your State: ")
            addnew['state'] = state

        elif not re.match("^[a-zA-Z]*$", state):
            addnew['state'] = state
        addnew['state'] = state

        self.list['data'].append(addnew)
        self.save()
        self.display()

    def newGet(self):
        file = open("Addressdata.json", "r")
        data_item = json.load(file)
        file.close()
        print("----- INVENTORY -----")
        for key in data_item:
            print("-------", key, "-------")
            for value in data_item[key]:
                price = weight = 0
                print("First Name :", value['name'])
                price += int(value["price"])
                weight += int(value["weight"])
                print("Weight : ", weight)
                print("Price : ", price)
                print()

    def update(self):
        flag = update = False
        if len(self.list['data']) >= 1:
            Fname = input("Enter the First Name ")
            Lname = input("Enter the Last Name ")
            for i in range(len(self.list['data'])):
                if (self.list['data'][i]['Fname'] == self.list['data'][i]['Fname']) and (
                        self.list['data'][i]['Lname'] == self.list['data'][i]['Lname']):
                    flag = True
                    if flag:
                        op = int(
                            input(" Select AnyOne Option to update your Profile\n 1 Mobile \n 2 Area \n 3 Zipcode \n 4 City \n 5 State \n "))
                        if op == 1:
                            mob = int(input("Enter Mobile num "))
                            self.list['data'][i]['mob'] = mob
                            update = True
                            self.display()
                        elif op == 2:
                            street = input("Enter the Street ")
                            self.list['data'][i]['street'] = street
                            update = True
                            self.display()
                        elif op == 3:
                            zipcode = int(input("Enter the zipcode num "))
                            self.list['data'][i]['zipcode'] = zipcode
                            update = True
                            self.display()
                        elif op == 4:
                            city = input("Enter the city ")
                            self.list['data'][i]['city'] = city
                            update = True
                            self.display()
                        elif op == 5:
                            state = input("Enter the state")
                            self.list['data'][i]['state'] = state
                            update = True
                            self.display()
                        else:
                            print("Invalid Option")
                            update = False
                            self.update()
                    else:
                        print('Enter numericals only')
                        self.update()
                else:
                    print("Enter valid name")
                    self.update()

    def save(self):
        file = input('Enter the file name: ')
        with open(file + '.json', 'w+') as j:
            json.dump(self.list, j, indent=2)
            j.close()

    def display(self):
            print(self.list)
            if len(self.list['data']) >= 1:
                print("Data in the file is Given below: \n")
                print('First Name \t\t\t Last Name \t\t\t\t Mobile \t\t\t\t\t Adress \t\t\t\t Zipcode \t\t\t\t\t City \t\t\t\t\t State \n')
                try:
                    for i in range(len(self.list['data'])):
                        print(self.list['data'][i]['Fname'], "\t\t\t\t", self.list['data'][i]['Lname'], "\t\t\t\t",
                              self.list['data'][i]['mobile'], "\t\t\t\t", self.list['data'][i]['area'], "\t\t\t\t",
                              self.list['data'][i]['zipcode'], "\t\t\t\t", self.list['data'][i]['city'], "\t\t\t\t",
                              self.list['data'][i]['state'], "\n")
                except ValueError:
                    print("Invalid Key")

            else:
                print("No data found")
                ch = input('do you want to Add new record? : Enter = y/n ')
                if ch.upper() == 'y' or ch == 'yes' or ch == 'Yes':
                    self.add()
                else:
                    sys.exit()


    def remove(self):
        if len(self.list['data']) >= 1:
            Fname = input("Enter the First Name ")
            Lname = input("Enter the Last Name ")
            for i in range(len(self.list['data'])):
                if (str(self.list['data'][i]['Fname']).casefold() == Fname.casefold()
                        and str(self.list['data'][i]['Lname']).casefold() == Lname.casefold()):
                    print(" Data Removed Successfully ")
                    del self.list['data'][i]
                    self.save()
                    self.display()
                    return
                else:
                    print(' Data Not Found ')
