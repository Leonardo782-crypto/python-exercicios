num=(int(input('Digite um numero: ')),
     int(input('Digite outro numero:')),
     int(input('Digite outro numero: ')),
     int(input('Digite outro numero:  ')))
print(f'voce digitou os valores{num}')
print(f'o numero 9 foi digitado {num.count(9)}')
if 3 in num:
 print(f'o numero 3 esta em {num.index(3)+1}')
else:
    print('o numero 3 nao foi digitado sua cahorra safada bandida')
print('os numeros pares sao  ',end='')
for n in num:
    if n % 2==0:
     print(n,end='')
