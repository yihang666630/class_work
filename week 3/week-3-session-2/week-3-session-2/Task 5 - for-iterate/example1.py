"""
course = "Computer Science"

for ch in course :  # should iter every character in the courpus
	print(ch)
	
# create a list data structure of the characters from the course string
# sort the list into alphabetical order
"""

course = "Computer Science"
cha_cour = []

for ch in course.lower().strip() :  # should iter every character in the courpus
	# NOTE: use lower() to avoid the sorted() function considering case issue
	cha_cour.append(ch)   # a new list contain ever character form courpus
alpha_ord = sorted(cha_cour)  # sorted() function order the cha in alphabetical order
print(alpha_ord)
	