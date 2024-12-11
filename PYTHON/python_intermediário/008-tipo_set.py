'''
# Sets - Conjuntos em Python (tipo set)
--> Conjuntos são representados graficamente pelo diagrama de Venn

# Sets são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.
--> parecem dicionários, mas não possuem chave, somente valor
--> um set vazio set(), na verdade, é um dicionário

# Sets são eficientes para remover valores duplicados de iteráveis.
--> seus valores serão sempre únicos
--> não aceitam valores mutáveis
--> eles não possuem índexes
--> não garantem ordem
--> são iteráveis (for, in, not in)

# Métodos úteis:
--> add, update, clear, discard
'''

set1 = set()        # vazio
set1 = {'David', 1, 2, 3}       # com dados

set2 = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5}       # valores duplicados
print(set2)     # duplicidade eliminada
print(1 in set2)
print(3 not in set2)