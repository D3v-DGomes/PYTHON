'''
While (enquanto) --> repete um bloco de código enquanto uma condição especificada for verdadeira.

Início: O loop começa verificando a condição especificada.

Execução: Se a condição for verdadeira, o bloco de código dentro do while é executado.

Reavaliação: Após a execução do bloco de código, a condição é reavaliada.

Repetição: Se a condição ainda for verdadeira, o bloco de código é executado novamente.

Término: O loop continua até que a condição se torne falsa.

Break --> é particularmente útil quando você deseja sair de um loop com base em uma condição específica, 
sem ter que esperar que a condição do loop se torne falsa.
'''

# Exemplo 1
condicao = True

while condicao:
    nome = input('Digite seu nome: ')
    print(f'Seu nome é {nome}.')

    if nome == 'sair':
        break

print('Você encerrou o laço de repetição.')

# Exemplo 2
contador = 0

while contador < 10:
    contador = contador + 1
    print(contador)

print('Acabou.')

'''
Operadores de atribuição com operadores aritméticos:

Os operadores de atribuição são frequentemente usados para atualizar variáveis dentro do loop.
Os operadores de atribuição são utilizados para modificar o valor de uma variável.
São essenciais para controlar a iteração do loop.

+= --> Adiciona um valor à variável e depois atribui o resultado à mesma variável.
-= --> Subtrai um valor da variável e depois atribui o resultado à mesma variável.
*= --> Multiplica a variável por um valor e depois atribui o resultado à mesma variável.
/= --> Divide a variável por um valor e depois atribui o resultado à mesma variável.
%= --> Calcula o módulo (resto da divisão) da variável por um valor e depois atribui o resultado à mesma variável.

continue --> é usada dentro de loops para pular o restante do código no corpo do loop para a próxima iteração. 
Quando o continue é encontrado, o controle do programa imediatamente passa para a próxima iteração do loop, 
ignorando qualquer código que venha após o continue na iteração atual.
'''

# Exemplo 3
n1 = 0

while n1 < 10:
    n1 += 1
    print(n1)

print('Acabou.')

# Exemplo 4
n2 = 1

while n2 < 60:
    n2 += 2

    if n2 == 20:
        print('O número 20 foi pulado.')
        continue

    if n2 >= 50 and n2 <= 58:
        print('Chegando ao topo!')
        continue

    print(n2)

    if n2 == 40:
        break

# Exemplo 5
qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha} {coluna}')
        coluna += 1
    linha += 1

print('Acabou.')
