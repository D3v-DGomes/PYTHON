'''
Write a program that reads the number of days, hours, minutes,
and seconds from the user. Calculate the total in seconds.
'''
days = int(input('Enter the number of days: '))
hours = int(input('Enter the number of hours: '))
minutes = int(input('Enter the number of minutes: '))
seconds = int(input('Enter the number of seconds: '))

total_seconds = seconds + (60 * (minutes +(60 * (hours + (days * 24)))))

