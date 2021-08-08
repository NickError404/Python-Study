valor_da_hora = float(input('\033[7mDigite quanto você ganha por hora no seu trabalho: '))

horas_trabalhadas = float(input('\033[7mDigite quantas horas você trabalha por dia: '))

result = valor_da_hora * (horas_trabalhadas * 30)


print(f'\033[1;32mO seu salário esperado neste mês é em volta de R${result}')