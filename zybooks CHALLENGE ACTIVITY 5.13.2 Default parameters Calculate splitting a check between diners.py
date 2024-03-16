# zybooks CHALLENGE ACTIVITY 5.13.2 Default parameters Calculate splitting a check between diners.py
# 
# Write a split_check function that returns the amount that each diner must pay to cover the cost of the meal.
# 
# The function has 4 parameters:
# 
# bill: The amount of the bill.
# people: The number of diners to split the bill between.
# tax_percentage: The extra tax percentage to add to the bill.
# tip_percentage: The extra tip percentage to add to the bill.
# 
# The tax or tip percentages are optional and may not be given when calling split_check. 
# 
# Use default parameter values of 0.15 (15%) for tip_percentage, and 0.09 (9%) for tax_percentage. 
# 
# Assume that the tip is calculated from the amount of the bill before tax.
# 
# Sample output with inputs: 25 2
# 
# Cost per diner: 15.5
# 
# Sample output with inputs: 100 2 0.075 0.21
# 
# Cost per diner: 64.25
# 
# 
# ================================================================== #
# 
# original zybooks code 
# 
# FIXME: Write the split_check function. HINT: Calculate the amount of tip and tax, add to the bill total, then divide by the number of diners.
# 
# ''' Your solution goes here '''
# 
# bill = float(input())
# people = int(input())
# 
# Cost per diner at the default tax and tip percentages
# print('Cost per diner:', split_check(bill, people))
# 
# bill = float(input())
# people = int(input())
# new_tax_percentage = float(input())
# new_tip_percentage = float(input())
# 
# Cost per diner at different tax and tip percentages
# print('Cost per diner:', split_check(bill, people, new_tax_percentage, new_tip_percentage))
# 
# 
# ================================================================== #
# 
# testing
# 
# FIXME: Write the split_check function. HINT: Calculate the amount of tip and tax,
# add to the bill total, then divide by the number of diners.
# 
# total = float(input('Enter bill total:\n'))
# people = int(input('Enter number of diners:\n'))
# 
# print('Cost per diner:', split_check(total, people, tax_rate = 0.075))
# 
# bill = float(input())
# people = int(input())
# 
# Cost per diner at the default tax and tip percentages
# print('Cost per diner:', split_check(bill, people))
# 
# bill = float(input())
# people = int(input())
# new_tax_percentage = float(input())
# new_tip_percentage = float(input())
# 
# Cost per diner at different tax and tip percentages
print('Cost per diner:', split_check(bill, people, new_tax_percentage, new_tip_percentage))
# 
# ================================================================== #
# 
# this code passes some zybooks tests 
# 
# FIXME: Write the split_check function. HINT: Calculate the amount of tip and tax,
# add to the bill total, then divide by the number of diners.
# 
# def split_check(bill, people, new_tip_percentage = 0.15, new_tax_percentage = 0.075):
#     total_bill = ((bill + (bill * new_tip_percentage) + (bill * new_tax_percentage))) / people
#     return total_bill
#  
# bill = float(input())
# people = int(input())
# 
# Cost per diner at the default tax and tip percentages
# print('Cost per diner:', split_check(bill, people))
# 
# bill = float(input())
# people = int(input())
# new_tax_percentage = float(input())
# new_tip_percentage = float(input())
# 
# Cost per diner at different tax and tip percentages
# print('Cost per diner:', split_check(bill, people, new_tax_percentage, new_tip_percentage))
# 
# ================================================================== #


