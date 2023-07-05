from random import randint
'''print('-=-'*15)
print('  VAMOS JOGAR PAR OU IMPAR!!! ')
print('-=-'*15)
s = cont = 0
c = randint(0,101)
while True:
    n = int(input('Digite um valor:'))
    v = str(input('Par ou Ímpar? [P ou I]:')).upper().strip()[0]
    s = c + n
    p = s % 2 == 0
    i = s % 2 == 1
    if v == p or i:
        print('Parabéns você ganhou!')
        print('Vamos jogar novamente...')
        cont += 1
    else:
        print(f'Gamer over! Você venceu {cont} vezes')
        break'''
v = 0
while True:
    jogador = int(input('Digite um numero:'))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    print('Deu Par' if total % 2 == 0 else 'Deu ímpar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Gamer Over! Você venceu {v} vezes.')







