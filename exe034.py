salario = float(input('Qual o seu salario: '))
if salario > 1250:
    print('A partir de agora, voce receberá um aumento de 10% e passará a ganhar R${:.2f}'.format(salario + (salario * 0.10)))
else:
    print('A partir de agora você receberá um aumento de 15% e passará  a ganhar R${:.2f}'.format(salario + (salario * 0.15)))