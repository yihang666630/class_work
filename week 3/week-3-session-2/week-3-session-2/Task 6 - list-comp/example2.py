
values = [ 1,4,2,6,3,7 ]

print(values)

newval = [ 2*x if x%2==0 else x for x in values ]

# what does this list comprehension produce and why?
'''
in word, newval contains:
when x is even, 2x is in the list;
when x is odd, x itself is in the list
this expresstion is a compression version of for-loop and if-else statement,
it can be re-write like:
'''
newval = []
for x in values:
    if x % 2 == 0:
        newval.append(2*x)
    else:
        newval.append(x)
print(newval)
# try to predict the result before printing it