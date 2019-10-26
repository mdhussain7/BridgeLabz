import json

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def displayall(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None:
                current = current.next_node
            current.next_node = new_node

    def fdisplay(self):
        current = self.head
        temp = ""
        while current:
            print(current.data, end = ' ')
            temp = temp + current.data + " "
            current = current.get_next()
        return temp

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        return found

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


# Main Code execution starts here

if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList()

    # Getting the words from the File and creating a file.
    #fname = input("\nEnter the File Name: ")
    fhand = open("CompanyShares.json", 'r')

    FLines = fhand.readlines()
    for line in FLines:
        words = line.split()
        for word in words:
            llist.insert_at_end(word)
    print("\n File contents in the List is:")
    llist.displayall()
    file = open("CompanyShares.json", "r+")
    item = json.load(file)
    file.close()



    for key in item:
        print("\n ------- ", key, " ------- \n")

        for value in item[key]:        
            print("Company:", value['Company'])
            print("Current:", value['Current'])
            print("%Gain:", value['%Gain'])
                
            
            llist.insert_at_end(value)
                
            print("\n------------------------------\n")
            f = open("Company.txt", "a+")
            llist.insert_at_end(f.write(str(llist)+","))
            print("Data is Written into 'Company.txt' Successfully")
            print()
            #a = llist.fdisplay()
            #print(a, "\n")
            #print ("Dict key-value are : ") 
            #for i in enumerate(str(a).items()): 
            #    print (i) 
            
    
    # Searching the word in the Linked List
    
    Searchword = input("\nEnter the Company to be searched : ")
    if llist.search(Searchword):
        print("Company", Searchword, " found in the File ")
    else:
        print("Company", Searchword, " not found in the File")
    #llist.displayall()
    
    
    
    # Updated Linked list is stored in the file New.txt
    fname = "New.txt"
    fhand = open(fname, 'w+')
    a = llist.fdisplay()
    print(a)
    fhand.write(a)
    fhand.close()

    print("File created with filename 'New.txt'")

