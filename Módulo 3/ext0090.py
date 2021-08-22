# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:   
# A) A soma de todos os valores pares digitados.          
# B) A soma dos valores da terceira coluna.    
# C) O maior valor da segunda linha.

numbers = [[0,0,0], [0,0,0], [0,0,0]]
par = []
total = 0
segunda_coluna = 0
maior_valor_segunda_coluna = 0

for i in range(0, 3):
    for c in range(0, 3):
        numbers[i][c] = int(input(f'{i} {c} Enter a value: '))
        if numbers[i][c] % 2 == 0:
            total += numbers[i][c]
        if c == 2:
            segunda_coluna += numbers[i][c]
        if i == 1:
            if c == 0 and i == 1:
                maior_valor_segunda_coluna = numbers[i][c]
            elif c > 1 and i == 1:
                if numbers[i][c] > maior_valor_segunda_coluna:
                    maior_valor_segunda_coluna = numbers[i][c]

for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{numbers[i][c]:^5}]', end='')
    print()

print(f'A soma de todos os valores pares {total}')
print(f'A soma de todos os valores da terceira coluna é {segunda_coluna}')
print(f'O maior valor da segunda linha é {maior_valor_segunda_coluna}')
