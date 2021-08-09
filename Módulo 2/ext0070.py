# Exercício Python 67: Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for
# negativo.

while True:
    value = int(input('Enter a value: '))
    if value <= 0:
        break
    print('=-' * 10)
    for c in range(1, 11):
        print(f'{value} X {c} = {value * c}')
    print('=-' * 10)
print('\033[31mBREAK')