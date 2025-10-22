
words = "Python textbook"
vowels = "aeiou"

# find all the vowels in the words string 
result = [c for c in words if c in vowels]

print(result)

# Test the code for different 'words' strings

# Modify the result to only show which vowels occur, not every occurrence.
result_2 = {c for c in words if c in vowels} #sets: the same elements only occur once
# Sort the list alphabetically.
result_final = sorted(result_2)
# Hint: consider the properties of different data structures