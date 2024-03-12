# Comma Code

spam = ['apples', 'bananas', 'tofu', 'cats'] # define the lists that will need to be used to create the sentence, or multiple lists if desired
schedule = ['IT75' , 'IT100' , 'IT105' , 'IT110'] # secondary list to further test function

def corrected(list): # corrected will be defined as a function to be applied to the list, this will enable the function to be used on lists named other than spam.

    counter = 0 # start a counter to keep track of number of loops.

    newlist = '' # establishes newlist as an empty list, so that the items in spam can be inputed.

    while counter < len(list) - 2: # run the while loop for all instances in the list except the last two as they need to be treated differently.
        newlist = newlist + list[counter] + ', ' # adds to newlist and makes it equal to what it adds. Here it is adding whatever item the list counter is on in addition to a comma afterwards.
        counter = counter + 1 # add 1 to the counter, and restart loop until the length condition is met.
        
    newlist = newlist + list[-2] + ' ,and ' # the second to last item within the list, [-2], is added to the newlist with the addition of ,and to make the sentence work.
    
    newlist = newlist + list[-1] + '.' # the last item in the list achieved by going backwards [-1], has a period added afterwards to close out the sentence.
    
    return newlist # the newlist is the output of the function corrected being applied to the list.

print(corrected(spam)) # prints the function corrected applied to the list spam.

print('My schedule this semester includes: ' + corrected(schedule)) # prints secondary list after the writing.
