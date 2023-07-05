# Tuplas
# É uma variavel composta que guarda multiplos valores.
# Tuplas são imutáveis (Não recebem atribuições a variavel)
# Enumerate (para numerar as tuplas)
# Sorted (Para colocar a tupla em ordem <-)
# É possível somar as variaveis em tuplas
# del apaga qualquer variavel ou tupla
# É possivel colocar o menor e o maior valor com (min e max)
# index mostra onde está a informação no banco de dados
# count

'''lanche = ('Hambúrhuer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi bastante!')'''

'''lanche = ('Hambúrhuer', 'Suco', 'Pizza', 'Pudim')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi bastante!')'''

lanche = ('Hambúrhuer', 'Suco', 'Pizza', 'Pudim')
for pos,comida in enumerate(lanche):
    print(f'Eu vou comer {comida}, na posição {pos}')
print('Comi bastante!')

