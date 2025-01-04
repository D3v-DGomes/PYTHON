# Problema dos parâmetros mutáveis em funções Python

# a função foi definida com seu parâmetro padrão sendo um mutável, 
# isso fará a função reutilizar os valores da lista em diferentes chamadas.
# Resultando em uma junção da chamada anterior com a autal.
def adc_clientes(nome, lista=[]):
    lista.append(nome)
    return lista

# primeiros valores adicionados
clientes_1 = adc_clientes('Luiz')
adc_clientes('Ana', clientes_1)
print(clientes_1)

# herda os primeiros valores e adiciona os novos
clientes_2 = adc_clientes('Jorge')
adc_clientes('Marcela', clientes_2)
print(clientes_2)

# solução:
def add_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

clientes_3 = add_clientes('Ângela')
add_clientes('Maicon', clientes_3)
print(clientes_3)

clientes_4 = add_clientes('Murilo')
add_clientes('Bárbara', clientes_4)
print(clientes_4)