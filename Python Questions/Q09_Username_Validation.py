# VALIDATE user inputs :
# -- Username is not more than 12 characters
# -- Username must not contain spaces
# -- Username must not contain digits

username = input("Enter your username: ")

if len(username) > 12:
    print("Error: Username must not be more than 12 characters.")
elif not username.find(" ") == -1:
    print("Error: Username can't contain spaces.")
elif not username.isalpha():
    print("Error: Username can't contain digits.")
else:
    print(f"Welcome {username}!")

