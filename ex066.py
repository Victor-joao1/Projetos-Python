cont = soma = 0
while True:
    n = int(input('Digite um numero [Digite 999 para parar]: '))
    cont += 1
    if n == 999:
        break
    soma += n
print(f'Foram digitados {cont} números e a soma deles é {soma} .')
