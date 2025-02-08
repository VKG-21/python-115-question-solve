#Positive, Negative, or Zero: Write a Python program that takes a number as input and prints whether it is positive, negative, or zero.

number = float(input("Enter a number:"))
if number == 0:
    print("This is zero!"),
elif number > 0:
    print("This number is greater than zero!"),
else:
    print("This number is less than zero!")
