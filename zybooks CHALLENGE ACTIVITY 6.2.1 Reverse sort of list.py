# zybooks CHALLENGE ACTIVITY 6.2.1 Reverse sort of list.py
# 
# Sort short_names in reverse alphabetic order.
# 
# Sample output with input: 'Jan Sam Ann Joe Tod'
# 
# ['Tod', 'Sam', 'Joe', 'Jan', 'Ann']
# 
# ================================================================== #
# 
# original zybooks code 
# 
# user_input = input()
# short_names = user_input.split()
# 
# ''' Your solution goes here '''
# 
# print(short_names)
# 
# ================================================================== #

# this code passes all zybooks tests

user_input = input()
short_names = user_input.split()

short_names.sort()
short_names.reverse()

print(short_names)

# ================================================================== #


