from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for c in range(0, 7):
    nasc = int(input('Em que ano você nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('Ao todo tivemos {} pessoas maior de idade \n'
                    'e {} pessoas menor de idade'.format(totalmaior, totalmenor))

