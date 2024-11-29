'''
Introdução ao try/except
try --> tentar executar o código
except --> ocorreu algum erro ao tentar executar o código.
'''

numero_str = input('Vou dobrar o número que você digitar: ')

try: # executar o código até ele dar erro.
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except: # após o código apresentar erro na fase do try, ele pula para cá como alternativa.
    print('Isso não é um número. Tente novamente.')
