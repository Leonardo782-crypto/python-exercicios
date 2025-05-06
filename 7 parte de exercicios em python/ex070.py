somaidade=0
mediaidade=0
maioridadehomem=0
for p in range(1,5):
    nome=str(input('Qual o seu nome? ')).strip()
    idade=int(input('Qual a sua idade? '))
    sexo=str(input('Qual seu sexo [M/F]? ')).strip()
    somaidade+=idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'Mm' and idade>maioridadehomem:
        maioridadehomem=idade
        nomevelho=nome
mediaidade=somaidade/4
print('A media idade do grupo é de {} anos '.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomevelho))