from random import randint
from time import sleep
n = randint(0,5)
print ('Vou pensar em um número entre 0 e 5. Tenter adivinha')
n1 = int(input('Digite um número:  '))
print ('PROCESSANDO.....')
sleep(1.5)
if n==n1:
    print ('PARABÉNS!, você acertou')
else:
    print ('Ganhei, o número que eu pensei foi {} e não {}'.format(n, n1))