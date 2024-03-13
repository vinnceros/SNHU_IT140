# zybooks 6.12 LAB Varied amount of input data.py
# 
# Statistics are often calculated with varying amounts of input data. 
# Write a program that takes any number of integers as input, and outputs the average and max.
# 
# Ex: If the input is:
# 
# 15 20 0 5
# 
# the output is:
# 
# 10 20
# 
# ================================================================== #
# 
# LAB ACTIVITY 6.12.1: LAB: Varied amount of input data
# 
# ''' Type your code here. '''
# 
# ================================================================== #

# this code passes all zybooks tests 

data = input()
strings = data.split()
numbers = list(map(int, strings))
print('%d %d'%(sum(numbers)/len(numbers), max(numbers)))

# ================================================================== #
