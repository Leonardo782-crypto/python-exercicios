preco=float(input('Qual e o preco do produto? R$ '))
novo=preco - (preco*5/100)
print('o produto que custava R${},na promocao com desconto custa R${}'.format(preco,novo))