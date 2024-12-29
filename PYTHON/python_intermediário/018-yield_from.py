'''
yield from --> permite delegar parte das operações de um generator para outro generator.
iterar manualmente sobre um subgerador e usar yield para produzir seus valores, 
pode-se usar yield from para delegar essa responsabilidade.

Explicação do exemplo:
- subgerador: Um subgerador que produz valores de 1 a 3;

- gerador_principal: Um gerador principal que utiliza yield from para delegar
a produção de valores ao subgerador e, em seguida, produz seus próprios valores (4 e 5).

'''

# Exemplo:
def subgerador():
    yield 1
    yield 2
    yield 3

def gerador_principal():
    yield from subgerador()
    yield 4
    yield 5

for valor in gerador_principal():
    print(valor)
