def leiaint(msg=0):
    while True:
        try:
            
            valor = int(input('Digite um numero: '))
        except (ValueError, TypeError):
            print('um valor incorreto.')
            continue
        except (KeyboardInterrupt):
            print('O usuario prefiriu não digitar o numero!')
            return 0
    
        else:
            return valor
def leaiafloat(msg=0):
    while True:
        try:
            valorf = float(input('Digite um numero real: '))
        except (ValueError, TypeError):
            print('um valor incorreto.')
            continue
        except (KeyboardInterrupt):
            print('O usuario prefiriu não digitar o numero!')
            return 0
        else:
            return valorf



print(f'Você acabou de digitar {leiaint()}')
print(f'Você acabou de digitar {leaiafloat()}')