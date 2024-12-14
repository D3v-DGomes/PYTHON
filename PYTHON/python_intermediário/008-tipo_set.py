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


set1.add('Matemática')      # Adiciona valor ao set. Só é permitido um valor por vez
print(set1)

set1.update('Exemplo')    # Adiciona valor ao set de forma desordenada
set1.update(('Exemplo_2',))      # Em formato de tupla não fica desordenado (a vírugla é importante)
print(set1)

set1.discard('Exemplo_2')     # Remove o valor mencionado
print(set1)

set1.clear()        # Limpa o set por completo
print(set1)


'''
Operadores úteis:
união | união (union) - Une
intersecção & (intersection) - Itens presentes em ambos 
diferença - Itens presentes apenas no set da esquerda
diferença simétrica ^ - Itens que não estão em ambos
'''

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(f'Conjunto A: {set1}')
print(f'Conjunto B: {set2}')

set3 =  set1 | set2     # união (sem repetição) entre o set1 e o set2
print(f'União entre A e B: {set3}')

set4 = set1 & set2      # intersecção entre o set1 e o set2
print(f'Intersecção de A e B: {set4}')

set5 = set1 - set2      # itens que estão presentes somente no set da esquerda
print(f'Diferença de A em B: {set5}')
set5_1 = set2 - set1
print(f'Diferença de B em A: {set5_1}')

set6 = set1 ^ set2      # itens que não estão presentes em ambos
print(f'Diferença simétrica (o que está somente em A e somente em B): {set6}')
