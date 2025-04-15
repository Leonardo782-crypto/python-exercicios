s1=float(input('Primeiro segmento: '))
s2=float(input('Segundo segmento: '))
s3=float(input('Terceiro segmento: '))
if s1<s2+s3 and s2<s1+s3 and s3<s1+s2:
    print('Os segmentos podem formar um TRIANGULO ',end='')
    if s1==s2==s3:
      print('EQUILATERO')
    elif s1!=s2 !=s3!=s1:
      print('ESCALENO')
    else:
      print('ISOSCELES')
else:
    print('Os angulos acima nao podem formar um triangulo')



