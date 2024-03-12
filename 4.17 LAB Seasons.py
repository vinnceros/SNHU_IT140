# Write a program that takes a date as input and outputs the date's season. 
# The input is a string to represent the month and an int to represent the day.
# 
# Ex: If the input is:
# 
# April
# 11
# the output is:
# 
# Spring
# 
# In addition, check if the string and int are valid (an actual month and day).
# 
# Ex: If the input is:
# 
# Blue
# 65
# the output is:
# 
# Invalid 
# The dates for each season are:
# Spring: March 20 - June 20
# Summer: June 21 - September 21
# Autumn: September 22 - December 20
# Winter: December 21 - March 19
# 
# Creating a list of months

list_of_months= ["January", "February", "March" , 
                "April" , "May" , "June" , "July" , "August" , 
                "September" , "October" , "November" , "December"
]
January = list_of_months[0]
February = list_of_months[1]
March = list_of_months[2]
April = list_of_months[3]
May = list_of_months[4]
June = list_of_months[5]
July = list_of_months[6]
August = list_of_months[7]
September = list_of_months[8]
October = list_of_months[9]
November = list_of_months[10]
December = list_of_months[11]

# Creating a list of months

list_of_days= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
                16,17,18,19,20,21,22,23,24,25,26,27,
                28,29,30,31
                ]


print('Please enter a month: ')
input_month = input()

print('Please enter a day: ')
input_day = int(input())

# Spring

if input_month == March and input_day in list_of_days[19:30]:
    print('Spring')
elif input_month == April and input_day in list_of_days[0:30]:
    print('Spring')
elif input_month == May and input_day in list_of_days[0:30]:
    print('Spring')
elif input_month == June and input_day in list_of_days[0:19]:
    print('Spring')

# Summer

elif input_month == June and input_day in list_of_days[20:30]:
    print('Summer')
elif input_month == July and input_day in list_of_days[0:30]:
    print('Summer')
elif input_month == August and input_day in list_of_days[0:30]:
    print('Summer')
elif input_month == September and input_day in list_of_days[0:20]:
    print('Summer')

# Autumn

elif input_month == September and input_day in list_of_days[21:30]:
    print('Autumn')
elif input_month == October and input_day in list_of_days[0:30]:
    print('Autumn')
elif input_month == November and input_day in list_of_days[0:30]:
    print('Autumn')
elif input_month == December and input_day in list_of_days[0:19]:
    print('Autumn')

# Winter

elif input_month == December and input_day in list_of_days[20:30]:
    print('Winter')
elif input_month == January and input_day in list_of_days[0:30]:
    print('Winter')
elif input_month == February and input_day in list_of_days[0:30]:
    print('Winter')
elif input_month == March and input_day in list_of_days[0:18]:
    print('Winter')        

else:
    print('Invalid')  