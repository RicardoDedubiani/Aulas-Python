from datetime import date
atual = date.today().year
sexo = int(input('''Voce é homem ou mulher?
[ 1 ] HOMEM
[ 2 } MULHER'''))
nasc = int(input('Que ano você nasceu? '))
idade = atual - nasc
print('Quem nasceu em {} faz {} anos em {}.'.format(nasc, idade, atual))
if sexo == 2:
    print('Você está liberada do alistamento militar!')
elif idade == 18:
    print('Voce tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce deveria ter se alistado a {} anos!'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
