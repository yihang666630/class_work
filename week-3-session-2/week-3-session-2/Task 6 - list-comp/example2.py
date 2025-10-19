
values = [ 1,4,2,6,3,7 ]

print(values)

newval = [ 2*x if x%2==0 else x for x in values ]

# what does this list comprehension produce and why?
# try to predict the result before printing it