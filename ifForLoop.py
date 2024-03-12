# If-for loop example
num = 0
while num >= 0:
    num = int(input('Enter an integer (negative to quit):\n'))

    if num >= 0:
        print('Depicted graphically:')
        for i in range(0, num, 5):
            print('*', end=' ')
        print('\n')

print('Goodbye.')

