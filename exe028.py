from random import randint
computador = randint(0, 5)
print('-=-'*20)
print('  Vou pensar em um número de 0 a 5... Tente adivinhar! ')
print('-=-'*20)
jogador = int(input("Em que numero eu pensei? "))
if jogador == computador:
    print("Parabens, voce venceu!")
else:
    print("Voce errou! Pensei no numero {}".format(computador))
