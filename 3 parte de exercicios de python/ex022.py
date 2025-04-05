import math
ca=float(input('Qual o comprimento do cateto adjacente? '))
co=float(input('Qual o comprimento do cateto oposto? '))
hi=math.hypot(ca,co)
print('a hipotenusa do dos catetos é {:.2f}'.format(hi))