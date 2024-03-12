# Create a "traditional" password using lowercase characters, UPPERCASE characters, and numbers.
# Follow the XKCD model of selecting four random words and concatenating them together to form your password.
# Of course, the above password does not make the IT department of most colleges and businesses happy.
# They still want you to have at least one capital letter and a number in your password.
# We’ll learn more about this in a couple of chapters but it is easy to replace parts of a string with a different string using the replace method.
# For example "pool".replace('o', 'e') gives us peel Once you have your final password you can replace some letters with number substitutions.
# For example its common to replace the letter l with the number 1 or the letter e with the number 3 or the o with a 0. You can get creative.
# For example, you can also easily capitalize a word using "myword".capitalize().


import random

# Lists to be used for password generation

nouns = ['tissue', 'processor', 'headquarters', 'favorite', 'cure', 'ideology', 'funeral', 'engine', 'isolation', 'perception', 'hat', 'mountain', 'session', 'case', 'legislature', 'consent', 'spread', 'shot', 'direction', 'data', 'tragedy', 'illness', 'serving', 'mess', 'resistance', 'basis', 'kitchen', 'mine', 'temple', 'mass', 'dot', 'final', 'chair', 'picture', 'wish', 'transfer', 'profession', 'suggestion', 'purse', 'rabbit', 'disaster', 'evil', 'shorts', 'tip', 'patrol', 'fragment', 'assignment', 'view', 'bottle', 'acquisition', 'origin', 'lesson', 'Bible', 'act', 'constitution', 'standard', 'status', 'burden', 'language', 'voice', 'border', 'statement', 'personnel', 'shape', 'computer', 'quality', 'colony', 'traveler', 'merit', 'puzzle', 'poll', 'wind', 'shelter', 'limit', 'talent']

verbs = ['represent', 'warm', 'whisper', 'consider', 'rub', 'march', 'claim', 'fill', 'present', 'complain', 'offer', 'provoke', 'yield', 'shock', 'purchase', 'seek', 'operate', 'persist', 'inspire', 'conclude', 'transform', 'add', 'boast', 'gather', 'manage', 'escape', 'handle', 'transfer', 'tune', 'born', 'decrease', 'impose', 'adopt', 'suppose', 'sell', 'disappear', 'join', 'rock', 'appreciate', 'express', 'finish', 'modify', 'keep', 'invest', 'weaken', 'speed', 'discuss', 'facilitate', 'question', 'date', 'coordinate', 'repeat', 'relate', 'advise', 'arrest', 'appeal', 'clean', 'disagree', 'guard', 'gaze', 'spend', 'owe', 'wait', 'unfold', 'back', 'waste', 'delay', 'store', 'balance', 'compete', 'bake', 'employ', 'dip', 'frown', 'insert']

adjs = ['busy', 'closer', 'national', 'pale', 'encouraging', 'historical', 'extreme', 'cruel', 'expensive', 'comfortable', 'steady', 'necessary', 'isolated', 'deep', 'bad', 'free', 'voluntary', 'informal', 'loud', 'key', 'extra', 'wise', 'improved', 'mad', 'willing', 'actual', 'OK', 'gray', 'little', 'religious', 'municipal', 'just', 'psychological', 'essential', 'perfect', 'intense', 'blue', 'following', 'Asian', 'shared', 'rare', 'developmental', 'uncomfortable', 'interesting', 'environmental', 'amazing', 'unhappy', 'horrible', 'philosophical', 'American']

# Generation of each word in password. 

one = random.choice(nouns + verbs + adjs) # The program randomly chooses one word from the selected lists. 
two = random.choice(nouns + verbs + adjs) # Each word is kept seperate for further manipulation below.
three = random.choice(nouns + verbs + adjs)
four = random.choice(nouns + verbs + adjs)

# Now that the four words for the password have been selected

Password = (one + two.capitalize() + three + four.capitalize()) 
# The now defined Password, capitalizes the second and fourth words
better = Password.replace('o', '0', 3).replace('e', '3', 2).replace('t', '7', 1) 
# A new better password is generated and replaces the first three o for zeros.
# It is done respectively for e to 3 and t to 7 so that each letter can still exist within the password.
print(better)

import string
import time
# import sys
# sys.setExecutionLimit(60000) # 60 seconds
# Explore the time module - there may be a function that can be used to limit the time the while loop will run.

my_password = "abcd" 
# Pre determined password for computer to guess

password_len = len(my_password) 
# Generates the length of the password for the program to guess in

guess_num = 0 
# start the number of guesses at 0

done = False 
# Done starts as a False value

start= time.time() 
# sets the start time to the current time as a float in seconds.

stoptime = 10 
# number of seconds after which the program should stop.

while not done: # As long as False the program will continue going
    
    if time.time() > start + stoptime : break # program will stop trying if the current time is greater than the stoptime added to the start time
    
    guess_num = guess_num + 1 #adds one to the total number of guesses until a done is True. This is the counter to let us know how many tries the computer took
    guessed_pw = "".join([random.choice(string.ascii_lowercase)for n in range(password_len)]) 
# defines guessed_pw as a blank joined with random lowercase ascii with a total length equal to that of the password. 
# Therefore a four letter password gerates guesses that are four in length.
    print(guessed_pw) #Prints the guessed passwords on screen, turn off for much quicker execution.
    
    if guessed_pw == my_password: # If the guessed password is the password then it will print how many tries it took, if not the same it continues the while loop
        print("found it after ", guess_num, " tries")
        done = True

