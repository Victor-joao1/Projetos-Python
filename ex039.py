idade = int(input('Digite sua idade:'))
if idade < 18:
    print('Ainda falta {} anos para o alistamento obrigatório!'.format(18 - idade))
elif idade > 18:
    print('Você já passou do tempo de alistamento obrigatório!')
else:
    idade == 18
    print('Está na hora, aliste-se já!')