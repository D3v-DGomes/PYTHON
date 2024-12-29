'''
try...finally --> usada para garantir que um bloco de código seja sempre executado, 
independentemente de ocorrer uma exceção ou não.
Útil para a liberação de recursos, como fechar arquivos ou conexões de rede, 
que precisam ser garantidamente liberados, mesmo se ocorrer um erro.
'''

try:        # execução do código
    print('Abrir arquivo')
    a = 8/0
except ZeroDivisionError:       # tratamento de exceção
    print('Erro: divisão por zero.')
else:       # continuação da execução caso não aja exceção. (método pouco usado)
    print('Código não deu erro. Execução continuou.')
finally:        # ação a ser executada mesmo havendo tratamento de exceções.
    print('Arquivo fechado')