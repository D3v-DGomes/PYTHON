'''
Generator function --> Usa a palavra-chave yield para retornar um valor para o chamador e, 
ao mesmo tempo, suspende sua execução, mantendo o estado da função.
Quando a função é chamada novamente, ela retoma a execução de onde parou, 
continuando da última instrução yield.

A palavra-chave yield é usada em vez de return para produzir um valor e pausar a execução da função. 
Quando a função é chamada novamente, ela retoma da última instrução yield.

Isso permite que você crie iteradores de forma eficiente, 
especialmente quando lidando com grandes volumes de dados.

--------------------------------------------------------------------------------------------------------

Vantagens dos Generators:
1- Economia de Memória: Generators produzem itens sob demanda, 
sem armazenar toda a sequência na memória;

2- Melhor Desempenho: Evita a criação de grandes listas ou sequências na memória, 
tornando a execução mais eficiente;

3- Facilidade de Implementação: Generators permitem a criação de iteradores
de maneira simples e legível.

--------------------------------------------------------------------------------------------------------

Quando Usar Generators:
1- Grandes Volumes de Dados: Quando você precisa processar grandes volumes de dados de forma eficiente.

2- Fluxos de Dados: Para lidar com fluxos de dados que chegam de forma contínua.

3- Iteradores Personalizados: Para criar iteradores personalizados de forma simples e eficiente.
'''

def generator(n=0, maximum=1000):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return
        

function_generator = generator(maximum=100)
for n in function_generator:
    print(n)


# Fibonacci:

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a 
        a, b = b, a + b

for num in fibonacci(10):
    print(num)