cad = 0
maior = 0
fmenor = 0
TRY = True
while TRY == True:
    sexo = ' '
    while sexo not in 'fm':
        sexo = str(input('Seu Sexo: f/m: ')).strip().lower()[0]
    idade = int(input('Digite sua idade: '))
    conti = ' '
    while conti not in 'yn': 
        conti = str(input('Continue?: y/n: ')).strip().lower()[0]
    if sexo in 'f' and idade <= 20:
        fmenor += 1
    if sexo in 'm':
        cad += 1
    if idade >= 18:
        maior += 1
    if conti in 'y':
        TRY = True
    elif conti in 'n':
        TRY = False

print(f'''
A quantidade de pessoas que tem mais de 18 é {maior}
A quantidade de homens cadastrados é de {cad}
A quantidade de mulheres com menos de 20 é de {fmenor}
''')
