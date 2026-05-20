#Exercise 02 : Shopping Cart Program 

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like to buy?: "))

total = price * quantity
print(f"The total no. of items are: {quantity}")
print(f"The total cost is: {total}")
print("THANK YOU FOR SHOPPING !!")