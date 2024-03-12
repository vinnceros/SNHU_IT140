welcome = 'Davy\'s auto shop services\n'
services = {'Oil change': 35,
            'Tire rotation': 19,
            'Car wash': 7,
            'Car wax': 12}
no_service = '-'

# Welcome Message 

print(welcome +
      'Oil change -- ${oil_chng:d}\n'.format(oil_chng = services['Oil change']) +
      'Tire rotation -- ${tire_rot:d}\n'.format(tire_rot = services['Tire rotation']) +
      'Car wash -- ${car_wash:d}\n'.format(car_wash = services['Car wash']) +
      'Car wax -- ${car_wax:d}\n'.format(car_wax = services['Car wax'])) 

# Select Service 

service1 = str(input('Select first service:\n'))
service2 = str(input('Select second service:\n'))

# Cost and total 

# SERVICES

print('\nDavy\'s auto shop invoice\n')

if service1 in services:
    print('Service 1:', service1 + ', ${serv1_cost:d}'.format(serv1_cost = services[service1]))
elif service1 == no_service:
    print('Service 1: No service')    

if service2 in services:
    print('Service 2:', service2 + ', ${serv2_cost:d}\n'.format(serv2_cost = services[service2]))
elif service2 == no_service:
    print('Service 2: No service\n')
    
# TOTAL COST

if service1 in services and service2 in services:
    total_cost = services[service1] + services[service2]
    print('Total: ${total_cost:d}'.format(total_cost = total_cost))
elif service1 == no_service and service2 in services:
    print('Total: ${serv2_cost:d}'.format(serv2_cost = services[service2]))
elif service2 == no_service and service1 in services:
    print('Total: ${serv1_cost:d}'.format(serv1_cost = services[service1]))
else:
    print('Total: $0')