# zybooks 7.8 LAB Word frequencies (lists).py
# 
# Write a program that first reads in the name of an input file and then reads the file using the csv.reader() method. 
# 
# The file contains a list of words separated by commas. 
# 
# Your program should output the words and their frequencies (the number of times each word appears in the file) without any duplicates.
# 
# Ex: If the input is:
# 
# input1.csv
# 
# and the contents of input1.csv are:
# 
# hello,cat,man,hey,dog,boy,Hello,man,cat,woman,dog,Cat,hey,boy
# 
# the output is:
# 
# hello 1
# cat 2
# man 2
# hey 2
# dog 2
# boy 2
# Hello 1
# woman 1
# Cat 1
# 
# Note: There is a newline at the end of the output, and input1.csv is available to download.
# 
# ================================================================== #
# 
# LAB ACTIVITY 7.8.1: LAB: Word frequencies (lists)
# 
# Downloadable file: input1.csv
# 
# contents of file: hello,cat,man,hey,dog,boy,Hello,man,cat,woman,dog,Cat,hey,boy
# 
# 
# original zybooks code 
# 
# import csv
# 
# Type your code here. 
# 
# ================================================================== #
# 
# failed zybooks tests 
# 
# import csv
# word_count = {}
# file_name = input()
# 
# with open(file_name, 'r') as csvfile:
#     file_contents = csv.reader(csvfile, delimiter=',')
# 
#     for line in file_contents :
#         # print(line)
#         for word in line:
#             if word in word_count:
#                 word_count[word] += 1
#             else:
#                 word_count[word] = 1
#     for word in word_count:
#         print(word, word_count[word])
# 
# ================================================================== #
# 
# failed 
# 
# import csv
# word_count = {}
# input1.csv = input()
# 
# with open(input1.csv, 'r') as csvfile:
#     file_contents = csv.reader(csvfile, delimiter=',')
# 
#     for line in file_contents :
#         # print(line)
#         for word in line:
#             if word in word_count:
#                 word_count[word] += 1
#             else:
#                 word_count[word] = 1
#     for word in word_count:
#         print(word, word_count[word])
# 
# ================================================================== #

# this code passes all zybooks tests 

# input name: input1.csv

import csv
filename = input()
with open(filename, 'r') as file:
    reader = csv.reader(file, delimiter = ',')
    result = dict()
    for i in reader:
        for j in i:
            if j in result:
                result[j] = result[j] + 1
            else:
                result[j] = 1
    for k in list(result.keys()):
        print("{} {}".format(k, result[k]))

# ================================================================== #
