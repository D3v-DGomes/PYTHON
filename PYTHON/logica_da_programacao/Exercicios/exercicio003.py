"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# Primeira alternativa
n1 = input('Digite um número inteiro: ')
try:
    n1 = float(n1)

    if n1 % 2 == 0:
        print(f'O número {n1} é PAR.')
    else: 
        print(f'O número {n1} é ÍMPAR.')
except ValueError:
    print('Digite um número.')



# Segunda alternativa
entrada = input('Digite um número inteiro: ')

if entrada.isdigit():
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro.')