'''
Write a program to approve a bank loan to byu a house.
The program should ask for the value of the house to perchased,
the salary and the number of years to pay. The monthly payment
cannot be higher than 30% of the salary. Calculate the payment
amount as the value of the house to be purchased divided by the 
number of months to pay.
'''

house_value = float(input('How much does the house cost? \n $'))
salary = float(input('How much is your salary? \n $'))
years_of_payment = int(input('How many years do you want to pay in? \n'))

monthly_payment = years_of_payment * 12
installment_value = house_value / monthly_payment

if installment_value <= salary * (30 / 100):
    print('Your bank loan has been granted!')
    print(f'- House value: {house_value:.2f} \n- Number of installments: {monthly_payment} \n- Amount of installments:{installment_value:.2f}')
else:
    print('Unfortunately the loan was not granted.')
