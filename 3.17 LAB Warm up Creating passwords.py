# FIXME (1): Finish reading another word and an integer into variables. 
# Output all the values on a single line

# (1) Prompt the user to enter two words and a number, storing each into separate variables.
# Then, output those three values on a single line separated by a space. (Submit for 1 point)

print('Enter favorite color:')
favorite_color = input()

print("Enter pet's name:")
pets_name = input()

print("Enter a number:")
entered_number = int(input())

print('You entered: ' + favorite_color + ' ' + pets_name + ' ' + str(entered_number))
print()

# FIXME (2): Output two password options
# (2) Output two passwords using a combination of the user input. Format the passwords as 
# shown below. (Submit for 2 points, so 3 points total).

first_password = favorite_color + '_' + pets_name
second_password = str(entered_number) + favorite_color + str(entered_number)

print('First password: ' + first_password)
print('Second password: ' + second_password)
print()

# FIXME (3): Output the length of the two password options
# (3)Output the length of each password (the number of characters in the strings). 
# (Submit for 2 points, so 5 points total).

print('Number of characters in ' + first_password + ': ' + str(len(first_password)))
print('Number of characters in ' + second_password + ': ' + str(len(second_password)))