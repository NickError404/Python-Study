# Exercício Python 080:
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

 

dates = []

for c in range(0, 5):
    date = int(input(f'Ask {c} Enter a value: '))
    if c == 0:
        for c in range(0, 1):
            dates.append(date)
    elif c > 0:
        if date > dates[0]:
            dates.insert(0, date)
        elif date < dates[0]:
            dates.insert(1, date)
dates.reverse()
print(f'Valores: {dates}')
