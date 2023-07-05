num = (int(input('Digite o primeiro numero:')),
      int(input('Digite o segundo numero:')),
      int(input('Digite o terceiro numero:')),
      int(input('Digite o ultimo numero:')))
print(f'O numero nove aparece {num.count(9)}')
if 3 in num:
    print(f'O numero 3 está na posição {num.index(3)}ª')
else:
    print('O numero 3 não foi digitado')
print('Os valores pares digitados foram:', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')









