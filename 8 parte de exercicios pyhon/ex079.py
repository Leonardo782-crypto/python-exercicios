resp='S'
soma=quant=media=0
while resp in 'Ss':
    num=int(input('Digite um numero:'))
    soma+=num
    quant+=1
    if quant==1:
        maior=menor=num
    else:
        if num>maior:
            maior=num
        if num<menor:
            menor=num
    resp=str(input('Voçe quer continuar[S/N]? ')).upper().strip()[0]
media=soma/quant
print('Voçe digitou {} numeros e a media foi de {}'.format(quant,media))
print('O maior valor obtido foi {} e menor foi de {}'.format(maior,menor))