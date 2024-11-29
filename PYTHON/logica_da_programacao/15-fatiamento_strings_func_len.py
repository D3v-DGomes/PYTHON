'''
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::] --> i = indice; f = fatiamento --> p = passos
Obs.: a função len retorna a quantidade de caracteres da str.
'''

var = 'Olá mundo'
print(len(var)) # Realiza a contagem da quantidade de caracteres da string, incluindo espaços em branco.
print(var[4:8]) # O primeiro indice é para indicar o início e o segundo indice é para indicar que só vai ser lido até o anterior a ele.
print(var[:9]) # Sem indicar o primeiro indice, subentende-se que é para começar do início.
print(var [0:9:2]) # lendo as strings de duas em duas letras.
print(var[::-1]) # lendo as strings de trás para frente.

