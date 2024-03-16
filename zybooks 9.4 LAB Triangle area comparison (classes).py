# zybooks 9.4 LAB Triangle area comparison (classes).py

# Given class Triangle, complete the program to read and set the base and height of triangle1 and triangle2, determine which triangle's area is larger, and output the larger triangle's info, making use of Triangle's relevant methods.

# Ex: If the input is:

# 3.0
# 4.0
# 4.0
# 5.0

# where 3.0 is triangle1's base, 4.0 is triangle1's height, 4.0 is triangle2's base, and 5.0 is triangle2's height, the output is:

# Triangle with larger area:

# Base: 4.00
# Height: 5.00
# Area: 10.00

# ================================================================== #

# LAB ACTIVITY 9.4.1: LAB: Triangle area comparison (classes)

# main.py

class Triangle:   
    def __init__(self):
        self.base = 0
        self.height = 0

    def set_base(self, user_base):
        self.base = user_base

    def set_height(self, user_height):
        self.height = user_height
   
    def get_area(self):
        area = 0.5 * self.base * self.height
        return area
   
    def print_info(self):
        print('Base: {:.2f}'.format(self.base))
        print('Height: {:.2f}'.format(self.height))
        print('Area: {:.2f}'.format(self.get_area()))

if __name__ == "__main__":
    triangle1 = Triangle()
    triangle2 = Triangle()

    # TODO: Read and set base and height for triangle1 (use set_base() and set_height())
      
    # TODO: Read and set base and height for triangle2 (use set_base() and set_height())
      
    # TODO: Determine larger triangle (use get_area())
      
    print('Triangle with larger area:')
    # TODO: Output larger triangle's info (use print_info())


# ================================================================== #
# 
# zybooks 9.4 LAB Triangle area comparison (classes).py
# 
# Given class Triangle, complete the program to read and set the base and height of triangle1 and triangle2, 
# determine which triangle's area is larger, and output the larger triangle's info, making use of Triangle's relevant methods.
# 
# Ex: If the input is:
# 
# 3.0
# 4.0
# 4.0
# 5.0
# 
# where 3.0 is triangle1's base, 4.0 is triangle1's height, 4.0 is triangle2's base, and 5.0 is triangle2's height, the output is:
# 
# Triangle with larger area:
# Base: 4.00
# Height: 5.00
# Area: 10.00
# 
# ================================================================== #
# 
# LAB ACTIVITY 9.4.1: LAB: Triangle area comparison (classes)
# 
# program input: 
# 
# 3.0
# 4.0
# 4.0
# 5.0
# 
# ================================================================== #

# this program passes all zybooks tests with the above program input 

class Triangle:
    def __init__(self):
        self.base = 0
        self.height = 0

    def set_base(self, user_base):
        self.base = user_base

    def set_height(self, user_height):
        self.height = user_height

    def get_area(self):
        area = 0.5 * self.base * self.height
        return area

    def print_info(self):
        print('Base: {:.2f}'.format(self.base))
        print('Height: {:.2f}'.format(self.height))
        print('Area: {:.2f}'.format(self.get_area()))


if __name__ == "__main__":
    triangle1 = Triangle()
    triangle2 = Triangle()

    triangle1.set_base(float(input()))
    triangle1.set_height(float(input()))

    triangle2.set_base(float(input()))
    triangle2.set_height(float(input()))

    area1 = triangle1.get_area()
    area2 = triangle2.get_area()

    print('Triangle with larger area:')

    if area1 > area2:
        triangle1.print_info()
    else:
        triangle2.print_info()


# ================================================================== #



