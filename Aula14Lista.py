#Listas parte 2
''' Aprendendo Listas compostas, possivel adicionar listas dentro de listas'''
''' dados = list ()
dados.append('pedro') #inserindo na lista 
dados.append('25') #inserindo na lista
pessoas = list() 
pessoas.append(dadps[:]) #Copiando a variavel "dados" e colocando como apenas um indice[0] == Pedro 25
'''

'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #Se não colocar o simbolo [:] vai atribuir umas lista a outra e vai dar errado
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) #Fiz uma cópia sem atribuir a váriavel
print(galera)'''

'''galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#print(galera[2][1]) #Selecionando um dado pelo indice, no caso o numero 13 que está na lista [2] indice [1]
for p in galera:
    #print(p[0]) #Selecionando apenas as pessoas pelo indice já que todas estão no indice [0]
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

galera = list()
dado = list()
totmai = totmen = 0 #inicio do contador 
for c in range(0, 3):
    dado.append(str(input('nome:')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:])
    dado.clear() #Apaga os dados cada vez que faz um looping para inserir dados novos

for p in galera: 
    if p[1] > 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1 #Contador maior de idade
    else:
        print(f'{p[0]} é menor de idade.') # Para cada nome de pessoa representado por [0]
        totmen += 1 #Contador menorde idade
print(f'Temos {totmai} maiores e {totmen} menores de idade.')





