from datetime import date
atual=date.today().year
nascimento=int(input('Qual ano voçe nasceu? '))
idade=atual-nascimento
print('O atleta tem {} anos'.format(idade))
if idade<=9:
    print('Voçe esta na categoria MIRIM')
elif idade>9 and idade <=14:
    print('Voçe esta na categoria INFANTIL')
elif idade>14 and idade <=19:
    print('Voçe esta na categoria JUNIOR')
elif idade>19 and idade <=25:
    print('Voçe esta na categoria SÉNIOR')
elif idade>25:
    print('Voçe esta na categoria MASTER')


