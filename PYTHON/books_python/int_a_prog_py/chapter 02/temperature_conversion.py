'''
Write program that a temperature entered in ºC to ºF.
The formula for this conversion is:
F = (9*C / 5) + 32
'''
celsius = float(input('Enter the temperature in (ºC): '))
fahrenheit = (9 * celsius / 5) + 32

print(f'Temperature in Degrees Celsius: ({celsius:.2f}ºC)')
print(f'Temperature in Fahrenheit: ({fahrenheit:.2f}ºF)')