# Calculadora com while

while True:
    ifen = '-'
    print(f'{ifen:-^18}')
    print()
    print('CALCULADORA WHILE')
    print()
    print(f'{ifen:-^18}')
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+ - / *): ')

    num_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        num_validos = True
    except:
        num_validos = None

    if num_validos is None:
        print('Um ou ambos os números digitados são inválidos. Tente novamente.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido. Tente novamente.')
        continue

    if len(operador) > 1:
        print('Escolha apenas um operador.')
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')
    
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} =', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} =', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} =', num_1_float * num_2_float)
    else:
        print('Algo de errado não está certo. Você não deveria chegar aqui.')

    sair = input('Deseja sair? [s]im  ').lower().startswith('s')

    if sair is True:
        break