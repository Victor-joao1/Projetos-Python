nascimento = int(input('Digite o ano do seu nascimento:'))
from datetime import datetime
conta = datetime.today().year - nascimento
if conta <= 9:
    print('Você está na classe mirim')
elif conta <= 14:
    print('Você está na classe infantil')
elif conta <= 19:
    print('Você está na classe junior')
elif conta <= 25:
    print('Você está na classe senior')
else:
    conta
    print('Você está na classe master')
print(conta)



