dias = int(input('Quantos dias serao alugados? '))
km = float(input('Quantos km rodados? '))
pagamento=(dias * 60) + (km * 0.15)
print('O total a se paga é R${:.2f}'.format(pagamento))
