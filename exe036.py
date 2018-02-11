casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))
prestaçao = casa / (anos * 12)
salarioBom = (salario * 0.30)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestaçao))
if prestaçao <= salarioBom:
    print('EMPRÉSTIMO APROVADO!')
else:
    print('EMPRÉSTIMO NEGADO!')
    print('Nessas condições, você poderá ter apenas um financiamento de R${:.2f}'.format(salarioBom))
