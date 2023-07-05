from random import randint
num = tuple(randint(i + 1,10) for i in range(0,5))
print('Os nuemros são: ', end='')
for n in num:
    print(f'{n}', end='')
print(f'\nO menor numero é {min(num)}')
print(f'O maior numero é {max(num)}')