# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para
# cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

jogos_inteiro = []
sorteados = []
conted = 0
c = int(input('Quantos jogos deseja gerar? '))
vx = 0
for i in range(0, c):
    while True:
        value = randint(0, 60)
        if value not in sorteados:
            sorteados.append(value)
            vx += 1
        if vx == 6:
            jogos_inteiro.append(sorteados[:])
            vx -= 6
            print(f'Sorteando: {sorteados}')
            sorteados.clear()
            break
        sleep(0.3)
print(f'Todos os valores sorteados: ')
for i in range(0, c):
    print(f'Lista {i} {jogos_inteiro[i]}', end='')
    print()
