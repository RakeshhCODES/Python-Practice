# IF-ELSE STATEMENT - DECISION MAKING
# if = Do some code only IF some condition is True
#      Else do something else

age = int(input("Enter your age: "))

if age >= 18:
    print("You're eligible for voter card!")
else:
    print("You're not eligible for voter card.")


# IF-ELIF-ELSE STATEMENT - DECISION MAKING

marks = int(input("Enter your marks: "))
if marks > 100:
    print("Invalid score.")
elif marks >= 90:
    print("Your Grade is A+")
elif marks >= 80:
    print("Your Grade is A")
elif marks >= 70:
    print("Your Grade is B+")
elif marks >= 60:
    print("Your Grade is B")
elif marks >= 50:
    print("Your Grade is C")
elif marks >= 40:
    print("Your Grade is D")
else:
    print("You failed in your exam.")