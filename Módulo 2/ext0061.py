# melhore o jogo do DESAFIO 0028 onde o computador vai "pensar" em um numero entre 0 e 10
# so que agora o jogador vai tentar adivinhar ate acertar,
# mostrando no final quantos palpites foram necessarios para vencer


from random import randint
import time
from typing import ForwardRef
from colorama import Fore, Back, Style
from time import sleep

print(Fore.CYAN + '''
Computador que pensa em números, HAHAHAHAHAHAHAHA
''')
sleep(1)
jogador = int(input('Adivinhe que número o computador vai pensar, de 1 a 10: '))
while jogador > 10 or jogador < 0:
    print(Fore.RED + f'Digite um valor válido {jogador} não é um número entre 0 a 10')
    jogador = int(input('Adivinhe que número o computador vai pensar, de 1 a 10: '))
pc = randint(0, 10)
print(Fore.LIGHTWHITE_EX + 'Processando...')
sleep(2)
while pc != jogador:
    print(Fore.RED + 'Você não adivinhou o número correto')
    print(Fore.RED + f'O computador pensou {pc} e você chutou {jogador}')
    jogador = int(input(Fore.YELLOW + 'Tente novamente!: '))
    while jogador > 10 or jogador < 0:
        print(Fore.RED + f'Digite um valor válido {jogador} não é um número entre 0 a 10')
        jogador = int(input('Adivinhe que número o computador vai pensar, de 1 a 10: '))
    print(Fore.WHITE + 'Processando...')
    sleep(2)
    pc = randint(0, 10)
print(Fore.GREEN + f'Parabéns, você acertou:\n Computador {pc}\n Jogador {jogador}')