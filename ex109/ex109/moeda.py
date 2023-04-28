def dobro(valor, format=False):
    dobrar = valor * 2
    return dobrar if format is False else moeda(dobrar)

def metade(valor, format=False):
    dividir = valor / 2
    return dividir if format is False else moeda(dividir)

def aumentando(valor = 0, taxa = 0, format=False):
    porcentagem = valor / 100 * taxa
    valor += porcentagem
    return valor if format is False else moeda(valor)

def dimunuindo(valor = 0, taxa = 0, format=False):
    porcentagem = valor / 100 * taxa
    valor -= porcentagem
    return valor if format is False else moeda(valor)

def moeda(valor = 0):
    return f'{valor}'.replace('.' , ',')

def resumo(valor = 0, taxaa = 10, taxar = 5):
    print('-'* 30)
    print('RESUMO DO VALOR'.center(30))
    print('-'* 30)
    print(f'preço analisado: {moeda(valor)}')
    print(f'Dobro do preço: {dobro(valor, True)}')
    print(f'Metade do preço: {metade(valor, True)}')
    print(f'Com aumento de {taxaa}%: {aumentando(valor, taxaa, True)}')
    print(f'Diminuindo o preço em {taxar}%: {dimunuindo(valor, taxar, True)}')
    print('-'* 30)