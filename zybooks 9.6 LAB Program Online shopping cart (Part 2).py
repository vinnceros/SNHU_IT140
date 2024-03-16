# zybooks 9.6 LAB Program Online shopping cart (Part 2).py
# 
# This program extends the earlier "Online shopping cart" program. (Consider first saving your earlier program).
# 
# (1) Extend the ItemToPurchase class to contain a new attribute. (2 pts)
# 
# item_description (string) - Set to "none" in default constructor
# Implement the following method for the ItemToPurchase class.
# 
# print_item_description() - Prints item_description attribute for an ItemToPurchase object. Has an ItemToPurchase parameter.
# 
# Ex. of print_item_description() output:
# 
# Bottled Water: Deer Park, 12 oz.
# 
# 
# (2) Build the ShoppingCart class with the following data attributes and related methods. 
# Note: Some can be method stubs (empty methods) initially, to be completed in later steps.
# 
# Parameterized constructor which takes the customer name and date as parameters (2 pts)
# Attributes
# customer_name (string) - Initialized in default constructor to "none"
# current_date (string) - Initialized in default constructor to "January 1, 2016"
# cart_items (list)
# Methods
# add_item()
# Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
# remove_item()
# Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
# If item name cannot be found, output this message: Item not found in cart. Nothing removed.
# modify_item()
# Modifies an item's quantity. Has parameter ItemToPurchase. Does not return anything.
# If item can be found (by name) in cart, modify item in cart.
# If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
# get_num_items_in_cart() (2 pts)
# Returns quantity of all items in cart. Has no parameters.
# get_cost_of_cart() (2 pts)
# Determines and returns the total cost of items in cart. Has no parameters.
# print_total()
# Outputs total of objects in cart.
# If cart is empty, output this message: SHOPPING CART IS EMPTY
# print_descriptions()
# Outputs each item's description.
# Ex. of print_total() output:
# 
# John Doe's Shopping Cart - February 1, 2016
# Number of Items: 8
# 
# Nike Romaleos 2 @ $189 = $378
# Chocolate Chips 5 @ $3 = $15
# Powerbeats 2 Headphones 1 @ $128 = $128
# 
# Total: $521
# 
# Ex. of print_descriptions() output:
# 
# John Doe's Shopping Cart - February 1, 2016
# 
# Item Descriptions
# Nike Romaleos: Volt color, Weightlifting shoes
# Chocolate Chips: Semi-sweet
# Powerbeats 2 Headphones: Bluetooth headphones
# 
# (3) In the main section of the code, prompt the user for a customer's name and today's date. Output the name and date. 
# Create an object of type ShoppingCart. (1 pt)
# 
# Ex:
# 
# Enter customer's name:
# John Doe
# Enter today's date:
# February 1, 2016
# 
# Customer name: John Doe
# Today's date: February 1, 2016
# 
# (4) Implement the print_menu() function to print the following menu of options to manipulate the shopping cart. (1 pt)
# 
# Ex:
# 
# MENU
# a - Add item to cart
# r - Remove item from cart
# c - Change item quantity
# i - Output items' descriptions
# o - Output shopping cart
# q - Quit
# 
# (5) Implement the execute_menu() function that takes 2 parameters: a character representing the user's choice and a shopping cart. 
# execute_menu() performs the menu options described below, according to the user's choice. (1 pt)
# 
# 
# (6) In the main section of the code, call print_menu() and prompt for the user's choice of menu options. Each option is represented by a single character.
# 
# If an invalid character is entered, continue to prompt for a valid choice. When a valid option is entered, execute the option by calling execute_menu(). # Then, print the menu and prompt for a new option. Continue until the user enters 'q'. Hint: Implement Quit before implementing other options. (1 pt)
# 
# Ex:
# 
# a - Add item to cart
# r - Remove item from cart
# c - Change item quantity
# i - Output items' descriptions
# o - Output shopping cart
# q - Quit
# 
# Choose an option:
# 
# (7) Implement Output shopping cart menu option in execute_menu(). (3 pts)
# 
# Ex:
# 
# OUTPUT SHOPPING CART
# John Doe's Shopping Cart - February 1, 2016
# Number of Items: 8
# 
# Nike Romaleos 2 @ $189 = $378
# Chocolate Chips 5 @ $3 = $15
# Powerbeats 2 Headphones 1 @ $128 = $128
# 
# Total: $521
# 
# (8) Implement Output item's description menu option in execute_menu(). (2 pts)
# 
# Ex:
# 
# OUTPUT ITEMS' DESCRIPTIONS
# John Doe's Shopping Cart - February 1, 2016

# Item Descriptions
# Nike Romaleos: Volt color, Weightlifting shoes
# Chocolate Chips: Semi-sweet
# Powerbeats 2 Headphones: Bluetooth headphones
# 
# (9) Implement Add item to cart menu option in execute_menu(). (3 pts)
# 
# Ex:
# 
# ADD ITEM TO CART
# Enter the item name:
# Nike Romaleos
# Enter the item description:
# Volt color, Weightlifting shoes
# Enter the item price:
# 189
# Enter the item quantity:
# 2
# 
# (10) Implement remove item menu option in execute_menu(). (4 pts)
# 
# Ex:
# 
# REMOVE ITEM FROM CART
# Enter name of item to remove:
# Chocolate Chips
# 
# (11) Implement Change item quantity menu option in execute_menu(). Hint: Make new ItemToPurchase object before using ModifyItem() method. (5 pts)
# 
# Ex:
# 
# CHANGE ITEM QUANTITY
# Enter the item name:
# Nike Romaleos
# Enter the new quantity:
# 3
# 
# 
# ================================================================== #
# 
# LAB ACTIVITY 9.6.1: LAB*: Program: Online shopping cart (Part 2)
# 
# Type code here
# 
# ================================================================== #


