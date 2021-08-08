



valor = float(input('\033[33mDigite o valor do produto:R$ '))
print('\033[1;36m{:=^40}'.format('Lojas Nick'))
método_de_pagamento = str(input('''
                       
                  \033[32mA Vista no Dinheiro  \033[37mDigite: Dinheiro
                   \033[31mA Vista no Cartão   \033[36mDigite: Cartão
                  \033[32mEm até 2x no Cartão  \033[37mDigite: 2x
                  \033[31m3x ou mais no Cartão \033[36mDigite: 4x
                  
\033[34mSelecione seu método de pagamento: ''')).strip()

if método_de_pagamento.lower() == 'dinheiro':
    dinheiro = valor - ((valor * 10) / 100)
    print(f'O valor do produto em Dinheiro será no total R$ {dinheiro:.2f}')
elif método_de_pagamento.lower() == 'cartão':
    cartão = valor - ((valor * 5) / 100)
    print(f'O valor do produto em Cartão de Crédito a vista portanto será no total R$ {cartão:.2f}')
elif método_de_pagamento.lower() == '2x':
    print(f'O valor do produto em Cartão Parcelamento de 2X será no total R$ {valor:.2f} ')
    print(f'Serão no total 2 parcelas de R$ {valor/2:.2f} cada')
elif método_de_pagamento.lower() == '4x':
    parcelas = int(input('\033[31mDigite a quantidade de parcelas: '))
    parcelado_4x = valor + ((valor * 20 / 100))
    print(f'O valor do produto em Cartão Parcelamento de 4X será no total R$ {parcelado_4x:.2f}')
    print(f'No total serão {parcelas} parcelas de R$ {valor / parcelas:.2f} cada')



