velocidade = float(input('Qual é a velocidade atual? '))
if velocidade < 81:
    print('Tenha um bom dia, dirija com segurança! ')
else:
    print('Multado! Voce excedeu o limite de velocidade de 80Km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar um multa de R${:.2f}.'.format(multa))
