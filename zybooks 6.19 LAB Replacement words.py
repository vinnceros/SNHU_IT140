# zybooks 6.19 LAB Replacement words.py 
# 
# Write a program that replaces words in a sentence. 
# The input begins with word replacement pairs (original and replacement).
# The next line of input is the sentence where any word on the original list is replaced.
# 
# Ex: If the input is:
# 
# automobile car   manufacturer maker   children kids
# The automobile manufacturer recommends car seats for children if the automobile doesn't already have one.
# 
# the output is:
# 
# The car maker recommends car seats for kids if the car doesn't already have one. 
# 
# You can assume the original words are unique.
# 
# ================================================================== #
# 
# LAB ACTIVITY 6.19.1: LAB: Replacement words
# 
# ''' Type your code here. '''
# 
# ================================================================== #

# this code passes all zybooks tests -- however, the input needs to be 
# automobile car   
# manufacturer maker   
# children kids 
# each of the above three entries on their own line in the program 

replacementDict = {}
s = input().split()
i = 0
while i<len(s):
    replacementDict[s[i]] = s[i+1]
    i += 2
sentence = input().split()
result = ""
for i in range(len(sentence)):
    if sentence[i] in replacementDict:
        result += replacementDict[sentence[i]]
    else:
        result += sentence[i]
    result += " "
result = result[:-1]
print(result)

# ================================================================== #
