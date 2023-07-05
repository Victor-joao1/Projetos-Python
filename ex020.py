from random import shuffle
aluno_1 = str(input('Digite o primeiro aluno:'))
aluno_2 = str(input('Digite o segundo aluno:'))
aluno_3 = str(input('Digite o terceiro aluno:'))
aluno_4 = str(input('Digite o quarto aluno:'))
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
shuffle(lista)
print('A ordem de apresentação será')
print(lista)
