# Week 4, Session 1: Task 2

# You are given the function mystery_func. Inspect the code in the function
# and your task is to write a corresponding docstrings here on
# what the function does and what is the return value.


def mystery_func(string):
    upper = 0
    lower = 0

    for ch in string:
        if ch.isupper():
            upper += 1
        if ch.islower():
            lower += 1
    return [upper, lower]


print(mystery_func("abc"))
print(mystery_func("The quick Brown Fox!"))
print(mystery_func("012345"))
print(mystery_func("ABC"))


# Can you predict the output of the following lines of code?
# Uncomment the lines of code one by one and run the program
# to see if you are right?

# print(mystery_func(200))
# print(mystery_func([2, 3]))
