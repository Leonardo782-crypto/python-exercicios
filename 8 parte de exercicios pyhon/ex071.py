
sexo=str(input('Qual o seu sexo[M/F]: ')).strip().upper()[0]
while sexo not in ('MF'):
    sexo=str(input('ERRO de dados,digite novamente:')).strip().upper()[0]
print('sexo {} valido com sucesso!'.format(sexo))