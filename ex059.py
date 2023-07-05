from time import sleep
print('----- BEM VINDO -----')
val1 = int(input('Insira o primeiro valor:'))
val2 = int(input('Insira o segundo valor'))
opçao = 0
while opçao != 5 :
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS 
    [5] SAIR DO PROGRAMA''')
    opçao = int(input('Qual é sua opção?'))
    if opçao == 1:
        print('A soma dos valores é {}'.format(val1 + val2))
    elif opçao == 2:
        print('A multiplicação dos valores é {}'.format(val1 * val2))
    elif opçao == 3:
        if val1 > val2:
            print('Maior numero é {}'.format(val1))
        else:
            print('Maior numero é {}'.format(val2))
    elif opçao == 4:
        val1 = int(input('Insira o primeiro valor:'))
        val2 = int(input('Insira o segundo valor'))
    elif opçao == 5:
        print('Aguarde...')
        sleep(2)
        print('saindo...')
    else:
        print('Opção invalida')
sleep(2)
print('Finalizando o programa...')
sleep(3)
print('Obrigado por usar meu programa!')


