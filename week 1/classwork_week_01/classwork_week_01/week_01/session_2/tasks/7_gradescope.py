"""
@author: Yihang Yu
Leeds ID: 201913006
The code is my own work. 
"""
# To test that you can successfully download a file and upload it to gradescope

# You are going to write a very simple program:

# Ask a user to enter two numbers (one per input)

# multiply those numbers together

# print out the result

# There is an extra point available for validating that they entered numbers!
# Add to your code so that if they 
# entered something other than an integer it prints
# 'That is not a number' and exits.

# simple test
num_1 = input("Enter an integer:")
num_2 = input("Enter another integer:")
try:
    num_1 = int(num_1)
    num_2 = int(num_2)
    res = num_1 * num_2
    print (f"The result is {res}")
except ValueError:
    print("That is not a number")


# Download your file, and upload it to the 'Week 1 Session 2 - 
# Practice Upload' task on Minerva.
# You will get some feedback - ensure you are passing the tests!