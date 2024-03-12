# 1. Calculates the overall grade for four equally weighted programming assignments, where each assignment is graded out of 50 points. 

# Hint: First calculate the percentage for each assignment (e.g., score / 50), then calculate the overall grade percentage (be sure to multiply the result by 100).


'''
assignment1_grade = float(input('Enter score on Programming assignment 1 (out of 50):\n'))
assignment2_grade = float(input('Enter score on Programming assignment 2 (out of 50):\n'))
assignment3_grade = float(input('Enter score on Programming assignment 3 (out of 50):\n'))
assignment4_grade = float(input('Enter score on Programming assignment 4 (out of 50):\n'))

assignment1_percentage = ((assignment1_grade) / 50)
assignment2_percentage = ((assignment2_grade) / 50)
assignment3_percentage = ((assignment3_grade) / 50)
assignment4_percentage = ((assignment4_grade) / 50)


overall_grade = ((assignment1_percentage + assignment2_percentage + assignment3_percentage + assignment4_percentage) * 100 / 4) 

print('Your overall grade is:', overall_grade)

'''


'''
2. Calculates the overall grade for four equally weighted programming assignments, 
where assignments 1 and 2 are graded out of 50 points and assignments 3 and 4 are graded out of 75 points.
'''

'''
assignment1_grade_p2 = float(input('Enter score on Programming assignment 1 (out of 50):\n'))
assignment2_grade_p2 = float(input('Enter score on Programming assignment 2 (out of 50):\n'))
assignment3_grade_p2 = float(input('Enter score on Programming assignment 3 (out of 75):\n'))
assignment4_grade_p2 = float(input('Enter score on Programming assignment 4 (out of 75):\n'))

assignment1_percentage_p2 = ((assignment1_grade_p2) / 50)
assignment2_percentage_p2 = ((assignment2_grade_p2) / 50)
assignment3_percentage_p2 = ((assignment3_grade_p2) / 75)
assignment4_percentage_p2 = ((assignment4_grade_p2) / 75)

overall_grade_p2_50 = ((assignment1_percentage_p2 + assignment2_percentage_p2) * 100 / 2) 
overall_grade_p2_75 = ((assignment3_percentage_p2 + assignment4_percentage_p2) * 100 / 2) 
overall_grade_average = (overall_grade_p2_50 + overall_grade_p2_75) / 2

print('Your overall grade is:', overall_grade_average)
print('Your 50 graded average:', overall_grade_p2_50)
print('Your 75 graded average:', overall_grade_p2_75)
'''


'''
Calculates the overall grade for a course with three equally weighted exams (graded out of 100) that account for 60% of the overall grade and four equally weighted 
programming assignments (graded out of 50) that account for 40% of the overall graded. 
Hint: The overall grade can be calculated as 0.6 * averageExamScore + 0.4 * averageProgScore.
Extend the program to support the grading scheme for one (or all) of the courses.
'''

#60 percent of toal grade
exam1_grade = float(input('Enter score on Exam 1 (out of 100):\n'))
exam2_grade = float(input('Enter score on Exam 2 (out of 100):\n'))
exam3_grade = float(input('Enter score on Exam 3 (out of 100):\n'))

#40 percent of total grade
assignment1_grade_p2 = float(input('Enter score on Programming assignment 1 (out of 50):\n'))
assignment2_grade_p2 = float(input('Enter score on Programming assignment 2 (out of 50):\n'))
assignment3_grade_p2 = float(input('Enter score on Programming assignment 3 (out of 50):\n'))
assignment4_grade_p2 = float(input('Enter score on Programming assignment 4 (out of 50):\n'))


exam1_percentage = ((exam2_grade) / 100)
exam2_percentage = ((exam2_grade) / 100)
exam3_percentage = ((exam2_grade) / 100)
exam_average = (exam1_percentage + exam2_percentage + exam3_percentage) / 3 * 100



assignment1_percentage_p3 = ((assignment1_grade_p2) / 50)
assignment2_percentage_p3 = ((assignment2_grade_p2) / 50)
assignment3_percentage_p3 = ((assignment3_grade_p2) / 50)
assignment4_percentage_p3 = ((assignment4_grade_p2) / 50)
assignment_average = (assignment1_percentage_p3 + assignment2_percentage_p3 + assignment3_percentage_p3 + assignment4_percentage_p3) / 4 * 100

overall_grade = (0.6 * exam_average) + (0.4 * assignment_average)

print('Your overall grade is:', overall_grade)
print('Exam average:', exam_average)
print('Assignment average:', assignment_average)