# Exercício Python 109: Modifique as funções que foram criadas no desafio 107 para que elas aceitem
# um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela
# função moedas3(), desenvolvida no desafio 108.

import moedas3


s = float(input('Enter a value R$: '))

print(f'''
O valor de {s:.2f} aumentado é: {(moedas3.aumentar(s, formato=True))}
O valor de {s:.2f} reduzido é: {(moedas3.diminuir(s, formato=True))}
O valor de {s:.2f} Dobrado é: {moedas3.dobro(s, formato=True)}
O valor de {s:.2f} Dividido é: {(moedas3.metade(s, formato=True))}   
''')
