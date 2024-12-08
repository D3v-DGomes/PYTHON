# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multi = multiplicar(1, 2, 3, 4, 5)
print(multi)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

# Método I:
def par_impar(numero):
    multiplo = numero % 2 == 0

    if multiplo:
        return f'{numero} é par.'
    return f'{numero} é ímpar.'

print(par_impar(3))

# Método II:
numero = float(input('Digite um número: '))

def parImpar():
    if numero % 2 == 0:
        return print(f'O número {numero:.2f} é par.')
    else:
        return print(f'O número {numero:.2f} é ímpar.')

parImpar()