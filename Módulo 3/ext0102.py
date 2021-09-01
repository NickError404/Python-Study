# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba
# vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer
# qual deles é o maior.

from random import randint

def maior(lsd):
    higher_list = max(lsd)
    higher_value = max(higher_list)
    for l in lsd:
        print(f'Listas {l}')
    print(f'Maior lista: {higher_list}')
    print(f'Maior valor dentre todas as listas: {higher_value}')

numCl = list()
num = list()
vx = int(input('Gerar quantas listas?: '))
for c in range(0, vx):
    for h in range(0, 7):
        numCl.append(randint(0, 100))
    num.append(numCl[:])
    numCl.clear()
maior(num)
