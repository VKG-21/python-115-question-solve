#Triangle Type Checker: Write a Python program that takes three sides of a triangle as input and determines whether it forms an equilateral, isosceles, or scalene triangle.

side_1 = int(input("Enter the length of one side:"))
side_2 = int(input("Enter the length of second side:"))
side_3 = int(input("Enter the length of third side:"))

if side_1==side_2 and side_1==side_3 and side_3==side_2:
    print("This is an equilateral triangle")
elif side_1==side_2 or side_1==side_3 or side_2==side_3:
    print("This is an isosceles triangle")
else:
    print("This is a scalene triangle")
