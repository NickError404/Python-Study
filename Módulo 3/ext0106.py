# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois
# parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser
# capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado
# corretamente.


jogador = str(input('Nome do jogador: ')).strip()
gols = input('Digite a quantidade de gols: ')
if gols.isnumeric():
    g = int(gols)
else:
    gols = 0

def ficha(nm='', gl=0):
    if nm == '':
        print('O nome não foi especificado: ')
    else:
        print(f'Nome: {nm}')
    if gl == 0:
        print('A quantidade de gols não foi especificada.')
    else:
        print(f'Gols: {gl}')

ficha(jogador, gols)