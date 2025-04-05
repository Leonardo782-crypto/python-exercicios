num=int(input('digite um numero inteiro  '))
print('''Escolha  uma das bases a seguir para transformar em :
[1]converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXAL''')
opcao=int(input('Qual sua opcao: '))
if opcao==1:
    print('O numero convertido para binario é {}'.format(bin(num)[2:]))
elif opcao==2:
    print('O numero convertido para octal é {}'.format(oct(num)[2:]))
elif opcao ==3:
    print('O numero convertido para hexal é {}'.format(hex(num)[2:]))
else:
    print('opcao invalida tente novamente!!!')