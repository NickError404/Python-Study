a = int(input('Digite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))

if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < b and c < a:
    menor = c

print(f'O menor é {menor}')

if a > b and a > c:
    maior = a
if b > a and a > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O maior é {maior}')