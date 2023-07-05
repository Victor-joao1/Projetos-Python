velocidade = float(input('Digite a sua velocidade:'))
resto = (velocidade - 80)
multa = resto * 7
if velocidade <= 80:
    print('Você está na velocidade permitida')
else:
    velocidade >=80
    print('Você excedou o limite permido')
    print(f'Você foi multado em R${multa}.')
