# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha
# com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.


numbers = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(0, 3):
    for c in range(0, 3):
        numbers[i][c] = int(input(f'{i} {c} Enter a value: '))
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{numbers[i][c]:^5}]', end='')
    print()
