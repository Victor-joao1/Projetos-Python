#Apredendo dicionários {} = dict()
'''filme = {'titulo':'Star Wars', 
'Ano':1977,
'diretor':'George Lucas' #Colocar os dois pontos apos a key atribui ao valor
}
print(filme['titulo']) #Não será mais necessários buscar dados por indices 
print(filme.values()) #Imprime o valor na tela
print(filme.keys()) #Imprime apenas as chaves sem os dados 
print(filme.items()) #Imprime todo o dicionário criado 
for k, v in filme.items():
    print(f'O {k} é {v}.')
del filme['titulo'] #Serve para apgar um elemento
#Podemos adicionar sem append, apernas com atribuição.'''

'''pessoas = {'nome': 'João', 'Sexo':'M', 'idade': 23}
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos.')'''

#Dicionários dentro de listas
'''brasil = []
estado1 = {'uf':'Rio de janeiro'}
estado2 = {'uf': 'São Paulo'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['uf'])'''
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa:' ))
    estado['sigla'] = str(input('Sigla do estado:' ))
    brasil.append(estado.copy()) #Aqui o metodo para copiar é .copy
for e in brasil:
    for v in e.values(): 
        print(v, end=' ')
    print()

