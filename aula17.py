#Variável Composta (LISTA) []
# Append para adicionar um elemento no final
# Insert(0,'elemento') para adicionar elementos em qualquer lugar da lista
# Del ou pop ('2') para eliminar pela chave ou indice
# Remove ('elemento') para eliminar com o valor
# Para utilizar um range é necessário utilizar List ex: list(range(0,7))
# Sort para ordenar valores para inverter podemos utilizar o reverse ex: valores.sort(reverse=True)
# Len contar os elementos

'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
#num.remove(2) #Só removeu o primeiro que apareceu
if 4 in num: #O in para estrutura condicional ajuda bastante para testar
    num.remove(4)
else:
    print('Não achei o numero 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''

valores =[]
'''valores.append(5)
valores.append(9)
valores.append(4)'''
for cont in range(0, 5):
    valores.append(int(input('Digite um valor:')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
# O python costuma atrelar as listar quando fazemos uma atribuição, quando mudamos em um lugar automaticamente muda a origem
# Para criar cópias é necesário [:] recebendo todos itens 

