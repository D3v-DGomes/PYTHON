'''
Operação ternária
--> permite avaliar uma condição em uma única linha de código, 
retornando um valor se a condição for verdadeira e outro valor se a condição for falsa.
'''

# Exemplo 1:
condicao = 100 == 101
variavel = 'Valor' if condicao else 'Outro valor'

print(variavel)

# Exemplo 2:
digito = 9
novo_digito = digito if digito <= 9 else 0
print(novo_digito)