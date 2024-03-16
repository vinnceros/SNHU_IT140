# zybooks CHALLENGE ACTIVITY 5.3.3 Function definition Volume of a pyramid
# 
# Define a function pyramid_volume with parameters base_length, base_width, and pyramid_height, 
# that returns the volume of a pyramid with a rectangular base.
# 
# Sample output with inputs: 4.5 2.1 3.0
# Volume for 4.5, 2.1, 3.0 is: 9.45
# Relevant geometry equations:
# Volume = base area x height x 1/3
# Base area = base length x base width.
# 
# ================================================================== #
# 
# original zybooks code: 
# 
# ''' Your solution goes here '''
# 
# length = float(input())
# width = float(input())
# height = float(input())
# print('Volume for 4.5, 2.1, 3.0 is:', pyramid_volume(length, width, height))
# 
# ================================================================== #

# passes all zybooks tesets 

base_area = 0
volume = 0
def pyramid_volume(base_length, base_width, pyramid_height):
    base_area = base_length * base_width
    volume = base_area * pyramid_height * (1/3)
    return volume

length = float(input())
width = float(input())
height = float(input())
print('Volume for 4.5, 2.1, 3.0 is:', pyramid_volume(length, width, height))


# ================================================================== #


