p1=float(input('Primeiro valor: '))
p2=float(input('Segundo valor: '))
opcao=0
while opcao!=5:
    print('''    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos numeros
    [5]sair do progama''')
    opcao=int(input('Qual sua opção? '))
    if opcao==1:
        soma=p1+p2
        print('A soma entre {} e {} é de {}'.format(p1,p2,soma))
    elif opcao==2:
        multiplicar=p1*p2
        print('A multiplicaçao entre {} e {} é de {}'.format(p1,p2,multiplicar))
    elif opcao==3:
        if p1>p2:
            maior=p1
        else:
            maior=p2
        print('O maior numero sera {}'.format(maior))
    elif opcao==4:
        print('Informe os numeros novamente!!!')
        p1=float(input('Primeiro valor: '))
        p2=float(input('Segundo valor: '))
print('FIM do progama')