# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.


lista = ('Lápis', 2.50,
         'Borracha', 4.55,
         'Pipa', 2,50,
         'Bicicleta', 5.55,
         'TechBusca', 255.00,
         'ProBusca', 155.00,
         'BotNet Service', 55.55,
         'Yasamuja', 100.00,
         'KaliService', 233.99)

def linhas():
    print('=-'*20)

linhas()
print('{:=^40}'.format('Lista de Compras'))
for c in lista:
    print('{:^40}'.format(c))
linhas()
