
fruit = [ 'apple','pear','banana','orange' ]

while fruit :
	print( fruit.pop() )
    
# Why does this work?
# Because the list is not empty, so the while loop will continue to run.
# What features of Python does it rely on?
"""
It relies on the boolean value of the list being True.
When the list is empty, the boolean value is False, so the while loop will stop.
When the list is not empty, the boolean value is True, so the while loop will continue to run.
This is a feature of Python that allows for easy iteration over a list.
"""