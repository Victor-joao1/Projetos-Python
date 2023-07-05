#from math import sqrt
#c1 = float(input('Digite o valor do c1:'))
#c2: float = float(input('Digite o valor do c2:'))
#s = float(c1**2 + c2**2)
#r = sqrt(s)
#print('O comprimento da hipotenusa é igua a {:.4}'.format(r))

'''from math import sqrt
c1 = float(input('Digite o c1:'))
c2 = float(input('Digite o c2:'))
sh = float(c1**2 + c2**2)
r = sqrt(sh)
print('A hipotenusa é igual a {:.4}'.format(r))'''

from math import hypot
ca = float(input('Digite o cateto adjacente:'))
co = float(input('Digite o cateto oposto:'))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
