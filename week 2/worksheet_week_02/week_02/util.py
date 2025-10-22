"""
Utility functions for Worksheet 1.2.
"""
import sys
"""
def read_numbers():
    """
    #Prompts the user to enter a series of numbers on a single line,
    #separated from each other by spaces.

    #Returns a list of float values corresponding to the numbers that were
    #input by the user.
"""
    line = input("Enter some numbers, separated by spaces: ")
    try:
        line.isnumeric()
        numbers = [float(item) for item in line.split()]
        return numbers
    except ValueError:
        sys.exit("Error: no numbers provided")

"""

def read_file(file_path):
    f = open(file_path, "r", encoding="utf-8")
    contents = f.read()
    f.close()
    try:
        numbers = [float(item) for item in contents.split()]
        return numbers
    except ValueError:
        sys.exit("Error: no numbers found")

def std(file_path):
    numbers = read_file(file_path)
    mean = sum(numbers) / len(numbers)
    var = sum((x-mean)**2 for x in numbers) / len(numbers)
    std = var ** 0.5
    return std
