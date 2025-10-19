#### advanced topic####
# 4. Data dictionaries

# lists are not always the best way!
# Because we're reading a csv file with a header, we might prefer to use a list of dictionaries

with open("student_data.csv", "r") as f: 
    data = f.readlines()

# still needs cleaning:
data = [ line.strip().split(",") for line in data]

clean = []

# optional but makes the code more readable in the loop
headers = data[0]

# and now we iterate through all the lines except the first one (the header row)
for row in data[1:]:
    # dict(zip()) is creating a dictionary by matching the pairs in the same index from headers and row
    clean.append( dict(zip(headers, row)))

print(clean)


# alternatively - a dict of dicts would be even better because you can search by ID!

clean_dict = {}

for row in data[1:]:
    clean_dict[row[0]] = dict(zip(headers[1:], row[1:]))

print(clean_dict)
print(clean_dict["1001"])