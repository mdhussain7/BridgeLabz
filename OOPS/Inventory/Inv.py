import json
file = open("Report.json", "r")
data_item = json.load(file)
file.close()
print("----- INVENTORY -----")
for key in data_item:
    print("-------", key, "-------")
    for value in data_item[key]:
        price = weight = 0
        print("Name :", value['name'])
        price += int(value["price"])
        weight += int(value["weight"])
        print("Weight : ", weight)
        print("Price : ", price)
        print()
