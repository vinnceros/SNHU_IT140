# zybooks CHALLENGE ACTIVITY 5.12.1 Change order of elements in function list argument
# 
# Write a function swap that swaps the first and last elements of a list argument.
# 
# Sample output with input: 'all,good,things,must,end,here'
# 
# ['here', 'good', 'things', 'must', 'end', 'all']
# 
# ================================================================== #
# 
# original zybooks code 
# 
# 
# ''' Your solution goes here '''
# 
# values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
# swap(values_list)
# 
# print(values_list)
# 
# 
# ================================================================== #
# 
# https://github.com/lau-sk/IT-140/blob/e21de7ff79cea231d69f9f20ec1d49d218303695/5.12.1:%20Change%20order%20of%20elements%20in%20function%20list%20argument
# 
# def swap(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
# 
# values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
# swap(values_list)
# 
# print(values_list)
# 
# ================================================================== #
# 
# https://github.com/asheikh3378/Chapter7_ZybooksChallangeQs/blob/ad440c7302ce7cb47de3d415b9c7623abc32c3cb/7.12.1
# 
# def swap(list):
#   list[0],list[-1] = list[-1],list[0]
#   return list
# list = ['all','good','things','must','end','here']
# list = swap(list)
# 
# values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
# swap(values_list)
# 
# print(values_list)
# 
# ================================================================== #
# 
# https://github.com/davidseungjin/Python/blob/a31145aa35f22b218be022505628c299a0666866/ch612_1.py
# 
# <<<<<<< HEAD
# def modify(my_list):
# 	my_list[1] = 99
# 
# 
# my_list = [10, 20, 30]
# modify(my_list)
# print('my_list is', my_list) #my_list still contains 99!
# 
# def modify(my_list2):
# 	my_list2[1] = 99
# 
# my_list2 = [10, 20, 30]
# modify(my_list2[:]) # Pass a copy of the list
# 
# print('my_list2 is', my_list2)
# 
# 
# def modify(my_list3):
# 	my_list3[1] = 99
# 	return my_list3
# 
# my_list3 = [10, 20, 30]
# modify(my_list3[:]) # Pass a copy of the list
# 
# print('my_list3 is', my_list3)
# print('modify(my_list3) is', modify(my_list3[:]))
# =======
# 
# ''' Your solution goes here '''
# def swap(a):
#     lastindex=0
#     for i in a:
#         lastindex += 1
#         #print('lastindex is', lastindex)
#     temp = a[0]
#     a[0] = a[lastindex-1]
#     a[lastindex-1] = temp
#    
# values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
# swap(values_list)
# 
# print(values_list)
# >>>>>>> be8b1a86d6b6777a71a68f0aaa5c582c521a595d
# 
# 
# 
# ================================================================== #
# 
# https://github.com/Cooks-Johns/coWorkers/blob/d0fb075f5841529d0ba4ba9b769787ba7310b835/lab/numSwap.py
# 
# one = 2
# two = 93
#
#
# def swap_values(user_val1, user_val2):
#     user_val1 = one
#     user_val2 = two
#     tmp = [user_val2, user_val1]
#     return tmp
# 
# 
#
# def print_val():
#
#     print('Sum: {:f}'.format(tmp))
# swap_values()
# print()
#
# 
# ----------------->        this is how you edit the list
# def modify(my_list):
#     my_list[1] = 99 # list location my_list[1]
#
# my_list = [10, 20, 30]
# modify(my_list)
# print(my_list)
# 
# -------------
# def modify(my_list):
#     my_list[1] = 99  # Modifying only the copy
#
# my_list = [10, 20, 30]
# modify(my_list[:])  # Pass a copy of the list
#
# print(my_list)  # my_list does not contain 99!
# 
# -------------
# 
# def add_grade(student_grades):
#     print('Entering grade. \n')
#     name, grade = input(grade_prompt).split()
#     student_grades[name] = grade
#
#
# def delete_name():
#     name = input(delete_prompt)
#     del student_grades[name]
#     print('Deleting grade.\n')
#
# def print_grades():
#     print('Printing grades.\n')
#     for name, grade in student_grades.items():
#         print(name, 'has a', grade)
#
#
# student_grades = {}  # Create an empty dict
# grade_prompt = "Enter name and grade (Ex. 'Bob A+'):\n"
# delete_prompt = "Enter name to delete:\n"
# menu_prompt = ("1. Add/modify student grade\n"
#                 "2. Delete student grade\n"
#                 "3. Print student grades\n"
#                 "4. Quit\n\n")
#
# command = input(menu_prompt).lower().strip()
#
#
# while command != '4':  # Exit when user enters '4'
#     if command == '1':
#         add_grade(student_grades)
#
#     elif command == '2':
#         delete_name()
#
#     elif command == '3':
#         print_grades()
#
#     else:
#         print('Unrecognized command.\n')
#
#     command = input().lower().strip()
# --------------------------->
# 
# 
# def get_tmp(user_val1, user_val2, ):
#     a = user_val1
#     b = user_val2
#     tmp = [b, a]
#     # print('Sum: {}'.format(tmp, sep=','))
#     return tmp
# 
# def mak_str():
#     t = ' '.join(str(x) for x in td)
#     print(t)
# 
# a, b = 5 , -21
# 
# td = get_tmp(a, b)
# 
# mak_str()
# 
#------------------------->
# def split(s):
#
#     token = values_list.split(',')
#     s = token
#     print(s)
#
#
#
# # values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
# values_list = 'all,good,things,must,end,here'
#
# if __name__ == '__mai
#     split(values_list)
# 
# 
# 
# def swap_values(a,b):
#     x = a
#     y = b
#     print('{} {}'.format(x, y))
# 
# b = int(input())
# a = int(input())
# 
# swap_values(a,b)
# 
# 
# 
# ================================================================== #

# this code passes all zybooks tests 

def swap(lst):
    lst[0], lst[-1] = lst[-1], lst[0]

values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
swap(values_list)

print(values_list)

# ================================================================== #


