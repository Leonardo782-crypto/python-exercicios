from random import randint
v=0
while True:
    jogador=int(input('Digite um valor: '))
    computador=randint(0,10)
    total=jogador+computador
    tipo=''
    while tipo not in 'PpIi':
        tipo=str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print(f'Voçe jogou {jogador}e o computador jogou {computador}.total foi {total}')
    if tipo=='P':
        if total%2==0:
            print('Voçê VENCEU CAHORRA!!!')
            v+=1
        else:
            print('VOCE PERDEU KKKKKKKKKKKKKKKKKKKKKKK MUITO RUIM')
            break
print(f'voce venceu {v}vezes')

