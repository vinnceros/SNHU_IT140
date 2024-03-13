
curr_power = 2
user_char = 'y'

while user_char == 'y':
   print(curr_power)
   curr_power = curr_power * 2
   user_char = input()

print('Done')

# While-Loop making a face

nose = '0'  # Looks a little like a nose -- it would be better if we used an upside down question mark (ô ¿ ô ) but harder to pull off 
user_value = '-'

while user_value != 'q':
    print(' {} {} '.format(user_value, user_value))  # Print eyes (the ones above are ALT and 147)
    print('  {}  '.format(nose))  # Print nose (the upside down question mark is ALT and 168)
    print(user_value*5)  # Print mouth
    print('\n')

# Get new character for eyes and mouth

    user_input = input("Enter a character ('q' for quit): \n")
    user_value = user_input[0]

print('Goodbye.\n')

# While-Loop another example

year_considered = 2020  # Year being considered
num_ancestors = 2  # Approx. ancestors in considered year
years_per_generation = 20  # Approx. years per generation

user_year = int(input('Enter a past year (neg. for B.C.): '))
print()

while year_considered >= user_year:
    print('Ancestors in {}: {}'.format(year_considered, num_ancestors))

    num_ancestors = num_ancestors * 2
    year_considered = year_considered - years_per_generation

# While-Loop more practice

entered_age = int(input())

while (entered_age < 15 or entered_age > 30):
    if entered_age < 15:
        print('Very young')
    else:
         print('Grown up')
    entered_age = int(input())

print('Perfect match', end='')    