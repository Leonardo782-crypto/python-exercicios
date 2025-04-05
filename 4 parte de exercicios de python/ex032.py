frase=str(input('Digite uma frase '))
Letra=frase.upper().strip()
maiuscula='A'
print('A letra A apareceu {} vezes na frase'.format(Letra.count(maiuscula)))
print('A primeira letra A apareceu ns posição{}'.format(frase.find(maiuscula)+1))
print('A última letra A apareceu na posição{}'.format(frase.rfind(maiuscula)+1))
