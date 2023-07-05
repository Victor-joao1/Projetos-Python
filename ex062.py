p1 = int(input('Digite o primeiro termo:'))
r = int(input('Digite a razão:'))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(p1), end=' ')
        p1 += r
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais deseja mostrar?'))
print('FIM')
print('Progressão finalizada com {} termos'.format(total))
