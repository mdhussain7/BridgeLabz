import Utility as u
n = int(input("Enter the number of elements you want to insert:"))
arr = list()
print("Enter the Elements:")
for i in range(n):
    arr.append(int(input()))
a = u.insertionSort(arr)
print("Sorted array is:")
for i in range(len(a)):
    print("%d" %a[i])
print("Bye!")
