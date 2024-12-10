'''
Dicionários em Python (tipo dict)
--> Dicionários são estruturas de dados do tipo par de "chave" e "valor".

--> Chaves podem ser consideradas como o "índice" que vimos na lista
e podem ser de tipos imutáveis como: str, int, float, bool, tuple, etc.

--> O valor pode ser de qualquer tipo, incluindo outro
 dicionário.

--> Usamos as chaves - {} - ou a classe dict para criar dicionários.

--> Imutáveis: str, int, float, bool, tuple
--> Mutável: dict, list

'''

# Exemplo:

pessoa = {      # Método mais comum, utilizando {}
    'nome': 'Ichigo',
    'sobrenome': 'Kurosaki',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},      # Dicionário dentro da lista
        {'rua': 'outra rua', 'número': 321},    # Dicionário dentro da lista
    ]
}

pessoa1 = dict(nome='Rukia', sobrenome='Kuchiki')      # Método menos utilizado, utilizando ()

print(pessoa)       # chamando o dicionário completo
print(pessoa1)      # chamando o dicionário completo

print(pessoa['altura'])
print(pessoa1['sobrenome'])


pessoa['Cor favorita'] = 'Azul'     # Adicionando um novo índice

print(pessoa, pessoa['Cor favorita'])