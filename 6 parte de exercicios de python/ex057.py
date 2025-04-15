from random import randint
from time import sleep

itens=('Pedra','Papel','Tesoura')
computador=randint(0,2)
print('''escolhe uma opção:
[0]PEDRA
[1]PAPEL
[2]TESOURA''')
jogador=int(input('qual e a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(2)
print('PO!!!')
print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
if computador ==0:
    if jogador==0:
     print('EMPATE')
    elif jogador==1:
        print('VOÇE GANHOU AEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
    elif jogador==2:
        print('VOÇE PERDEU HAHAHAHAHAHAAH SEU RUIM')
    else:
        print('JOGADA INVALIDA')
elif computador==1:
    if jogador == 0:
        print('VOÇE PERDEU,VOÇE É MUITO RUIMMMMMMMMM+')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOÇE GANHOU AEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
    else:
        print('JOGADA INVALIDA')
elif computador==2:
    if jogador == 0:
         print('VOÇE GANHOU AEEEEEEEEEEEEEEEEEE')
    elif jogador == 1:
         print('VOÇE PERDEU HAAAHAHAHAHAHAHAHAHAAHHAAHAHAHAHAA')
    elif jogador == 2:
         print('EMPATE')
    else:
        print('JOGADA INVALIDA')