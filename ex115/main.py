import functions
pessoas = []
arquivo = 'arquivo.txt'
head = '''
    1 - Ver pessoas cadastradas
    2 - Cadastrar nova pessoa
    3 - Sair do Sistema
    '''
if functions.arquivoExiste(arquivo):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    functions.criarArquivo(arquivo)
while True:
    print('-' * 30)
    titulo = 'MENU PRINCIPAL'
    print(titulo.center(30))
    print('-' * 30)
    
    interface = int(input(head))
    print('-' * 30)

    if interface == 2:
        functions.cadastrar(functions.dados()) #Adiciona o retorno na lista
    elif interface == 1:
        functions.lerArquivo(arquivo)
        #functions.mostrar(pessoas)
    else:
        break
