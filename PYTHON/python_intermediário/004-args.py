'''
*args
--> São argumentos não nomeados que possuem a função de empacotamento e desempacotamento.
--> É uma maneira de permitir que uma função aceite um número variável de argumentos posicionais
--> É usado para passar uma lista de argumentos para uma função quando você 
não sabe de antemão quantos argumentos serão passados.
--> Originalmente *args é uma tupla, mas pode ser modificado para uma outra classe.
'''

def soma(*args):
    total = 0
    for numero in args:
        print(f'Total = {total} + {numero}')
        total = total + numero
        print(f'Total = {total}')
    print(total)

soma(1, 2, 3)


def soma2(*args):
    total = 0
    for numero in args:
        total += numero
    return total


soma_sequencial_2 = soma2(2, 4, 6, 8, 10)
print(f'A soma entre 2, 4, 6, 8 e 10 é igual a: {soma_sequencial_2}')

algarismos = 1, 2, 3, 4, 5, 6, 7, 8, 9, 0       # Isto é uma tupla
print(algarismos)       # Será exibido como tupla, ou seja, mostrando os (). Pois estão empacotados
print(*algarismos)      # Será exibido como strings. Porque estão desempacotados