# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o
# dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da
# idade, com quantos anos a pessoa vai se aposentar.

import datetime

dictctps = {}
year = datetime.date.today().year

dictctps['name'] = str(input('Enter your name: ')).strip()
dictctps['Birth'] = int(input('Enter your Birth Date: '))
dictctps['ctps'] = int(input('Your CTPS: '))
if dictctps['ctps'] != 0:
    dictctps['work'] = int(input('Year Of Hiring: '))
    wage = float(input('Wage R$: '))
print(dictctps.items())

for k, v in dictctps.items():
    if v == dictctps['Birth']:
        age = (v - year) * -1
        print(f'{k} tem o valor de {(age)}')
    else:
        print(f'{k} tem o valor de {v}')
retirement = (age - 65) * -1
print(f'Aposentadoria daqui: {retirement} anos')
