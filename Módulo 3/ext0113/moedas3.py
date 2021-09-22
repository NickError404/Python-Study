


def aumentar(date=0, formato=False):
    r = float(input('Enter a value to be added %: '))
    result = (date + (date * r / 100))
    return result if formato is False else moeda(result)

def diminuir(date=0, formato=False):
    r = float(input('Enter a value to be removed %: '))
    result = date - (date * r / 100)
    return result if formato is False else moeda(result)

def dobro(date=0, formato=False):
    result = date * 2
    return result if formato is False else moeda(result)

def metade(date=0, formato=False):
    result = date / 2
    return result if not formato else moeda(result)

def moeda(date=0, moeda = 'R$', format=False):
    return f'{moeda}{date:>.2f}'.replace('.', ',')
