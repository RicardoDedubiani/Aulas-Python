num = int(input('Digite um número para ver a tabuada: '))
for c in range(1, 21):
    print('{} x {:2} = {}'.format(num, c, c * num))
