'''
Escopo de funções em Python:

--> Escopo é o local onde determinado código pode atingir. Existem dois tipos de escopo:

Escopo global
--> É onde todo código é alcançável

Escopo local
--> É onde apenas nomes do mesmo local podem ser alcançados.

--> Não é possível ter acesso a nomes de escopos internos nos escopos externos.
--> A palavra global faz uma variável do escopo externo 
ser a mesma no escopo interno.
--> Ao executar uma variável que se encontra tanto no escopo externo quanto no interno,
a função sempre priorizará a que está mais próxima de onde o código está sendo executado.
'''

x = 2       # Pode ser alcançado por todo código

def escopo():
    global x        # Ao utilizar esse comando, pode-se alterar a variável global e afetar o escopo global
    x = 20
    z = 4       # Escopo local, só pode ser alcançado por códigos dentro dessa função

    def outro_escopo():
        x = 15      # Variável mais próxima. Caso não exista, a mais próxima será a do escopo() - DE DENTRO PARA FORA
        y = 3       # Só pode ser alcançado nesse local. Nenhuma função externa consegue alcançar
        print(x,y)
        print(x, y, z)
        
    outro_escopo()

    print(x, z)

print(x)
escopo()
