'''
UNIR LISTAS:
- Crie uma função zipper (como zipper de roupas)
- O trabalho dessa função será unir duas listas na ordem.
- Use todos os valores da menor lista.

Ex.:
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']

Resultado:
[('Salvador', 'BA'), ('Ubatuba, 'SP'), ('Belo Horizonte', 'MG')]
'''
'''
preciso fazer uma função que crie uma nova lista e acrescente nela os valores de duas listas distintas.

Primeiro, precisarei pegar o primeiro índice de cada lista e concatenar na nova lista.
Segundo, após pegar o índice referido, preciso apagar o primeiro índice das duas listas antigas.
Terceiro, preciso criar uma condição para que a nova lista seja menor ou igual a 3, 
pois assim o último valor 'RJ' não será concatenado.
'''
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

# solução 01:
def zipper(lista1, lista2):
    intervalo_minimo = min(len(lista1), len(lista2))
    return [
        (lista1[i], lista2[i]) for i in range(intervalo_minimo)
    ]

print(zipper(cidades, estados))

# solução 02:
print(list(zip(cidades, estados)))      # o zip utiliza a lista menor para concatenar

# solução 03:
from itertools import zip_longest

print(list(zip_longest(cidades, estados, fillvalue='SEM CIDADE')))  
# zip_longest usa a lista maior para concatenar
     
    




