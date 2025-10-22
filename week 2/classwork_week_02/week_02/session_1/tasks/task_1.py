# Week 2, Session 1: Task 1

# Create a shopping list

shopping = ["eggs", "milk", "flour", "carrots"]
print(shopping)

# We forgot something, so add it to list

shopping.append("bananas")
print(shopping)

# We bought something, so remove it from list

shopping.remove("eggs")
print(shopping)

# Replace bananas with grapes

shopping[3] = "grapes"
print(shopping)

# Add yoghurt, just after milk
shopping.insert(0, "yoghurt")

print(shopping)