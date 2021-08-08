import random
import re
from typing_extensions import IntVar
from colorama import Back, Style, Fore
from random import choice

def jokepô():
    select = input(Fore.CYAN + Style.BRIGHT + '''Selecione dentre 
    Pedra
    Papel
    Tesoura: ''')

    if select.lower() == 'pedra':
        select = 0
    elif select.lower() == 'papel':
        select = 1
    elif select.lower() == 'tesoura':
        select = 2
    elif select.lower() == '/exit':
        exit()
    else:
        print(Fore.RED + 'Opção Inválida!')

    joke = ['pedra', 'papel', 'tesoura']
    jogador = joke[int(select)]
    pc = choice(joke)

    print(Fore.WHITE + Back.BLACK + Style.BRIGHT + f'Você selecionou {jogador} e o Computador selecinou {pc}')

    if jogador.lower() == 'pedra' and pc.lower() == 'tesoura':
        print(Fore.GREEN + 'Você ganhou!')
    elif jogador.lower() == 'tesoura' and pc.lower() == 'papel':
        print(Fore.GREEN + 'Você ganhou!')
    elif jogador.lower() == 'papel' and pc.lower() == 'pedra':
        print(Fore.GREEN + 'Você ganhou!')
    elif jogador == pc:
        print(Fore.YELLOW + 'Empate :/')
    else:
        print(Fore.RED + 'Você Perdeu!!!!')
    return select


jokepô()
