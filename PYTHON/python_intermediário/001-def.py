'''
Introdução às funções:
--> Funções são blocos de código que realizam uma tarefa específica e podem ser reutilizados em diferentes partes de um programa. 
Definir uma função ajuda a tornar o código mais organizado, modular e fácil de ler.
--> Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
--> Por padrão as funções no Python retornam None.

(def):
--> é a palavra-chave usada para definir uma função.
'''

def imprimir(a, b, c):      # As letras a, b e c são parâmetros.
    print(a, b, c)

imprimir(1, 2, 3)       # Os números 1, 2 e 3 são argumentos.
imprimir(7, 8, 9)

def saudacao(nome='usuário não identificado'):      # A string após o parâmetro é um valor padrão caso não seja um novo não seja definido
    print(f'Olá, {nome}!')

saudacao('Lázaro')
saudacao('Moisés')
saudacao()


'''
Argumentos nomeados e não nomeados em funções Python:
--> Argumento nomeado tem nome com sinal de igual=
--> Argumento não nomeado recebe apenas o argumento (valor)
'''

def soma(x, y, z):
    # Definição:
    print(f'{x=} {y=} {z=}', '|', 'x + y + z =', x + y + z)

soma(1, 2, 4)      # Argumento não nomeado
soma(y=1, x=2, z=6)      # Argumento nomeado


'''
Valores padrão para parâmetros:
--> Ao definir uma função, os parâmetros podem ter valores padrão.
--> Caso o valor não seja enviado para o parâmetro,
o valor padrão será usado.
'''

def multiplicacao(m, n, o=None):        # A letra "o" está com valor padrão atribuido por conta da possibilidade de não ter um valor atribuido.
    if o is not None:
        print(f'{m=} {n=} {o=}', '|', 'm * n * o =', m * n * o)
    else:
        print(f'{m=} {n=}', '|', 'm * n =', m * n)

multiplicacao(2, 3)
multiplicacao(4, 2, 3)