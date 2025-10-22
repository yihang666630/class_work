# Week 2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetable = {"leek", "tomato", "potato"}

# What do you think will be printed here?

both = fruit.intersection(vegetable)
print(both)
'''
the print result would be "tomato" cause we're finding intersection part of two sets.
'''

# Why does the following code diplay five items?

food = fruit.union(vegetable)
print(food)
'''
the display rules of set that don't allow the same elment appear in a set beyond twice.
'''

# Add an item to fruit
fruit.add("grapes")
print(fruit)

# Remove an item from vegetables
vegetable.remove("tomato")   # or use the discard to avoid keyworderorr like: vegetable.discard("item")
# Find and display symmetric difference of the two sets

sym_dif = food - both  #or using built_in function sym_dif = fruit.symmetric_difference(vegetable)