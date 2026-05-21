#Hypotenuse of a right angled triangle

import math

a = float(input("Enter value of length a: "))
b = float(input("Enter value of length b: "))

c = math.sqrt(pow(a, 2)  + pow(b, 2))
print("Hypotenuse = math.sqrt(pow(a, 2) + pow(b, 2))")
print(f"Hypotenuse of a right angled triangle is: {round(c ,2)}")