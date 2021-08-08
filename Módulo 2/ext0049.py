#  Exercício Python 46:
#  Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
#  indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from typing import Container
import colorama
from time import sleep

print(colorama.Fore.CYAN + ('''
Iniciando Contagem Regressiva!
'''))
for cont in range(10, -1, -1):
    print(colorama.Fore.RED + f'Faltam {cont} segundos para o estouro de fogos de artifício')
    sleep(1)
    
print(colorama.Fore.CYAN + ('PIU PIU PIU PIU PIU POW POW PIU!!!!!'))
