r1 = int(input('Primeiro lado do Triângulo: '))
r2 = int(input('Segundo lado do Triângulo: '))
r3 = int(input('Terceiro lado do Triângulo: '))
if (r1<r2+r3) & (r2<r1+r3) & (r3<r1+r2):
    print ('As retas {}, {}, {} formar um Triângulo!'.format(r1, r2, r3))
    if r1== r2 and r2==r3:
        print ('E um Triângulo EQUILÁTERO. ')
    elif r1!=r2 and r2!=r3 and r1!=r3:
        print ('E um Triângulo ESCALENO.')
    else:
        print ('E um Triângulo ISOCELES.')
else:
    print (f'As retas {r1}, {r2}, {r3} NÃO forma um Triângulo!')
