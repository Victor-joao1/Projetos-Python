def voto(n):
    ''' -> A função retorna se a pessoa está apta a votar. 
    :Quando o nascimento é menor que 16 o voto é negado.
    :Quando a pessoa está entre 16 e 18 anos é optativo assim como as pessoas a cima de 65
    :Quando a pessoa tem entre 18 e 65 anos ela é obrigada a votar
    '''
    from datetime import date
    idade = date.today().year - n
    if idade < 16:
        return 'Voto negado!'
    elif 16 <= idade < 18 or idade > 65:
        return 'Voto opcional!'
    elif idade > 18 < 65:
        return 'Voto obrigatório!'
    
#Programa principal

nascimento = int(input('Digite sua data de nascimento: '))    
print(voto(nascimento))
help(voto)