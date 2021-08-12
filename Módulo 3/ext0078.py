# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:

# A) Quantas vezes apareceu o valor 9.

# B) Em que posição foi digitado o primeiro valor 3.

# C) Quais foram os números pares.


tuplex = (int(input('Digite um Valor: ')),
int(input('Digite um valor: ')),
int(input('Digite um valor: ')),
int(input('Digite um valor: ')))

if 3 in tuplex:
    print(f'O primeiro valor 3 apareceu na posição {tuplex.index(3)}')
else:
    print('Não contém nenhum número 3 nesta tupla')
for n in tuplex:
    if n % 2 == 0:
        print(n, end=' ')

print(f'''
O valor 9 apareceu {tuplex.count(9)} vezes na tupla.
''')