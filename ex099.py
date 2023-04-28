def maior(* num):
    cont = maior = 0
    for valor in num:
        print(valor)
    if cont == 0:
        maior = valor
    else:
        if valor > maior:
            maior = valor
    cont += 1
    print(f'O maior valor informado é {maior}')







#Programa principal
maior(2, 6, 7, 8 ,23)
