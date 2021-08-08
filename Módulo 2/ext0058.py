

maior = 0
menor = 0

for c in range(0, 6):
    peso = float(input('Seu peso: '))
    if c == 0:
        maior = peso
        menor = peso
    elif c != 0:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'{maior} Foi o maior peso\n {menor} foi o menor peso')
    