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

