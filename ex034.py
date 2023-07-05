salario = float(input('Qual é o seu salário?'))
if salario >= 1250:
    novo = salario + (salario * 10 / 100) #calculo de porcentagem
    print('Seu salário ira aumentar R$ {} e você receberá {:.2f}'.format(salario * 0.10, novo))
else:
    salario <= 1250
    novo = salario + (salario * 15 / 100)
    print('Seu salário ira aumentar R$ {} e você receberá {:.2f}'.format(salario * 0.15, novo))

