# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

larger_num = 0
lower_num = 0
num = []
tuple_num = ()
for c in range(0, 5):
    n = randint(0, 1000)
    if n > larger_num:
        larger_num = n
    if c == 0:
        lower_num = n
    elif c != 0:
        if n < lower_num:
            lower_num = n
    num.append(n)
    tuple_num = num

cont = len(tuple_num)

for c in range(0, c+1):
    print(tuple_num[c], end=' ')

print(f'''
O maior número da Tupla é {larger_num}
O menor número da Tupla é {lower_num}
''')


from random import randint


num = (randint(0, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(10, 1000), randint(9, 999))

for n in num:
    print(f'{n}', end=' ')
print(f'\nO maior valor da tupla foi {max(num)}')
print(f'O maior valor da tupla foi {min(num)}')