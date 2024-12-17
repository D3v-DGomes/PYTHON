'''
List comprehension é uma forma rápida para criar listas
--> permite que você crie uma nova lista aplicando uma expressão a cada item de um iterável,
como uma lista ou um range, opcionalmente filtrando itens com uma condição.
'''
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=45)

# Método tradicional:
lista = []

for numero in range(10):
    lista.append(numero)
# print(lista)

# Com list comprehension:
lista_2 = [numero * 2 for numero in range(10)]      # multiplicando os números do range por 2

# print(lista_2)

# Mapeamento de dados & Filtro de dados em list comprehension:
# --> altera o valor, mas mantém a mesma quantidade de elementos
# --> o que está à esquerda do FOR é mapeamento, à direita é filtro (utilizando if sem else)
produtos = [
    {'nome': 'produto 1', 'preco': 20,},
    {'nome': 'produto 2', 'preco': 10,},
    {'nome': 'produto 3', 'preco': 50,},
]

novos_produtos = [
    {**produto, 'nome': produto['nome'], 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
# print(*novos_produtos, sep='\n')
# p(novos_produtos)


# lista = [n for n in range(10) if n < 5]        
novos_produtos = [
    {**produto, 'nome': produto['nome'], 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10    # filtro
]
p(novos_produtos)

# List comprehension com mais de um for:

# método tradicional:
# nova_lista = []
# for x in range(3):
#     for y in range(3):
#         nova_lista.append((x, y))

# print(nova_lista)

# com list comprehension:
new_list = [
    (x, y, z) 
    for x in range(2) 
    for y in range(2)
    for z in range(2)
    if x + y + z <= 3
]
print(new_list)



