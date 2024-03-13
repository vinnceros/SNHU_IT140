# zybooks 6.18 LAB Word frequencies.py
# 
# Write a program that reads a list of words. 
# Then, the program outputs those words and their frequencies.
# 
# Ex: If the input is:
# 
# hey hi Mark hi mark
# 
# the output is:
# 
# hey 1
# hi 2
# Mark 1
# hi 2
# mark 1
# 
# ================================================================== #
# 
# LAB ACTIVITY 6.18.1: LAB: Word frequencies
# 
# ''' Type your code here. '''
# 
# ================================================================== #

# this code passes all zybooks tests 

words = input().split()
for word in words:
    count = 0
    for w in words:
        if w == word:
            count += 1
    print(word, count)

# ================================================================== #

