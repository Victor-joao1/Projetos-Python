casa = float(input('Digite o valor da casa que deseja comprar:'))
salario = float(input('Digite qual é sua renda mensal:'))
tempo = int(input('Em quanto anos você vai pagar?'))
prestação = (casa / tempo) / 12
porcentagem = salario * 40 /100
if prestação <= porcentagem:
    print('Seu emprestimo imobiliario foi aprovado!')
    print('O valor da prestação será de R${:.2f}'.format(prestação))
else:
    prestação >= porcentagem
    print('Seu emprestimo não foi aprovado!')
    print('O valor da prestação será de R${:.2f}'.format(prestação))


