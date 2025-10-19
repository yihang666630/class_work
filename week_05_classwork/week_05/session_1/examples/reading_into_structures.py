# 2. Reading data into a structure is also very simple:

with open("student_data.csv", "r") as f:
    # this creates a list of strings:
    data = f.readlines()

print(data)

