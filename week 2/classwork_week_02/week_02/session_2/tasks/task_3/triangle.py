# Week 2, Session 2: Task 3
# Triangle Tester

# Ask user for the lengths of three sides of a triangle

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Conditional block to check the type of triangle

if side1 == side2 == side3:
    print("This is an equilateral triangle.")
elif side1==side2 or side1==side3 or side2==side3:
    print("This is an isosceles triangle.")
elif side1 != side2 != side3:
    print("This is a scalene triangle.")
