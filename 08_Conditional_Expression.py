# Conditional Expressions : A one line if-else statement (ternrary operator) that print or assign one of two values based on a condition.

num = int(input("Enter a number: "))
result = "Even number" if num % 2 == 0 else "Odd number"
print(result)



marks = float(input("Enter your marks:"))
exam_result = "Pass" if 100 > marks >= 30 else "FAIL"
print(exam_result)


user_role = input("Enter your role(admin or guest): ")
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)