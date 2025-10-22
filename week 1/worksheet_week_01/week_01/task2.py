"""
@author: Yihang Yu
Leeds ID: 201913006
The code is my own work. 
"""

"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, 
other than any provided template code, was written and developed by you independently.
Name: Yihang Yu
"""

name = input("Enter your name: ")
mon_amo = input("Enter the amount you want to save every month: ")
try:
   mon_amo = int(mon_amo)
   total_amo = mon_amo * 12
   print(f"{mon_amo} -> {total_amo}")

   interest = total_amo * 0.008
   total_with_interest = total_amo + interest
   print(f"{total_amo} -> £{total_with_interest:.2f}")
except ValueError:
    print("Invalid amount")





# Ask the user to input an amount they want to save every month - 
# this should be an integer.
# Validate that they have entered an integer.


# Calculate the total amount of money they will have saved by 
# the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.


# Calculate the total amount of money including interest 
# (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

