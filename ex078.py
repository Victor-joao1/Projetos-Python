valores = []
maior = menor = 0
for c, cont in enumerate(range(0, 5)):
    valores.append(int(input(f'Digite um valor para posição {c} -> ')))
    '''maior = menor= valores[0]
if valores[1] > valores[0]: # Essa foi a minha resposta 
    maior = valores[1]
if valores[2] > maior:
    maior = valores[2]
if valores[3] > maior:
    maior =valores[3]
if valores[4] > maior:
    maior = valores[4]'''
    if c == 0:
        maior = menor = valores[c] #Para ler o primeiro numero da ordem caso tenha dois numeros iguais
    else:
        if valores[c] > maior: #Checagem do maior numero
            maior = valores[c]
        if valores[c] < menor: #Checagem do menor numero
            menor = valores[c]
print(f'Os valores são {valores} ')
print()
print(f'O maior valor é {maior} ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}º Posição...')
print()
print(f'O menor valor é {menor} ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}º Posição...')
