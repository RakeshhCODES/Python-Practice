# TypeCasting : Process of converting a variable from one data type to another
#[str() int() float() bool()]

name = "Rakesh"
age = 25
cgpa = 7.3
is_student = True

print(type(name)) #data type of a variable 
print(type(age))
print(type(cgpa))
print(type(is_student))

cgpa = int(cgpa) #converting float to integer
print(cgpa)
age = float(age) #converting integer to float
print(age) 