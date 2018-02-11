soma = 0
cont = 0
for c in range(1, 101, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma é {} e a quantidade é {}'.format(soma, cont))
