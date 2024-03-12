# Given the number of rows and the number of columns, write nested loops to print a rectangle.
# 
# Sample output with inputs: 2 3
# * * * 
# * * * 
# 

num_rows = int(input())
num_cols = int(input())

# Note 1: You will need to declare more variables
# Note 2: Place end=' ' at the end of your print statement to separate seats by spaces

c1 = 1
while c1 <= num_rows:
    c2 = 'A'
    while c2 < chr(ord('A') + num_cols):
        print('{}{}'.format(c1, c2), end=' ')
        c2 = chr(ord(c2) + 1)
    c1 += 1

print()