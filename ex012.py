prod = float(input('Qual o valor do produto? R$'))
des = prod - (prod*5/100)
print('O produto com o valor R${}, com desconto de 5% ficar com o valor de R${}'.format(prod, des))