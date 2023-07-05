from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Suas opções são:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POW!!!')
print('-='*11)
print('O computador escolheu {}'.format(itens[computador]))
print('O player jogou {}'.format(itens[jogada]))
print('-='*11)
if computador == 0: #Computador jogou pedra.
    if jogada == 0:
        print('EMPATE!')
    elif jogada == 1:
        print('--PLAYER WIN--')
    elif jogada == 2:
        print('YOU LOSER!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1: #Computador jogou papel.
    if jogada == 0:
        print('YOU LOSER!')
    elif jogada == 1:
        print('EMPATE!')
    elif jogada == 2:
        print('--PLAYER WIN--')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2: #Computador jogou tesoura.
    if jogada == 0:
        print('--PLAYER WIN--')
    elif jogada == 1:
        print('YOU LOSER!')
    elif jogada == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVALIDA!')
