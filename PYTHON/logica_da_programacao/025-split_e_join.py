'''
split()
--> é usada para dividir uma string em uma lista 
de substrings com base em um separador específico.

separator (opcional)
--> delimitador onde a string será dividida. 
Se não for especificado, o padrão é qualquer espaço em branco.

maxsplit (opcional)
--> O número máximo de divisões que você deseja fazer. 
Se não for especificado, todas as possíveis divisões serão feitas.
'''
frase = 'A repetição, com correção, até a exaustão, leva à perfeição.'
str_split_1 = frase.split()
str_split_2 = frase.split(',')
str_split_3 = frase.split(',', 1)

print(str_split_1)
print()
print(str_split_2)
print()
print(str_split_3)


'''
join()
--> é usada para concatenar uma lista (ou qualquer iterável) de strings em uma única string,
com um delimitador especificado entre cada elemento.

--> Essa função é muito útil quando você precisa combinar várias strings em uma, 
separadas por um delimitador específico, como um espaço, vírgula ou qualquer outro caractere.
'''

palavras = ["Olá", "mundo!", "Python", "é", "incrível!"]
frase_completa = ' '.join(palavras)
frase_unida = '-'.join(palavras)

print(frase_completa)
print(frase_unida)