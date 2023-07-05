from random import randint
aleatorio = randint(0, 10)
print('Você é capaz de acertar o numero que estou pensando???')
cont = 0
acertou = False
while not acertou:
    chute = int(input('Digite seu palpite aqui --> '))
    cont += 1
    if chute == aleatorio:
        acertou = True
    else:
        if chute < aleatorio:
            print('Chute um numero maior!')
        elif chute > aleatorio:
            print('Chute um numero menor!')
print('Acertou com {} palpites!'.format(cont))

