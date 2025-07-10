primeiro=int(input('Qual o primeiro termo? '))
razao=int(input('Razao da PA: '))
termo=primeiro
cont=1
total=0
mais=10
while mais !=0:
    total=total + mais
    while cont<=total:
        print('{},'.format(termo),end='')
        termo+=razao
        cont+=1
    print('PAUSA!!!')
    mais=int(input('Quantos termos voçe quer mostrar a mais? '))
print('O processo foi finalizado com {}'.format(total))