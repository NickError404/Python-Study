# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas
# # aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e
# # use algumas dessas funções.




def aumentar(date):
    r = float(input('Enter a value to be added: '))
    result = date + r
    return result

def diminuir(date):
    r = float(input('Enter a value to be removed: '))
    result = date - r
    return result

def dobro(date):
    result = date * 2
    return result

def metade(date):
    result = date / 2
    return result