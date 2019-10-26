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
            print(current.data, end=' \n ')
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
            print(current.data, end = ' \n ')
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



def check(inp):

    try:
        if (inp == "y") or (inp == "Y") or (inp == "yes") or (inp == "Yes"):
            return 1
        else:
            return 0
    except ValueError:
        print("Invalid Entry!! \n Please Enter the proper Entry ")


        
# Main Code execution starts here 
if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList()
    ll = LinkedList()
    # Getting the words from the File and creating a file.
    #fname = input("\nEnter the File Name: ")
    try :
        name = input(" Enter your Name: ")
        ll.insert_at_end(name)
    
        company = input(" Enter the Company Name: ")
        ll.insert_at_end(company)
        while True:
            Shares = int(input(" Enter the Share Amount: "))
            llist.insert_at_end(Shares)
            inp = input(" Want to insert some More Shares? (y/n) ")
            while check(inp):
                Shares = int(input(" Enter the Share Amount: "))
                llist.insert_at_end(Shares)
                print("\n", ll.displayall())
                llist.displayall()
                print(llist.fdisplay())
                inp = input(" Want to insert some More Shares? (y/n) ")
                if check(inp):
                    Shares = int(input(" Enter the Share Amount: "))
                    llist.insert_at_end(Shares)
                    ll.displayall() 
                    print(ll.fdisplay())
                    llist.displayall()
                    print(llist.fdisplay())
                    break
            dl = input(" Want to delete the share from the List ? (y/n) ")
            
            if check(dl):
                print(" List of Shares Before deleting : \n", ll.displayall(), "\n", llist.displayall())
                dlt = int(input(" Enter the Share you want to delete: ")) 
                llist.delete(dlt)
                print(" List of Shares After deleting : ", ll.displayall(), "\n", llist.displayall())
            else:
                print(" List of Shares Before Adding the New : ", ll.displayall(), "\n", llist.displayall())
                Shares = int(input(" Enter the Share Amount: "))
                llist.insert_at_end(Shares)
                print(" List of Shares After Adding the New : ", ll.displayall(), "\n", llist.displayall())
                break
                
    except ValueError:
        print(" Enter the proper Value ")
        print(" Please try Again by running this Software ")
    except KeyboardInterrupt:
        print(" Force Quit ")
        print(" Please try Again by running this Software ")
        print(" Bye!! ")
         
         
    
    

