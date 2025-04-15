forma=float(input('dinheiro total: R$ '))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro /cheque
[2] à vista cartão
[3] 2x no cartão 
[4] 3x ou mais na cartão''')
opcao=int(input('Qual sua opção: '))
if opcao==1:
 dinheiro=(forma * 10 /100)
 print('o preço a vista no dinheiro é {:.2f}'.format(dinheiro))
elif opcao==2:
    dinheiro=(forma *5/100)
    print('O preço a vista no cartão é {:.2f}'.format(dinheiro))
elif opcao==3:
    dinheiro=(forma/2)
    print('O preço no cartão em 2 vezes é {:.2f}'.format(dinheiro))
    print('Voçe pagara em dois meses o valor!!!')
elif opcao==4:
    dinheiro=forma + (forma*20/100)
    totalparc=int(input('Quantas parcelas sera? '))
    dinheirofinal=dinheiro/totalparc
    print('O preço sera {:.2f}R$ em {} parcelas'.format(dinheirofinal,totalparc))
else:
    print('algo foi digitado incorretamente,seu lixo')