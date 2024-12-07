"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

###########################################

Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
import re
import sys


entrada = input('Informe o seu CPF: ')

# Primeiro dígito
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_sequencial = entrada == entrada[0] * len(entrada)

if entrada_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

nove_digitos = cpf_enviado_usuario[:9]
contagem_regressiva = 10

resultado_da_soma = 0
for digito in nove_digitos:
    resultado_da_soma += int(digito) * contagem_regressiva
    contagem_regressiva -= 1

primeiro_digito = ((resultado_da_soma * 10) % 11)
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

# Segundo dígito
dez_digitos = cpf_enviado_usuario[:10]
nova_contagem_regressiva = 11

resultado_da_soma_2 = 0
for digito_2 in dez_digitos:
    resultado_da_soma_2 += int(digito_2) * nova_contagem_regressiva
    nova_contagem_regressiva -= 1

segundo_digito = ((resultado_da_soma_2 * 10) % 11)
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

cpf_gerado_no_calculo = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if cpf_enviado_usuario == cpf_gerado_no_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido.')







