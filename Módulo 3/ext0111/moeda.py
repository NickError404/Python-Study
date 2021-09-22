# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas
# # aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e
# # use algumas dessas funções.


def aumentar(date=0):
    r = float(input('Enter a value to be added %: '))
    result = (date + (date * r / 100))
    return result

def diminuir(date=0):
    r = float(input('Enter a value to be removed %: '))
    result = date - (date * r / 100)
    return result

def dobro(date=0):
    result = date * 2
    return result

def metade(date=0):
    result = date / 2,  
    return result

