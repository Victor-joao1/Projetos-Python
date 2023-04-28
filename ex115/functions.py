def dados():
    try:
        pessoa = {'nome': str(input('Digite seu nome: ')),
                'idade': int(input('Digite sua idade: ')),
                'sexo': str(input('Digite seu sexo: '))}
        return pessoa
    except (ValueError, TypeError):
        print(f'Digitação incorreta erro de {Exception.__class__}')


def mostrar(pessoas):
    print(pessoas)

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt' )
        a.close
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close
    except:
        print('Existe um erro na criação do arquivo!')
    else:
        print('Novo arquivo criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        print('Arquivo criado com sucesso! ')
        print(a.readlines())
    finally:
        a.close

def cadastrar(dados):
    try:
        a = open(dados, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{dados}')
        except:
            print('Houve um erro ao escrever!')
            a.close
