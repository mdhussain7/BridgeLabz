import re
from datetime import date


class RegulerEx:

    def input(self):
        mystring = '''Hello <<name>>, We have your full name as <<full name>> in our system,
                        your contact number is 91-xxxxxxxxxx,
                        Please,let us know in case of any clarification 
                        Thank you BridgeLabz 01/01/2016. '''
        today = date.today()

        d = today.strftime('%d/%m/%Y')
        fname = str(input("Enter the user frist name"))
        if not re.match("^[a-zA-Z]*$", fname):  # regex if invalid data
            print("Error! Only letters a-z allowed!")
        lname = str(input("Enter the last name"))
        if not re.match("^[a-zA-Z]*$", lname):  # regex if invalid data
            print("Error! Only letters a-z allowed!")
        mob = input("Enter mobile num")
        if not re.match("^[0-9]*$", mob):  # regex to check number
            print("Error! Only numerical 0-9 allowed!")

        if fname.isalpha() and lname.isalpha() and mob.isdigit():
            Full_name = fname + " " + lname
            mobile = '91-' + mob
            data = [fname, Full_name, mobile, d]
            pattern = ['<<name>>', '<<full name>>', '91-xxxxxxxxxx', '01/01/2016']
        for i in range(4):
            mystring = re.sub(pattern[i], data[i], mystring)  # regular expression to replace patterns by User data
        print(mystring)

obj = RegulerEx()
obj.input()
