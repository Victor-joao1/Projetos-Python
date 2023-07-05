print('-'*20)
print('   LOJA DO JOÃO  ')
print('-'*20)
total = cont = menor = totmil = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('Valor do produto: R$'))
    cont += 1
    if cont == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
    resp = ' '
    if valor > 1000:
        totmil += 1
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    total += valor
print(f'O valor total dos produtos é R${total:.2f}')
print(f'{totmil} produtos custam mais de R$1000')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

