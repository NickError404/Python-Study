


print('''
\033[32m[1] Binário
\033[33m[2] Octal
\033[34m[3] Hexadecimal
\033[31m[0] Sair
''')

op = int(input('\033[36mDigite uma opção: '))
if op == 1 or op == 2 or op == 3:

    num = int(input('\033[36mDigite um valor: '))
    if op == 1:
        bin = str(bin(num))
        print(f'\033[33mO O valor {num} convertido em Binário é: {bin[2:]}')
    elif op == 2 :
        oct = str(oct(num))
        print(f'O valor {num} convertido em Octal é: {oct[2:]}')
    elif op == 3:
        hex = str(hex(num))
        print(f'O valor de {num} convertido em Hexadecimal é: {hex[2:]}')

elif op == 0:
    print('\033[31mSaindo...')
    exit()
else:
    print('\033[31mAlgo deu errado em seus cálculos')