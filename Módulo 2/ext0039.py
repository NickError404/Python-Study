'''
nome = str(input('Digite qualquer nome: ')).strip()
if nome.lower() == 'pp' or nome.lower() == 'bb':
    print('Seu nome é masculino')
elif nome.lower() == 'anna' or nome.lower() == 'kiss':
    print('Seu nome é feminino')
elif nome.lower() == 'igor':
    print('nomezinho esquisito em {}'.format(nome))
else:
    print('Seu nome é bem normal {} :('.format(nome))
'''
'''
Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não 
pode exceder 30% do salário ou então o empréstimo será negado.
'''




Valor_da_Casa = float(input('\033[36mDigite o valor da casa: '))
Salário = float(input('\033[36mDigite seu salário: '))
Anos = int(input('\033[36mDigite em quantos anos você vai pagar esse empréstimo: '))

prestação = Valor_da_Casa / (Anos * 12)
minino = Salário * 30 / 100

if prestação <= minino:
    print(f'\033[34mValor da prestação {prestação:.2f} e o valor mínimo é {minino:.2f}')
    print('\033[32mEmpréstimo aprovado!')
elif prestação > minino:
    print(f'\033[34mValor do prestação {prestação:.2f}, valor mínimo {minino:.2f}')
    print('\033[31mEmpréstimo recusado!')
else:
    print('\033[7mAlgo deu errado nessa conta!')

