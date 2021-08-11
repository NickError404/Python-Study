# Exercício Python 72:
# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo
# por extenso.
print('{:=^40}'.format('CONVERSOR DE NÚMEROS POR EXTENSO!'))
while True:
    select = int(input('Digite um número de 0 a 20: '))
    if 0 <= select <= 20:
        break
por_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
'Cinco', 'Seis', 'Sete', 'Oito',
'Nove', 'Dez', 'Onze', 'Doze',
'Treze', 'Catorze', 'Quinze',
'Dezeseis', 'Dezessete', 'Dezoito',
'Dezenove', 'Vinte')
print(f'{por_extenso[select]}')
    