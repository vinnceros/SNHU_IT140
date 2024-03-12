# 6.21 LAB Driving costs functions

def driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon):

    return (driven_miles / miles_per_gallon) * dollars_per_gallon

if __name__ == '__main__':

    milesPerGallon = float(input())

    dollarsPerGallon = float(input())

    print('{:.2f}'.format(driving_cost(10, milesPerGallon, dollarsPerGallon)))
    print('{:.2f}'.format(driving_cost(50, milesPerGallon, dollarsPerGallon)))
    print('{:.2f}'.format(driving_cost(400, milesPerGallon, dollarsPerGallon)))

    print('{:.2f}'.format(driving_cost(50, 20.0, 3.1599)))