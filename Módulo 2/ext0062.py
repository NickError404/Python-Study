# from os import abort


# Crie um programa que leia dois valores e mostre um menu na tela:

# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos numeros
# [5] sair do programa

# seu programa devera realizar a operaçao solicitada em cada caso.


from colorama import Fore


value_1 = float(input('Digite o primeiro valor: '))
value_2 = float(input('Digite o segundo valor: '))

select = int(input((Fore.CYAN + f'''
\033[33m[1] Somar
\033[36m[2] Multiplicar
\033[33m[3] Maior
\033[36m[4] Novos Valores
\033[33m[5] Sair do Programa
''')))
if select > 5 or select < 1:
    print(Fore.RED + f'{select} não é uma opção válida!!\n tente novamente')
while select == 4 or select > 5 or select < 1:    
    if select > 5 or select < 1:
        print(Fore.RED + f'{select} não é uma opção válida!!\n tente novamente')
    value_1 = float(input('Digite o primeiro valor: '))
    value_2 = float(input('Digite o segundo valor: '))
    select = int(input((Fore.CYAN + f'''
    \033[33m[1] Somar
    \033[36m[2] Multiplicar
    \033[33m[3] Maior
    \033[36m[4] Novos Valores
    \033[33m[5] Sair do Programa
    ''')))

if select == 1:
    soma = value_1 + value_2
    print(f'A soma de todo os valores é {soma}')
elif select == 2:
    mult = value_1 * value_2
    print(f'A multiplicação de {value_1} X {value_2} é {mult}')
elif select == 3:
    if value_1 > value_2:
        print(f'{value_1} é maior que {value_1}')
    elif value_2 > value_1:
        print(f'{value_2} é maior que {value_1}')
elif select == 5:
    exit()
