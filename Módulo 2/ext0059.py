# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, 
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
tot = 0
mais_velho_idade = 0
mulher_menor_20 = 0
mulheres = 0
homens = 0

for c in range(1, 5):
    print(f'''\033[33mPessoa {c}''')
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo H para homem e M para mulher: ')).strip()
    tot += idade
    if c == 1:
        mais_velho_idade = idade
    elif c != 1:
        if idade > mais_velho_idade and sexo == 'h':
            mais_velho_idade = idade
            nome_mais_velho = nome

    if sexo.lower() == 'm':
        mulheres += 1
        if idade < 20:
            mulher_menor_20 += 1
        
    elif sexo.lower() == 'h':
        homens += 1
    else:
        print('\033[31mOpa amigão, digitou algo errado aí em :/')
        exit()

média = tot / c - 1
print(f'''
A média de idade deste grupo de {c} pessoas é: {média}
O homem mais velho é {nome_mais_velho} que tem seus {mais_velho_idade} anos
O total de mulheres com menos de 20 anos são: {mulher_menor_20} Mulheres
''')
