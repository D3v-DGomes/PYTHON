'''
Usar JSON (JavaScript Object Notation) em Python é bastante comum para manipulação de dados, 
especialmente para troca de dados entre um servidor e uma aplicação web. 
A biblioteca padrão json do Python facilita a leitura e a escrita de dados em formato JSON.


A função json.dump() é usada para escrever um objeto Python (como um dicionário) 
em um arquivo no formato JSON. É especialmente útil quando você precisa salvar dados em JSON 
para armazenamento ou transferência.


A função json.load() é usada para ler dados de um arquivo JSON e convertê-los em um objeto Python 
(como um dicionário). Esta função é útil para carregar dados JSON armazenados 
em arquivos para uso posterior em seu programa.

'''
import json

pessoa = {
    'nome': 'David',
    'sobrenome': 'Gomes Silva',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.74,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('aula117.json', 'w', encoding='utf-8') as arquivo:
    json.dump(pessoa, arquivo, indent=2)    # indent= serve para deixar o arquivo identado corretamente.


with open('aula117.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa))
    print(pessoa['altura'])