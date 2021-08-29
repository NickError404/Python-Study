# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade
# de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o
# total de gols feitos durante o campeonato.


data_game = dict()
gouls = list()

data_game['name'] = str(input('Nome do jogador: ')).strip()
jg = data_game['games'] = int(input('Quantos jogos ele participou: '))

for h in range(0, jg):
    gouls.append(int(input(f'valor do jogo {h+1}: ')))
data_game['total'] = sum(gouls)
print('='*45)
for k, v in data_game.items():
    print(f'\033[36mO valor de {k} é:\033[37m{v:>3}')
for k, v in enumerate(gouls):
    print(f'\033[36mO valor do {k+1} jogo é:\033[37m{v:>3}')
print('='*45)
