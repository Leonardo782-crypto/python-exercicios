from random import randint
c=randint(0,5)
print('Vou pensar em numero entre 0 e 5,tente advinhar...')
j=int(input('Qual numero eu pensei? '))
if j==c:
    print('Parabens voçe acertou!!!')
else:
    print('eu ganhei HAHAHAHAHAH seu lixo eu pensei em {}'.format(c))