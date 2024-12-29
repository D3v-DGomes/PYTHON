'''
dir() --> é uma função embutida que é utilizada para descobrir 
quais são os atributos e métodos de um objeto.
É bastante útil para inspecionar e explorar objetos durante
o desenvolvimento e depuração de código.

-----------------------------------------------------------------------------------

hasattr() --> utilizado para verificar se um objeto possui um atributo específico.
Útil quando você precisa checar a existência de um atributo antes de acessá-lo, 
evitando assim erros potenciais.

Exemplo:
hasattr(objeto, nome_atributo)
objeto: O objeto que você deseja verificar.

nome_atributo: O nome do atributo que você está verificando
deve ser passado como uma string.

True: Se o objeto possui o atributo especificado.
False: Se o objeto não possui o atributo especificado.

-----------------------------------------------------------------------------------

getattr() --> utilizado para acessar o valor de um atributo de um objeto
de forma dinâmica.
pode ser especialmente útil quando você não sabe de antemão quais atributos 
estarão presentes em um objeto e deseja acessar ou manipular seus 
atributos de forma programática.

Exemplo:
getattr(objeto, nome_atributo, valor_padrão=None)
objeto: O objeto do qual você deseja obter o atributo.

nome_atributo: O nome do atributo que você deseja acessar, passado como uma string.

valor_padrão (opcional): Um valor padrão a ser retornado caso o atributo
não exista no objeto. Se não for fornecido e o atributo não existir, 
será gerada uma exceção AttributeError.
'''

# hasattr():
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome}."

# Criar uma instância da classe Pessoa
pessoa = Pessoa("Alice", 30)

# Verificar a existência de atributos
tem_nome = hasattr(pessoa, 'nome')
tem_idade = hasattr(pessoa, 'idade')
tem_sobrenome = hasattr(pessoa, 'sobrenome')
tem_cumprimentar = hasattr(pessoa, 'cumprimentar')

print(f"Tem nome: {tem_nome}")           # Saída: Tem nome: True
print(f"Tem idade: {tem_idade}")         # Saída: Tem idade: True
print(f"Tem sobrenome: {tem_sobrenome}") # Saída: Tem sobrenome: False
print(f"Tem cumprimentar: {tem_cumprimentar}") # Saída: Tem cumprimentar: True


# getattr():
class Pessoa2:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome}."

# Criar uma instância da classe Pessoa
pessoa = Pessoa2("Alice", 30)

# Usar getattr para acessar atributos
nome = getattr(pessoa, 'nome')
idade = getattr(pessoa, 'idade')

print(nome)  # Saída: Alice
print(idade)  # Saída: 30

