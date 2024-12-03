'''
Introdução:
- Quantidade de valores e variáveis devem ser IGUAIS.
'''

nomes = ['Amélia', 'Clara', 'Débora']
nome1, nome2, nome3 = nomes

name1, *_ = ['Bárbara', 'Rute', 'Emily']    # é possível atribuir valores que estão sobrando a uma variável precedida de *.

print(nome2)
print(name1, _)
