import pytest


class Stack(object):
    def __init__(self):
        self.values = []

    def push(self, value):
        """
        Add a value to the top of the
        stack
        """
        self.values.append(value)

    def pop(self):
        """
        Pop values
        """
        return self.values.pop()


class Queue(object):
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def pop(self):
        return self.values.pop(0)


stack = Stack()

queue = Queue()


class PalindromeChecker(object):
    """
    Checks if a word is a palindrome or not
    using two
    """

    def __init__(self, word):
        self.word = word
        self.queue = Queue()
        self.stack = Stack()

    def check_palindrome(self):
        for letter in self.word:
            self.queue.push(letter)
            self.stack.push(letter)
        for i in range(len(self.word)):
            if self.queue.pop() != self.stack.pop():
                return False
        return True


# Driver Code
if __name__ == '__main__':
    s = input("Enter the String:")
    res = PalindromeChecker(s)
    if res.check_palindrome():
        print(s, " is a palindrome")
    else:
        print(s, " is not a palindrome")
