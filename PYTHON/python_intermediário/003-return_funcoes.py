'''
Retorno de valores de funções (return)
--> é utilizada dentro de uma função para indicar o valor que a função deve retornar quando é chamada.
--> devolve um valor da função para o código que chamou a função. 
Este valor pode ser de qualquer tipo: números, strings, listas, dicionários, objetos, etc.
--> Quando uma função atinge uma declaração return, a execução da função é imediatamente interrompida,
e qualquer código após return dentro da função não será executado.
--> Se uma função não possui uma declaração return, ou se return é chamada sem um valor, 
a função retornará implicitamente None. Dessa forma, não será possível atribuir o valor
para uma variável com o intuito de realizar outras operações com ela.
'''

def soma(x , y):
    print(x + y)        # Sem utilizar o return a variável que o armazenará continuará sendo None

soma1 = soma(1, 1)
soma2 = soma(2, 2)
print(soma1, soma1 is None)


def subtracao(a, b):
    return a - b        # Permite que o valor da variável seja diferente de None
    print(a * b)        # Comando inalcançável pois a função foi interrompida na linha acima

subtracao1 = subtracao(8, 3)
print(subtracao1, subtracao1 is None)
