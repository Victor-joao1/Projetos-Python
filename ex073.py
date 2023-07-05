times = ('Palmeiras','Internacional','Fluminense','Corinthians','Flamengo','Athletico-PR',
         'Atlético-MG','Fortaleza','São Paulo','América-MG','Botafogo','Santos','Goiás',
         'Bragantino','Coritiba','Cuiabá','Ceará','Atlético-GO','Avaí','Juventude')
print('-='*30)
print(f'Times do Brasileirão: {times}')
print('-='*30)
print(f'Os cinco primeiros são: {times[0:5]}')
print('-='*30)
print(f'Os quatro ultimos são: {times[-4:]}') #O -4 começou da posição da direita até o final :
print('-='*30)
print(f'Os times em ordem alfabética: {sorted(times)}') #O sorted colocou em ordem alfabética
print('-='*30)
print(f'O bragantino está na {times.index("Bragantino")}ª posição.') #Index acha a posição do objeto na tupla
print('-='*30)