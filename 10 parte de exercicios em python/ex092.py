lista=('Lápis',1.75,
       'Borracha',2,
       'Caderno',15.90,
        'estojo',25,
       'transferidor',4.20,
       'Compasso',9.99,
       'Mochila',120.32,
        'canetas',22.30,
        'Livros',34.90,)
for pos in range(0,len(lista)):
    if pos % 2==0:
        print(f'{lista[pos]:.<30}',end='')
    else:
        print(f'R${lista[pos]:>7.2f}')