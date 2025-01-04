'''
A função map() em Python é bastante útil para aplicar uma função a todos os 
itens de um iterável (como uma lista ou tupla). Basicamente, ela mapeia a função fornecida 
a cada item do iterável e retorna um objeto map (que pode ser convertido em uma lista 
ou outro tipo de contêiner).

# map --> para mapear dados.
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

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem=1.1)

def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(
            produto['preco']
        )
    }

novos_produtos = list(map(
    muda_preco_de_produtos,
    produtos
))

print_iter(produtos)
print_iter(novos_produtos)

print(
    list(map(
        lambda x: x * 3,
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ))
)

