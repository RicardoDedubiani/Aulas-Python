dia = int(input("Por quantos dias o carro foi alugado? "))
km = float(input("Quantos kilometros foram rodados? "))
totalAluguel = (dia*60) + (km*0.15)
print("O valor total do aluguel é de R${:.2f}. ".format(totalAluguel))
