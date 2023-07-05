p1 = int(input('Digite o primeiro termo:'))
r = int(input('Digite a razão:'))
cont = 1
while cont <= 10:
    print('{} -> '.format(p1), end=' ')
    p1 += r
    cont += 1
print('FIM')



