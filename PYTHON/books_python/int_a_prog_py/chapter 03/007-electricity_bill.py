'''
Write a program that calculates the price to be paid for 
the supply of electricity. Ask for the amount of kWh consumed
and the type of installation: R for residences, C for businesses, 
I for indrustries. Calculate the price to be paid according to
the following table:

+---------------------------------------+
|   Priceby type and consumption range  |
+---------------------------------------+
| Type        | Range (kWh)   | Price   |
+=======================================+
| Residential | until 500     | $ 0.40  |
|             | above 500     | $ 0.50  |
+---------------------------------------+
| Commercial  | until 1000    | $ 0.50  |
|             | above 1000    | $ 0.60  |
+---------------------------------------+
| Industrial  | until 5000    | $ 0.55  |
|             | above 5000    | $ 0.65  |
+---------------------------------------+
'''

consumption = int(input('Consumption in kWh: '))
print()
type_of_installation = input('Intallation type: \n[R] - Residential \n[C] - Commercial \n[I] - Industrial \nPlease, enter the type: ').upper()

if type_of_installation == 'R':
    if consumption <= 500:
        price = 0.40
    else:
        price = 0.50
elif type_of_installation == 'C':
    if consumption <= 1000:
        price = 0.50
    else:
        price = 0.60
elif type_of_installation == 'I':
    if consumption <= 5000:
        price = 0.55
    else:
        price = 0.65
else: 
    price = 0
    print('Error! Unknown installation type.')

cost = consumption * price
print(f'Amount to pay: ${cost:.2f}')