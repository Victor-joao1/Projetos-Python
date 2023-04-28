dados = list()
pessoas = dict()
cont = media = 0
while True:
    pessoas['nome'] = str(input('Digite seu nome: '))
    pessoas['sexo'] = str(input('Digite seu sexo: '))
    pessoas['idade'] = int(input('Digite sua idade: '))
    dados.append([pessoas['nome'], pessoas['sexo'], pessoas['idade']])
    cont += 1
    # del(pessoas['nome'], pessoas['idade'], pessoas['sexo'])
    media += pessoas['idade']
    continuar = str(input('Deseja continuar cadastrando pessoas? [S/N]'))
    if continuar in 'Nn':
        break
print(dados)
mediatot = media / cont
print(f'Foram cadastradas {cont} pessoas.')
print(f'A média de idade é {mediatot:5.2f}')
for pessoas in dados:
    if pessoas['idade'] >= mediatot:
        print(f'Está a cima da media de idade {pessoas["nome"]}.')
print()
for pessoas in dados:
    if pessoas['sexo'] in 'Ff':
        print(f'As mulheres na lista são: {pessoas["nome"]}.')
print()