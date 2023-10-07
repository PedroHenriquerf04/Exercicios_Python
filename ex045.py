from random import randint 
from time import  sleep 
print ('\033[32m{:=^30}'.format('  Jokenpô '),'\033[m')
print ('''Escolha.... 
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
itens = ('Pedra', 'Papel', 'Tesoura')
escolha = int(input('Sua opção: '))
compt = randint(0, 2)
print ('\033[32m='*30,'\033[m')

print ('PEDRA')
sleep(1)
print ('PAPEL')
sleep(1)
print ('TESOURA...')
sleep(1)

print ('Computador jogou {}'.format(itens[compt]))
print ('O jogador jogou {}'.format(itens[escolha]))
print ('\033[32m='*30,'\033[m')   
if compt ==0:
    if escolha == 0:
        print ('EMPATE')
    elif escolha == 1:
        print ('JOGADOR GANHOU')
    elif escolha == 2:
        print ('COMPUTADOR GANHOU ')
    else:
        print ('Jogada INVÁLIDA')       
        
elif compt  ==1:
    if escolha == 0:
        print ('COMPUTADOR GANHOU ')
    elif escolha == 1:
        print ('EMPATE')
    elif escolha == 2:
        print ('JOGADOR GANHOU ')
    else:
        print ('Jogada INVÁLIDA')

elif compt ==2:
    if escolha == 0:
        print('JOGADOR GANHOU ')
    elif escolha == 1:
        print ('COMPUTADOR GANHOU ')
    elif escolha == 2:
        print ('EMPATE')
    else:
        print ('Jogada INVÁLIDA')