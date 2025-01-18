'''
Modify the previous program so that the user also types 
the beginning and end of the multiplication table, instead of
starting with 1 and 10.
'''

number = (int(input('Multiplication table of: ')))
starting_point = (int(input('Enter the starting point of the multiplication table: ')))
ending_point = (int(input('Enter the ending point of the multiplication table: ')))

while starting_point <= ending_point:
    print(f'{number} x {starting_point} = {number * starting_point}')
    starting_point = starting_point + 1