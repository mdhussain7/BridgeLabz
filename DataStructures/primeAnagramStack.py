# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
        self.prev = None  # Initialize prev as null


# Stack class contains a Node object
class Stack:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to add an element data in the stack
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

        # Function to pop top element and return the element from the stack

    def pop(self):
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

        # Function to return top element in the stack

    def top(self):
        return self.head.data

    # Function to return the size of the stack
    def size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count

    # Function to check if the stack is empty or not
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    # Function to print the stack
    def printstack(self):
        # print("stack elements are:")
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next


def reverseWords(input):
    inp = str(input).strip("[]")

    # split words of string separated by space
    inputWords = str(inp).split(" ")

    inputWords = inputWords[-1::-1]
    # now join words with space
    output = ' '.join(inputWords)

    return output


def primes(n):
    array = [i for i in range(2, n + 1)]
    p = 2

    while p <= n:
        i = 2 * p
        while i <= n:
            array[i - 2] = 0
            i += p
        p += 1

    return [num for num in array if num > 0]


def add(list1):
    total = 0

    # creating a list

    # Iterate each element in list
    # and add them in variale total
    for ele in range(0, len(list1)):
        total = total + list1[ele]

    # printing total value
    return total


def anagram(a):
    # initialize a list
    anagram_list = []
    for i in a:
        for j in a:
            if i != j and (sorted(str(i)) == sorted(str(j))):
                anagram_list.append(i)
    return anagram_list


def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


s = Stack()

if __name__ == "__main__":
    a = primes(1000)

    print(reverseWords(a))

    print(" The Anagram elements are: ", anagram(a))
    Ana = anagram(a)
    Ind = Remove(Ana)
    print("The Anagram elements After Removing the Redundant Elements:", Ind)
    Sum = add(Ind)
    print(" Sum of Anagram Numbers in the Prime Numbers is: ", Sum)
