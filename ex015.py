km = float(input('Quantos KM você  rodou com  o carro? '))
dias = int(input('Quantos dias você ficou com o carro: '))
tot = (km*0.15) + (dias*60)
print ('O Aluguel do carro irá custa R${:.2f} '.format(tot))