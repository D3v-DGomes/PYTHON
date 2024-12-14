'''
lambda é uma função anônima que contém apenas uma linha.
Ou seja, tudo deve ser contido dentro de uma única expressão.
'''

lista = [1, 2, 44, 65, 321, 331, 5, 6, 67, 8, 0, 10]
lista.sort()        # utilizado para ordenar a lista referida
print(lista)

lista.sort(reverse=True)    # utilizado para ordenar a lista referida de trás para frente
print(lista)

lista_2 = [22, 5, 6, 77, 1, 0, 3, 8, 99, 192, 191]

print(sorted(lista_2))      # ordena a lista referida com uma cópia raza

# lambda:
dicionario = [
    {'nome': 'Raul', 'sobrenome': 'Seixas'},
    {'nome': 'Renato', 'sobrenome': 'Russo'},
    {'nome': 'Cássia', 'sobrenome': 'Eller'},
    {'nome': 'Nando', 'sobrenome': 'Reis'},
    {'nome': 'Charlie', 'sobrenome': 'Brown Jr.'}
]
def exibir(lista):
    for item in lista:
        print(item)
    print()

lam1 = sorted(dicionario, key=lambda item: item['nome'])
lam2 = sorted(dicionario, key=lambda item: item['sobrenome'])

exibir(lam1)
exibir(lam2)

def executa(funcao, *args):
    return funcao(*args)

# Exemplo 1:
def soma(x, y):
    return x + y

# transformando def em lambda:
soma = lambda x, y: x + y
print(soma(2, 5))

# ou
print(
    executa(
        lambda x, y: x + y, 2, 3
    )
)


# Exemplo 2:
def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

# transformando def em lambda:
duplica = executa(
    lambda multiplicador: lambda numero: numero * multiplicador, 5
)

print(duplica(2))       # multiplicando 5 * 2


# Exemplo 3:
print(
    executa(
        lambda *args: sum(args),
        2, 4, 6, 8, 10
    )
)