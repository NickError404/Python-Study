
soma = 0
cont = 0
for mult_3 in range(1, 501, 2):
    if mult_3 % 3 == 0:
        cont += 1
        soma += mult_3
print(f'A soma de todos os {cont} valores solicitados é {soma}')
