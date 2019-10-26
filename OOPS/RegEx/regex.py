import re
import warnings
from datetime import date
warnings.simplefilter(action='ignore', category=FutureWarning)
class PatternMatching:
    
    def pattern():
    
        Fname = input(" Enter your First Name : ")
        if not re.match("^[a-zA-Z]*$", Fname):  
            print("Error! Only letters a-z allowed!")
            
            
        Mname = input(" Enter your Middle Name : ")
        if not re.match("^[a-zA-Z]*$", Mname):  # regex if invalid data
            print("Error! Only letters a-z allowed!")
            
            
        Lname = input(" Enter your Last Name : ")
        if not re.match("^[a-zA-Z]*$", Lname):  # regex if invalid data
            print("Error! Only letters a-z allowed!")
            

        FullName = Fname + " " + Mname + " " + Lname
        print(FullName)
        
        today = date.today()
        dates = today.strftime('%d/%m/%Y')
        
        pnum = input("Enter the Mobile Number:")

        if not re.match("^[0-9]*$", pnum):  # regex to check number
            print("Error! Only numerical 0-9 allowed!")
    
        cont = list()

        f = input("Enter the File Name: ")
        with open(f, "r") as wf:
            con = wf.readlines()
            #cont.append(con)
        print(con)
    
        #for i in con:
         #   text = str(con[i])
        #print(text)
    

        cont = con
        if Fname.isalpha() and Lname.isalpha() and pnum.isdigit() and Mname.isalpha():
            number = '91-' + pnum
            data = [Fname, FullName,number,dates] 
            pat = ['<<name>>', '<<full name>>', '91-xxxxxxxxxx', '01/01/2016']

        for i in range(4):
            cont = re.sub(pat[i],data[i],str(cont))
        print(cont)

        f = open('newReg.txt','w+')
        f.write(cont)
        f.close()
        

#Driver Code

if __name__ == '__main__':
    PatternMatching.pattern()
    

