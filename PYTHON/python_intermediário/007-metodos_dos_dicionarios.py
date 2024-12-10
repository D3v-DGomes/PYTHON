'''
Métodos úteis dos dicionários em Python:

# len --> Quantas chaves
# key --> iterável com as chaves
# values --> iterável com os valores
# items --> iterável com chaves e valores
# setdefault --> adiciona valor se a chave não existe
# copy --> retorna uma cópia rasa (shallow copy)
# get --> obtém uma chave
# pop --> apaga um item com a chave espeficiada (del)
# popitem --> apaga o último item adicionado
# update --> atualiza um dicionário com outro
'''

pessoa = {
    'nome': 'David',
    'sobrenome': 'Gomes',
    'sobrenome2': 'Silva',
}

pessoa.setdefault('Idade', '90')    # adicionando uma chave e um valor que não existiam
print(len(pessoa))      # Quantidade de chaves
print(pessoa.keys())    # Conteúdo das chaves
print(pessoa.values())  # Valores das chaves
print(pessoa.items())   # Informa a chave e o seu valor

d1 = {
    'chave 1': 1,
    'chave 2': 2,
    'lista 1': [0, 1, 2],
}
d2 = d1.copy()      # cópia raza utilizada para copiar uma variável sem que as alterações desta apontem para a memória daquela. Mas não se aplica a subníveis (listas, tuplas, etc.)

d2['chave 1'] = 1000
d2['lista 1'][1] = 3356     # altera os valores das duas variáveis porque não fez a cópia do subnível e as alterações são direcionadas para a primeira variável
print(d1)
print(d2)



pessoa2 = {
    'nome': 'Kevin',
    'sobrenome': 'Gomes',
}
print(pessoa2['nome'])
print(pessoa2.get('idade', 'Não existe'))       # tenta obter a chave especificada e caso ela não exista, informa uma mensagem alternativa

nome = pessoa2.pop('sobrenome')     # elimina a chave especificada do dicionário
print(nome)
print(pessoa2)

ultima_chave = pessoa2.popitem()
print(ultima_chave)     # apagando o último item que foi adicionado ao dicionário
print(pessoa2)

pessoa2.update({        # atualiza chaves e valores existentes, e também cria novos
    'sobrenome': 'Silva',
    'idade': '24 anos',
    'altura': '1,73m'
})

print(pessoa2)