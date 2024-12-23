'''
Write a program to calculate the reduction in a smoker's lifespan.
Ask how many cigarettes he smokes per day and how many years he has smoked.
Consider that a smoker loses 10 minutes of life with each cigarette, and
calculate how many days of life a smoker will lose. Display the total in days.
'''
cigarettes_per_day = int(input('How many cigarettes do you smoke a day? '))
months_of_use = int(input('How many months have you been smoking cigarettes? '))

wasted_time = cigarettes_per_day * 10
lost_months = wasted_time * (months_of_use * 30)
lost_days = (lost_months / 60) / 24

print(f'So far, you have lost {lost_days:.0f} days of life.')