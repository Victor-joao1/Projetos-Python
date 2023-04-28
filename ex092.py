from datetime import date
trabalhador = dict()
trabalhador['nome'] = str(input('Digite seu nome: '))
Nascimento = int(input('Digite o ano do seu nascimento: '))
trabalhador['sexo'] = str(input('Digite o seu sexo: '))
trabalhador['idade'] = date.today().year - Nascimento
trabalhador['CTPS'] = int(input('Digite o numero da sua CTPS caso não tenha em mão digite [0]: '))
if trabalhador['CTPS'] > 0:
    trabalhador['contratação'] = int(input('Digite o ano de sua contratação: '))
    trabalhador['salario'] = float(input('Digite o seu salário: '))
print('-=' * 30)
print('==========EXTRATO DE APOSENTADORIA==========')
print(f'Nome: {trabalhador["nome"]}')
print(f'Idade: {trabalhador["idade"]}')
if trabalhador['CTPS'] > 0:
    print(f'CTPS: {trabalhador["CTPS"]}')
    print(f'Ano de contratação: {trabalhador["contratação"]}')
    print(f'Salário: {trabalhador["salario"]}')
if trabalhador['sexo'][0] in 'Mm':
    if trabalhador['idade'] < 65:
        print(f'Faltam {65 - trabalhador["idade"] } anos para se aposentar.')
    else:
        print('O senhor já pode se aposentar!')
if trabalhador['sexo'][0] in 'Ff':
    if trabalhador['idade'] < 60:
        print(f'Faltam {60 - trabalhador["idade"]} anos para se aposentar.')
    else:
        print('A senhora já pode se aposentar!')


