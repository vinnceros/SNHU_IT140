# Program to print all 2-letter domain names.
# 
# Note that ord() and chr() convert between text and the ASCII or Unicode encoding:
# -  ord('a') yields the encoded value of 'a', the number 97.
# -  ord('a')+1 adds 1 to the encoded value of 'a', giving 98.
# -  chr(ord('a')+1) converts 98 back into a letter, producing 'b'

print('Two-letter domain names:')

letter1 = 'a'
letter2 = '?'
while letter1 <= 'z':  # Outer loop
    letter2 = 'a'
    while letter2 <= 'z':  # Inner loop
        print('{}{}.com'.format(letter1, letter2))
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)

# Nested-Loop another example

num = 0
while num >= 0:
    num = int(input('Enter an integer (negative to quit):\n'))

    if num >= 0:
        print('Depicted graphically:')
        for i in range(0, num, 5):
            print('*', end=' ')
        print('\n')

print('Goodbye.')  