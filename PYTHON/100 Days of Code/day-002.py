print('Seja bem-vindo à calculadora de gorjetas!')

conta = float(input('Qual foi o valor total da conta? \n R$'))
gorjeta = int(input('Quanta gorjeta você gostaria de dar: 10%, 12%, ou 15%?  '))
pessoas = int(input('Quantas pessoas devem dividir a conta?  '))
conta_com_gorjeta = ((gorjeta / 100) * conta) + conta
valor_por_pessoa = conta_com_gorjeta / pessoas

print(f'Valor da conta com a gorjeta: R${conta_com_gorjeta}')
print(f'Valor que cada pessoa deve pagar: R${valor_por_pessoa}')