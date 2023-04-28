def MaiorNota(listaNotas):
    maiorNota = 0
    for nota in listaNotas:
        if nota > maiorNota:
            maiorNota = nota
    print(f'A maior nota é {maiorNota}')

def MenorNota(listaNotas):
    MenorNota = 0
    for nota in listaNotas:
        if nota < MenorNota:
           MenorNota = nota
    print(f'A menor nota é {MenorNota}')

def Media(listaNotas):
    soma = cont = 0
    for nota in listaNotas:
        cont += 1
        soma += nota
        media = soma / cont
    print(f'A media de notas é {round(media, 2)}')



       
#Programa principal

ListaNotas = [] #Parametro das função definidos em baixo
while True:
        n = float(input('Digite sua nota: '))
        ListaNotas.append(n)
        continuar = str(input('Deseja continuar inserindo notas? [S/N]')).upper()[0]
        if continuar == 'N':
            break

MaiorNota(ListaNotas) #Lembrar de colocar um parametro para a função, que no caso é a lista do programa principal
MenorNota(ListaNotas)
Media(ListaNotas)





