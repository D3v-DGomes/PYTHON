'''
Métodos de classe + factories (fábricas)

São métodos onde "self" será "cls", ou seja, ao invés de recerber a instância
no primeiro parâmetro, receberemos a própria classe.

O decorador @classmethod é usado para definir métodos que pertencem à classe, 
e não às instâncias da classe. Esses métodos têm acesso ao próprio objeto da classe 
através de um parâmetro que, por convenção, é chamado de cls.

'''

class Dados:
    ano_atual = 2024    # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Olá, mundo!')

    # Pessoas com idades iguais:
    @classmethod
    def idades_iguais(cls, nome):
        return cls(nome, 45)
    
    # Nomes anônimos:
    @classmethod
    def nome_anonimo(cls, idade):
        return cls('Anônimo', idade)


p1 = Dados('Jonas', 27)
Dados.metodo_de_classe()

p2 = Dados.idades_iguais('Jacob')
print(p2.nome, p2.idade)

p3 = Dados.nome_anonimo(25)
print(p3.nome, p3.idade)



