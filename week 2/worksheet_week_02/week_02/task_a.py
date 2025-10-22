"""
@author: Yihang Yu
Leeds ID: 201913006
The code is my own work. 
"""

import sys
grade = input("Enter your grade that is interger and in 0-100: ")

# try-expect block 
try:
  grade = int(grade)
  if grade >= 0 and grade <= 39:
     print(f"{grade} is a Fail")
  elif grade >= 40 and grade <= 69:
     print(f"{grade} is a Pass")
  elif grade >= 70 and grade <= 100:
     print(f"{grade} is a Distinction")
  else:
      sys.exit("Error: Grade must be an integer between 0 and 100")
except ValueError:
  sys.exit("Error: Grade must be an integer between 0 and 100")