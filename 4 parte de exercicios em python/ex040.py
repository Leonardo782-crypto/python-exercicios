d=float(input('Qual a distancia da viagem em  km? '))
if d<=200:
    print('O preço da viagem curta foi de: R${} '.format(d*0.50))
else:
    print('O preço da viagem longa foi de: R${} '.format(d*0.45))
