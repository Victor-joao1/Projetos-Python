# Estrutura de repetição for
'''for c in range(0, 7):
    print(c)
print('Fim')''' # Contagem crescente em lista de repetição de numeros positivos

'''for c in range(0, 7, -1):
    print(c)
print('Fim')''' # contagem decrescente com repetição de numeros positivos

'''n = int(input('Digite um numero:'))
for c in range(0, n+1):
    print(c)
print('Fim')'''

'''i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')'''

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor:'))
    s += n
print('O somatório de todos os valores foi {}'.format(s))

