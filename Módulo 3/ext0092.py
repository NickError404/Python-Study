# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde
# tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita
# que o usuário possa mostrar as notas de cada aluno individualmente.


alunos_notas = [[]]
conti = True
while conti == True:
    alunos_notas[0].append(str(input('\033[33mDigite um nome: ')))
    nota1 = (float(input('Digite sua nota: ')))
    nota2 = (float(input('Digite sua nota: ')))
    alunos_notas.append([[nota1], [nota2], [((nota1+nota2)/2)]])
    ask = str(input('Continue? Y/N: '))
    if ask in 'Yy':
        conti = True
    elif ask in 'Nn':
        conti = False
for c, i in enumerate(alunos_notas[0]):
    print(f'Aluno: {alunos_notas[0][c]}\nMédia: {alunos_notas[3][c]}')
while conti == False:
    pos = ' '
    while pos not in alunos_notas[0]:
        pos = str(input('Se deseja ver as notas de algum aluno em específico, digite o nome do aluno correspondente: '))
        if pos in alunos_notas[0]:
            index = alunos_notas[0].index(pos)
        else:
            print('\033[31mAluno não encontrado: tente novamente!\033[33m')
    print('='*35)
    print(f'Aluno: {alunos_notas[0][index]}\nNota_1: {alunos_notas[1][index]}\nNota_2 {alunos_notas[2][index]}')
    print('='*35)
    ask = str(input('Deseja ver a nota de mais a algum aluno? Y/N '))
    if ask in 'Yy':
        conti = False
    elif ask in 'nn':
        conti = True
