
sum = 0

for k in range(1,10) :
    sum = sum + k**2

print(f"1.{sum}")
    
# modify the code to sum the squares of even numbers up to and including 20

sum = 0

for k in range(1,21):
    if k % 2 == 0:
       sum = sum + k**2
print(f"2.{sum}")

# modify the code to print the sum at each iteration

sum = 0

for k in range(1,10) :
    sum = sum + k**2
    print(sum)    #if want the print rsult for every iteration then note the indetentation