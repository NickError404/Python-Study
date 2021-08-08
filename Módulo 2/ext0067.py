

num = 0
t1 = 0
list = []
n = 2
t2 = 0
while num != 999:
    num = int(input('Tente um número: '))
    if num != 999:
        list.append(num)
cont = len(list)

print(f'Quantidade de números digitados: {cont}')

cc = 0
ccc = 0
while cc < cont:
    ccc += list[cc]
    cc += 1

print(f'A soma de todos os valores é {ccc}')    