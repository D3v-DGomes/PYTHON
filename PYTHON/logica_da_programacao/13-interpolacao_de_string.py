'''
Interpolação básica de strings
s --> string
d e i --> int
f --> float
x ou X --> hexadecimal
'''

nome = 'Kevin'
preco = 1000.5658
var = '%s, o valor do curso de Python é R$%.2f' % (nome, preco)
print(var)
print('O hexadecimal de %d é %03X' % (1500, 1500))