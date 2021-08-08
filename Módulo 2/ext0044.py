'''
Progrma de natação militar.
'''





idade = int(input('Digite sua idade, somente números: '))

mirim = 9 

infantil = 14

junior = 19

senior = 25


if idade <= mirim:
    print('Mirim')
elif idade > mirim and idade <= infantil:
    print('infantil')
elif idade > infantil and idade <= junior:
    print('junior')
elif idade > junior and idade <= senior:
    print('Senior')
elif idade > senior:
    print('Master')