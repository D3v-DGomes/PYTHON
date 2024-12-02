'''
Listas em Python
Tipo List - Mutável
- Suporta vários valores de qualquer tipo. 
- Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
'''

# ÍNDICE COM STRING:
#        +01234  
#        -54321   
string = 'ABCDE'    # 5 caracteres

# ÍNDICE COM LIST:
#        0    1      2             3     4    
#       -5   -4     -3            -4    -5  
lista = [123, True, 'David Gomes', 1.33, []]
print(lista)
print(lista[2], type(lista[2]))

lista[-3] = 'João'  # alterando o valor de um dos itens da lista
print(lista[-3])


lista_1 = [10, 20, 30, 40]
numero = lista_1[2]
print(numero)

del lista_1[2]  # apagando o item da lista. Após excluir um item, o índice da lista também é atualizado.
print(lista_1)

lista_1.append(50)  # adicionando um item ao final da lista. Não pode adicionar mais que um por comando.
print(lista_1)

ultimo_item = lista_1.pop() # removendo o último item da lista.
print(lista_1, 'Removido:', ultimo_item)

lista_1.insert(1, 5)

lista_1.clear() # limpando a lista como um todo.
print(lista.clear())



