# Exercício Python 082:
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

dates_par = []
dates_impar = []
dates = []
while True:
    dates.append(int(input('Enter a value the be dates: ')))
    if dates[-1] % 2 == 0:
        dates_par.append(dates[-1])
    else:
        dates_impar.append(dates[-1])
    ask = ' '
    while ask not in 'YyNn':
        ask = str(input('Wanta a Continue? Y/N'))
    if ask in 'Nn':
        break
print(f'''
Total values added: {dates}
Par values: {dates_par}
Ímpar Values: {dates_impar}
''')