'''distancia = float(input('Quantos km você irá viajar?'))
a_baixo = distancia <= 200
a_cima = distancia >= 200
if a_baixo:
    print('O preço da passagem é {:.2f}'.format(distancia * 0.50))
else:
    a_cima
    print('O preço da passagem é {:.2f}'.format(distancia * 0.45))'''

distância = float(input('Quantos km você irá viajar?'))
print('Você está prestes a começar a viagem de {}km.'.format(distância * 0.45)) #calculos não cabem nas chaves
preço = distância * 0.50 if distância <= 200 else distância * 0.45 # Operador ternario
print('E o preço da sua passagem será de R${:.2f}'.format(preço))