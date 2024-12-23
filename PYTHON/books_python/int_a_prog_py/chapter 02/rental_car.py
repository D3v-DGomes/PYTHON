'''
Write a program that asks the number of kilometers traveled
by a car rented by the user, as well as the number of days for which
the car was rented. Calculate the price to pay, knowing that the
car costs $60 per day and $0,45 per kilometer driven.
'''
kilometers_traveled = float(input('Enter how many kilometers were traveled: '))
days_of_use = int(input('Please, inform how many days the car was used: '))

daily = days_of_use * 60
kilometers_driven = kilometers_traveled * 0.45
total_cost = daily + kilometers_driven

print(f'The car was used for {days_of_use} days.')
print(f'The car traveled {kilometers_traveled:.2f}km.')
print(
    f'Daily price: ${daily:.2f} \n'
    f'Price per distance traveled: ${kilometers_driven} \n'
    f'Total cost: ${total_cost:.2f}' 
)