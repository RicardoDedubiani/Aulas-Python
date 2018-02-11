real = float(input('Quantos reais você tem? R$ '))
dolar = real / 3.27
print('Com R${}, você tem US${:.2f}'.format(real, dolar))