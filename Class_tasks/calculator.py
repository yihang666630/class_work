# savings calculator
# get amount of money monthly
input = input("Please enter the amount of money you save monthly: ")
try:
    input = int(input)
    print (f"You save {input * 12} in a year")
except ValueError:
    print("Invalid amount")
# get interest
intre = int(input) * 12 * 0.08
#get amount of money with interest
total = int(input) * 12 + intre
print(f"With interest you will save {total} in a year")