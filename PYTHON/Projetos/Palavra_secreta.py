"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada estána palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""

import os

ifen = '-'
palavra_secreta = 'esperança'
letras_acertadas = ''
numero_tentativas = 0

print(f'{ifen:-^16}')
print('JOGO DA FORCA')
print(f'{ifen:-^16} \n')
print('REGRAS DO JOGO:')
print('1- Digite uma letra para tentar descobrir a palavra secreta;')
print('2- Ao digitar a letra correta ela será desbloqueada na palavra secreta;')
print('3- Digitar mais que uma letra não é permitido; \n')
print('OBJETIVO DO JOGO:')
print('Descobrir a palavra secreta com o menor número de letras digitadas para obter o melhor grau de desempenho possível. \n')
print('O grau de desempenho é formado por:')
print(
    '1- EXCELENTE = Entre 7 e 8 tentativas; \n'
    '2- ÓTIMO = Entre 9 e 10 tentativas; \n'
    '3- BOM = Entre 11 e 12 tentativas; \n'
    '4- RUIM = 13 ou mais tentativas. \n'
)
print('DICA: Ela é a última que morre.')


while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(f'Palavra formada: {palavra_formada.upper()}')

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU! PARABÉNS!!')
        print(f'A palavra era {palavra_secreta}')
        print(f'Número de tentativas: {numero_tentativas}')
        letras_acertadas = ''
        if 7 <= numero_tentativas <= 8:
            print('Grau de desempenho: EXCELENTE')
        elif 9 <= numero_tentativas <= 10:
            print('Grau de desempenho: ÓTIMO')
        elif 11 <= numero_tentativas <= 12:
            print('Grau de desempenho: BOM')
        else:
            print('Grau de desempenho: RUIM')
        numero_tentativas = 0

        sair = input('Deseja sair? [s]im  [n]ão  ').lower().startswith('s')

        if sair is True:
            break



