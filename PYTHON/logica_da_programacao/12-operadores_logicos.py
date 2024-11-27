# if / elif / else
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair': # O elif pode ser repetido quantas vezes for necessário.
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair. Tente novamente')

'''
OPERADORES DE COMPARAÇÃO (RELACIONAIS)

OP              SIGNIFICADO             EXEMPLO (TRUE)
>               maior                   2 > 1
>=              maior ou igual          2 >= 2
<               menor                   3 < 5
<=              menor ou igual          5 <= 5
==              igual                   'a' == 'a'
!=              diferente               'a' != 'b'

'''
# EXERCÍCIO

n1 = input('Digite um valor: ')
n2 = input('Digite outro valor: ')

if n1 > n2:
    print(f'O primeiro valor {n1} é maior que o segundo valor {n2}')
elif n1 == n2:
    print(f'Os valores são iguais.')
else:
    print(f'O segundo valor {n2} é maior que o primeiro {n1}')
    

# OPERADOR LÓGICO "and"
# and / or / not

# and --> Todas as condições devem ser verdadeiras. Se QUALQUER valor for considerado falso, a expressão INTEIRA será falsa.
# São considerados falsy: 0, 0.0, '' e False.
ent = input('[E]ntrar [S]air: ')
senha_dig = input('Senha: ')
senha_perm = '654321'

if ent == 'E' and senha_dig == senha_perm:
    print('Entrar')
else:
    print('Sair')

# or --> QUALQUER condição verdadeira avalia TODA a expressão como verdadeira.
# São considerados falsy: 0, 0.0, '' e False.
if (ent == 'E' or ent == 'e') and senha_dig == senha_perm:
    print('Entrar')
else:
    print('Sair')

# not --> Utilizado para inverter os valores booleanos.
# not True = False
# not False = True
print(not True)
print(not False)

# OPERADORES in e not in
# Strings são iteráveis
#  0  1  2  3  4 
#  D  a  v  i  d
# -5 -4 -3 -2 -1

name1 = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

print(name1[2])
print(name1[-4])
print('vid' in name1)
print('k' in name1)

if encontrar in name1:
    print(f'{encontrar} está em {name1}')
else:
    print(f'{encontrar} não encontrado em {name1}')

