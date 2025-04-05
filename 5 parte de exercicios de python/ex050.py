from datetime import date
atual=date.today().year
nascimento=int(input('Qual ano a pessoa nasceu? '))
idade=atual-nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento,idade,atual))
if idade==18:
    print('Voce tem que se alistar imediatamente!!!')
elif idade<18:
    saldo=18-idade
    print('voce nao tem 18 anos ainda.faltam {} anos para o alistamento!!'.format(saldo))
    ano=saldo+atual
    print('faltam ainda {]'.format(ano))
elif idade>18:
    saldo=idade-18
    print('voce ja deveria ter se alistado ha {} anos'.format(saldo))
    ano=atual-saldo
    print('seu alistamento foi em {}'.format(ano))
