'''
Write a program that asks for the initial value of a debt
and the monthly interest. Also asks for the monthly amount 
that will be paid. Print the number of months for the debt
to be paid, the total amount paid and the total interest paid.
'''
debt = float(input('Initial debt value: $'))
interest_rate = float(input('Monthly interest (Ex.: 5 for 5%): '))
payment = float(input('Amount to be paid monthly: $'))
month = 1

if debt * (interest_rate / 100) > payment:
    print('Your debt cannot be paid off because the interest rate exceeds the monthly payment amount.')
else:
    balance = debt
    interest_paid = 0

    while balance > payment:
        fees = balance * interest_rate / 100
        balance = balance + fees - payment
        interest_paid = interest_paid + fees
        print(f'Debt balance in the month {month} is ${balance}')
        month = month + 1
    
    print(f'To pay a debt of ${debt:.2f} the {interest_rate:.2f}% interest.')
    print(f'You will need {month - 1} months, paying a total of ${interest_paid:.2f} in interest.')
    print(f'Last month, you would have a residual balance of ${balance:.2f} to pay.')


