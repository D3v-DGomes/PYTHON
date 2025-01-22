'''
Métodos estáticos são métodos estão dentro da classe, mas não tem acesso ao self
nem ao cls. Em resumo, são funções que existem dentro da sua classe.

Basicamente, é uma função dentro de uma classe, pois nele não temos acesso
ao __init__, self e nem ao cls.
'''

class Classe:
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('Oi', args, kwargs)


def funcao(*args, **kwargs):
    print('Oi', args, kwargs)


c1 = Classe()
c1.funcao_que_esta_na_classe(1, 2, 3)
funcao(1, 2, 3)
Classe.funcao_que_esta_na_classe(nomeado=1)
funcao(nomeado=1)