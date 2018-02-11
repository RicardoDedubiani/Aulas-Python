from math import sin, cos, tan, radians
angulo = float(input("Insira o valor do angulo: "))
seno = sin(radians(angulo))
print("O seno do angulo de {} é {:.2f}".format(angulo, seno))
cosseno = cos(radians(angulo))
print("O cosseno do angulo de {} é {:.2}".format(angulo, cosseno))
tangente = tan(radians(angulo))
print("A tangente do angulo de {} é {:.2f}".format(angulo, tangente))
