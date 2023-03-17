from random import randint
print('-=' * 30)
print('     GERADOR DE JOGOS DA MEGA SENA     ')
print('-=' * 30)
lista = list()
jogos = list()
quant = int(input('Quantos jogos deseja sortear? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'Os números sorteados foram {jogos}')