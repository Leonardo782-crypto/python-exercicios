s1=float(input('Primeiro segmento'))
s2=float(input('Segundo segmento'))
s3=float(input('Terceiro segmento'))
if s1==s2 and s1==s3 and s2==s3:
  print('Seu triangulo é equilatero')
elif s1==s2 or s1==s3 or s2==s3:
    print('Seu triangulo é isosceles')
else:
    print('Seu triangulo é escaleno')

