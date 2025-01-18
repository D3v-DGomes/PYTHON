'''
Modify the above program to display the results in the same
formate as a multiplication table: 2x1 = 2; 2x2 = 4...
'''

n = int(input('Multiplication table of: '))
x = 1

while x <= 10:
    y = n + x
    print(f'{n} + {x} = {y}')
    x = x + 1

    