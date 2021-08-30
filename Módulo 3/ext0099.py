# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as
# dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.



def media(L, C):
    M = L * C
    print(f'\033[32m {L} de lado e {C} de comprimento convertidos em M²:\033[35m {M:.0f}m²')


lado = float(input('\033[33mDimensões do lado: '))
comprimento = float(input('\033[33mDimensões do comprimento: '))
media(lado, comprimento)

