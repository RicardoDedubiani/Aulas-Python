n1 = float(input('PRIMEIRA NOTA: '))
n2 = float(input('SEGUNDA NOTA: '))
media = (n1 + n2) / 2
print('A média do aluno é {}.'.format(media))
if media < 5:
    print('O aluno está reprovado')
elif 7 > media >= 5:
    print('O aluno está de recuperação')
elif media >= 7:
    print('O aluno está aprovado')
