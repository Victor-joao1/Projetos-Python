lista = list()
valoresi = list()
valoresp = list()
for v in range(0, 7):
    n = int(input('Digite um valor:'))
    if n % 2 == 0:
        valoresp.append(n)
        lista.append(valoresp[:])
        valoresp.sort()
        
    else:
        valoresi.append(n)
        lista.append(valoresi[:])
        valoresi.sort()       
print(f'Os valores pares pares digitados foram {valoresp}')
print(f'Os valores pares ímpares digitados foram {valoresi}')
