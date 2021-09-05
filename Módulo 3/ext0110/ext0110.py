# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e
# use algumas dessas funções.



import moeda


s = float(input('Enter a value: '))

print(f'''
Valor aumetado de {s} é: {moeda.aumentar(s)}
Valor subtraído de {s} é: {moeda.diminuir(s)}
Valor dobrado de {s} é: {moeda.dobro(s)}
A metade de {s} é: {moeda.metade(s)}
''')