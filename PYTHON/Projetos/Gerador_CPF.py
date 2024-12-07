import random

print('Gerando CPFs válidos: ')

for _ in range(20):
    nove_digitos = ''

    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    contagem_regressiva = 10

    resultado_da_soma = 0
    for digito in nove_digitos:
        resultado_da_soma += int(digito) * contagem_regressiva
        contagem_regressiva -= 1

    primeiro_digito = ((resultado_da_soma * 10) % 11)
    primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

    # Segundo dígito
    dez_digitos = nove_digitos + str(primeiro_digito)
    nova_contagem_regressiva = 11

    resultado_da_soma_2 = 0
    for digito_2 in dez_digitos:
        resultado_da_soma_2 += int(digito_2) * nova_contagem_regressiva
        nova_contagem_regressiva -= 1

    segundo_digito = ((resultado_da_soma_2 * 10) % 11)
    segundo_digito = segundo_digito if segundo_digito <= 9 else 0

    cpf_gerado_no_calculo = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

    print(f'CPF válido: {cpf_gerado_no_calculo}')