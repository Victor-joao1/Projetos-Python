#Modulos e pacotes

#Modularaziação - Serve para organização e particionar o codigo

#Principal

import uteis #Importando o modulo que eu criei com 

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num) # Aqui importei o modulo.função
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}') # Aqui importei o modulo.função

 