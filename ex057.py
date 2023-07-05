'''sexo = str(input('Digite o seu gênero com M ou F:')).upper()
genero = 'F' 'M'
while sexo not in genero: # lembrar de por a variavel no lugar correto
    sexo = str(input('Dados invalidos! Digite novamentente seu gênero'))
print('Gênero {} resgistrado com secesso.'.format(sexo))'''

sexo = str(input('Informe seu sexo: [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} resgistrado com sucesso'.format(sexo))
