a = float(input('Insira o primeiro valor: '))
b = float(input('Insira o segundo valor: '))
c = float(input('Insira o terceiro valor: '))
if a < b + c and b < a + c and c < a + b:
    print('É possível formar um triangulo! ')
    if a == b == c:
        print('Equilátero')
    elif a == b != c or a == c != b or b == c !=a:
        print('Isosceles')
    elif a != b != c:
        print('Escaleno')
else:
    print('Não é possível formar um triangulo!')
