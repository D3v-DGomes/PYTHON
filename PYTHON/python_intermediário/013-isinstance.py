# isinstance - para saber se objeto é de determinado tipo

lista = [
    'a', 1, 1.1, ['d', 'b', 'c'], (1, 2, 4, 5),
    {0, 2}, {'nome': 'Anderson'},
]

for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('STR')
        print(item.upper())

    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)

    else:
        print('OUTRO')
        print(item)