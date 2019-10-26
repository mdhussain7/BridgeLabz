import json

file = open("stock.json", "r")
item = json.load(file)
file.close()
print("-------------------- Stock Data --------------------")
for key in item:
    print("\n ------- ", key, " ------- \n")

    for value in item[key]:
        price = weight = 0
        print("Name :", value['name'])
        print("Carret :", value['carret'])
        price += int(value["price"])
        weight += int(value["weight"])
        print("Weight : ", weight)
        print("Price : ", price)
        total = int(weight) * (price)
        print("Total Amount: ", total)
        value['total'] = total
        print(value)
        ls = list()
        ls.append(value)
        print("\n------------------------------\n")
        f = open("stockData.json", "a+")
        f.write(str(ls)+",")
        print("Data is Written into stockData.json Successfully")
        print()
