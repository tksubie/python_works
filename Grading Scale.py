print('Hello user, I am here to help you compute your grade from a percentage to a letter grade.')
print('What grade did you get on your assignment?')
grade = input()                     # Grade as a string
new_grade = float(grade)              # Create grade into an integer

# If you got extra credit
if new_grade > 100:
    print('Looks like you are an over achiever, nice job, A+ in my books!')

# If the grade is an A
elif new_grade >= 93.00:
    print('Outstanding, that is an A.')
elif new_grade >= 90.00 < 92.99:
    print('Outstanding, that is an A-.')

# If the grade is a B
elif new_grade >= 87.00 < 89.99:
    print('High quality, that is a B+.')
elif new_grade >= 83.00 < 86.99:
    print('High quality, that is a B.')
elif new_grade >= 80.00 < 82.99:
    print('High quality, that is a B-.')

# If the grade is a C
elif new_grade >= 77.00 < 79.99:
    print('Acceptable, that is a C+.')
elif new_grade >= 73.00 < 76.99:
    print('Acceptable, that is a C.')
elif new_grade >= 70.00 < 72.99:
    print('Acceptable, that is a C-.')

# If the grade is a D
elif new_grade >= 67.00 < 69.99:
    print('Passing, that is a D+.')
elif new_grade >= 63.00 < 66.99:
    print('Passing, that is a D.')
elif new_grade >= 60.00 < 62.99:
    print('Passing, that is a D-.')

# If the grade is an F
elif new_grade <= 59.99:
    print('Looks like you have to reevaluate your studies, that is an F, not passing.')
