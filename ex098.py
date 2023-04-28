from time import sleep
'''def contagem():
    print('-='* 25)
    print(str('Contagem de 1 até 10 de 1 em 1'))
    for c in range(1, 11):
        print(c, end='')
    
def regressiva():
    print(str('Contagem regressiva de 10 até 0 de 2 em 2'))
    for c in range(10, 0, 2):
        print(c, end= '')
def personalizado(i, f, p):
    print('-='* 25)
    for c in range(i, f, p):
        print(c, end= '')
contagem()
regressiva()
print()
print('Sua vez de personalizar a contagem')
i = int(input('Inicio: '))
f = int(input('Final: '))
p = int(input('Passos: '))
personalizado(i, f, p)'''

def contador(i, f, p):
    print('-='* 25)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(2.5)

    if p < 0:
        p*= 1
    if p == 0:
        p = 1
    if i < f:
        cont = i
    
        while cont <= f:
            print(f'{cont}', end='', flush=True)
            sleep(0.5)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end='', flush=True) 
            sleep(0.5)
            cont -= p   
        print('FIM!')

# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 25)
print('Sua vez de personalizar a contagem')   
ini = int(input('Inicio: '))
fim = int(input('Final: '))
pas = int(input('Passos: '))
contador(ini, fim, pas)
        
