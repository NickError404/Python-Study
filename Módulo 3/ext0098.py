# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo
# um sistema de visualização de detalhes do aproveitamento de cada jogador.



data_game = dict()
gouls = list()

while True:
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
    print(f'\033[036mAproveitamento: \033[37m{data_game["total"] / len(gouls):>3}')
    while True:
        ask = str(input('Continue? [S/N] ')).upper()
        if ask in 'SN':
            break
        else:
            print('\033[31;1mError')
    if ask in 'N':
        break
    gouls.clear()
