import random
n1=(input('Primeiro aluno: '))
n2=(input('Segundo aluno '))
n3=(input('Terceiro aluno: '))
n4=(input('Quarto aluno: '))
alunos=[n1,n2,n3,n4]
random.shuffle(alunos)
print('A ordem da apresentação será {}'.format(alunos))