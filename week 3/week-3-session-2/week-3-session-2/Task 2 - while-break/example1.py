"""
k = 2
while True :
    k = 2*k 
    print(k)
"""    

# As written this is an infinite loop.
# If you run it, use <Ctrl>C to exit the running program. This is so called 'keyboardinterrupt'
# 1. Add a break statement to exit the loop if k>200
k = 2
while True:
    k = 2*k 
    print(k)
    if k > 200:
        break
# 2. Rewrite the code to directly use the while loop instead of break.
k = 2
while k > 200:
    k = 2*k 
    print(k)  