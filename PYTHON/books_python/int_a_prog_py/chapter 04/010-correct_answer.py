'''
Make a program that corrects three multiple choice questions.
The answer to the first question is 'b', the second is 'a' and the third is 'd'.
'''

points = 0
question = 1

while question <= 3:
    answer = input(f'Answer to the question {question}: ').lower()

    if question == 1 and answer == 'b':
        points = points + 1
    if question == 2 and answer == 'a':
        points = points + 1
    if question == 3 and answer == 'd':
        points = points + 1

    question = question + 1

print(f'The student scored {points} point(s).')
    