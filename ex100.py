from random import randint
def sorteia(lista):
    for c in range(0, 5):
        sorteio = randint(0, 5)
        lista.append(sorteio)
    print(sorteio)

def somapar(lista):
    soma = 0 
    for par in lista:
        if par % 2 == 0:
            soma += par
    print(f'Pares de {lista}, temos {soma}')

numeros = list()
sorteia(numeros)
somapar(numeros)


