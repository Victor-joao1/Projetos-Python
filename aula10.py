# Condicionais
# if - Utilizado para estruturas simples
# else - Utilizado para estruturas compostas
# todo comando colado do lado esquerdo irá acontecer de qualquer forma

'''name = str(input('Wath your name?'))
if name == 'João':
    print('Que nome lindo você tem')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {name}!')'''

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
print('PARABÉNS' if m >=6 else 'ESTUDE MAIS!')
