# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.
from random import randint


stack = True
cont = 0
while stack == True:
    player = int(input('Enter a value: '))
    select = str(input('I/P: ')).strip().lower()[0]
    pc = randint(0, 11)
    total = pc + player
    if total % 2 == 0 and select in 'p':
        cont += 1
        print('Player Wins')
    elif total % 2 == 1 and select in 'i':
        print('Player Wins')
        cont += 1
    else:
        print('Pc Wins')
        stack = False

print(f'Você selecionou {select}')
print(f'O valor total é {total}')
print(f'Você ganhou {cont} vezes consecutivas')

