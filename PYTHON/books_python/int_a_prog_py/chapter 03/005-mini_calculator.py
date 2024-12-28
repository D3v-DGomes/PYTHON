'''
Write a program that reads two numbers and asks you what
operation you want to perform. You should be able to calculate
addition, subtraction, multiplication, and division. Print the
result of the requested operation.
'''

print('Choose one of the operations:')
operation = int(input(' [1] - Addition; \n [2] - Subtraction; \n [3] - Multiplication; \n [4] - Division; \n'))
print()
num_1 = float(input('Enter the first number: '))
num_2 = float(input('Enter the second number: '))

if operation == 1:
    print(f'{num_1} + {num_2} = {num_1 + num_2}')
    
elif operation == 2:
    print(f'{num_1} - {num_2} = {num_1 - num_2}')

elif operation == 3:
    print(f'{num_1} x {num_2} = {num_1 * num_2}')

elif operation == 4:
    print(f'{num_1} / {num_2} = {num_1 / num_2}')

else:
    print('Please, choose one of the available operations.')