maior=0
menor=0
num=list()
for c in range(0,5):
    num.append(int(input(f'Digite um valor{c}: ')))
    if c==0:
        maior=menor=num[c]
    else:
        if num[c]>maior:
            maior=num[c]
        if num[c]<menor:
            menor=num[c]
print(f'Voçe digitou os valores {num}')
print(f'O maior valor foi {maior} e esta na posição ',end='')
for c,n in enumerate(num):
    if n==maior:
        print(f'{c}...',end='')

print(f'O menor valor digitado foi {menor} e esta na posição ',end='')
for c,n in enumerate(num):
    if n==menor:
        print(f'{c}...',end='')


