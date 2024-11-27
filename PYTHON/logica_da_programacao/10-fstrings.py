# Formatação de strings para facilitar a digitação do código:

# Cálculo de IMC
nome = 'David'
altura = 1.73
peso = 75
imc = peso / altura ** 2

# f-string:
linha_1 = f'{nome} tem {altura:.2f} de altura e atualmente está pesando {peso:.2f}kg. O seu IMC é de {imc:.2f}'

# imprimindo:
print(linha_1)

# Utilizando o .format:
string = '{0} tem {1:.2f} de altura e atualmente está pesando {2}kg. O seu IMC é de {3:.2f}'
formato = string.format(nome, altura, peso, imc)
print(formato)

# Utilizando o .format com parâmetros nomeados:
string_2 = '{n1} tem {n2:.2f} de altura e atualmente está pesando {n3:.2f}kg. O seu IMC é de {n4:.2f}'
formato_2 = string_2.format(n1= nome, n2= altura, n3= peso, n4= imc)
print(formato_2)