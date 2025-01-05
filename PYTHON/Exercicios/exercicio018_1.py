'''
Salve sua classe em JSON;
Salve os dados da sua classe JSON e depois crie novamente as instâncias
da classe com os dados salvos. Faça arquivos separados.
'''
import json

CAMINHO_ARQUIVO = 'exercicio018.json'

class FichaCadastral:

    def __init__(self, nome, sobrenome, ano_nasc, tel, alt, cor_olhos, cor_pele):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nasc = ano_nasc
        self.tel = tel
        self.alt = alt
        self.cor_olhos = cor_olhos
        self.cor_pele = cor_pele

    def get_dados_cadastrais(self):
        return (self.nome, 
                self.sobrenome, 
                self.ano_nasc, 
                self.tel, 
                self.alt, 
                self.cor_olhos, 
                self.cor_pele
            )


cadastro_1 = FichaCadastral(
    'David Kevin', 
    'Gomes Silva', 
    2000, 
    71991320043, 
    1.74, 
    'Castanho escuro', 
    'Parda'
)

cadastro_2 = FichaCadastral(
    'Ana',
    'Melo',
    1996,
    47988230765,
    1.58,
    'Azul',
    'Branca'
)

cadastro_3 = FichaCadastral(
    'André',
    'Santos Silva',
    1978,
    21992465783,
    1.81,
    'Preto',
    'Preta'
)

dados = [vars(cadastro_1), 
        vars(cadastro_2), 
        vars(cadastro_3)
]

with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, indent=2)
