'''
Funções decoradoras --> permitem adicionar funcionalidades a funções existentes
sem alterar seu código.

Decorar = adicionar  / remover / restringir / alterar

Funções decoradoras são funções que decoram outras funções Decoradores 
são usados para fazer o Python usar as funções decoradoras em outras funções.
'''

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna

@criar_funcao
def inverte_string(string):     # função principal que vira a def interna()
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')
    

inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)

print(); print()

# Funções decoradoras com parâmetros:
def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('Decoradora 1')
        def aninhada(*args, **kwargs):
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes

@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y

decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x * y)
dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)

print(dez_mais_cinco)
print(dez_vezes_cinco)

print(); print()

# Ordem dos decoradores:
def parametros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)

        def sua_nova_funcao(*args, **kwargs):
            ress = func(*args, **kwargs)
            final = f'{ress} {nome}'
            return final
        return sua_nova_funcao
    return decorador

# A ordem dos decoradores funciona de baixo para cima:
@parametros_decorador(nome='Terceiro')
@parametros_decorador(nome='Secundo')
@parametros_decorador(nome='Primeiro')
def soma1(x, y):
    return x + y


dois_mais_sete = soma1(2, 7)
print(dois_mais_sete)