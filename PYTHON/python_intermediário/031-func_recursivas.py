'''
Funções recursivas e recursividade:

São funções que podem se chamar de volta, muito úteis para dividir problemas
em partes menores.

Toda função recursiva deve ter:
--> Um problema que possa ser dividido em partes menores;
--> Um caso recursivo que resolve o pequeno problema;
--> Um caso base que para a recursão.

# Exemplo de um problema recursivo:
fatorial --> n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
'''

def func_recursiva(inicio=0, fim=20):
    # Caso base:
    if inicio >= fim:
        return fim
    
    print(inicio, fim)
    # Caso recursivo:
    # contar até chegar ao final
    inicio += 1
    return func_recursiva(inicio, fim)

print(func_recursiva())

print()
# Exercitando:
def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)

print(factorial(10))