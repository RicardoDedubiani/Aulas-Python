salario = float(input('Qual é o seu salário? R$ '))
aumento = salario*0.15
print('Levando em consideração que o seu salário é de R$ {:.2f}, com um aumento de 15%, você passará a ganhar R$ {:.2f} '.format(salario, salario+aumento))
