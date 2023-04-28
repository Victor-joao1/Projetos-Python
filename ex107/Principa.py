import moeda 
valor = float(input('Digite o preço: '))
print(f'O dobro do preço é {moeda.dobro(valor)} reais.')
print(f'A metade do preço é {moeda.metade(valor)} reais.')
print(f'O valor aumentando 10% é {moeda.aumentando(valor)}')
print(f'O valor diminuindo 10% é {moeda.dimunuindo(valor)}')