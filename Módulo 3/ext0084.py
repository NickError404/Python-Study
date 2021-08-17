# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                  
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

dates = []
Five = False
while True:
    dates.append(int(input('Enter a value: ')))
    if 5 in dates:
        Five = True
    ask = str(input('Want a continue? Y/N: '))
    if ask in 'Nn':
        break

if Five == True:
    print('A five values was a entered')
else:
    print('A five value was not entered')

print(f'Typed Values {len(dates)}')
dates.sort(reverse=True)
print(f'Decresed Values {dates}')

