#Tratamento de erros, Try e exception. 
#Um unico try pode ter diversos exception

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    c = a / b
#except Exception as erro: #Indentificando qual é o erro
    #print(f'O erro encontrado foi {erro.__class__}') #Imprimindo o erro na tela
except ZeroDivisionError:
    print('Não é possivel dividir por zero!')
except (ValueError, TypeError):
    print('Valor ou tipo não compativeis!')
except KeyboardInterrupt: # caso não insiram valores
    print('O usuario prefiriu não importar os dados!')
else:
    print(f'O resultado é {c:.1f}')
finally:
    print('Volte sempre!')