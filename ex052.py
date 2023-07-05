num = int(input('Digite um numero:'))
tot = 0
for c in range(2,num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[33m', end='')
    print('{}'.format((c), end=''))
print('O número {} foi dívisivel {} vezes'.format(num, tot))
if tot == 2:
    print('Esse numero é primo!')
else:
    print('Esse número é primo!')
