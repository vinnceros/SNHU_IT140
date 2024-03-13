# zybooks 6.13 LAB Filter and sort a list.py 
# 
# Write a program that gets a list of integers from input, and outputs non-negative integers in ascending order (lowest to highest).
# 
# Ex: If the input is:
# 
# 10 -7 4 39 -6 12 2
# 
# the output is:
# 
# 2 4 10 12 39 
# 
# For coding simplicity, follow every output value by a space. 
# 
# Do not end with newline.
# 
# ================================================================== #
# 
# LAB ACTIVITY 6.13.1: LAB: Filter and sort a list
# 
# ''' Type your code here. '''
#
# ================================================================== #

# this code passes all zybooks tests  

string = input()
numbers = list(map(int, string.split()))
positive = [i for i in numbers if i >= 0]
positive.sort()
for i in positive:
    print(i, end = ' ')

# ================================================================== #


