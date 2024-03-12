# Print air_temperature with 1 decimal point followed by C.
# 
# Sample output with input: 36.4158102
# 36.4C

air_temperature = float(input('Enter aire temp:'))

print('{temp:.1f}'.format(temp=air_temperature) + 'C')

