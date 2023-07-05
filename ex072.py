numeros = ('zero', 'um', 'dois', 'Três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True: #Forma de validar os dados
    ex = int(input('Digite um numero de 0 até 20:'))
    if 0 <= ex <= 20: #Validação de dados
        break
    print('Tente novamente!')
print(f'Você digitou o numero {numeros[ex]}.')
