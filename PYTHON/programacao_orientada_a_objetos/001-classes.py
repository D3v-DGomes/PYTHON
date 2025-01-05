'''
Classes são moldes para criar novos objetos (instâncias) que podem ter seus próprios
atributos e métodos.

Os objetos gerados pelas classes podem usar seus dados internos para realizar várias
ações. Por convenção, usamos PascalCase para nomes de classes.

__init__: É o método inicializador (ou construtor) que cria uma nova instância da classe. 
Ele é chamado quando a classe é instanciada.

--> A classe não possui os dados;
--> A instância da classe (objeto) possui os dados;
--> Uma classe pode gerar várias instâncias;
--> O parâmetro padrão self é a própria instância.
'''

# Molde:
class Pessoa:
    def __init__(self, nome, sobrenome):        # o primeiro parâmetro deve ser sempre self
        self.nome = nome    # self é a instância da classe
        self.sobrenome = sobrenome

p1 = Pessoa('David', 'Silva')       # p1 e p2 são instâncias 
p2 = Pessoa('Poliana', 'Silva')

print(p1.nome, p1.sobrenome)
print(p2.nome, p2.sobrenome)

print()
'''
Métodos em instâncias de classes Python:
São funções definidas dentro de uma classe que operam nos objetos dessa classe.

Os métodos de instância são uma maneira poderosa de encapsular a funcionalidade 
relacionada aos objetos de uma classe.

--> Hard coded é algo que foi escrito diretamente no código
'''

class Carro:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
    
    def descricao(self):
        print(f'Descrição do veículo: {self.marca}, {self.modelo}, {self.cor}')


etios = Carro('Toyota', 'Etios', 'Preto')
etios.descricao()

hb20 = Carro('Hyundai', 'HB20S', 'Cinza')
hb20.descricao()

city = Carro('Honda', 'Novo City', 'Azul marinho')
city.descricao()

print()
'''
Escopo da classe e de métodos da classe:

--> O self pode ser chamado em qualquer instância dentro da classe;
--> As regras de escopo de variáveis locais e globais permanecem as mesmas;
'''

class Animal:
    def __init__(self, animal):
        self.animal = animal        # o self pode ser chamado em qualquer método da classe

    def comendo(self, alimento):
        return f'{self.animal} está comendo {alimento}.'
    
    def executar(self, *args, **kwargs):        # forma de referenciar os dados de outro método
        return self.comendo(*args, **kwargs)

leao = Animal('LEÃO')
print(leao.animal)
print(leao.comendo('GARÇA'))
print(leao.executar('VEADO'))

print()
'''
Mantendo estados dentro da classe:
'''

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} Já está filmando...')
            return
        
        print(f'{self.nome} está filmando...')
        self.filmando = True

    def parar_de_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando...')
            return
        
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar enquanto filma.')
            return
        
        print(f'{self.nome} está fotografando...')
        

camera_cannon = Camera('Cannon')
camera_cannon.filmar()
camera_cannon.filmar()
camera_cannon.fotografar()
camera_cannon.parar_de_filmar()
camera_cannon.parar_de_filmar()
camera_cannon.fotografar()

print()

camera_sony = Camera('Sony')
camera_sony.filmar()
camera_sony.filmar()
camera_sony.fotografar()
camera_sony.parar_de_filmar()
camera_sony.parar_de_filmar()
camera_sony.fotografar()

print()
'''
Atributos de classe:
São variáveis que pertencem à própria classe e são compartilhados por todas as instâncias
dessa classe. Eles são úteis quando você deseja armazenar um valor comum a todas 
as instâncias de uma classe.

--> necessário ter cuidado, pois podem ser alterados fora do escopo da classe.
'''

class DadosPessoais:
    ano_atual = 2024    # atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return DadosPessoais.ano_atual - self.idade
    

cadastro_1 = DadosPessoais('Angelo', 46)
cadastro_2 = DadosPessoais('Mariana', 76)
cadastro_3 = DadosPessoais('Mainara', 27)

print(cadastro_1.get_ano_nascimento())
print(cadastro_2.get_ano_nascimento())
print(cadastro_3.get_ano_nascimento())

    
print()

        
    
