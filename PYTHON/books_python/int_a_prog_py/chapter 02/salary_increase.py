'''
Write a program that calculates a salary increase.
The program should ask for the salary amount and the
percentage of the increase. Display the amount of the
increase and the new salary.
'''
current_salary = float(input('Inform the value of your salary: $'))
percentage_increase = float(input('Inform the value of the percentage increase: '))

increase_value = (current_salary * (percentage_increase / 100))
new_salary = current_salary + increase_value

print(f'Increase value: ${increase_value:.2f}')
print(f'Value the new salary: ${new_salary:.2f}')