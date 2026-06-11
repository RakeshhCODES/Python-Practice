# Indexing - accessing individual elements of a sequence using []
# Slicing - accessing a range of elements in a sequence

# Indexing
player = "Virat Kohli"
print(player[0])
print(player[1])
print(player[2])
print(player[3])
print(player[4])
print(player[-3]) #Negative indexing starts frm the end of the string. -1:Last Character


# Slicing
print(player[0:5])  #Start index is inclusive & Ending index is exclusive
print(player[:7])
print(player[3:8]) # 3 -Start Index & 8 -Ending Index.
print(player[5:])  # When Ending Index is not provided, it'll go till the end of the string.
print(player[:])   # This returns the whole string as output.
print(player[::2]) # This will return every 2nd character from the string.
print(player[::-1]) # This will return the string in reverse order.
print(player[-10:-1]) # This will return the string from index -10 to -1 (exclusive).