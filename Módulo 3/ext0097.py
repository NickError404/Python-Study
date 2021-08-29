# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com
# as mulheres D) Uma lista de pessoas com idade acima da média

# cadastrados = list()
# idade = 0
# mulheres = list()
# acima_media = list()

# while True:
#     cadastro = {'nome':str(input('Digite seu nome: ')).strip()}
#     cadastro['sexo'] = ' '
#     while cadastro['sexo'] not in 'MF':
#         cadastro['sexo'] = str(input('Digite seu sexo M/F: ')).upper().strip()[0]
#         if cadastro['sexo'] in 'F':
#                 mulheres.append(cadastro['nome'])
#     idade = cadastro['idade'] = int(input('Digite sua idade: '))
#     cadastrados.append(cadastro)
#     ask_conti = str(input('Deseja cadastrar mais alguém? Y/N: ')).upper()[0]
#     if ask_conti in 'N':
#         break
# media = (idade / len(cadastrados))
# print(f'Pessoas cadastradas: {len(cadastrados)}')
# print(f'A média de idade das pessoas cadastradas: {media}')
# print('Mulheres cadastradas')
# for h in mulheres:
#     print(h)

# for h in cadastrados:
#     if h['idade'] > media:
#         print(h)

soma = média = 0
galera = list()
pessoa = dict()
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo? [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Adicionar mais?: [S/N] ')).upper()
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 30)
print(f'A) Ao todos temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
