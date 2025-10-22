"""
@author: Yihang Yu
Leeds ID: 201913006
The code is my own work. 
"""

from util import *
import sys
file_path = input("Enter the file path: ")
numbers = read_file(file_path)
if not numbers:
    sys.exit("Error: no numbers provided")
# Compute min and max and mean (simple one)
min = min(numbers)
max = max(numbers)
mean = sum(numbers) / len(numbers)
std = std(file_path)

# median (differnt situation: computing median for even/odd length)
sorted_nums = sorted(numbers)
n = len(sorted_nums)
if n % 2 == 1:
    median = sorted_nums[n // 2]
else:
    median = (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2

# Output
print(f"Minimum = {min}")
print(f"Maximum = {max}")
print(f"Mean    = {mean:.1f}")
print(f"Median  = {median}")
print(f"Standard Deviation = {std:.1f}")