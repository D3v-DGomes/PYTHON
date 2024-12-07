'''
round() 
--> é utilizada para arredondar números para um número especificado de dígitos após a vírgula decimal. 
--> ao utilizá-la o valor retorna como float em vez de string como ocorre usando f'{string}'.
'''

n1 = 0.2
n2 = 0.33
n3 = n1 + n2

print(type(f'{n1:.2f}'))
print(type(n2))
print(type(round(n3, 2)))

print(f'{n1:.2f}')
print(n2)
print(round(n3, 2))