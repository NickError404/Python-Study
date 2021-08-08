import random




n = int(input('Deseja que o computador pense de 1 a que número?: '))

num = random.randint(1, n)

adv = int(input('Adivinhe em que número o computador pensou: '))


if adv == num:
    print('Parabéns, você adivinhou em que número eu pensei')
else:
    print(f'Você errou, eu pensei no número {num}')