# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais

# – ISÓSCELES: dois lados iguais, um diferente

# – ESCALENO: todos os lados diferentes

lado_1 = float(input('Digite o primeiro valor:'))
lado_2 = float(input('Digite o segundo valor: '))
lado_3 = float(input('Digite o terceiro valor: '))

if lado_1 < lado_2 + lado_3 and lado_2 < lado_1 + lado_3 and lado_3 < lado_2 + lado_1:
    print('Os segmentos a seguir podem formar um formato ', end='')
    if lado_1 == lado_2 == lado_3:
        print('\033[32mEquilátero')
    elif lado_1 != lado_2 != lado_3 != lado_1:
        print('\033[32mEscaleno')
    else:
        print('\033[32mIsóceles')
else:
    print('\033[31mOs segmentos a cima não podem formar um triângulo.')