from colorama import Fore, Back, Style
tabu = int(input(Fore.CYAN + 'Digite um valor: '))

for tabuada in range(1, 11):
    print(Fore.GREEN + f'{tabu} X {tabuada} é {tabu * tabuada}')