largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura*altura
print('As medidas de sua parede são {} x {} que dão uma área de {:.2f}.\nPor isso, para pintar a parede será necessário'
' um total de {:.2f} litros de tinta.'.format(largura, altura, area, area/2))