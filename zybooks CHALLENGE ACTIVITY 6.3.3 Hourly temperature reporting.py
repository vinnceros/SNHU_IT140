# zybooks CHALLENGE ACTIVITY 6.3.3 Hourly temperature reporting.py
# 
# Write a loop to print all elements in hourly_temperature. 
# 
# Separate elements with a -> surrounded by spaces.
# 
# Sample output for the given program with input: '90 92 94 95'
# 
# 90 -> 92 -> 94 -> 95 
# 
# Note: 95 is followed by a space, then a newline.
# 
# ================================================================== #
# 
# original zybooks code 
# 
# user_input = input()
# hourly_temperature = user_input.split()
# 
# ''' Your solution goes here '''
# 
# ================================================================== #

# this code passes all zybooks code 

user_input = input()
hourly_temperature = user_input.split()

string = []
for temp in hourly_temperature:
    string.append(temp)
print(' -> '.join(string), end=' ')
print()

# ================================================================== #

