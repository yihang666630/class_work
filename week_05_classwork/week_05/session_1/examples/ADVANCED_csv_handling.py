#### Advanced topic ####
# 5. csv handling

'''
The data dictionary solution is nice, but inelegant - we can actually do this much easier by using
a library called 'csv' which can do this all in one go:

'''

import csv

# Load CSV data into a list of dictionaries
with open("student_data.csv", "r") as infile:
    reader = csv.DictReader(infile)
    student_data = list(reader)  

print(student_data) 

# If you want a quick challenge - use this method to create a dict of dicts like in the other advanced example!