num=cont=soma=0
while num !=999:
    num=int(input('Digite um numero[999 para parar]:'))
    cont+=1
    soma+=num
print('Voçe digitou {} numeros e a soma entre eles é {}'.format(cont-1,soma-999))