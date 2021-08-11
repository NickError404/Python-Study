# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:

# A) Quantas vezes apareceu o valor 9.

# B) Em que posição foi digitado o primeiro valor 3.

# C) Quais foram os números pares.

par = 0
pares = []
tuplex = (int(input('Digite um Valor: ')),
int(input('Digite um valor: ')),
int(input('Digite um valor: ')),
int(input('Digite um valor: ')))
for c in tuplex:
    if tuplex[c] % 2 == 0:
        par += 1
        pares.append(tuplex)


print(f'''
O valor 9 apareceu {tuplex.count(9)} vezes na tupla.
O primeiro valor 3 apareceu na posição {tuplex.index(3)}
A quantidade de números pares é de {par} e eles são os números {pares}
''')