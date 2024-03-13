# zybooks 4.14 LAB Count input length without spaces, periods, or commas

# Given a line of text as input, output the number of characters excluding spaces, periods, or commas.

# Ex: If the input is:

# Listen, Mr. Jones, calm down.

# the output is:

#  21

# Note: Account for all characters that aren't spaces, periods, or commas (Ex: "r", "2", "!").

# ================================================================== #

# LAB ACTIVITY 4.14.1 LAB: Count input length without spaces, periods, or commas

# ================================================================== #

# this code passes all zybooks tests 

user_text = input()

count = 0
for x in user_text:
    if not(x in " .,"):
        count += 1
print(count)

# ================================================================== #

