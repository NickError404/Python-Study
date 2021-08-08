# maior_de_idade = 0
# menor_de_idade = 0
# for i in range(1, 8):
#     name = int(input(f'Quest {i} Sua idade: '))
#     if name >= 18:
#         # print(f'{name} é maior de idade')
#         maior_de_idade += 1

#     elif name < 18:
#         # print(f'{name} é menor de idade')
#         menor_de_idade += 1
# print(f'Ao total são {maior_de_idade} pessoas maiores de idade\n e {menor_de_idade} pessoas menores de idade')

from datetime import date


data = date.today().year
maior = 0 
menor = 0

for i in range(1, 8):
    idade = int(input('Em que ano você nasceu: '))
    sub_idade = idade - data
    converter = sub_idade * -1
    if converter < 18:
        menor += 1
    elif converter >= 18:
        maior += 1
print(f'de maior {maior}\n de menor {menor}')