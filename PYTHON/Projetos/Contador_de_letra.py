# Contador para identificar qual letra se repetiu mais na frase (espaços não são contabilizados):
frase = input('Digite uma frase: ')
frase_atual = frase.lower()

i = 0
qtd_apareceu_mais = 0
letra_apareceu_mais = ''

while i < len(frase_atual):
    letra_atual = frase_atual[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase_atual.count(letra_atual)

    if qtd_apareceu_mais < qtd_atual:
        qtd_apareceu_mais = qtd_atual
        letra_apareceu_mais = letra_atual

    i += 1

print(
    f'A letra que apareceu mais vezes foi: '
    f'"{letra_apareceu_mais}" \n' 
    f'A quantidade de vezes que a letra "{letra_apareceu_mais}" apareceu foi: {qtd_apareceu_mais}x'
)