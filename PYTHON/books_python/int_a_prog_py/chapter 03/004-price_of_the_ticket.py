'''
Write a program that asks how far a passenger wants
to travel in kilometers. Calculate the price of the ticket,
charching $0.50 per kilometer for trips up to 200km, and
$0.45 for linger trips.
'''

distance = float(input('How many kilometers is your trip? '))

if distance <= 200:
    price_of_the_ticket = distance * 0.50
    print(f'The value of your ticket is ${price_of_the_ticket:.2f}')

else:
    price_of_the_ticket = distance * 0.45
    print(f'The value of your ticket is ${price_of_the_ticket:.2f}')