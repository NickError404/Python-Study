# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias
# notas de alunos e vai retornar um dicionário com as seguintes informações:

# – Quantidade de notas   
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

result = dict()
def nota():
    notas = list()
    conti = False
    while conti == False:
        notas.append(float(input('Coloque uma nota: ')))
        ask = ' '
        while ask not in 'YyNn':
            ask = str(input('Deseja continuar: [Y/N] '))
        if ask in 'Yy':
            conti = False
        else:
            conti = True
    s = sum(notas)
    q = len(notas)
    ma = max(notas)
    mi = min(notas)
    me = s / q
    result['Todas as notas'] = s
    result['Quantidade de notas registradas'] = q
    result['Maior Nota'] = ma
    result['Menor Nota'] = mi
    result['Média Nota'] = me
    opcional = ' '
    while opcional not in 'YyNn':
        opcional = str(input('Deseja ver os status opcionais? [Y/N] ')).strip()[0]
    if opcional in 'Yy':
        if me < 5:
            result['Situação'] = 'Reprovado'
        elif 5 < me <7.5:
            result['Situação'] = 'Recuperação'
        elif me >= 7.5:
            result['Situação'] = 'Aprovado'
    return result
nota()
for k, v in result.items():
    print(f'O valor de {k} é {v}')
