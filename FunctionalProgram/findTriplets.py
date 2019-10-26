def findTriplets(arr, n):
    """
    :param arr: Elements of the array
    :type n: Number of Elements
    """
    found = True   # Boolean Expression
    for i in range(0, n - 2):  # Looping in to the array elements till (n-2) element for the 'i' th element
        for j in range(i + 1, n - 1):  # Looping in to the array from the (i+1)th elements position till  penultimate
            # element
            for k in range(j + 1, n):  # Taking the jth elements position till the last elements position
                if (arr[i] + arr[j] + arr[k]) == 0:  # Checking the sum of ith jth and kth  to be Zero
                    found = True
                    return (arr[i], arr[j], arr[k])  # Returning the elements If a+b+c = 0
        if not found:
            d = " Not exist "
            return d


def main():
    n = int(input("Enter the Number of elements:\n"))  # Taking the input from the user to find the length of the array
    arr = list()  # creating a list to store the elements
    print("\nEnter the elements:")
    for i in range(n):  # Looping for the N number of elements
        arr.append(int(input()))  # Taking the user input and storing it to the array list
    print(findTriplets(arr, n))  # calling the function to find the triplets


# Driver code

main()
