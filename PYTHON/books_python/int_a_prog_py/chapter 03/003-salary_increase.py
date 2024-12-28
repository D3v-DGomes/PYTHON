'''
Write a program that asks for the employee's salary and
calculates the increase amount. For salaries greater than
$1250.00, calculate an increase of 10%. For those lower
or equal, of 15%.
'''

salary = float(input('Inform the value of your current salary: $'))

if salary > 1250:
    new_salary = salary + (salary * 10/100)
    print(f'Current salary: ${salary:.2f} \n  New salary: ${new_salary:.2f} \n Percentage increase: 10%')

if salary <= 1250:
    new_salary = salary + (salary * 15/100)
    print(f'Current salary: ${salary:.2f} \n New salary: ${new_salary:.2f} \n Percentage increase: 15%')
