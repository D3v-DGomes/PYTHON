'''
Variável livre é uma variável utilizada dentro do escopo de uma função,
mas que foi definida no escopo global e não no local à função.

--> As variáveis livres não podem ser modificadas em um escopo 
diferente ao qual ela foi criada.

--> nonlocal: é usada para declarar que uma variável existente no escopo 
externo deve ser referenciada, em vez de criar uma nova variável local.
É útil quando você tem uma função aninhada e deseja modificar 
uma variável no escopo da função externa.
'''

# exemplo 1:
x = 10

def letra():
    return print(x)

letra()

# exemplo 2:
def soma():
    x = 5
    y = 8
    def resultado():
        return x + y
    return resultado

soma_xy = soma()

print(soma_xy())

# comandos úteis:
def fora(x):
    a = x 
    def dentro():
        print(locals())     # para saber quais são as variáveis locais
        print(dentro.__code__.co_freevars)      # saber variáveis livres
        return a
    return dentro

variables = fora(5)
print(variables())

print(globals())        # saber todas as variáveis globais

# uso de nonlocal:
def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna

nova_str = concatenar('a')
print(nova_str('b'))
print(nova_str('c'))
print(nova_str('d'))