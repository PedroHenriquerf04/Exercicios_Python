di = float(input('Quanto de dinheiro você tem? R$'))
dólar  = di/4.94
euro = di /5.40
print('Com R${} você teria US${:.2f} é €{:.2f}'.format(di, dólar, euro))