# zybooks CHALLENGE ACTIVITY 6.3.1 Get user guesses.py
# 
# Write a loop to populate the list user_guesses with a number of guesses. 
# 
# The variable num_guesses is the number of guesses the user will have, which is read first as an integer. 
# 
# Read each guess (an integer) one at a time using int(input()).
# 
# Sample output with input:
# 
# 3 9 5 2
# 
# user_guesses: [9, 5, 2]
# 
# ================================================================== #
# 
# original zybooks code 
# 
# num_guesses = int(input())
# user_guesses = []
# 
# ''' Your solution goes here '''
# 
# print('user_guesses:', user_guesses)
# 
# ================================================================== #

# this code passes all zybooks tests

num_guesses = int(input())
user_guesses = []

for i in range(num_guesses):
    num_guesses = int(input())
    user_guesses.append(num_guesses)

print('user_guesses:', user_guesses)

# ================================================================== #

