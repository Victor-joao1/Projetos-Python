from random import randint
num = tuple(randint(i + 0,10) for i in range(0,5)) #Foi necessário declarar que é uma tupla e colocar dentro de um laço
print(f'Os valores sorteados: ', end='')
for n in num: #laço for simples
    print(f'{n} ', end='')
print(f'\nO menor valor é {min(num)}') #O python disponibiliza de recursos para mostrar o minimo e o maximo
print(f'O maior valor é {max(num)}')

