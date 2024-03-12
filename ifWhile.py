# What is the output of the following code?
# 
# Answer:
# 13 16 19 113 116 119 
# 
# outer loop: i1 = 1,11 
# inner loop: i2=3,6,9 
# i1 cannot exceed 19 so the outer loop only runs twice. 
# i2 cannot exceed 9 so the inner loop will run 3 times.

i1 = 1
while i1 < 19:
    i2 = 3
    while i2 <= 9:
        print('{}{}'.format(i1,i2), end=' ')
        i2 = i2 + 3
    i1 = i1 + 10
