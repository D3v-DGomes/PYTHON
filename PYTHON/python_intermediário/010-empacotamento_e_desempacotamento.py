# Empacotamento e desempacotamento de dicionários 
a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    'nome': 'Killua',
    'sobrenome': 'Zoldyck',
}
c, d = pessoa       # retorna as chaves
print(c, d)

e, f = pessoa.values()      # retorna os valores
print(e, f)

g, h = pessoa.items()       # retorna as chaves e os valores
print(g, h)

dados_pessoa = {
    'idade': 19,
    'altura': 1.74,
    'religião': 'não informado',
}

pessoa_completa = {**pessoa, **dados_pessoa}        # os ** serve para extrair o dicionário
print(pessoa_completa)
# args e kwargs
# args
# kwargs = keyword arguments (argumentos nomeados)
def mostrar_args_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostrar_args_nomeados(12.500, nome='Gon', sobrenome='Freecss')
print()
mostrar_args_nomeados(**pessoa_completa)