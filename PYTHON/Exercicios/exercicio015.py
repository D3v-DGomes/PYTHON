'''
Considerando duas listas de inteiros ou flutuantes (lista A e lista B)
Alguns dos valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
'''

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

# solução 01:
lista_c = []
for i in range(len(lista_b)):
    lista_c.append(lista_a[i] + lista_b[i])
print(lista_c)

# solução 02:
lista_soma = []
for i, _ in enumerate(lista_b):
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)

# solução 03:
uniao_de_listas = [x + y for x, y in zip(lista_a, lista_b)]
print(uniao_de_listas)

# solução 04 (se a união for feita pela lista maior):
from itertools import zip_longest

nova_uniao = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(nova_uniao)

