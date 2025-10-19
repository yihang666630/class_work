# 1. Opening a file is very simple:

with open("student_data.csv", "r") as f: # opening 'student_data.csv' in read mode
    for line in f: # files are iterable!
        print(line)

