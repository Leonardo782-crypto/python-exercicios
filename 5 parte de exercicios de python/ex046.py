c=float(input('Qual é o valor da casa?R$'))
s=float(input('Qual o seu sálario?R$ '))
a=int(input('Em Quantos anos voçe vai pagar?'))
pm=c/(a*12)
if pm>(s*30/100):
 print('O valor da casa passa de 30% da sua casa,entao nao sera possivel')
else:
    print('O valor nao ultrapassa 30% do salario')
print('A prestaçao sera de {:.2f}'.format(pm))