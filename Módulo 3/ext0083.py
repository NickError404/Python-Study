# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

dates = []

for c in range(0, 5):
    n = int(input(f'ASK {c} Enter a value: '))
    if c == 0 or n > dates[-1]:
        dates.append(n)
        print('Adicionado')
    else:
        pos = 0
        while pos < len(dates):
            if n <= dates[pos]:
                dates.insert(pos, n)
                print('Inserido')
                break
            pos += 1
print('=-' * 30)
print(f'Os valores digitados são {dates}')