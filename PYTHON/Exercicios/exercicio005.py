"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

name = len(input('Digite o seu primeiro nome: '))

if name <= 4:
    print(f'Seu nome é curto. Ele possui {name} letras.')
elif 5 <= name <= 6:
    print(f'Seu nome é normal. Ele possui {name} letras.')
elif name >= 7:
    print(f'Seu nome é muito grande. Ele possui {name} letras')
else:
    print('Isso não é um nome.')