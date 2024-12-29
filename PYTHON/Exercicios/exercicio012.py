# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]


print('Produtos originais: \n', *produtos, sep='\n')
print()

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_por_nome_decrescente = sorted(
    copy.deepcopy(novos_produtos),
    reverse=True,
    key=lambda p: p['nome']
)

print('Produtos por nome decrescente: \n', *produtos_por_nome_decrescente, sep='\n')
print()

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_com_preco_crescente = sorted(
    copy.deepcopy(novos_produtos),
    key=lambda p: p['preco']
)

print('Produtos com preço crescente: \n', *produtos_com_preco_crescente, sep='\n')


