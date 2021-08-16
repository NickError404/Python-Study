# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

date = []
maximum = minimum = 0
for c in range(0, 5):
    date.append(int(input('Enter a value: ')))
    if c == 0:
        maximum = minimum = date[c]
    else:
        if date[c] > maximum:
            maximum = date[c]
        if date[c] < minimum:
            minimum = date[c]

print(f'Os valores digitados {date}')
print(f'O maior valor digitado foi {maximum}', end=' ')
for i, v in enumerate(date):
    if v == maximum:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {minimum}', end=' ')    
for i, v in enumerate(date):
    if v == minimum:
        print(f'{i}...', end='')
