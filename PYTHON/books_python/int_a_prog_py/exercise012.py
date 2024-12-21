'''
Write an expression that will be used to decide whether or not a student hass passed.
To pass, all of the student's grades must be greater than or equal to 7.
Consider that the student only takes three subjects, and that the grade
for each one will be stored in the following variables:
subject1, subject2 and subject3
'''
subject1 = 7.5
subject2 = 9.4
subject3 = 6.8

final_average = subject1 >= 7 and subject2 >= 7 and subject3 >= 7
print(final_average)
