# Aula 15 - Aprendendo Break
n = s = 0
while True: #Criando pontos de paradas sem flag pôs a flag é somada junto com os numeros (ex: while n != 999)
    n = int(input('Digite um numero:'))
    if n == 999:
        break #Ponto de parada
    s += n
print('A soma vale {}'.format(s))
