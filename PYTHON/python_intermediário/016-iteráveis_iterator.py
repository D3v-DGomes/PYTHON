'''
Generator expression, iterables e iterators em python.

Todo generator é um iterator, mas um iterator não é um generetor.

Diferença entre lista e generator:

Uma lista armazena todos os seus elementos na memória de uma vez. 
Isso pode ser ineficiente se a lista contiver muitos elementos, pois consumirá muita memória.

Um generator não armazena todos os seus elementos na memória de uma vez. Em vez disso, 
gera os elementos sob demanda, o que é muito mais eficiente em termos de uso de memória.
O generator não possui índice pelo fato de gerar valores sob demanda.
'''
import sys

iterable = ['eu', 'have', '__iter__']
iterator = iter(iterable)   # tem __iter__ e __next__
lista = [x for x in range(1000)]        
generator = (n for n in range(1000))

print(sys.getsizeof(lista))     # retorna a quantidade de bites utilizados para armazenamento.
print(sys.getsizeof(generator))     # retorna a quantidade de bites utilizados para armazenamento.

print(lista)

for n in generator:
    print(n)


