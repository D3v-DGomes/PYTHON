'''
função filter no python
A função filter() em Python é usada para criar uma sequência de elementos 
para os quais uma função retorna True. Em outras palavras, filter() aplica 
a função fornecida a cada item do iterável e retorna apenas aqueles 
para os quais a função retornou True.

--> filter é um filtro funcional.
'''

from functools import partial
from types import GeneratorType

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# a função filter precisa de dois parâmetros para ser executada.
# o primeiro é a função desejada e o segundo, a origem.
novos_produtos = filter(
    lambda produto: produto['preco'] > 10,
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)



