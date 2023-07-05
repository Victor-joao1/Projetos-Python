n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero:'))
n3 = int(input('Digite o terceiro numero:'))
if n1 < n2 < n3:
    print(f'O maior numero é {n3} e o menor numero é {n1}')
elif n1 > n2 > n3:
    print(f'O maior numero é {n1} e o menor numero é {n3}')
elif n2 > n3 > n1:
    print(f'O maior numero é {n2} e o menor numero é {n1}')
elif n2 < n3 < n1:
    print(f'O maior numero é {n1} e o menor numero é {n2}')
elif n3 < n1 < n2:
    print(f'O maior numero é {n2} e o menor numero é {n3}')
elif n3 > n1 > n2:
    print(f'O maior numero é {n3} e o menor numero é {n2}')