# zybooks 3.11 LAB Smallest number

# Write a program whose inputs are three integers, and whose output is the smallest of the three values.

# Ex: If the input is:

# 7
# 15
# 3

# the output is:

# 3
# 388168.2533680.qx3zqy7

# LAB ACTIVITY 3.11.1: Smallest number


# ================================================================== #


# my code for 3.11.1 LAB ACTIVITY: Smallest number -- this code passes all zybooks tests 

first_num = int(input())
second_num = int(input())
third_num = int(input())

if (first_num < second_num) and (first_num < third_num):
    smallest_num = first_num
elif (second_num < first_num) and (second_num < third_num):
    smallest_num = second_num
else:
    smallest_num = third_num

print (smallest_num)


# ================================================================== #

