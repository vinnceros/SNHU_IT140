# Part 1 - PYTHONROCKS

# Part 2

def encrypt(text,s): # define the function encrypt with the text to encrypt and shift desired
    result = "" # initialize the result being empty
  
    for i in range(len(text)): # establishes the loop as long as i is within the range of the length of the text
        char = text[i] # identify the character to shift within the string text based on the position in the loop, i
  
        if (char.isupper()): # if the character is upper case
            result += chr((ord(char) +s -65) %26 +65) # result is equal to the last result plus a character whose location is equal to the integer representation in unicode of the character that is being encrypted.
            # Then the shift length is added to it and if it is upper case 65 is removed. 
	    # The remainder of dividing by 26 and add 65 to get the new uppercase location for the letter.

        else: # if not upper case then lower case handles it
            result += chr((ord(char) +s -97) %26 +97) # result is equal to the last result plus a character whose location is equal to the integer representation in unicode of the character that is being encrypted.
            # Then the shift length is added to it and if it is lower case 65 is removed. 
	    # The remainder of dividing by 26 and add 65 to get the new lowercase location for the letter
  
    return result # gives back the result which is all the characters shifted within the length i
  

text = input("Input the text you want encrypted: ") # requests the text to be encrypted and sets it as text
s = int(input("The amount you want to shift the text: ")) # defines the shift as an integer and requests it from the user

print ("Cipher: " + encrypt(text,s)) # prints the result of the user requested information through the function encrypt

# The result of the example in part 2 is 'gurdhvpxoebjasbkwhzcfbiregurynmlqbt'

# Part 3

# cipher =  input('Please input cipher to brute force decrypt ') 
# to be used to brute force inputed cipher

cipher =  'dzeevjfkrlezkvuwffksrcctcls' # to decrypt specific message (this one is encrypted by shifting 17
alphabet = 'abcdefghijklmnopqrstuvwxyz' # used to determine values that are located in the cipher to shift

for attempt in range(len(alphabet)): # starts the loop and defines the number of attempts it will take in the range of alphabet
    translated = '' # translated starts empty
    
    for character in cipher: # starts loop for each character in the cypher
        
        if character in alphabet: # if the character is located in alphabet
            num = alphabet.find(character) # then it finds the location of it and makes that number
            num -= attempt # number then becomes the number minus the current attempt
            
            if num < 0: # checks to see if number is lower than 0
                num += len(alphabet) # if it is then the length of the alphabet is added as to allow it to loop around so that a minus two can rotate to y
            translated += alphabet[num] # translated has the number location within alphabet added to it and becomes the new translated
            
        else: # if the character is not located in the alphabet 
            translated += character # then the character itself is added to the translated text
            
    print(str(attempt) + " / " + translated) # prints the string for the numbered attempt and adds the translated cipher for that attempt

# Part 4

alphabet = 'abcdefghijklmnopqrstuvwxyz '
key =      'mwgpbdzxrylacsokjfhtnueivq'
plaintext = 'of shoes and ships and sealing wax of cabbages and kings'

ciphertext = '' # cipher starts empty
   
for character in plaintext: # creates loop for each character in the string plaintext
      
    if character in alphabet: # checks to see if the character is in the alphabet string
       num = alphabet.find(character) # assigns a number to the location of the character in the alphabet string
       ciphertext += key[num]  # adds the equivalant numbered character in the key string to the cipher          

    else:# if the character is not in the alphabet
        ciphertext += character # adds that character to the cipher
  
print(ciphertext) # prints the cipher where the outcome of each loop has been added.   

# Part 5

alphabet = 'abcdefghijklmnopqrstuvwxyz '
key = 'mwgpbdzxrylacsokjfhtnueivq'
ciphertext = 'hzqftcqumfqfzxcxcdqscqhzqfmqfzxcxcdquxhzqmllqzxfqaxdzh'

plaintext = '' # cipher starts empty
   
for character in ciphertext: # creates loop for each character in the string plaintext
      
    if character in key: # checks to see if the character is in the alphabet string
       num = key.find(character) # assigns a number to the location of the character in the alphabet string
       plaintext += alphabet[num]  # adds the equivalant numbered character in the key string to the cipher          

    else: # if the character is not in the alphabet
        plaintext += character # adds that character to the cipher
      
print(plaintext) # prints the plaintext where the outcome of each loop has been added.

# Part 6

alphabet =  'abcdefghijklmnopqrstuvwxyz '
key = str(input("Enter 27 character key to use for encryption: "))
ciphertext = input("Enter text to be decrypted: ")

plaintext = '' # cipher starts empty
   
for character in ciphertext: # creates loop for each character in the string plaintext
      
    if character in key: # checks to see if the character is in the alphabet string
       num = key.find(character) # assigns a number to the location of the character in the alphabet string
       plaintext += alphabet[num] # adds the equivalant numbered character in the key string to the cipher          

    else: # if the character is not in the alphabet
        plaintext += character # adds that character to the cipher

print(plaintext) # prints the plaintext where the outcome of each loop has been added.

# Part 7

password = input('enter a password: ')

nkey = ''.join(sorted(set(password), key=password.index))
print(nkey)

alphabet =  'abcdefghijklmnopqrstuvwxyz'

# print(max(nkey))
# one, two = alphabet.split(max(nkey),1)

one, two = alphabet.split(nkey[-1], 1)

# print('first section ', one)
# print('second section ', two)

for char in nkey:
    one = one.replace(char,"")

for char in nkey:
    two = two.replace(char,"")

# print('new first ', one)
# print('new first ', two)

fkey = nkey + two + one
print(fkey)

key = fkey

# def encrypt(self):
# plaintext = input('Enter phrase to be encrypted: ')
# ciphertext = '' 
# cipher starts empty
# 
# for character in plaintext: 
# creates loop for each character in the string plaintext
#      
#    if character in alphabet: #checks to see if the character is in the alphabet string
#       num = alphabet.find(character) #assigns a number to the location of the character in the alphabet string
#       ciphertext += key[num]  #adds the equivalant numbered character in the key string to the cipher          
# 
#    else:#if the character is not in the alphabet
#        ciphertext += character #adds that character to the cipher
# 
# print(ciphertext)#prints the cipher where the outcome of each loop has been added.   
# 
# def decrypt(self):

ciphertext = input('Enter phrase to be decrypted: ')
plaintext = '' # cipher starts empty 
   
for character in ciphertext: # creates loop for each character in the string plaintext
     
    if character in key: # checks to see if the character is in the alphabet string
       num = key.find(character) # assigns a number to the location of the character in the alphabet string
       plaintext += alphabet[num]  # adds the equivalant numbered character in the key string to the cipher          

    else: # if the character is not in the alphabet
        plaintext += character # adds that character to the cipher
            
print(plaintext) # prints the plaintext where the outcome of each loop has been added.    




