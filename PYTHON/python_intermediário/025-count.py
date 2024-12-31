'''
# necessário importar o itertools

count é um iterador infinito

    DIFERENÇAS ENTRE count() e range():

Objetivo:
count(): Conta a ocorrência de um valor específico.
range(): Gera uma sequência de números inteiros.

Uso:
count(): Usada com listas e strings.
range(): Usada para criar sequências numéricas para iteração.

Saída:
count(): Retorna um número inteiro representando a quantidade de vezes que o valor aparece.
range(): Retorna um objeto de tipo range que pode ser iterado.

Com range, é possível passar start, stop e step: range(0, 2, 50);
Com count, só é possível informar o start e o step, pois ele é um contator infinito.

O count é um iterator e um iterador ao mesmo tempo, já o range, é somente o último.
'''
from itertools import count

count1 = count(start=0, step=2)
range1 = range(0, 100, 2)

print('Informaçõe sobre o count:')
print('Count:', hasattr(count1, '__iter__'))
print('Count:', hasattr(count1, '__next__'))
print()
print('Informações sobre o range:')
print('Range:', hasattr(range1, '__iter__'))
print('Range:', hasattr(range1, '__next__'))

print()

print('Count:')
for i in count1:
    if i >= 100:
        break
    print(i)

print()

print('Range:')
for i in range1:
    if i > 100:
        break
    print(i)