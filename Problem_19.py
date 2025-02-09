#Number Ranges: Write a Python program that takes an integer as input and prints whether the number falls within the ranges: 0-50, 51-100, 101-150, or above 150.

num = int(input("Enter an integer:"))
num>=0
if num >=0 and num<51:
    print("The number is in the range 0-50"),
elif num>=51 and num<101:
    print("The number is in the range 51-100"),
elif num>=101 and num<151:
    print("The number is in the range 101-150"),
else:
    print("The number is greater than 150")