listagem = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar')
for l in listagem:
    print(f'\nNa plavra {l} temos ', end='')
    for letra in l:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

