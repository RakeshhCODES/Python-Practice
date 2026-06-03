#input() = a function that prompts the user to enter data and returns the entered data as a string
name = input("Enter your name: ")
age = int(input("Enter your age: "))

room_temp = input("Enter room temperature: ")
room_temp = float(room_temp)

print(f"Hello {name}!")
print(f"You are {age} years old.")
print(f"Room temperature is {room_temp} degrees Celsius.")
