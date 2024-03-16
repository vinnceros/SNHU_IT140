# zybooks CHALLENGE ACTIVITY 5.13.1 Return number of pennies in total.py
# 
# Write a function number_of_pennies() that returns the total number of pennies given a number of dollars and (optionally) a number of pennies.
# 
# Sample output with inputs: 5 6 4
# 
# 506
# 400
# 
# ================================================================== #
# 
# original zybooks code 
# 
# 
# ''' Your solution goes here '''
# 
# print(number_of_pennies(int(input()), int(input()))) # Both dollars and pennies
# print(number_of_pennies(int(input())))               # Dollars only
# 
# ================================================================== #

# this code passes all zybooks tests 


def number_of_pennies(num_dollars, num_pennies=0):
    total = num_dollars * 100 + num_pennies
    return total

print(number_of_pennies(int(input()), int(input()))) # Both dollars and pennies
print(number_of_pennies(int(input())))               # Dollars only


# ================================================================== #

