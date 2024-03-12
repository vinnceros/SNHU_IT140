# (2) Complete the get_num_of_characters() function, which returns the number of characters in the user's string. 
# We encourage you to use a for loop in this function. (2 pts)
# (3) Extend the program by calling the get_num_of_characters() function and then output the returned result. (1 pt)

def get_num_of_characters(inputStr):
    num_of_characters = 0
    for character in inputStr:
        num_of_characters = num_of_characters + 1
    return num_of_characters

# (4) Extend the program further by implementing the output_without_whitespace() function. output_without_whitespace() outputs the 
# string's characters except for whitespace (spaces, tabs). Note: A tab is '\t'. Call the output_without_whitespace() function in main(). (2 pts)

def output_without_whitespace(input):
    no_space_input = ''
    for a in input:
        if a != ' ':
            no_space_input = no_space_input + a
    return no_space_input
    
if __name__ == '__main__':
#(1) Prompt the user to enter a string of their choosing. Output the string. (1 pt)
    print('Enter a sentence or phrase:')
    user_unput1 = input()

    print('You entered: ' + user_unput1)

    print('Number of characters: ' + str(get_num_of_characters(user_unput1)))
    
    print('String with no whitespace: ' + str(output_without_whitespace(user_unput1)))   