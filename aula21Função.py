# =-=-=-=-=-=-= TOPICOS =-=-=-=-=-=-=
# Interactive Help (Ajuda interativa)
# docstrings
# Argumentos opcionais 
# Escopo de váriaveis
# Retorno de resultados

# Ajuda interativa 
#help(print) 

#docstrings

'''def contador (i, f, p):
    """ -> Faz uma contagem e mostra na tela.
    :paramatro i: inicio da contagem #Docstring da função, serve como manual quando chamar a função help()
    :paramatro f: final da contagem
    :paramatro p: pesso da contagem 
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('Fim!')

help(contador)'''

#Parametros opicionais 

'''def somar(a=0, b=0, c=0): # O zero é colocado ao lado para tornar o parametro opcional, podendo até mesmo chamar a função vazia.
    """-> Faz a soma de três resultados e mostra o resultado na tela.
    :parametro a: o primeiro valor
    :parametro b: o segundo valor
    :parametro b: o terceiro valor
    """
    s = a + b + c
    print(s)'''

#Escopo de variaveis

'''Escopo global == A varial fora da função pode ser atribuida com seu valor dentro da função.
   Escopo Local == A variavel fica limitada a atribuição dentro da função, delimitando seu campo de ação.
'''
def teste(b): #O valor de a foi atribuido a b
    b += 4 #foi somado com o valor b
    c = 2
    print(f'A dentro a vale(a)')
    print(f'A dentro b vale(b)')
    print(f'A dentro c vale(c)')

a = 5
teste(a)
#Se for chamados b e c vai ocorrer um erro pôs são locais 

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s #retorna a função para a variável 

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2} e {r3}')

