from time import sleep 
print('='*30)
print('Calcular o fatorial de um número')
n = int(input('Digite o número: '))
n2 = n-1
res = n
print('='*30)
print('CALCULANDO... ')
sleep (1)
print('{}! ='.format(n), end=' ')
while n2 != 0:
        if n2 == 1:
            print ('{} '.format(n2), end='')
        else:
            print('{} X'.format(n2), end=' ')
        res = res*n2
        n2 = n2-1
print('= {}'.format(res))
