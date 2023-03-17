lista = list()
pessoas = list()
cont = maisp = menosp = 0
while True:
    pessoas.append(str(input('Digite seu nome:')))
    pessoas.append(float(input('Digite seu peso:')))
    cont += 1
    lista.append(pessoas[:])
    pessoas.clear()
    continuar = input('Deseja continuar? [S/N]')
    if continuar in 'Nn':
        break
print(lista)
for p in lista:
    if p[1] > 70.0:
        print(f'{p[0]} é uma pessoa mais pesada.')
        maisp += 1
    else:
        print(f'{p[0]} é uma pessoa mais leve.')
        menosp += 1
print(f'Temos {maisp} pessoas pesadas e {menosp} pessoa mais leves.')



