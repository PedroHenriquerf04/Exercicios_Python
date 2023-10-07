import random 
print('\033[36m='*30,'\033[m')
print('{:^30}'.format('Par ou Ímpar'))
print('\033[36m='*30,'\033[m')
tort = 0
while True:
    n = int(input('Digite um número: '))
    opção = str(input('Escolha Par ou Ímpar [P/I]: ')).strip().upper()
    pc = random.randint(0, 10)
    valor = pc + n
    if opção == 'P' and valor % 2 ==0:
        tort +=1
    elif opção == 'I' and valor % 2 == 1:
        tort +=1 
    else:
        print('Computador jogou {}'.format(pc))
        break
    print('\033[36m='*30,'\033[m')
print('\033[36m='*30,'\033[m')
print('O jogador ganhou {} vezes consecutiva'.format(tort))