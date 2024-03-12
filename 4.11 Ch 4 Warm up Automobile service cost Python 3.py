# (1) Prompt the user for an automobile service. Output the user's input. (1 pt)
# 
print('Enter desired auto service: ')
automobile_service = input()
print('You entered: ' + automobile_service)
# 
# (2) Output the price of the requested service. (4 pts)
# 
# The program should support the following services:
# Oil change -- $35
# Tire rotation -- $19
# Car wash -- $7
# 
# If the user enters a service that is not listed above, then output the following error message:
# Error: Requested service is not recognized
# 
# Creating a list of services

list_of_services = ["Oil change", "Tire rotation", "Car wash"]

if automobile_service == list_of_services[0]:
    print('Cost of oil change: ' + '$35')
elif automobile_service == list_of_services[1]:
    print('Cost of tire rotation: ' + '$19')
elif automobile_service == list_of_services[2]:
    print('Cost of car wash: ' + '$7')
else:
    print('Error: Requested service is not recognized')







