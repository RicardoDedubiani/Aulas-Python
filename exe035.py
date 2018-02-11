a = float(input('Insira o primeiro valor: '))
b = float(input('Insira o segundo valor: '))
c = float(input('Insira o terceiro valor: '))
if a < b + c and b < a + c and c < a + b:
    print('É possível formar um triangulo! ')
else:
    print('Não é possível formar um triangulo! ')
