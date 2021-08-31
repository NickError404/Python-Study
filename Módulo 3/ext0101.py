# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba 
# três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da
# função criada:     
# a) de 1 até 10, de 1 em 1       
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep

def contagem1():
    for c in range(1, 11):
        print(c, end=' | ', flush=True)
        sleep(0.5)
    print()
    print('='*45)
    for h in range(10, -2, -2):
        print(h, end=' | ', flush=True)
        sleep(0.5)
    print()

contagem1()
inicial = int(input('De: '))
final = int(input('Até: '))
jumpers = int(input('Pulando de: '))

def contagem(i, f, j):
    s = 0
    if j == 0:
        j = 1
    if i > f:
        j = -j
    elif i == f:
        print(f'\033[31mO valor inicial é {i} igual ao final {f}')
    for v in range(i, f+1, j):
        print(f'{v:^3}', end=' | ', flush=True)
        sleep(0.5)
        s += 1
        if s >= 3:
            print()
            s -= 3

contagem(inicial, final, jumpers)
