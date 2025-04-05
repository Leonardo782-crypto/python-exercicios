casa=float(input('Qual é o valor da casa?R$'))
salario=float(input('Quanto e o seu salario?R$'))
anos=int(input('Quantos anos de financiamento?'))
prestacao=casa/(anos*12)
minimo=salario*30/100
print('Para pagar uma casa de {:.2f} em {} anos'.format(casa,anos),end='')
print('a prestacao sera de {:.2f}'.format(prestacao))
if prestacao<=minimo:
    print('emprestimo pode ser concedido!!')
else:
    print('o empestimo nao podera ser concedido')
        