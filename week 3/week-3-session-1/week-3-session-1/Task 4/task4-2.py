# Adapt this code to use a match instead of an if statement
# you could also:
# - make the inputs more robust
# - try and add a loop to make the program repeat (if you have done python before)



# Display the menu
print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

choices = [
    ('1', "Add"),
    ('2', 'Substract'),
    ('3', 'Multiply'),
    ('4', "Divide"),
    ('5', "Exit")
]

# Get user choice
try:
   choice = input("Enter your choice (1-5): ")
except ValueError:
    exit("Please enter right format!")
# Get numbers to operate on
try:
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))
except ValueError:
    exit("Not a number, enter again")
# Process the choice using match-case block
for choice in choices:
    match choice:
        case ('1'):
              result = num1 + num2
              print(f"The result of addition is: {result}")

        case ('2'):
             result = num1 - num2
             print(f"The result of addition is: {result}")

        case ('3'):
            result = num1 * num2
            print(f"The result of addition is: {result}")

        case ('4'):
            if num2 != 0:
               result = num1 / num2
               print(f"The result of division is: {result}")
            else:
               print("Error: Cannot divide by zero.")

        case ('5'):
             print(f"Exiting the program")

        case _:
            print("Invalid choice. Please select a number between 1 and 5.")
