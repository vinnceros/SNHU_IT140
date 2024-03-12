# For-Loop: Iterate through a dictionary

channels = {
    'MTV': 35,
    'CNN': 28,
    'FOX': 11,
    'NBC': 4,
    'CBS': 12
}

for c in channels:
    print('{} is on channel {}'.format(c, channels[c]))
print()


# For-Loop: Iterate through strings

my_str = ''
for character in "Take me to the moon.":
    my_str += character + '_'
print(my_str)    
print()


# For-Loop: Iterate through a list, then calculate average

daily_revenues = [
    1890.75   # Sunday
    2356.23,  # Monday
    1800.12,  # Tuesday
    1792.50,  # Wednesday
    2058.10,  # Thursday
    1988.00,  # Friday
    2002.99,  # Saturday   
]

total = 0
for day in daily_revenues:
    total += day

average = total / len(daily_revenues)

print('Weekly revenue: ${:.2f}'.format(total))
print('Daily average revenue: ${:.2f}'.format(average))
print()


# For-Loop: Iterate through a list in reverse

names = [
    'Biffle',
    'Bowyer', 
    'Busch',
    'Gordon',
    'Patrick'
]

for name in names:
    print(name, '|', end=' ')

print('\nPrinting in reverse:')
for name in reversed(names):
    print(name, '|', end=' ')
