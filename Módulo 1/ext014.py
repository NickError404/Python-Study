




peso = float(input('\033[33mDigite quantos quilos: '))


if peso > 50:
        peso -= 50
        peso *= 4
        print(f'\033[31mPeso excedente!, você deverá pagar uma multa no total de R${peso}')
else:
    print('\033[32mVocê não excedeu o limite de peso regulamentado pelo estado!, não devera pagar nada.')

