# Step 1: Create an empty list for the shopping list.
# optional: see if there is an existing shopping list file and load that
# hint: use try/except to check if the file exists, or import os and use os.path.exists()

# Step 2: Define a function to add an item to the list.
# Prompt the user for the item name and add it to the list.

# Step 3: Define a function to remove an item from the list.
# Prompt the user for the item name to remove and delete it from the list if it exists.
# hint: use list.remove() or check if item is in list first

# Step 4: Define a function to write the current shopping list to a file called 'shopping_list.txt'.
# hint: use 'w' mode to overwrite the file each time with the current list
# hint: don't forget \n for new lines

# Step 5: create the main program loop with a small menu system which lets the user:
# - Call the functions to add or remove items.
# - After each action, write the updated shopping list to 'shopping_list.txt'.
# - Add a way of exiting the program
# hint: use a while loop with a menu and user choice