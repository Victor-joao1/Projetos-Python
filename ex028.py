from random import randint
aleatorio = randint(0, 5) #Faz o computador sortear um numero
chute = int(input('Chute um numero aleatório de 0 a 5:'))
if chute >=6 :
    print('Insira um numero de 0 a 5.')
elif aleatorio < chute:
    print('Você errou!!!')
elif aleatorio > chute:
    print('Você errou!!!')
else:
    chute == randint
    print('Você acertou!')
