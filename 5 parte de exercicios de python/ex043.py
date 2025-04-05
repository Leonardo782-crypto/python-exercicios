s=float(input('Qual é o salario do funcionario? R$ '))
if s<=1250:
    print('Voçe ganha menos do que um trabalhador médio no Brasil,tu ta fodido,o aumento é de {}'.format(s+ (s*15/100)))
else:
    print('Voçe ganha mais que um trabalhador médio,da para sobreviver,o aumento é de {}'.format(s+(s*10/100)))