print('-=-' * 30)
print(' ============= APROVEITAMENTO ANUAL ============= ')
totgols = 0
aproveitamento = dict()
aproveitamento['Jogador'] = str(input('Digite seu nome: '))
aproveitamento['partidas'] = int(input('Digite a quantidade de partidas jogadas: '))
for p in range(0 , aproveitamento['partidas']):
    aproveitamento['gol'] = int(input(f' Digite quantos gols foram marcados na {p + 1}º partida? '))
    totgols += aproveitamento['gol']    
print('-=' * 30)
print('=====SALDO DE GOLS NA TEMPORADA=====')
print(f'Jogador: {aproveitamento["Jogador"]}')
print(f'Partidas jogadas: {aproveitamento["partidas"]}')
print(f'Total de gols: {totgols}')
