'''
Write a program that asks for the initial deposit and interest rate
of a savings account. Display the values month by month for the
first twenty-four months. Write the total interest earned for the period.
'''

deposit = float(input('Initial deposit: $'))
rate = float(input('Interest rate (Ex.: 3 for 3%): '))
month = 1
balance = deposit

while month <= 24:
    balance = balance + (balance * (rate / 100))
    print(f'Balance of the month {month} is ${balance:.2f}.')
    month = month + 1

print(f'The gain obtained from interest was ${balance - deposit:.2f}.')