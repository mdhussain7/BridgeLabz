class Node: 
	
	# Class to create nodes of linked list 
	# constucter initializes node automatically 
	def __init__(self,data): 
		self.data = data 
		self.next = None
	
class Stack: 
	
	# head is default NULL 
	def __init__(self): 
		self.head = None
	
	# Checks if stack is empty 
	def isempty(self): 
		if self.head == None: 
			return True
		else: 
			return False
	
	# Method to add data to the stack 
	# adds to the start of the stack 
	def push(self,data): 
		
		if self.head == None: 
			self.head=Node(data) 
			
		else: 
			newnode = Node(data) 
			newnode.next = self.head 
			self.head = newnode 
	
	# Remove element that is the current head (start of the stack) 
	def pop(self): 
		
		if self.isempty(): 
			return None
			
		else: 
			# Removes the head node and makes 
			#the preceeding one the new head 
			poppednode = self.head 
			self.head = self.head.next
			poppednode.next = None
			return poppednode.data 
	
	# Returns the head node data 
	def peek(self): 
		
		if self.isempty(): 
			return None
			
		else: 
			return self.head.data 
	
	# Prints out the stack	
	
	def display1(self): 
		
		iternode = self.head 
		if self.isempty(): 
			print("Stack Underflow") 
		
		else: 
			
			while(iternode != None): 
				
				print("Shares: ", iternode.data," ",end = " ") 
				iternode = iternode.next
			return
	 
	def display(self): 
		
		iternode = self.head 
		if self.isempty(): 
			print("Stack Underflow") 
		
		else: 
			
			while(iternode != None): 
				
				print(iternode.data," ",end = " ") 
				iternode = iternode.next
			return
			
		
# Driver code 

def check(inp):

    try:
        if (inp == "y") or (inp == "Y") or (inp == "yes") or (inp == "Yes"):
            return 1
        else:
            return 0
    except ValueError:
        print("Invalid Entry!! \n Please Enter the proper Entry ")

 
if __name__ == '__main__':

    MyStack = Stack() 
    name = Stack()
    company = Stack()
    try :
        n = input(" Enter your Name: ")
        name.push(n)

        Company = input(" Enter the Company Name: ")
        company.push(Company)
        while True:
            Shares = int(input(" Enter the Share Amount: "))
            MyStack.push(Shares)
            inp = input(" Want to insert some More Shares? (y/n) ")
            while check(inp):
                Shares = int(input(" Enter the Share Amount: "))
                MyStack.push(Shares)
                
                name.display()
                print()
                company.display()
                print()
                MyStack.display1()                
                print()
                
                inp = input(" Want to insert some More Shares? (y/n) ")
                if check(inp):
                    Shares = int(input(" Enter the Share Amount: "))
                    MyStack.push(Shares)

                    name.display()
                    print()
                    company.display()
                    print()
                    MyStack.display1()                
                    print()                    

                    break
                    
            dl = input(" Want to delete the share from the List ? (y/n) ")
            
            if check(dl):
                print(" List of Shares Before deleting : \n")
                MyStack.display1()
                print("\nTop Share is ",MyStack.peek()) 
                MyStack.pop()
                print(" List of Shares After deleting : \n")
                MyStack.display1()
            else:
                print(" List of Shares Before Adding the New : \n")
                MyStack.display1()
                Shares = int(input(" Enter the Share Amount: "))
                print("\nTop Share is ",MyStack.peek()) 
                MyStack.push(Shares)
                print(" List of Shares After Adding the New : \n")
                MyStack.display1()
                break
                
    except ValueError:
        print(" Enter the proper Value ")
        print(" Please try Again by running this Software ")
    except KeyboardInterrupt:
        print(" Force Quit ")
        print(" Please try Again by running this Software ")
        print(" Bye!! ")


