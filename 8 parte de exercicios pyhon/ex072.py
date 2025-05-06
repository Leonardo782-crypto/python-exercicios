from random import randint
computador=randint(0,10)
print('''Sou seu computador...
acabei de pensar em um numero entre 0 e 10
sera que voçe consegue advinhar?''')
acertou=False
palpites=0
while not acertou:
    jogador=int(input('Qual e o seu palpite?'))
    palpites+=1
    if jogador==computador:
        acertou=True
    else:
        if jogador>computador:
            print('Hmmm voçe e bem burrinho ne,tenta menos ai o animal')
        elif jogador<computador:
           print('Hmmmm voçe e muito burro pqp,tenta MAISSSS')
print('Graças a Deus acertou pqp,voçe acertou com um total de {} tentativas'.format(palpites))
