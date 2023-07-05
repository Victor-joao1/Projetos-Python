pre = float(input('Insira o valor do produto:'))
desc = float(pre * 0.05)
valor_descontado = float(pre - desc)
print('Seu preço com 5% de desconto é {:.2f}'.format(valor_descontado))


