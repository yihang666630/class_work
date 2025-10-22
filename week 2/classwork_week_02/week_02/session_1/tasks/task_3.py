# Week 2, Session 1: Task 3

fruit = ("apple", "banana", "cherry")
print(fruit)

# Find and display position of "banana"
index_ban = fruit.index('banana')
print(index_ban)
# Display how many times "cherry" occurs
cout_che = fruit.count('cherry')
print(cout_che)
# Unpack tuple
fruit = ("apple", "banana", "cherry")
#version_1
print(*fruit)
#version_2
a, b, c = fruit
print(f"{a}\n{b}\n{c}")