distancia = float(input('Qual a distancia da viagem? '))
if distancia > 200:
    print('A viagem possui mais de 200 km e custará: R${:.2f}'.format(distancia * 0.45))
    print('Voce terá um desconto por viajar mais de 200 km')
else:
    print('A viagem possui até 200 km e custará: R${:.2f}'.format(distancia * 0.50))
    print('Essa distancia não da direito a desconto')