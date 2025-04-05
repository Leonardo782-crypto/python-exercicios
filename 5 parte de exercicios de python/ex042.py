n1=float(input('Dia o primeiro numero: '))
n2=float(input('Diga o segundo numero: '))
n3=float(input('Diga o terceiro numero: '))
menor=n1
if n2<n1 and n2<n3:
 menor=n2
 if n3<n1 and n3<n2:
  menor=n3
maior=n1
if n2>n1 and n2>n3:
    maior=n2
if n3>n1 and n3>n2:
    maior=n3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))