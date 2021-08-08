




km = float(input('Quantos quilometros seu carro estava: '))



if km > 80:
    print('Você ultrapassou o limite permitido')
    print(f'Sua kilometragem excedente foi de Km/h{km-80}, você deve pagar uma multa no total de R$:{(km-80) * 7}')
elif km <= 70:
    print('você não excedeu o limite permitido! :)')