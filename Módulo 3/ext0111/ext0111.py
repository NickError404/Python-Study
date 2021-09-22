
from utilidadesCEV import moedas


s = float(input('Enter a value R$: '))

print(f'''
O valor de {s:.2f} aumentado é: {moedas.aumentar(s)}
O valor de {s:.2f} reduzido é: {moedas.diminuir(s)}
O valor de {s:.2f} Dobrado é: {moedas.dobro(s)}
O valor de {s:.2f} Dividido é: {moedas.metade(s)}
''')
