peso = float(input('Digite o seu peso:'))
altura = float(input('Digite sua altura:'))
IMC = peso / (altura ** 2)
if IMC < 18.5:
    print('Você está a baixo do peso!')
elif 18.5 <=IMC  < 25:
    print('Você está no peso ideal!')
elif 25 <= IMC < 30:
    print('Você está com sobrepeso!')
elif 30 <= IMC < 40:
    print('Você está com obsidade!')
else:
    IMC < 40
    print('Você está com obsidade morbida!')
