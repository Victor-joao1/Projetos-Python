nota = dict()
nota['nome'] = str(input('Digite seu nome: '))
nota['primeira nota'] = float(input('Digite a primeira nota: '))
nota['segunda nota'] = float(input('Digite a segunda nota: '))
nota['media'] = (nota['primeira nota'] + nota['segunda nota'] / 2)
print(f'Nome: {nota["nome"]}')
print(f'Média igual a: {nota["media"]}')
if nota['media'] >= 7:
    print('Você está aprovado!!!')
else:
    print('Estude Mais!!!')
