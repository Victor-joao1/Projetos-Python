print('10 TERMOS DE UMA PA \n=======================')
primeiro = int(input('Primeiro Termo:'))
razao = int(input('Razão:'))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU')
