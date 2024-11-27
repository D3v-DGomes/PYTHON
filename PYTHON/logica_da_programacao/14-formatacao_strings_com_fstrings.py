'''
Formatação básica de strings
s --> string
d --> int
f --> float
.<nº de digitos> x ou X --> hexadecimal
(Caractere)(><^)(quantidade)
> --> esquerda
< --> direita
^ --> centro
Sinal - ou + 
Ex.: 0 >- 100, .1f
Conversion flags --> !r !s !a
'''
var1 = 'ABCD'
print(f'{var1}')
print(f'{var1:->10}')
print(f'{var1:-<10}')
print(f'{var1:-^10}')
print(f'{1000.545455669:,.1f}')