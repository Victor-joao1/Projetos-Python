tot18 = toth = totm20 = 0
while True:
    idade = int(input('Qual é sua idade?'))
    sexo = str(input('Qual é o seu sexo? [M/F] ')).upper().strip()[0]
    continuar = str(input('Deseja continuar a cadastrar pessoas? [Sim/Não] ')).upper().strip()[0]
    if continuar == 'S':
        if sexo == 'M':
            toth += 1
        if sexo == 'F':
            if idade < 20:
                totm20 += 1
        if idade >= 18:
            tot18 += 1
    elif continuar == 'N':
        break
print(f'Foram cadastrados {toth} homens, {tot18} pessoas tem mais de 18 anos, {totm20} mulheres tem menos de 20 anos.')
