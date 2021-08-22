# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.


total = [[], []]
for i in range(0, 7):
    num = int(input('Enter a value: '))
    if num % 2 == 0:
        total[0].append(num)
    else:
        total[1].append(num)


total[0].sort()
total[1].sort()
print(f'Valores pares:{total[0]} \nValores impares: {total[1]}')


