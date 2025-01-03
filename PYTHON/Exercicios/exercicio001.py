"""
Exercício
Peça ao usuário para digitar seu nome;
Peça ao usuário para digitar sua idade;
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome};
        Seu nome de trás para frente é {nome invertido};
        Seu nome contém (ou não) espaços;
        A primeira letra do seu nome é {letra};
        A última letra do seu nome é {letra};
Se nada for digitado em nome ou idade:
    Exiba:
        "Desculpe, você deixou campos vazios."
"""
name = input('Digite o seu nome: ')
age = input('Digite a sua idade: ')

if name and age:
    print(f'Seu nome é {name}')
    print(f'Seu nome de trás para frente é {name[::-1]}')

    if ' ' in name:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    print(f'Seu nome tem {len(name)} letras')
    print(f'A primeira letra do seu nome é {name[0]}')
    print(f'A última letra do seu nome é {name[-1]}')
else:
    print('Desculpe, você deixou campos vazios. Tente preencher o formulário corretamente.')