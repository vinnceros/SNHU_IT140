# (1) Output a menu of automotive services and the corresponding cost of each service. (2 pts)
# Ex. Davy's auto shop services
# Oil change -- $35
# Tire rotation -- $19
# Car wash -- $7
# Car wax -- $12

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print()

# (2) Prompt the user for two services from the menu. (2 pts)
# Ex. Select first service:
# Oil change
# Select second service:
# Car wax

print('Select first service: ')
first_service = input()

print('Select second service: ')
second_service = input()
print()

# (3) Output an invoice for the services selected. Output the cost for each service and the total cost. (3 pts)
# Ex. Davy's auto shop invoice
# Service 1: Oil change, $35
# Service 2: Car wax, $12
# Total: $47

print("Davy's auto shop invoice ")
print()

# Creating a list of services

list_of_services = ["Oil change", "Tire rotation", "Car wash" , "Car wax" , "-"]

if first_service == list_of_services[0]:
    print('Service 1: Oil change, $35')
elif first_service == list_of_services[1]:
    print('Service 1: Tire rotation, $19')
elif first_service == list_of_services[2]:
    print('Service 1: Car wash, $7')
elif first_service == list_of_services[3]:
    print('Service 1: Car wax, $12')
elif first_service == list_of_services[4]:
    print('Service 1: No service')    
else:
    print('Error: Requested service is not recognized')

if second_service == list_of_services[0]:
    print('Service 2: Oil change, $35')
elif second_service == list_of_services[1]:
    print('Service 2: Tire rotation, $19')
elif second_service == list_of_services[2]:
    print('Service 2: Car wash, $7')
elif second_service == list_of_services[3]:
    print('Service 2: Car wax, $12')
elif second_service == list_of_services[4]:
    print('Service 2: No service')    
else:
    print('Error: Requested service is not recognized')
print()

# Determining the price of first entry

price1 = 0
if first_service == list_of_services[0]:
    price1 = int(35)
elif first_service == list_of_services[1]:  
    price1 = int(19)
elif first_service == list_of_services[2]:  
    price1 = int(7) 
elif first_service == list_of_services[3]:  
    price1 = int(12)
elif first_service == list_of_services[4]:  
    price1 = int(0)    
else:
    price1 = int(0)  

# Determining the price of second entry

price2 = 0
if second_service == list_of_services[0]:
    price2 = int(35)
elif second_service == list_of_services[1]:  
    price2 = int(19)
elif second_service == list_of_services[2]:  
    price2 = int(7) 
elif second_service == list_of_services[3]:  
    price2 = int(12)
elif second_service == list_of_services[4]:  
    price2 = int(0) 
else:
    price2 = int(0)  

print("Total: " + '$' + str(price1 + price2))    