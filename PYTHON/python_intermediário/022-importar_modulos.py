# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import zzznovo_modulo
from zzznovo_modulo import soma, soma_ab
import importlib

print('Este módulo se chama', __name__)
print(zzznovo_modulo)
print(soma(5,7))
print(soma_ab)

importlib.reload(zzznovo_modulo)        # para recarregar a importação do módulo.
