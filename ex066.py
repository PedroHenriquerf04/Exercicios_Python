print('~'*30)
print('[999] e o número de saída')
c = n = d = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c += 1
    d += n
print('~'*30)
print(f'O total de números digitado foi {c} e o somatório é {d}')
