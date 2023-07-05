'''from math import factorial     # É possivel importar uma blibioteca para fatorial
n = int(input('Digite o numero qual deseja saber o fatorial:'))
f = factorial(n)
print('O factorial de {} é {}'.format(n, f))'''
from time import sleep
n = int(input('Digite o numero qual deseja saber o fatorial:'))
c = n
f = 1
print('calculando {}! '.format(n), end='')
sleep(3)
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))