totp=totmil=menor=cont=0
barato=' '
while True:
    p=str(input('Qual o nome do produto: '))
    v=float(input('Qual o valor dele:R$'))
    cont=+1
    totp=+v
    if v > 1000:
        totmil=+1
    if cont ==1:
        menor=v
    else:
        if v<menor:
            menor=v
            barato=p
    resp=' '
    while resp not in 'SN':
        resp=str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if resp=='N':
        break
print('FIM DO PROGAMA CACHORRA!!!')
print(f'o valor total dos produtos foram {totp}')
print(f'apenas {totmil}custam mais de 1000 real su piranha')
print(f'ta aqui o preço dessa coisa dificil de fazer(o mais barato0{barato}')