from itertools import permutations


# Permutation of String Recursive Manner
def allPermutations(s1):
    length = len(s1)
    if length < 2:
        return s1  # Returning the String as its length is less than 2
    perm = [''.join(p) for p in permutations(s1)]  # Reversing the each and individual character with appropriate
    # Permutations
    return perm  # returning the words stored in the list


# Permutation of String Iterative Manner
def perms(word):
    stack = list(word)  # Taking the list of word into the stack
    results = [stack.pop()]  # Popping the each and individual character stored inside the stack
    while len(stack) != 0:  # Lopping until the stack length becomes '0'
        c = stack.pop()  # removing the each element present at the Top of Stack and Storing it in the variable C
        # which is also a Stack
        new_results = []  # Creating the new list to store the words after permutation
        for w in results: # Picking the  word from the stack
            for i in range(len(w) + 1):  # Looping until it becomes equal to the length of the  word
                new_results.append(w[:i] + c + w[i:])  # Appending each character of the word from 0 till 'i'th position
        results = new_results  # Storing the new_results items back into the results List
    return results


# Driver Code
if __name__ == "__main__":
    str1 = input("Enter the String:")
    print(allPermutations(str1))
    print(perms(str1))
    if allPermutations(str1) == perms(str1):  # Comparing the Recursive and Iterative Method
        print("Permutations of both are same")
    else:
        print("Permutations are not same")
