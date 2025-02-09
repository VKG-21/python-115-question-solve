#Quadratic Equation Solver: Write a Python program that takes the coefficients (a, b, c) of a quadratic equation as input and calculates and prints the real roots (if they exist) or a message indicating the complex roots.

import cmath
a = int(input("Enter a number:"))
b = int(input("Enter another number:"))
c = int(input("Enter third number:"))

d = (b**2)-(4*a*c)

sol_1 = (-b-cmath.sqrt(d))/(2*a)
sol_2 = (-b+cmath.sqrt(d))/(2*a)

print('The solutions are {0} and {1}'.format(sol_1, sol_2))
