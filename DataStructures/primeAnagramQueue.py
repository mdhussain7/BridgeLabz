class Node:
    def __init__(self, value):
        self.data = value
        self.front = None



class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def en_queue(self, value):
        new_node = Node(value)

        if self.tail is not None:
            # make the front attribute of old node point to new node
            self.tail.front = new_node

        else:
            # if first ever node in Queue both front and tail will point to it
            self.head = new_node

        self.tail = new_node
        self.count += 1

    def de_queue(self):
        if not self.is_empty():
            # point head to next node
            self.head = self.head.front
            self.count -= 1
            print("Deletion Sucess")
        else:
            print("Empty QUEUE")

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.front

    def is_empty(self):
        if self.head is None and self.tail is None:
            return True
        else:
            return False

    def peek_front(self):
        return self.head.data

    def peek_back(self):
        return self.tail.data

    def queue_search(self, value):
        # start from the head
        p = self.head
        while p is not None:
            # make p reference to next node
            if p.front is not None:
                if p.data == value:
                    print("Found value")
                    return p.data
                p = p.front
            else:
                print("fail")
                return 0


    def length(self):
        return self.count

    def primes(self,n):
        array = [i for i in range(2,n+1)]
        p = 2

        while p <= n:
            i = 2*p
            while i <= n:
                array[i-2] = 0
                i += p
            p += 1

        return [num for num in array if num > 0]

    def add(self,list1):
        total = 0

# creating a list

# Iterate each element in list
# and add them in variale total
        for ele in range(0, len(list1)):
            total = total + list1[ele]

# printing total value
        return total

    def anagram(self,a):
    # initialize a list
        anagram_list = []
        for i in a:
            for j in a:
                if i != j and (sorted(str(i))==sorted(str(j))):
                    anagram_list.append(i)
        return anagram_list

    def Remove(self,duplicate):
        final_list = []
        for num in duplicate:
            if num not in final_list:
                final_list.append(num)
        return final_list


    def reverseWords(self,input):
        inp = str(input).strip("[]")

    # split words of string separated by space
        inputWords = str(inp).split(" ")

        inputWords = inputWords[-1::-1]
    # now join words with space
        output = ' '.join(inputWords)

        return output



if __name__ == "__main__":

    print("-------Test Queue---------")
    print("-------Test En Queue------")
    my_queue = Queue()
    test_list = my_queue.primes(1000)

    for i in test_list:
        my_queue.en_queue(i)
    print("-------En Queue Done-------")
    for i in my_queue:
        print(i.data)
    print("------Queue Print Done-----")

    #print("------Queue Print Done-----")
    #print(my_queue.peek_back())
    #print(my_queue.peek_front())
    #print("----------De Queue---------")
    #my_queue.de_queue()
    #print("--------De Queue Done------")

    print("The Elemets after reversing Primenumbers ", my_queue.reverseWords(test_list))
    for i in my_queue:
        print(i.data)
    print("-----Queue Print Done------")

    print(" The Anagram elements are: ", my_queue.anagram(test_list))
    Ana = my_queue.anagram(test_list)
    print("The Anagram elements after removal of Redundant elements are ", my_queue.Remove(Ana))
    for i in my_queue:
        print(i.data)
    print("-----Queue Print Done------")

    Ind = my_queue.Remove(Ana)
    print(my_queue.Remove(Ana))
    print("The Anagram elements After Removing the Redundant Elements:", Ind)
    for i in my_queue:
        print(i.data)
    print("-----Queue Print Done------")


    Sum = my_queue.add(Ind)
    print(my_queue.add(Ind))
    print(" Sum of Anagram Numbers in the Prime Numbers is: ",Sum)
    for i in my_queue:
        print(i.data)
    print("-----Queue Print Done------")

    #print("-----Test search-------")
    #x = my_queue.queue_search('999')
   # print(x)
    print("-------Full De Queue-------")
    while my_queue.length() != 0:
        my_queue.de_queue()
    print("--------De Queue Done------")
    for i in my_queue:
        print(i.data)
    print("-----Queue Print Done------")




