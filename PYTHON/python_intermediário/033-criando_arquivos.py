# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
import os

caminho_arquivo = 'aula116.txt'

with open(caminho_arquivo, 'w+', encoding='utf-8') as arquivo:     # Criando arquivo    # permitir leitura de caracteres especiais
    arquivo.write('Linha 1\r')  # Escrevendo no arquivo
    arquivo.write('Linha 2\r')
    arquivo.writelines(         # para escrever mais de uma linha
        ('Linha 3 \r', 'Linha 4\r', 'ATENÇÃO \r')     
    )
    arquivo.seek(0 , 0)     # para mover o cursor para o topo do arquivo
    print(arquivo.read())   # exibir na tela o conteúdo escrito no arquivo
    print('Lendo')
    print(arquivo.readline())       # lê uma linha por vez, como se fosse um __next__
    print(arquivo.readline())       # lê a quebra de linha também
    print('Lendo')
    print(arquivo.readline(), end='')   # para não ler a quebra de linha
    print('ATENÇÃO')
    print()

    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())        # também ignora a leitura das quebras de linha


print()
print('#' * 20)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())


# os.remove(caminho_arquivo)        para apagar o arquivo      
# os.unlink(caminho_arquivo)        para apagar o arquivo
os.rename(caminho_arquivo, 'Aula116-2.txt')     # para renomear ou mudar o caminho do arquivo