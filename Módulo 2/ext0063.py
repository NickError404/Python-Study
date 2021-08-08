# faça um programa que leia um numero qualquer
# e mostre o seu fatorial.

# Ex:
# 5! = 5x4x3x2x1 = 120

fatorial = int(input('Fatorial '))
c = fatorial
f = 1

print(f'Calculando {fatorial}...')
while c > 0:
    print(f' x ' if c > 1 else' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
