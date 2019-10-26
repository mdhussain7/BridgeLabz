import math
x = float(input("Enter the X Co-ordinate:"))  # X Co-ordinate
y = float(input("Enter the Y Co-ordinate:"))  # Y Co-ordinate
distance = math.sqrt(x*x + y*y)  # Applying the distance formula of Euclidean
print(" The Euclidean Distance from origin '",x,"' and '",y,"' is '",distance,"'")
