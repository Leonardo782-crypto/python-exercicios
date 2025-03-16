v=float(input('Qual a velocidade do carro atual? '))
if v >=80:
    print('Voçe sera multado por exceder o limite de 80km/h,sua multa sera de R$280')
multa=(v-80)*7
print('Voçe deve pagar uma multa de {}'.format(multa))
