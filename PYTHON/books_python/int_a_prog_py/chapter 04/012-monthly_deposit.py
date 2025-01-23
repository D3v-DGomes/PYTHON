'''
Change the previous program so that it also asks for
the amount deposited monthly. This amount will be deposited
at the beginning of each month, and you must consider it for the
calculation of interest for the following month.
'''

deposit = float(input('Initial deposit: $'))
rate = float(input('Interest rate (Ex.: 3 for 3%): '))
investiment = float(input('Monthly deposit: $'))
month = 1
balance = deposit

while month <= 24:
    balance = balance + (balance * (rate / 100)) + investiment
    print(f'Balance of the month {month} is ${balance:.2f}.')
    month = month + 1

print(f'The gain obtained from interest was ${balance - deposit:.2f}.')