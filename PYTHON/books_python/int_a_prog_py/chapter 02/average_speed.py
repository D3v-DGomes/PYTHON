'''
Write a program that calculates the time of a car trip.
Ask for the distance to be travaled and the expected
average speed fot the trip.
'''
distance = float(input('Enter the distance traveled in kilometers: '))
average_speed = float(input('Enter the speed you want to travel in km/h: '))

travel_time = 60 * (distance / average_speed)

print(f'Your trip will last {travel_time:.2f} minutes.')