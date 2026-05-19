# VARIABLES : container for a value that can change [string , integer , float , boolean]

#Strings
first_name = "Rakesh"
last_name = " Mohapatra"

full_name = first_name+last_name
print(full_name)

#Integers
age = 25
quantity = 100

print(f"You are {age} years old")
print(f"You are buying {quantity} items")

#Float
price = 16.28
cgpa = 7.3

print(f"The price of the item is ${price}")
print(f"Your CGPA is : {cgpa}")

#Boolean
is_student = True

if is_student:
    print("You are a student")
else:
    print("You are not a student")