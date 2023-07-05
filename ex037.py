numero = int(input('Digite um numero inteiro:'))
print('Escolha uma das bases de conversão')
numero_binario = print('[1] Para numero binário')
numero_octal = print('[2] Para numero octal')
numero_hexadecimal = print('[3] para numero hexadecimal')
opção = int(input('Sua opção:'))
if opção == 1:
    print('{} convertido para binário é igual a {}'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print('{} convertido para octal é igual a {}'.format(numero, oct(numero)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção invalida tente novamente.')