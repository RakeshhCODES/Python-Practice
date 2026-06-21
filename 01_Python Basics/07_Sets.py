# Sets - Sets are used to store multiple items in a single variable
# Set is [UNORDERED] , [UNINDEXED] & [UNCHANGEABLE - but it allows adding ang removing items.]
# Duplicates are not allowed.
# written with {} brackets.

s1 = {"apple", "banana", "cherry"}
print(s1)

print(len(s1))

s2 = set(("apple", "banana", "cherry"))
print(s2)  #set() constructor is used to make a set.

s3 = {"apple", "banana", "cherry", "kiwi", "orange"}
for items in s3:
    print(items)  #for loop is used to access set items 

s4 = {"apple", "banana", "cherry"}
s4.add("kiwi")  #Adding items into a set
print(s4)

s5 = {"apple", "banana", "cherry"}
s6 = {"orange","mango","kiwi"}
s5.update(s6)   #Adding elements from s6 to s5
print(s5)

s7 = {"apple", "banana", "cherry"}
s7.remove("cherry")
print(s7)

s8 = {"apple", "banana", "cherry"}
x = s8.pop()
print(x)  #pop() is used to remove random item
print(s8)

s9 = {"apple", "banana", "cherry"}
s9.clear()  
print(s9)

s10 = {"apple", "banana", "cherry"}
for items in s10:
    print(items)

s11 = {"AB","BC","CD"}
s12 = {16 , 28 , 44}    # union() method joins 2 sets.
s13 = s11.union(s12)
print(s13)

s14 = {"AB","BC","CD"}
s15 = {16 , 28 , 44}
s16 = s14 | s15
print(s16)

s17 = {"apple", "banana", "cherry"}
s18 = {16 , 28 , 44}
s19 = {"AB","BC","CD"}
s20 = {"Rakesh"}
newset = s17.union(s18 , s19 , s20)
print(newset)

s21 = {"apple", "banana", "cherry"}
s22 = {"google","microsoft","apple"}
s23 = s21.intersection(s22)  #intersesction() methpd returns a new set , that only contains the items that are present in both sets.
print(s23)

s24 = {"apple", "banana", "cherry"}
s25 = {"google","microsoft","apple"}
s26 = s24.difference(s25) #difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
print(s26)

s27 = {"apple", "banana", "cherry"}
s28 = {"google","microsoft","apple"}
s29 = s27.symmetric_difference(s28) #symmetric_difference() method will keep only the elements that are NOT present in both sets.
print(s29)

s30 = frozenset({"apple", "banana", "cherry"})
print(s30)
print(type(s30))