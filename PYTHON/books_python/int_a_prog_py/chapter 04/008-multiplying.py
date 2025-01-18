'''
Write a program that reads two numbers. Print the result of multiplying 
the first by the second. Use only the addition and subtraction operators 
to calculate the result. Remember that we can understand the multiplication 
of two numbers as successive sums of one of them.
'''
multiplier = int(input('Enter the number you want to multiply: '))
multiplying = int(input('Enter the number of times you want to multiply it: '))
x = 1
r = 0

while x <= multiplying:
    r = r + multiplier
    x = x + 1

print(f'{multiplier} x {multiplying} = {r}')
