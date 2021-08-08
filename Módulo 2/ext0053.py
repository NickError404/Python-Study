value = 0
cont = 0

for c in range(1, 7):
    num = int(input(f'Digite seu {c} Valor: '))
    if num % 2 == 0:
        cont += 1
        value += num
        if cont <= 1:
            print(f'Você digitou {cont} valor par e a soma do mesmo é {value}')
        else:

            print(f'Você digitou {cont} valores pares e a soma dos mesmos é {value}')