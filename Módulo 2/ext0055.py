
num = int(input('Enter a number: '))
tot = 0
for c in range(1 , num + 1):

    if num % c == 0:
        tot += 1

if tot == 2:
    print(f'{num} é um número primo')
else:
    print(f'Não é um número primo, portant ele é divisivel {tot} vezes')