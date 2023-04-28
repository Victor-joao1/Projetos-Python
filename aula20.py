# Funções parte 1
# def ou definindo função serve para criar rotinas 
# Toda função tem parenteses no final, print(), int(), float() input()...
'''def mostralinha():
    print('-------------------')
mostralinha()
print(' SISTEMA DE ALUNOS')
mostralinha()'''

#Com Parametros 

'''def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

#programa principal 
titulo(' CURSO EM VIDEO ')
titulo(' APRENDA PYTHON ')
titulo(' GUSTAVO GUANABARA ')'''

'''def soma (a, b):
    s = a + b
    print(s)
# Programa principal 
soma(4, 5)
soma(8, 9)
soma(2, 1)'''
'''def contador(*num): # (*) desempacota os numeros e permite colocar quantas numeros necessarios no parametro.
    tam = len(num)
    print(f'REcebi os valores {num} e são ao todo {tam} números.')
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''

#Dobrar valores
def dobra(lst):
    pos = 0 
    while pos < len(lst):
        lst *= 2
        pos += 1

valores = [6, 3, 9]
dobra(valores)
print(valores)

 