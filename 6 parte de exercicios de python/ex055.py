peso=float(input('Qual é o seu peso? Kg'))
altura=float(input('Qual é sua altura? m'))
IMC=peso / (altura**2)
if IMC<18.5:
 print('Voçe esta abaixo do peso')
elif IMC>18.5 and IMC<25:
 print('peso ideal')
elif IMC>25 and IMC<30:
 print('sobrepeso')
elif IMC>30 and IMC<40:
 print('obesidade')
elif IMC>49:
    print('obesidade morbida')
print('O IMC dessa pessoa é de {:.1f}'.format(IMC))