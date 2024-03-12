# Total Change

change = int(input('')) # receive input from the user
if change > 0:                          # checks if there is change to provide coins
    if change >= 100:                   # checks if the amount is greater or equal to 100
        if (change // 100) != 0:        # this is to check if there is change at this point
            if (change // 100) > 1:     # provide the plural if more than 1
                print('{} Dollars'.format(change // 100))
                change = (change % 100)
            else:
                print('{} Dollar'.format(change // 100)) # prints the dollar amount without a float
                change = (change % 100) # this leaves the remainder after calculating the amount of change
        else:                           # if there is no change do this
            change = (change % 100)     # if there no change here there will be no output
    if change <= 99:                    # checks if the amount is lower or equal to 99
        if (change // 25) != 0:         # this is to check if there is change at this point
            if (change // 25) > 1:
                print('{} Quarters'.format(change // 25))
                change = (change % 25)
            else:
                print('{} Quarter'.format(change // 25))
                change = (change % 25)
        else:
            change = (change % 25)
    if change <= 24:                    # checks if the amount is lower or equal to 24
        if (change // 10) != 0:         # this is to check if there is change at this point
            if (change // 10) > 1:
                print('{} Dimes'.format(change // 10))
                change = (change % 10)
            else:
                print('{} Dime'.format(change // 10))
                change = (change % 10)
        else:
            change = (change % 10)
    if change <= 9:                     # checks if the amount is lower or equal to 9
        if (change // 5) != 0:          # this is to check if there is change at this point
            if (change // 5) > 1:
                print('{} Nickels'.format(change // 5))
                change = (change % 5)
            else:
                print('{} Nickel'.format(change // 5))
                change = (change % 5)
        else:
            change = (change % 5)
    if change <= 4:                     # checks if the amount is lower or equal to 4
        if (change // 1) != 0:          # this is to check if there is change at this point
            if (change // 1) > 1:
                print('{} Pennies'.format(change // 1))
            else:
                print('{} Penny'.format(change // 1))
else:
    print('No change')                  # tells the user to fuck off if there is nothing to convert