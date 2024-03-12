# Collatz

def user_number():#defining the number inputed by the user
    
    while True: #creating a loop incase the user inputs an incorrect number

        try:
            number = int(input("Enter a number to test the Collatz Conjecture: ")) # requests a number by the user and makes it an integer.
            print("The collatz sequence is:") # if a correct input is put in then try is True and the program continues

        except ValueError: # If the input is not an integer then the message is printed.
            print("You did not select a correct number, please try again.")

        else:    
            return number # this re-runs the loop until a proper integer is picked.

def collatz(n): # define the collatz function
    print(n) # prints the first number in the sequence
    
    while n != 1: # continues while loop as long as the number is not equal to 1

        if n % 2 == 0: # If the number divided by 2 has a remainder equal to 0, the number is even and continues. If not it is odd and goes to else.
            n = n // 2 # n being even, is divided by 2 in an attempt to get closer to 1
            print(n) # prints the number and restarts the loop.

        else: # If not even, the number should be odd
            n = n * 3 + 1 # odd number is multipled by 3 and 1 added to it in an attempt to get an even number
            print(n) # prints the new number and continues loop.

collatz(user_number()) # uses the function collatz on the number inputed by the user.
