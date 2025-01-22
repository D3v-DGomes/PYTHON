'''
@property --> é um getter em Python (decorator)
getter --> é um método para obter um atributo:
cor = get_cor()

@property é uma propriedade do objeto, ela é um método que se
comporta como um atributo.

Geralmente é utilizada nas seguintes situações:

--> Como getter;
--> para evitar quebrar código cliente;
--> para habilitar setter;
--> para executar ações ao obter um atributo

# código cliente é um código que utiliza o seu código.
'''

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
    
    @property
    def cor(self):
        print('Property')
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 321
    
caneta = Caneta('Preta')
print(caneta.cor)
print(caneta.cor_tampa)
    