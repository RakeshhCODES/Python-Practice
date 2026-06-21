# TUPLES - Used to store multiple items in a single variable.
#          Written with round brackets().
# Tuple items are : [ORDERED], [UNCHANGEABLE] & [DUPLICATE VALUES are allowed].
# Items are INDEXED starting from [0].


tuple1 = ("apple" , "banana" , "cherry")
print(tuple1)
print(len(tuple1))

tuple2 = ("apple" , "banana" , "cherry" ,'kiwi')
print(tuple2[0])

tuple3 = ("apple" , "banana" , "cherry" ,'kiwi')
print(tuple3[-1])

tuple4 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple4[1:5])

tuple5 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple5[:5])

tuple6 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple6[3:])

tuple7 = ("apple", "banana", "cherry", "orange")
list1 = list(tuple7)
list1[2] = "kiwi"       #Tuples are unchangeable so 1st-Convert tuple into list 2nd-Change the list 3rd-Convert the list back to tuple.
tuple7 = tuple(list1) 
print(tuple7)

tuple8 = ("apple", "banana", "cherry", "orange")
list2 = list(tuple8)
list2.append("kiwi")     #Convert tuple into list then, Add items through append() method and then convert back to tuple.
tuple8 = tuple(list2)
print(tuple8)

tuple9 = ("apple", "banana", "cherry", "orange")
x = ("kiwi",)  #Another way to add item to a tuple 
tuple9 += x
print(tuple9)

tuple10 = ("apple", "banana", "cherry", "orange")
list3 = list(tuple10)
list3.remove("apple")   #Convert tuple into list , remove items by remove() method and the convert the list back to tuple
tuple10 = tuple(list3)
print(tuple10)

tuple11 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
for items in tuple11:    #This prints all the items of the tuple.
    print(items)

tuple12 = ("AB","BC","CA")
tuple13 = (16 , 28 , 44)   #Adding two tuples.
tuple14 = tuple12 + tuple13
print(tuple14)

tuple15 = ("apple", "banana", "cherry")
tuple16 = tuple15 * 2  #Multiplying Tuples
print(tuple16)

