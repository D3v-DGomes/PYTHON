'''
Combinations, permutations e product - Itertools
Combinação --> a ordem não importa: iterável + tamanho do grupo;
Permutação --> a ordem importa;
Protudo --> a ordem importa e repete valores únicos.
'''
from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')

pessoas = [
    'João', 'Ivi', 'Diego', 'Zete',
]

camisetas = [
    ['Branca', 'Verde'],
    ['P', 'M', 'G'],
    ['masculino', 'feminino', 'infantil'],
    ['Algodão', 'Poliéster'],
]

# combinations: a ordem não importa, mas não há repetição dos dados que já foram apresentados.
print_iter(combinations(pessoas, 2))
print()
# permutations: a ordem importa e há repetição dos dados.
print_iter(permutations(pessoas, 2))
print()
# products: a ordem importa e os dados são utilizados para compor combinações únicas.
print_iter(product(*camisetas))



