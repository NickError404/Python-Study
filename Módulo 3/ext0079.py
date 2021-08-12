# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.


lista = ('Lapís', 2.99,
'Caneta', 5.80,
'Pipa', 5.80,
'Avião', 555.000,
'Taxa_Selic', 5.77,
'Kent Cigar', 12.99)

print('{:=^45}'.format('Lista de Compras'))
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<35}', end='')
    else:
        print(f'R${lista[pos]:.>3.2f}')
print('-' * 45)