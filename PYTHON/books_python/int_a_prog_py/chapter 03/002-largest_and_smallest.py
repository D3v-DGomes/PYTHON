'''
Write a program that reads three numbers and prints
the largest and smallest numbers.
'''

number_1 = int(input('Enter the first integer: '))
number_2 = int(input('Enter the second integer: '))
number_3 = int(input('Enter the third integer: '))

if number_1 > number_2 and number_1 > number_3:
    print(f'Largest number: {number_1}')
elif number_2 > number_1 and number_2 > number_3:
    print(f'Largest number: {number_2}')
else:
    print(f'Largest number: {number_3}')

if number_1 < number_2 and number_1 < number_3:
    print(f'Smallest number: {number_1}')
elif number_2 < number_1 and number_2 < number_3:
    print(f'Smallest number: {number_2}')
else:
    print(f'Smallest number: {number_3}')