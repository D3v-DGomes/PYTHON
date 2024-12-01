# A função FOR em Python é usada para iterar sobre uma sequência ou qualquer outro objeto iterável.
# Ela permite executar um bloco de código várias vezes, uma para cada item da sequência.
# Geralmente é utilizado para sequências que já sabemos o início e o fim.

texto = 'Python'
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto + '*')


# O uso combinado de for e range em Python é uma maneira eficiente de iterar sobre uma sequência de números.
# A função range(start, stop, step) gera uma sequência de números e o loop for é usado para executar um bloco de código um número específico de vezes.

numeros = range(10, 0, -1)

for numero in numeros:
    print(numero)


# FOR com if:

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)

    else:
        print('For completo com sucesso.')