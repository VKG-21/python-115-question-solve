#Grades Classification: Write a Python program that takes a student’s percentage as input and prints their corresponding grade according to the following criteria: – 90% or above: A+ – 80-89%: A – 70-79%: B – 60-69%: C – Below 60%: Fail

grade = float(input("Enter your percentage:"))

if grade >= 90:
    print("Your grade is A+!"),
elif grade >= 80:
    print("Your grade is A!"),
elif grade >= 70:
    print("Your grade is B!"),
elif grade >= 60:
    print("Your grade is C!"),
else:
    print("You failed!")
