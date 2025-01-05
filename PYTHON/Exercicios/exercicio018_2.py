import json

from exercicio018_1 import CAMINHO_ARQUIVO, FichaCadastral

with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    ficha_de_cadastro = json.load(arquivo)

    cadastro_1 = FichaCadastral(**ficha_de_cadastro[0])
    cadastro_2 = FichaCadastral(**ficha_de_cadastro[1])
    cadastro_3 = FichaCadastral(**ficha_de_cadastro[2])

    print(cadastro_1.get_dados_cadastrais())
    print(cadastro_2.get_dados_cadastrais())
    print(cadastro_3.get_dados_cadastrais())
    


