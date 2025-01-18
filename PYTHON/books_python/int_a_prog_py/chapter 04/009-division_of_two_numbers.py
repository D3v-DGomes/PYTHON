'''
Write a program that reads two numbers. Prints the result of multiplying 
the first number by the second number, as well as the remainder of the division. 
Use only the addition and subtraction operators to calculate the result. 
Remember that we can learn the quotient of the division of two numbers 
as the number of times we can subtract the divisor from the dividend.
'''

dividend = int(input('Enter the dividend: '))
divisor = int(input('Enter the divisor: '))
quotient = 0
x = dividend

while x >= quotient:
    x = x - divisor
    quotient = quotient + 1 

rest = x

print(f'{dividend} / {divisor} = quotient: {quotient} rest: {rest} ')

