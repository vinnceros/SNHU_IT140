# zybooks CHALLENGE ACTIVITY 6.3.2 Sum extra credit.py
# 
# Assign sum_extra with the total extra credit received given list test_grades. 
# 
# Full credit is 100, so anything over 100 is extra credit.
# 
# Sample output for the given program with input: '101 83 107 90'
# 
# Sum extra: 8
# 
# (because 1 + 0 + 7 + 0 is 8)
# 
# ================================================================== #
# 
# original zybooks code 
# 
# user_input = input()
# test_grades = list(map(int, user_input.split())) # test_grades is an integer list of test scores
# 
# sum_extra = -999 # Initialize 0 before your loop
# 
# ''' Your solution goes here '''
# 
# print('Sum extra:', sum_extra)
# 
# ================================================================== #

# this code passes all zybooks tests

user_input = input()
test_grades = list(map(int, user_input.split())) # test_grades is an integer list of test scores

sum_extra = -999 # Initialize 0 before your loop

sum_extra = 0 
for i in test_grades:
    if i > 100:
        extra = i - 100
        sum_extra += extra

print('Sum extra:', sum_extra)

# ================================================================== #

