# String Methods - 

#len() - returns the length of the string. 
name1 = input("Enter your name: ")
result1 = len(name1)
print(result1)
print("This is the length of the string using len().")


#find() - returns the first occurence of the given character
name2 = input("Enter your name: ")
result2 = name2.find("a")
print(result2)
print('This is the first occurence of the character using find().')

#rfind() - returns the last occurence of the given character
name3 = input("Enter your name: ")
result3 = name3.rfind("a")
print(result3)
print('This is the last occurence of the character using rfind().')


#capitalize() - Converts the first character to upper case
name4 = input("Enter your name: ")
result4 = name4.capitalize()
print(result4)
print("This is the string with the 1st character capitalized using capitalize().")

#count()- Returns the number of times a specified value occurs in a string
name5 = input("Enter your name: ")
result5 = name5.count("a")
print(result5)
print("This is the number of times the character occurs in the string using count().")

#replace() - Replaces a specific value with another value in a string
name6 = input("Enter your name: ")
result6 = name6.replace("a", "A")
print(result6)
print("This is the string with the character replaced using replace().")

#swapcase() - Converts uppercase characters to lowercase and lowercase characters to uppercase
#upper() - Converts all characters in a string to uppercase
#lower() - Converts all characters in a string to lowercase
