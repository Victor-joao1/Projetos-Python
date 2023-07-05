print('-='*20)
print('Analisador de triângulos')
print('-='*20)
r1 = float(input('Digite a primeira reta:'))
r2 = float(input('Digite a segunda reta:'))
r3 = float(input('Digite a terceira reta:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Você pode formar um triângulo')
    if r1 == r2 == r3:
        print('Equilátero')
    if r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Você não pode formar um triângulo')