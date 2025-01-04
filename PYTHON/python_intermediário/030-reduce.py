'''
A função reduce() faz parte do módulo functools e é usada para aplicar
uma função cumulativa a todos os itens de um iterável (como uma lista), 
reduzindo-o a um único valor. Em outras palavras, ela combina os elementos 
de um iterável usando uma função fornecida.

--> reduce transforma um iterável em um valor.
'''
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# forma tradicional:
total = 0

for preco in produtos:
    total += preco['preco']

print(total)

# com reduce:

# alternativa 01:
def funcao_reduce(acumulador, produto):
    print('Acumulador:', acumulador)
    print('Produto:', produto)
    print()
    return acumulador + produto['preco']

novo_total = reduce(
    funcao_reduce,
    produtos,
    0
)

print(novo_total)
print()

# alternativa 02:

novo_total2 = reduce(
    lambda acumulador, produto: acumulador + produto['preco'], 
    produtos,
    0
)

print(f'Valor total de todos os produtos: R${novo_total2:.2f}')
