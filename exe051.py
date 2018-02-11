pt = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
decimo = pt + 10 * rz
for c in range(pt, decimo, rz):
    print(c, end='-> ')
print('ACABOU')
