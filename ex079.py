numeros = list()
while True:
   n = int(input('Digite um valor:'))
   if n not in numeros: #Não deixando os numeros duplicarem
       numeros.append(n) #Adicionando o numero a lista
       print('Adicionado com sucesso...')
   else:
    print('Valor duplicado, não será adicionado')
   r = input('Quer continuar [S/N]?')
   if r in 'Nn':
       break #Parando o laço de repetição sem flag
print('-='*30)
numeros.sort() #Para colocar os numeros em ordem
print(f'Você criou uma lista com os seguintes numeros {numeros}')


