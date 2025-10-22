
# create a for loop and use range to print the list of numbers 
# between 3 and 50 that are divisible by 3

div_3 = [] # initialization

for a in range (3, 51):  # should contain the integer between 3-50
    if a % 3 == 0:       # the interger 3 can devides
        div_3.append(a)  # add every integer in the original empty list
print(div_3)    # not the indentation print out the final list