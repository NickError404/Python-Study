# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

conti = True

average = 0

minimum = 0

maximum = 0

cont = 0

Error = True

while conti == True:
    value = int(input('\033[32mEnter a value: '))   
    if cont == 0:
        minimum = value
    if value < minimum:
        minimum = value
    if maximum < value:
        maximum = value
    average += value
    while Error == True:
        conti = str(input('Want a continue? \033[32mY \033[33mor \033[31mN: ')).strip()[0]
        if conti.lower() == 'y':
            conti = True
            Error = False
        elif conti.lower() == 'n':
            conti = False
            Error = False
        else:
            Error = True
            print('\033[31mInvalid Option!!')
    cont += 1
    Error = True
print(f'''
The average value is: {average / 2}
The minimum value is: {minimum}
The maximum value is: {maximum}
''')