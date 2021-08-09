# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
# vai informar quantas cédulas de cada valor serão entregues. OBS:

# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
from colorama import Fore, Style

print(Fore.RED + '=-'*20)
print(Style.DIM + Fore.CYAN + 'SEC PEGASUS')
print(Fore.RED + '=-'*20)

price = int(input('Quantos deseja sacar: '))
value = price
tigre = mico = beija_flor = papagaio = 0
while value != 0:
    while value >= 1 and value < 10:
        beija_flor += 1
        value -= 1
    while value > 1 and value < 20:
        papagaio += 1
        value -= 10
    while value > 10 and value < 50:
        mico += 1
        value -= 20
    while value >= 50:
        tigre += 1
        value -= 50
print('=-' * 20)
print(f'''
NOTAS DE 50: {tigre} somando {50 * tigre} em notas
NOTAS DE 20: {mico} somando {20 * mico} em notas
NOTAS DE 10: {papagaio} somando {10 * papagaio} em notas
NOTAS DE 1: {beija_flor} somando {1 * beija_flor} em notas
TOTAL: {price}
''')
print('=-' * 20)
