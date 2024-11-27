# Conversão de tipos, coerção de tipos, type convertion, typecasting e coercion são a mesma coisa com nomes distintos.
# É o ato de converter um tipo em outro.

# Tipos imutáveis e primitivos:

# str, int, float, bool
print(2 + 2) # soma de dois dados do tipo int.
print('a' + 'b') # concatenação de dois dados do tipo str.
print('1' + 1) # impossível realizar soma ou concatenação porque os dados são de tipos diferentes.
print(int('1') + 1) # haverá soma entre os dois dados porque o primeiro foi convertido para o mesmo tipo do segundo.
print(type(float('1.3') + 1)) # soma entre um float e um int.
print(bool(' ')) # transformando a str vazia em um valor booleano.
print(str(11) + 'b') # convertendo o dado do tipo int para o tipo str.