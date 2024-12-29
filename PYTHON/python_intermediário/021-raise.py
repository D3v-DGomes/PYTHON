'''
# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

raise --> é usada para criar exceções. Ela permite que você sinalize que ocorreu um erro
ou situação excepcional durante a execução do seu programa, 
interrompendo o fluxo normal do código e transferindo o controle para o manipulador 
de exceções mais próximo (se houver).
'''

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True


def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True


def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d


print(divide(8, '0'))