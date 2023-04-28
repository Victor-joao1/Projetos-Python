from time import sleep
alunos = list()
while True:
    nome = str(input('Qual o seu nome? '))
    nota1 = float(input('Digite sua primeira nota: '))
    nota2 = float(input('Digite sua segunda nota: '))
    media = nota1 + nota2 / 2
    alunos.append([nome, [nota1, nota2], media])
    continuar = str(input('Quer continuar?'))
    if continuar in 'Nn':
        break
print('-=' * 30)
print(f'{"NO.":<4} {"NOME":<10} {"MÉDIA":>8}')
print('-' * 60)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('De qual aluna deseja ver a nota? (555) interrompe o programa.'))
    if opc == 555:
        break
    if opc <= len(alunos) - 1:
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')
sleep(3)
print('OBRIGADO POR USAR MEU PROGRAMA!!!')

    