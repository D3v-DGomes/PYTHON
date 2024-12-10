'''
Closure e funções que retornam outras funções:
--> é uma função que lembra o ambiente onde foi criada, 
incluindo quaisquer variáveis que estavam presentes no escopo quando a função foi definida.

--> um closure permite que uma função "lembre-se" do estado de seu escopo ao ser chamada,
mesmo que esse escopo não exista mais no momento da chamada.

Características:
--> Funções Aninhadas: São funções definidas dentro de outras funções.

--> Escopo Léxico: Refere-se ao escopo onde a função foi definida, não onde ela é chamada.

Closures são úteis em várias situações, como:
--> Encapsulamento: Permitem encapsular dados e lógica em uma função, 
escondendo variáveis do escopo global ou externo.

--> Funções de Retorno: São frequentemente usados para criar funções de retorno (callbacks) 
ou funções personalizadas em tempo de execução.

--> Gerenciamento de Estados: Ideais para funções que precisam manter 
ou gerenciar estados entre chamadas, sem usar variáveis globais.

Resumindo:
--> Closures ajudam a criar código mais organizado, modular e encapsulado, 
além de permitir funcionalidades avançadas como gerenciamento de estados e criação de funções personalizadas.
'''

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!' 
    return saudar

retornar_bom_dia = criar_saudacao('Bom dia')        # Criando uma função closure
retornar_boa_noite = criar_saudacao('Boa tarde')    # Criando uma função closure

for nome in ['Maria', 'João', 'Angela', 'Daiane', 'Marcelo']:
    print(retornar_bom_dia(nome))       # Chamando as funções closure
    print(retornar_boa_noite(nome))     # Chamando as funções closure