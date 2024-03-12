# Challenge Activity 1 #
# 
# print_pattern() prints 5 characters. Call print_pattern() twice to print 10 characters. Example output:
# *****
# *****

def print_pattern():
   print('*****')

print_pattern()
print_pattern()

# Challenge Activity 2 #
# 
# Define print_shape() to print the below shape. Example output:
# ***
# ***
# ***
# 
# ''' Your solution goes here '''

def print_shape():
    print('***')
    print('***')
    print('***')

print_shape()

# Challenge Activity # 

def output_minutes_as_hours(orig_minutes):
    hours = orig_minutes / 60
    print(str(orig_minutes) + ' is equal to ' + str(hours) + ' hours.')

n = float(input('Tell me a number of minutes and I will tell you how many hours it is '))

output_minutes_as_hours(n)

# Challenge Activity 2 #
# 
# Define a function print_total_inches, with parameters num_feet and num_inches, that prints the total number of inches.
# Note: There are 12 inches in a foot.

def print_total_inches(feet, inches):
    
    inchfeet = feet * 12
    total_inches = inchfeet + inches
    print('Total inches: ' + str(total_inches))

feet = float(input('How many feet is the object '))
inches = float(input('Additional inches '))
print_total_inches(feet, inches)

# Challenge Activity 1 #
# 
# Complete the program by writing and calling a function that converts a temperature from Celsius into Fahrenheit.
# Use the formula F = C x 9/5 + 32. Test your program knowing that 50 Celsius is 122 Fahrenheit.

def c_to_f(c):
    temp_f = c * 9 / 5 +32
    return  temp_f

temp_c = float(input('Enter temperature in Celsius: '))
temp_f = None
print('The temperature in Fahrenheit is ' + str(c_to_f(temp_c)))

# Challenge Activity 1 #
# 
# Write a function so that the main program below can be replaced by the simpler code that calls function mph_and_minutes_to_miles().
# Original main program:

def distance(mph, time):
    hours_traveled = time / 60.0
    miles_traveled = hours_traveled * mph
    return miles_traveled

miles_per_hour = float(input('Miles per hour: '))
minutes_traveled = float(input('Minutes traveled: '))

print('Miles: ' + str(distance(miles_per_hour, minutes_traveled)))

