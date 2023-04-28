import moeda 
valor = float(input('Digite o preço: '))
print(f'O dobro do preço é {moeda.moeda(moeda.dobro(valor))} reais.')
print(f'A metade do preço é {moeda.moeda(moeda.metade(valor))} reais.')
print(f'O valor aumentando 10% é {moeda.moeda(moeda.aumentando(valor, 10))}')
print(f'O valor diminuindo 10% é {moeda.moeda(moeda.dimunuindo(valor, 10))}')
