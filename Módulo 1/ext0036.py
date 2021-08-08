



salário = float(input('Digite seu salário: '))

if salário <= 1250:
    novo_salário = salário * 15 / 100
else:
    novo_salário = salário * 10 / 100

print(f'Você recebeu um reajuste de R${novo_salário:.2f}, seu salário agora é {salário+novo_salário:.2f}')