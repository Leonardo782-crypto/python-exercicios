nota1=float(input('Qual foi sua primeria nota? '))
nota2=float(input('Qual foi sua segunda nota? '))
media=(nota1 + nota2) /2
if media<5:
    print('Sua nota foi abaixa que 5.0,seu BURRO!!!,REPROVADO')
elif media>=5 and media<=6.9:
    print('sua nota foi entre 5.0 e 6.9,voce esta de RECUPERAÇÃO!!!')
elif media>=7:
    print('Sua nota foi acima de 7.0 ou igual,parabens!!!,APROVADO')
print('a media do aluno foi de {:.1f}'.format(media))
