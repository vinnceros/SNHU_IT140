# Write a function shampoo_instructions() with parameter num_cycles. 
# If num_cycles is less than 1, print "Too few.". If more than 4, 
# print "Too many.". Else, print "N : Lather and rinse." num_cycles times, 
# where N is the cycle number, followed by "Done.".
# 
# Sample output with input: 2
# 1 : Lather and rinse.
# 2 : Lather and rinse.
# Done.
# 
# Hint: Define and use a loop variable.

def shampoo_instructions(num_cycles):

    cycle = 1  
    if num_cycles < cycle:
        print('Too few.')
    elif num_cycles > 4:
        print('Too many.') 
    else:
        cycle2 = 0     
        while cycle2 < num_cycles:
                cycle2 +=1  
                print(str(cycle2) + ' : Lather and rinse.')                          
        print('Done.')

user_cycles = int(input())
shampoo_instructions(user_cycles)