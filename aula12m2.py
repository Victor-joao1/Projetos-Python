# Condições alinhadas
'''if
    bloco 1
elif              #podemos utilizar quantos quisermos
    bloco 2
else
    loco 3 '''

nome = str(input('Qual é seu nome?'))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
else:
    print('Seu nome é bem normal')
print(f'Tenha um bom dia, {nome}!')
