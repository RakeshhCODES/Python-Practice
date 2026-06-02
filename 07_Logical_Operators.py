# LOGICAL OPERATORS - Evaluate multiple conditions. [or , and , not]
#                     or - At least one condition must be True. 
#                     and - All conditions must be True.
#                     not - Inverts the condition [not True = False, not False = True]

# or OPERATOR
temp1 = int(input("Enter the temperature: "))
is_raining = False

if temp1 > 35 or temp1 < 0 or is_raining:
    print("The outdoor event is cancelled.")
else:
    print("The outdoor event is still scheduled.")


# and OPERATOR
temp2 = int(input("Enter the temperature: "))
is_sunny = True

if temp2 >= 28 and is_sunny:
    print("It is sunny.")
    print("It's a great day for the beach!")
elif temp2 <= 0 and is_sunny:
    print("It is sunny.")
    print("It's a great day for skiing!")
elif 28 > temp2 > 0 and is_sunny:
    print("It is warm.")
    print("It's a great day for a picnic!")


# not OPERATOR
is_weekend = True
if not is_weekend:
    print("It's a weekday. Time to work!")
else:   
    print("It's the weekend! Time to relax!")
    