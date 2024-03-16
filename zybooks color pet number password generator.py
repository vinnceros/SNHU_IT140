fav_color = input('Enter favorite color:\n')
pet_name = input('Enter pet\'s name:\n')
number = input('Enter a number:\n')

print(f'You entered: {fav_color} {pet_name} {number}\n')

password1 = fav_color + '_' + pet_name
password2 = number + fav_color + number

print(f'First password: {password1}')
print(f'Second password: {password2}\n')

print(f'Number of characters in {password1}:', len(password1))
print(f'Number of characters in {password2}:', len(password2))
