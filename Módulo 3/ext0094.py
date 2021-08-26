# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados
# aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário
# em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
import operator
from time import sleep


players = {}
for p in range(0, 4):
    players[f'player{p}'] = randint(1, 8)

dict_sorted = sorted(players.items(), key=operator.itemgetter(1))
print('\033[33m=-'*45)
for k, v in dict_sorted:
    print(f'\033[32mPlayer: {k}\nPoints: {v}')
    sleep(1)
print('\033[33m=-'*45)
