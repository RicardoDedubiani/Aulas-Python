n1 = int(input('Insira um valor: '))
n2 = int(input('Insira outro valor: '))
if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
elif n1 < n2:
    print('{} é menor que {}'.format(n1, n2))
else:
    print('{} é igual a {}'.format(n1, n2))
