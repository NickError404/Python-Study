# Exercício Python 090: Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.



from typing import ItemsView


alunos_média = {}

alunos_média['nome'] = str(input('Nome: '))
alunos_média['média'] = float(input(f'Média de {alunos_média["nome"]}: '))

if alunos_média['média'] >= 7.5:
    alunos_média['situação'] = 'Aprovado'
elif 5 <= alunos_média['média'] < 7:
    alunos_média['situação'] = 'Recuperação'
else:
    alunos_média['situação'] = 'Reprovado'

print(f'''
Aluno: {alunos_média["nome"]}
Média: {alunos_média["média"]}
Situação: {alunos_média["situação"]}
''')

print(f'No dicionário está assim:\n {alunos_média.items()}\n{alunos_média.keys()}\n{alunos_média.values()}')


for k, v in alunos_média.items():
    print(f'{k} está no valor de {v}')
