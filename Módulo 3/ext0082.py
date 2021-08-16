# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.



value = []
conti = True
date = 0
cont = 0

while conti == True:
    date = int(input(f'\033[33mAsk {cont} Enter a value: '))
    if date not in value:
        value.append(date)
    else:
        print('\033[31mThis one a value not add in date :/\033[033m')
    cont += 1
    continue_ask = ' '
    while continue_ask not in 'YyNn':
        continue_ask = str(input('Want a continue? Y/N: '))
        if continue_ask.lower() == 'y':
            conti = True
        elif continue_ask.lower() == 'n':
            conti = False
value.sort()
print(f'{value}', end=' ')



