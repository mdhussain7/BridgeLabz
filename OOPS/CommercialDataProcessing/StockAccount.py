import json

class StockAccount:


    def fileInput(self,filename):
        
        file = open(filename, "r+")
        item = json.load(file)
        file.close()
        print("-------------------- Account Data --------------------")
        for key in item:
            print("\n ------- ", key, " ------- \n")

            for value in item[key]:
                            
                print("Name :", value['name'])
                print("Age :", value['Age'])
                print("Dob :", value['Dob'])
                print("Address :", value['Address'])
                
                ls = list()
                ls.append(value)
                
                print("\n------------------------------\n")
                f = open("stockAccountData.json", "a+")
                f.write(str(ls)+",")
                print("Data is Written into 'stockAccountData.json' Successfully")
                print()
        
        file = open("Shares.json", "r+")
        item = json.load(file)
        file.close()
                
        for key in item:
            print("\n ------- ", key, " ------- \n")

            for value in item[key]:
                    
                print("Share :", value['share'])
                print("Amount:", value['amount'])
                print("Stock:", value['stock'])
                print("Symbol:", value['symbol'])
                
                ls = list()
                ls.append(value)
                
                print("\n------------------------------\n")
                f = open("stockAccountData.json", "a+")
                f.write(str(ls)+",")
                print("Data is Written into 'stockAccountData.json' Successfully")
                print()
        
        file = open("products.json", "r+")
        item = json.load(file)
        file.close()
                
        for key in item:
            print("\n ------- ", key, " ------- \n")

            for value in item[key]:        
                print("Product:", value['product'])
                print("Count:", value['count'])
                print("ProductionDate:", value['productionDate'])
                print("Investment:", value['investment'])
                
                ls = list()
                ls.append(value)
                
                print("\n------------------------------\n")
                f = open("stockAccountData.json", "a+")
                f.write(str(ls)+",")
                print("Data is Written into 'stockAccountData.json' Successfully")
                print()
                
                #amount += int(value["amount"])
                #count += int(value["count"])
                
        #print("Ampount : ", amount)
        #print("Count : ", count)
                
        #total = int(amount) * int(count)
                
        #print("Total Amount: ", total)
        #value['total'] = total
        #print(value)
                
                

            
        
        #StockAccount.valueOf(amount)
        #print(cont)
        
        
        
        
    def valueOf(self):
        f = open(filename,"r+")
        text = list()
        for i in f:
            text.append(f.readlines())
        print(text)
        #amount = int(input("Enter the amount that you want to spend on shares: ")
        #add = text.append(amount)
        
        
        
    def buy(amount,symbol):
        f = open(filename,"r+")
        cont = list()
        for i in f:
            print(f.readlines())
       
          
           
    def sell(amount,symbol):
        f = open(filename,"r+")
        cont = list()
        for i in f:
            cont = f.readlines()
        print(cont)
         
            
            
    def save(filename):
        
        
          
        f = open("StockA.txt","w+")
        cont = list()
        for i in f:
            cont = f.readlines()
        print(cont)
            
              
    def displayReport():
        f = open(filename,"w+")
        cont = list()
        for i in f:
            cont = f.readlines()
        print(cont)
        

StAc = StockAccount()

if __name__ == '__main__' :

    inp = input(" Are You having an Existing Account? (y/n):")
    
    if (inp == "y") or (inp == "Y"):
        filename = input("Enter the File name: ")
        StAc.fileInput(filename)
        StAc.valueOf()
        
    else:
        f = open("newUser.json","a+")
        name = input("Enter the Name: ")
        Age = int(input("Enter the Age: "))
        phno = int(input("Enter your Mobile Number: "))
        amount = int(input("Enter the Amount for Shares: "))
        cont = f.write(' [{'+'     "Name" : "'+ name +'",\n' + '        "Age"  : "'+str(Age)+'",\n'+'       "Ph.No" : "'+str(phno)+'",\n'+'"Share Amount" : "'+str(amount)+'" }]')
        print("The Data has been Stored Successfully in 'newUser.json' file. ")
        
        
        
        
