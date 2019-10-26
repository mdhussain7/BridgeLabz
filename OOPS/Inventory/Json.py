import json
import re
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)


class Json:

    def Inventory(self):

        fh = input("Enter the File Name:")
        try:
            with open(fh, 'r') as f:
                json_text = f.read()
        except FileNotFoundError:
            print('Invalid File Name')
            exit()

        # Decode the JSON string into a Python dictionary.
        data = json.loads(json_text)
        # print(data)

        # Encode the Python dictionary into a JSON string.
        strData = json.dumps(data, indent=0)
        # print(strData)

        cont = list()
        with open("data.json", "w") as wf:
            json.dump(strData, wf)

        print("\nThe data is Written in to the 'data.json' file in the present Directory ")
        # separate those non-digit characters
        print()

        res = re.split("\D+", strData)

        res1 = (re.split("[^a-zA-Z]*", strData))

        integr = []
        # print the result
        for elements in res:
            # print (elements)
            integr.append(elements)

        wwt = int(str(integr[1:2]).strip("['']"))
        # print(wwt)
        wppkg = int(str(integr[2:3]).strip("['']"))
        # print(wppkg)
        Wtotal = wwt * wppkg
        rwt = int(str(integr[3:4]).strip("['']"))
        # print(wwt)
        rppkg = int(str(integr[4:5]).strip("['']"))
        # print(rppkg)
        Rtotal = rwt * rppkg
        pwt = int(str(integr[5:6]).strip("['']"))
        # print(pwt)
        pppkg = int(str(integr[6:7]).strip("['']"))
        # print(pppkg)
        Ptotal = pwt * pppkg

        name = str(res1[1:2]).strip("['']")
        # print(name)

        wheat = str(res1[2:3]).strip("['']")
        # print(wheat)
        Weight = str(res1[3:4]).strip("['']")
        # print(Weight)
        pricePerKg = str(res1[4:5]).strip("['']")
        # print(pricePerKg)

        rice = str(res1[6:7]).strip("['']")
        # print(rice)

        pulse = str(res1[10:11]).strip("['']")
        # print(pulse)



        data = {'Inventory': [{name  : wheat, Weight : wwt , pricePerKg : wppkg , 'Total' : Wtotal }, {name  : rice, Weight : rwt , pricePerKg : rppkg , 'Total' : Rtotal },{name  : pulse, Weight : pwt , pricePerKg : pppkg , 'Total' : Ptotal }]}
        result = json.dumps(data, sort_keys=True, indent=4)
        print(result)
        json.dump(result, open("NewInventory.json", "a+"))
        json.dump(result, open("NewInventory.txt", "a+"))

        print("The Price of Wheat , Rice and Pulses, per KG is in 'NewInventory.json' ")


js = Json()

# Driver Code

if __name__ == '__main__':
    js.Inventory()
