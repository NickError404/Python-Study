


km = float(input('Digite a kilometragem: '))


if km <= 200:
    print(f'O total a pagar pela viagem é R${0.50*km}')

elif km > 200:
    print(f'Você recebeu o desconto de 5 centavos por Km/h pela quimetragem acima de 200,\n então você pagará um total de R${0.45*km}')


