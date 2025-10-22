
animals = [ 'dog','cat','hamster','goldfish' ]

not_fish = [ item for item in animals if item != 'goldfish'] 
# this remove the 'goldfish' from the original list

print(not_fish)

# write the equivalent for loop to create the not_fish list from animals
"""
instead of using if-statement to create a new list
we can oprate by the index in the original list
"""
#version 1
del animals[3] # don't need to return the deleted elements
print(not_fish)
#version 2
not_fish = animals.remove("goldfish") # remove(), know the exact elements name
#version 3
animals.pop(3) # if assgined to a new variable, then it can return the deleted item
# print your result to verify it is the same