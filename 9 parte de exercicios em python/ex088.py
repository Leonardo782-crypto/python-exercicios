cont=('zero','um','dois','tres','quatro','cinco','seis'
      ,'sete','oito','nove','dez','onze','doze','treze','catorze',
      'quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
while True:
 num=int(input('Digite um numero de 1 ate 20: '))
 if 0<=num<=20:
     break
 print('TENTE NOVAMENTE')
print(f'Voçe digitou o numero {cont[num]}')
