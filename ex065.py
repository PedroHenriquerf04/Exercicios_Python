a = 's'
cont = média =0
maior = menor = 0
c = 1
while a == 's' or a == 'S':
    n = int(input('Digite um número: '))
    cont += 1 
    média += n
    if c == 1:
        maior = n
        menor = n
    elif n < menor:
        menor = n
    elif n > maior:
        maior = n
    c +=1
    a = str(input('Quer continuar [S/N]: '))
print('Você digitou {} números, e a média entre eles {}'.format(cont,  média/cont))
print('O menor número foi {} e o maior foi {}'.format(menor, maior))