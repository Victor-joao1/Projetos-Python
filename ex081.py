lista = list()
cont = 0
while True:
    n = int(input('Digite um numero:'))
    lista.append(n)
    lista.sort(reverse=True)
    cont += 1
    continuar = input('Deseja continuar [S/N]?')
    if continuar in 'Nn':
        break
print(f'Foram digitados {cont} numeros, são os seguintes valores {lista}')
if 5 in lista:
    print('O valor 5 faz parte da Lista!')
else:
    print('O valor 5 não faz parte da lista!')
