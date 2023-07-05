material = ('Lápis', '1.75',
            'Borracha', '2.00',
            'Estojo', '25.00',
            'Caderno', '15.90',
            'Mochila', '120.32')
print('-'*30)
print('LISTAGEM DE PREÇOS')
print('-'*30)
for pos in range(0, len(material)):
    if pos % 2 == 0:
        print(f'{material[pos]:.<30}', end='')
    else:
        print(f'R${material[pos]:>7}')
