'''
Modify the previous program to print from 1 to the number
entered by the user, but this time only odd numbers.
'''

end = int(input('Enter the last number to print: '))
x = 0

while x <= end:
    if x % 2 != 0:
        print(x)
    x = x + 1