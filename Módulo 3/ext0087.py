# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.


pessoas = list()
c = heavy = light = 0
while True:
    nome = str(input('Diga-me o seu nome: '))
    peso = int(input('Digame-me o seu peso: '))
    c += 1
    if c == 1:
        heavy = peso
        heavy_name = nome
        light = peso
        light_name = nome
    elif c >= 2:
        if peso <= light:
            light = peso
            light_name = nome
        if peso >= heavy:
            heavy = peso
            heavy_name = nome
    continuar = str(input('Deseja continuar? Y/N: '))
    if continuar in 'Nn':
        break
pessoas.append(light)
pessoas.append(light_name)
pessoas.append(heavy)
pessoas.append(heavy_name)
print(f'Pessoas mais leves {pessoas[2:]}')
print(f'Pessoas mais pesadas {pessoas[:2]}')
print(f'Quantidade de pessoas cadastradas {c}')