produto = {
    'nome': 'Caneta azul',
    'preco': 2.55,
    'categoria': 'Papelaria',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor 
    in produto.items()
}

print(dc)