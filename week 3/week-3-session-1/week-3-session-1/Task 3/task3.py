# Sample items with their prices
items = {
    "apple": 0.5,
    "banana": 0.3,
    "orange": 0.8,
    "grapes": 2.0,
    "watermelon": 3.0
}

# Get user input for the items and their quantities
item_selected = input("Enter the item you want to purchase (apple, banana, orange, grapes, watermelon): ").strip().lower()
quantity = int(input("Enter the quantity: "))

# Initialize total cost
total_cost = 0

# Using match statements to calculate the total cost
match item_selected:
    case "apple":
        total_cost = items["apple"] * quantity
    case "banana":
        total_cost = items["banana"] * quantity
    case "orange":
        total_cost = items["orange"] * quantity
    case "grapes":
        total_cost = items["grapes"] * quantity
    case "watermelon":
        total_cost = items["watermelon"] * quantity
    case _:
        print("Item not available.")

# Print total cost if the item was valid
if total_cost > 0:
    print(f"The total cost for {quantity} {item_selected}(s) is: £{total_cost:.2f}")
