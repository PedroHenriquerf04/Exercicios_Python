from math import hypot
co = float(input('Medida do catetos oposto: '))
ca = float(input('Medida do catetos adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa é {:.2f}'.format(hi))