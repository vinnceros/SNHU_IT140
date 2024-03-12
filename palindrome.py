import itertools
pal = []
num1 = list(range(100, 1000))

product = [x * y for x, y in itertools.product(num1, num1)]
    
for i in product: 
    z = len(str(i)) // 2
    first_num = str(i)[:z]
    reverse_last_num = str(i)[::-1]
    last_num = str(reverse_last_num)[:z]
    if first_num == last_num and i not in pal:
        pal.append(i)

pal.sort()
print(pal)