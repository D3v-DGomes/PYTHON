'''
Write a program that asks the speed of a user's car. 
If it exceeds 80km/h, display a message saying that the user
has been fined. In this case, display the amount of the fine,
charging $55.00 per km above 80km/h.
'''

car_speed = float(input('Enter the car speed in km/h: '))

if car_speed <= 80:
    print('Vehicle within the permitted speed.')
else:
    speeding_ticket = (car_speed - 80) * 55
    print(f'You have been fined for exceeding the speed limit.')
    print(f'The amount of your fine is ${speeding_ticket:.2f}')