# Precedência de execução dos operadores aritméticos por ordem de prioridade:
# 1. (n + n)
# 2. **
# 3. * ou / ou // ou %
# 4. + ou -

conta_1 = 1 + 1 ** 5 + 5 # Sem a precedência
print(conta_1)

conta_2 = (1 +1) ** (5 + 5) # Com a precedência
print(conta_2)