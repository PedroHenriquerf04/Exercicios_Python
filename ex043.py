altura = float(input('Qual sua altura? '))
peso = float(input('Qual seu peso? '))
imc =  peso/(altura**2)
print ('Uma pessoa com {}kg e {:.2f}m tem um IMC de {:.1f}.'.format(peso, altura, imc))
print ('CLASSIFICAÇÃO: ')
if imc < 18.5:
    print ('Abaixo do PESO')
elif imc < 25:
    print ('PESO ideal')
elif imc < 30:
    print ('SOBREPESO')
elif imc < 40:
    print ('OBESIDADE')
else:
    print ('OBESIDADE MÓRBIDA')