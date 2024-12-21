'''
Write an expression to determine whether or not a person should
pay tax. Consider that people whose salary is greater than $1200 pay tax.
'''
salary = int(input('Enter the amount of your salary: $'))

if salary > 1200:
    print('Tax will be charged.')
else:
    print('Tax will not be charged.')
