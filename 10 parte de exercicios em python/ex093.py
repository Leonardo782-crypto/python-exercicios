
palavras=('aprender','progamar','estudar','python','borracha',
          'mamar','alguem vai ter que chorar pros mlk ri','venda')
for p in palavras:
    print(f'\nNa palvra{p.upper()} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end='')