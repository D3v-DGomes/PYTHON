# Utilizada para entrada de dados e interação com o usuário.
# O código não será finalizado enquanto o usuário não inserir um dado.
# O tipo de dado retornado sempre será uma str
nome = input('Qual o seu nome? ')
print(f'O seu nome é {nome=}') # O símbolo de = serve para retornar o valor que foi atrinbuido com a resposta do usuário.

n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')

soma = int(n1) + int(n2) # Conversão de tipos para que a resposta do usuário deixe de ser uma str.
print(f'A soma dos números é: {soma}')