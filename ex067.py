neg = cont = 0
while True:
    n = int(input('Qual numero deseja ver a tabuada?'))
    if n < neg:
        break
    print('-' *30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('Programa encerrado!')


