sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
print(sexo)
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe se sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
