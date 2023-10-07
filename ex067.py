print('{:^40}'.format('TABUADA'))
print('~'*40)
while True:
    n = int(input('Qual o número vocêque ver a tabuada? '))
    print('~'*40)
    if n < 0:
        break
    for c in range (1, 11):
        print('{} X {:2} = {:2}'.format(n, c, n*c))
    print('~'*40)
print('Fim')