row = int(input("Enter the number of rows:"))
col = int(input("Enter the number of columns:"))

matrix = []
print("Enter the entries row wise:")

for i in range(row):
    a = []
    for j in range(col):
        a.append(int(input()))
    matrix.append(a)
print("The 2D array is given below:")
for i in range(row):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()
