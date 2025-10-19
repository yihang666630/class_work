# Step 1: Open a file called 'student_data.csv' to read each student's grades.
# hint: skip the header row with data[1:]
# hint: you could handle file errors with try/except

# Step 2: Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3

# Step 3: Sort the students by their average grade in descending order.
# hint: you might want to store each student as a dictionary with name and average
# hint: use the sorted() function with a key parameter, or list.sort()

# Step 4: Open a file called 'report.txt'
# Write each student's name and their average grade to the report in order
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f