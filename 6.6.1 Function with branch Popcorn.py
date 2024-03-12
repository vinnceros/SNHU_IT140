# Define function print_popcorn_time() with parameter bag_ounces. 
# If bag_ounces is less than 3, print "Too small". If greater than 10, 
# print "Too large". Otherwise, compute and print 6 * bag_ounces followed by 
# "seconds". End with a newline.
# 
# Sample output with input: 7
# 42 seconds

def print_popcorn_time(bag_ounces):
    if bag_ounces < 3:
        print('Too small')
    elif bag_ounces >10:
        print('Too large')
    else:
        compute = 6 * bag_ounces
        print(str(compute) + " seconds")        

user_ounces = int(input())
print_popcorn_time(user_ounces)